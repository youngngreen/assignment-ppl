from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

class ASTGeneration(D96Visitor):

# program: classdecls EOF;
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(self.visit(ctx.classdecls()))

# classdecls: classdecl classdecls | classdecl;
    def visitClassdecls(self, ctx: D96Parser.ClassdeclsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.classdecl())
        return self.visit(ctx.classdecl()) + self.visit(ctx.classdecls())

# classdecl: CLASS ID (COLON ID | ) LCB (memberlist | ) RCB;
    def visitClassdecl(self, ctx: D96Parser.ClassdeclContext):
        classname = ctx.ID(0).getText()
        memlist = self.visit(ctx.memberlist()) if ctx.memberlist() else []
        parentname = Id(ctx.ID(1).getText()) if ctx.ID(1) else None
        ## check kind of main method
        if classname == "Program":
            for i in range(0, len(memlist)):
                if isinstance(memlist[i], MethodDecl) and memlist[i].name.name == "main" and memlist[i].param == []:
                    memlist[i].kind = Static()
        ###################
        return [ClassDecl(Id(classname), memlist, parentname)]

# memberlist: member memberlist | member;
    def visitMemberlist(self, ctx: D96Parser.MemberlistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.member())
        return self.visit(ctx.member()) + self.visit(ctx.memberlist())

# member: attribute | method;
    def visitMember(self, ctx: D96Parser.MemberContext):
        if ctx.attribute():
            return self.visit(ctx.attribute())
        return self.visit(ctx.method())

# attribute: mu_attribute | im_attribute;
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        if ctx.mu_attribute():
            return self.visit(ctx.mu_attribute())
        return self.visit(ctx.im_attribute())

# mu_attribute: VAR att_names COLON typ (ASSIGN exprlist | ) SEMICOLON ;
    def visitMu_attribute(self, ctx:D96Parser.Mu_attributeContext):
        att_names = self.visit(ctx.att_names()) # list: [[id1, I/S1],[id2, I/S2],...]
        typ = self.visit(ctx.typ())
        if ctx.exprlist():
            valueinits = self.visit(ctx.exprlist())
            return list(map(lambda id, value: AttributeDecl(id[1], VarDecl(id[0], typ, value)), att_names, valueinits))
        if type(typ) is ClassType:
            return list(map(lambda id: AttributeDecl(id[1], VarDecl(id[0], typ, NullLiteral())), att_names))
        return list(map(lambda id: AttributeDecl(id[1], VarDecl(id[0], typ, None)), att_names))
        
# im_attribute: VAL att_names COLON typ (ASSIGN exprlist | ) SEMICOLON ;
    def visitIm_attribute(self, ctx:D96Parser.Im_attributeContext):
        att_names = self.visit(ctx.att_names()) # list: [[id1, I/S1],[id2, I/S2],...]
        typ = self.visit(ctx.typ())
        if ctx.exprlist():
            valueinits = self.visit(ctx.exprlist())
            return list(map(lambda id, value: AttributeDecl(id[1], ConstDecl(id[0], typ, value)), att_names, valueinits))
        if type(typ) is ClassType:
            return list(map(lambda id: AttributeDecl(id[1], ConstDecl(id[0], typ, NullLiteral())), att_names))
        return list(map(lambda id: AttributeDecl(id[1], ConstDecl(id[0], typ, None)), att_names))
        
# att_names: att_id COMMA att_names | att_id;
    def visitAtt_names(self, ctx:D96Parser.Att_namesContext):
        idd = self.visit(ctx.att_id()) # list: [id, In/Sta]
        if ctx.att_names():
            return [idd] + self.visit(ctx.att_names()) # list: [[id1, I/S1],[id2, I/S2],...]
        return [idd]

# att_id: ID | DOLLARID;
    def visitAtt_id(self, ctx:D96Parser.Att_idContext):
        if ctx.ID():
            return [Id(ctx.ID().getText()), Instance()]
        return [Id(ctx.DOLLARID().getText()), Static()]

# method: regularmethod | specialmethod;
    def visitMethod(self, ctx: D96Parser.MethodContext):
        if ctx.regularmethod():
            return self.visit(ctx.regularmethod())
        return self.visit(ctx.specialmethod())

# regularmethod: (ID | DOLLARID) LP (paramlist | ) RP blockstm;
    def visitRegularmethod(self, ctx: D96Parser.RegularmethodContext):
        kind = Instance() if ctx.ID() else Static()
        name = ctx.getChild(0).getText()
        param = self.visit(ctx.paramlist()) if ctx.paramlist() else []
        body = self.visit(ctx.blockstm())
        return [MethodDecl(kind, Id(name), param, body)]

# specialmethod: constructor | destructor;
    def visitSpecialmethod(self, ctx: D96Parser.SpecialmethodContext):
        if ctx.constructor():
            return self.visit(ctx.constructor())
        return self.visit(ctx.destructor())

# constructor: CONSTRUCTOR LP (paramlist | ) RP blockstm;
    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        kind = Instance()
        name = Id('Constructor')
        param = self.visit(ctx.paramlist()) if ctx.paramlist() else []
        body = self.visit(ctx.blockstm())
        return [MethodDecl(kind, name, param, body)]

# destructor: DESTRUCTOR LP RP blockstm;
    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        kind = Instance()
        name = Id('Destructor')
        param = []
        body = self.visit(ctx.blockstm())
        return [MethodDecl(kind, name, param, body)]

# paramlist: paramdecl SEMICOLON paramlist | paramdecl;
    def visitParamlist(self, ctx: D96Parser.ParamlistContext):
        paramdecl = self.visit(ctx.paramdecl())
        if ctx.getChildCount() == 1:
            return [VarDecl(id, typ) for (id, typ) in paramdecl]
        return [VarDecl(id, typ) for (id, typ) in paramdecl] + self.visit(ctx.paramlist())
        
        # if ctx.getChildCount() == 1:
        #     return list(map(lambda id, typ: VarDecl(id, typ), paramdecl))
        # return list(map(lambda id, typ: VarDecl(id, typ), paramdecl)) + self.visit(ctx.paramlist())

# paramdecl: idlist COLON typ;
    def visitParamdecl(self, ctx: D96Parser.ParamdeclContext):
        typ = self.visit(ctx.typ()) # Int/Float/...
        idlist = self.visit(ctx.idlist()) # ids
        return [(id, typ) for id in idlist] # [[id1, type1], [id2, type2], [,], [,],...]

# idlist: (ID | DOLLARID) COMMA idlist | (ID | DOLLARID);
    def visitIdlist(self, ctx: D96Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.getChild(0).getText())]
        return [Id(ctx.getChild(0).getText())] + self.visit(ctx.idlist())

# typ: INT | FLOAT | STRING | BOOLEAN | arraytype | ID; // ID is class type
    def visitTyp(self, ctx: D96Parser.TypContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())
        else: # classtype
            return ClassType(Id(ctx.ID().getText()))

# arraytype: ARRAY LSB typ COMMA NONZEROINT RSB;
    def visitArraytype(self, ctx: D96Parser.ArraytypeContext):
        size = int(ctx.NONZEROINT().getText())
        eleType = self.visit(ctx.typ())
        return ArrayType(size, eleType)

# indexopr: LSB expr RSB indexopr | LSB expr RSB; // association: LEFT???
    def visitIndexopr(self, ctx: D96Parser.IndexoprContext):
        expr = self.visit(ctx.expr())
        if ctx.indexopr():
            return [expr] + self.visit(ctx.indexopr())
        return [expr]

# objectcreation: ID LP (exprlist | ) RP; // association: RIGHT, but teacher's comfirmation is: no test case for this association.
    def visitObjectcreation(self, ctx: D96Parser.ObjectcreationContext):
        param = self.visit(ctx.exprlist()) if ctx.exprlist() else []
        classname = Id(ctx.ID().getText())
        return NewExpr(classname, param)


# expr: expr1 (ADDSTR | EQUALSTR) expr1 | expr1;
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        return BinaryOp(op, left, right)

# expr1: expr2 (EQUAL | NEQ | LT | GT | LTE | GTE) expr2 | expr2;
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2(0))
        right = self.visit(ctx.expr2(1))
        return BinaryOp(op, left, right)

# expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        return BinaryOp(op, left, right)

# expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        return BinaryOp(op, left, right)

# expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        return BinaryOp(op, left, right)

# expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.expr6():
            return self.visit(ctx.expr6())
        op = ctx.NOT().getText()
        body = self.visit(ctx.expr5())
        return UnaryOp(op, body)

# expr6: SUB expr6 | expr7;
    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.expr7():
            return self.visit(ctx.expr7())
        op = ctx.SUB().getText()
        body = self.visit(ctx.expr6())
        return UnaryOp(op, body)

# # expr7: (ID | DOLLARID) indexopr | expr8;
#     def visitExpr7(self, ctx: D96Parser.Expr7Context):
#         if ctx.getChildCount() == 1:
#             return self.visit(ctx.expr8())
#         return ArrayCell(Id(ctx.getChild(0).getText()), self.visit(ctx.indexopr()))

# expr7: expr7 indexopr | expr8;
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        return ArrayCell(self.visit(ctx.expr7()), self.visit(ctx.indexopr()))

# expr8:
# 	expr8 DOT ID // Instance attribute access
# 	| expr8 DOT ID LP (exprlist | ) RP  // Instance method access
# 	| selfexpr
# 	| expr9 ; // check association: LEFT

    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.getChildCount() == 3: # Instance attribute access
            obj = self.visit(ctx.expr8())
            fieldname = Id(ctx.ID().getText())
            return FieldAccess(obj, fieldname)
        elif ctx.expr9():
            return self.visit(ctx.expr9())
        else: # Instance method access
            obj = self.visit(ctx.expr8())
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.exprlist()) if ctx.exprlist() else []
            return CallExpr(obj, method, param)


# expr9:
# 	ID DOUBLECOLON DOLLARID // Static attribute access
# 	| ID DOUBLECOLON DOLLARID LP (exprlist | ) RP // Static method invocation
# 	| expr10; // check association: NONE

    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr10())
        elif ctx.getChildCount() == 3:
            obj = Id(ctx.ID().getText())
            fieldname = Id(ctx.DOLLARID().getText())
            return FieldAccess(obj, fieldname)
        else:
            obj = Id(ctx.ID().getText())
            method = Id(ctx.DOLLARID().getText())
            param = self.visit(ctx.exprlist()) if ctx.exprlist() else []
            return CallExpr(obj, method, param)

# expr10: NEW objectcreation| expr11;
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.expr11():
            return self.visit(ctx.expr11())
        return self.visit(ctx.objectcreation())

# expr11: LP expr RP | ID | DOLLARID | literal;
    def visitExpr11(self, ctx: D96Parser.Expr11Context):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.literal():
            return self.visit(ctx.literal())
        else: # ID | DOLLARID
            return Id(ctx.getChild(0).getText())

# literal: intlit | FLOATLIT | booleanlit | STRINGLIT | arraylit | NULL;
    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.intlit():
            return self.visit(ctx.intlit())
        elif ctx.FLOATLIT():
            value = float(ctx.FLOATLIT().getText())
            return FloatLiteral(value)
        elif ctx.booleanlit():
            return self.visit(ctx.booleanlit())
        elif ctx.STRINGLIT():
            value = ctx.STRINGLIT().getText()
            return StringLiteral(value)
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.NULL():
            return NullLiteral()
        else: # Self
            return SelfLiteral()

# exprlist: expr COMMA exprlist | expr;
    def visitExprlist(self, ctx: D96Parser.ExprlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())

# statement: vardecl | constdecl | assignmentstm | ifstm | foreachstm | breakstm | continuestm | returnstm | methodinvostm | blockstm;
    def visitStatement(self, ctx: D96Parser.StatementContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl())
        elif ctx.assignmentstm():
            return [self.visit(ctx.assignmentstm())]
        elif ctx.ifstm():
            return [self.visit(ctx.ifstm())]
        elif ctx.foreachstm():
            return [self.visit(ctx.foreachstm())]
        elif ctx.breakstm():
            return [self.visit(ctx.breakstm())]           
        elif ctx.continuestm():
            return [self.visit(ctx.continuestm())]
        elif ctx.returnstm():
            return [self.visit(ctx.returnstm())]
        elif ctx.methodinvostm():
            return [self.visit(ctx.methodinvostm())]
        else: # blockstm
            return [self.visit(ctx.blockstm())]

# statementlist: statement statementlist | statement;
    def visitStatementlist(self, ctx: D96Parser.StatementlistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.statement())
        return self.visit(ctx.statement()) + self.visit(ctx.statementlist())

# vardecl: VAR varnames COLON typ (ASSIGN exprlist | ) SEMICOLON ;
    def visitVardecl(self, ctx: D96Parser.VardeclContext):
        variable = self.visit(ctx.varnames()) # list[Id]
        varType = self.visit(ctx.typ()) # type: Int, Float,...
        if ctx.exprlist():
            varInit = self.visit(ctx.exprlist()) # list[varInit]
            return list(map(lambda x, y: VarDecl(x, varType, y), variable, varInit))
        if type(varType) is ClassType:
            return list(map(lambda x: VarDecl(x, varType, NullLiteral()), variable))
        return list(map(lambda x: VarDecl(x, varType, None), variable))
             
# constdecl: VAL varnames COLON typ (ASSIGN exprlist | ) SEMICOLON ;
    def visitConstdecl(self, ctx: D96Parser.ConstdeclContext):
        constant = self.visit(ctx.varnames()) # list[Id]
        constType = self.visit(ctx.typ()) # type: Int, Float,...
        if ctx.exprlist():
            value = self.visit(ctx.exprlist()) # list[value]
            return list(map(lambda x, y: ConstDecl(x, constType, y), constant, value)) # x: Id, y: value
        if type(constType) is ClassType:
            return list(map(lambda x: ConstDecl(x, constType, NullLiteral()), constant))
        return list(map(lambda x: ConstDecl(x, constType, None), constant)) # x: Id       

# varnames: ID COMMA varnames | ID;
    def visitVarnames(self, ctx: D96Parser.VarnamesContext):
        idd = Id(ctx.ID().getText()) # id
        if ctx.varnames():
            return [idd] + self.visit(ctx.varnames()) # list[id]
        return [idd] # list[id]

# # assignmentstm: lhs ASSIGN expr SEMICOLON;
#     def visitAssignmentstm(self, ctx: D96Parser.AssignmentstmContext):
#         lhs = self.visit(ctx.lhs())
#         exp = self.visit(ctx.expr())
#         return Assign(lhs, exp)

# assignmentstm: expr ASSIGN expr SEMICOLON;
    def visitAssignmentstm(self, ctx: D96Parser.AssignmentstmContext):
        lhs = self.visit(ctx.expr(0))
        exp = self.visit(ctx.expr(1))
        return Assign(lhs, exp)

# # lhs: ID | DOLLARID | expr indexopr;
#     def visitLhs(self, ctx: D96Parser.LhsContext):
#         if ctx.ID():
#             return Id(ctx.ID().getText())
#         elif ctx.DOLLARID():
#             return Id(ctx.DOLLARID().getText())
#         else: # expr indexopr
#             return ArrayCell(self.visit(ctx.expr()), self.visit(ctx.indexopr()))

# ifstm: IF LP expr RP blockstm (else_stms | );
    def visitIfstm(self, ctx:D96Parser.IfstmContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.blockstm())
        elseStmt = self.visit(ctx.else_stms()) if ctx.else_stms() else None
        return If(expr, thenStmt, elseStmt)

# else_stms: elseif_stm else_stms | elseif_stm | else_stm;
    def visitElse_stms(self, ctx:D96Parser.Else_stmsContext):
        if ctx.getChildCount() == 1:
            if ctx.elseif_stm():
                expr = self.visit(ctx.elseif_stm())
                return If(expr[0], expr[1])
            else:
                return self.visit(ctx.else_stm())
        expr = self.visit(ctx.elseif_stm())
        else_stms = self.visit(ctx.else_stms())
        return If(expr[0], expr[1], else_stms)


# elseif_stm: ELSEIF LP expr RP blockstm;
    def visitElseif_stm(self, ctx:D96Parser.Elseif_stmContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.blockstm())
        return expr, thenStmt

# else_stm: ELSE blockstm;
    def visitElse_stm(self, ctx:D96Parser.Else_stmContext):
        return self.visit(ctx.blockstm())

# foreachstm: FOREACH LP ID IN expr DOUBLEDOT expr (BY expr | ) RP blockstm;
    def visitForeachstm(self, ctx: D96Parser.ForeachstmContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        loop = self.visit(ctx.blockstm())
        expr3 = self.visit(ctx.expr(2)) if ctx.expr(2) else IntLiteral(1) # "by 1" if no "by" as teacher's confirmation
        return For(id, expr1, expr2, loop, expr3)

# breakstm: BREAK SEMICOLON;
    def visitBreakstm(self, ctx: D96Parser.BreakstmContext):
        return Break()

# continuestm: CONTINUE SEMICOLON;
    def visitContinuestm(self, ctx: D96Parser.ContinuestmContext):
        return Continue()

# returnstm: RETURN (expr | ) SEMICOLON;
    def visitReturnstm(self, ctx: D96Parser.ReturnstmContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return()

# methodinvostm: insmethodstm | stamethodstm;
    def visitMethodinvostm(self, ctx: D96Parser.MethodinvostmContext):
        if ctx.insmethodstm():
            return self.visit(ctx.insmethodstm())
        return self.visit(ctx.stamethodstm())

# insmethodstm: expr DOT ID LP (exprlist | ) RP SEMICOLON;
    def visitInsmethodstm(self, ctx: D96Parser.InsmethodstmContext):
        obj = self.visit(ctx.expr())
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.exprlist()) if ctx.exprlist() else []
        return CallStmt(obj, method, param)

# stamethodstm: ID DOUBLECOLON DOLLARID LP (exprlist | ) RP SEMICOLON;
    def visitStamethodstm(self, ctx: D96Parser.StamethodstmContext):
        obj = Id(ctx.ID().getText())
        method = Id(ctx.DOLLARID().getText())
        param = self.visit(ctx.exprlist()) if ctx.exprlist() else []
        return CallStmt(obj, method, param)

# blockstm: LCB (statementlist | ) RCB;
    def visitBlockstm(self, ctx: D96Parser.BlockstmContext):
        inst = self.visit(ctx.statementlist()) if ctx.statementlist() else []
        return Block(inst)

# intlit: ZEROINT | NONZEROINT;
    def visitIntlit(self, ctx: D96Parser.IntlitContext):
        return IntLiteral(int(ctx.getChild(0).getText()))

# booleanlit: TRUE | FALSE;
    def visitBooleanlit(self, ctx: D96Parser.BooleanlitContext):
        value = True if ctx.TRUE() else False
        return BooleanLiteral(value)

# arraylit: idxarray | mularray;
    def visitArraylit(self, ctx: D96Parser.ArraylitContext):
        if ctx.idxarray():
            return self.visit(ctx.idxarray())
        return self.visit(ctx.mularray())

# idxarray: ARRAY LP idxarraycontent RP;
    def visitIdxarray(self, ctx: D96Parser.IdxarrayContext):
        return self.visit(ctx.idxarraycontent())

# idxarraycontent: intarr | floatarr | boolarr | stringarr;
    def visitIdxarraycontent(self, ctx: D96Parser.IdxarraycontentContext):
        if ctx.intarr():
            return ArrayLiteral(self.visit(ctx.intarr()))
        elif ctx.floatarr():
            return ArrayLiteral(self.visit(ctx.floatarr()))
        elif ctx.boolarr():
            return ArrayLiteral(self.visit(ctx.boolarr()))
        else: # stringarr
            return ArrayLiteral(self.visit(ctx.stringarr()))

# intarr: intlit COMMA intarr | intlit;
    def visitIntarr(self, ctx: D96Parser.IntarrContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.intlit())]
        return [self.visit(ctx.intlit())] + self.visit(ctx.intarr())

# floatarr: FLOATLIT COMMA floatarr | FLOATLIT;
    def visitFloatarr(self, ctx: D96Parser.FloatarrContext):
        floatlit = FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.getChildCount() == 1:
            return [floatlit]
        return [floatlit] + self.visit(ctx.floatarr())

# stringarr: STRINGLIT COMMA stringarr | STRINGLIT;
    def visitStringarr(self, ctx: D96Parser.StringarrContext):
        strlit = StringLiteral(ctx.STRINGLIT().getText())
        if ctx.getChildCount() == 1:
            return [strlit]
        return [strlit] + self.visit(ctx.stringarr())

# boolarr: booleanlit COMMA boolarr | booleanlit;
    def visitBoolarr(self, ctx: D96Parser.BoolarrContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.booleanlit())]
        return [self.visit(ctx.booleanlit())] + self.visit(ctx.boolarr())

# mularray: ARRAY LP mularraycontent RP;
    def visitMularray(self, ctx: D96Parser.MularrayContext):
        return ArrayLiteral(self.visit(ctx.mularraycontent()))

# mularraycontent: arraylit COMMA mularraycontent | arraylit;
    def visitMularraycontent(self, ctx: D96Parser.MularraycontentContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.arraylit())]
        return [self.visit(ctx.arraylit())] + self.visit(ctx.mularraycontent())

########### note #######################