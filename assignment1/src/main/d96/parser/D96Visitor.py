# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecls.
    def visitClassdecls(self, ctx:D96Parser.ClassdeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecl.
    def visitClassdecl(self, ctx:D96Parser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberlist.
    def visitMemberlist(self, ctx:D96Parser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attrbnames.
    def visitAttrbnames(self, ctx:D96Parser.AttrbnamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attrbname.
    def visitAttrbname(self, ctx:D96Parser.AttrbnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#valueinit.
    def visitValueinit(self, ctx:D96Parser.ValueinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#regularmethod.
    def visitRegularmethod(self, ctx:D96Parser.RegularmethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#specialmethod.
    def visitSpecialmethod(self, ctx:D96Parser.SpecialmethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramlist.
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramdecl.
    def visitParamdecl(self, ctx:D96Parser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typ.
    def visitTyp(self, ctx:D96Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arraytype.
    def visitArraytype(self, ctx:D96Parser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayaccess.
    def visitArrayaccess(self, ctx:D96Parser.ArrayaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classtype.
    def visitClasstype(self, ctx:D96Parser.ClasstypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexopr.
    def visitIndexopr(self, ctx:D96Parser.IndexoprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instanceaccess.
    def visitInstanceaccess(self, ctx:D96Parser.InstanceaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#staticaccess.
    def visitStaticaccess(self, ctx:D96Parser.StaticaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#insattrbaccess.
    def visitInsattrbaccess(self, ctx:D96Parser.InsattrbaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#staattrbaccess.
    def visitStaattrbaccess(self, ctx:D96Parser.StaattrbaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#insmethodaccess.
    def visitInsmethodaccess(self, ctx:D96Parser.InsmethodaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stamethodaccess.
    def visitStamethodaccess(self, ctx:D96Parser.StamethodaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#objectcreation.
    def visitObjectcreation(self, ctx:D96Parser.ObjectcreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#selfexpr.
    def visitSelfexpr(self, ctx:D96Parser.SelfexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr11.
    def visitExpr11(self, ctx:D96Parser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprlist.
    def visitExprlist(self, ctx:D96Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statementlist.
    def visitStatementlist(self, ctx:D96Parser.StatementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varnames.
    def visitVarnames(self, ctx:D96Parser.VarnamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignmentstm.
    def visitAssignmentstm(self, ctx:D96Parser.AssignmentstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifstm.
    def visitIfstm(self, ctx:D96Parser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseifstms.
    def visitElseifstms(self, ctx:D96Parser.ElseifstmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseifstm.
    def visitElseifstm(self, ctx:D96Parser.ElseifstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elsestm.
    def visitElsestm(self, ctx:D96Parser.ElsestmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#foreachstm.
    def visitForeachstm(self, ctx:D96Parser.ForeachstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#breakstm.
    def visitBreakstm(self, ctx:D96Parser.BreakstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continuestm.
    def visitContinuestm(self, ctx:D96Parser.ContinuestmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#returnstm.
    def visitReturnstm(self, ctx:D96Parser.ReturnstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodinvostm.
    def visitMethodinvostm(self, ctx:D96Parser.MethodinvostmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#insmethodstm.
    def visitInsmethodstm(self, ctx:D96Parser.InsmethodstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stamethodstm.
    def visitStamethodstm(self, ctx:D96Parser.StamethodstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockstm.
    def visitBlockstm(self, ctx:D96Parser.BlockstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#intlit.
    def visitIntlit(self, ctx:D96Parser.IntlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#booleanlit.
    def visitBooleanlit(self, ctx:D96Parser.BooleanlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arraylit.
    def visitArraylit(self, ctx:D96Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idxarray.
    def visitIdxarray(self, ctx:D96Parser.IdxarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idxarraycontent.
    def visitIdxarraycontent(self, ctx:D96Parser.IdxarraycontentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#intarr.
    def visitIntarr(self, ctx:D96Parser.IntarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#floatarr.
    def visitFloatarr(self, ctx:D96Parser.FloatarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stringarr.
    def visitStringarr(self, ctx:D96Parser.StringarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#boolarr.
    def visitBoolarr(self, ctx:D96Parser.BoolarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mularray.
    def visitMularray(self, ctx:D96Parser.MularrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mularraycontent.
    def visitMularraycontent(self, ctx:D96Parser.MularraycontentContext):
        return self.visitChildren(ctx)



del D96Parser