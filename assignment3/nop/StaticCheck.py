
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

# class Utils:
#     def lookup(self,name,lst,func):
#         for x in lst:
#             if name == func(x):
#                 return x
#         return None


class varControl:

    # def visitVarDecl(self, ctx: VarDecl, o: object):
    #     kind, env = o
    #     name = ctx.variable.name
    #     if env.get(name) is not None:
    #         raise Redeclared(Attribute(), name)
    #     env[name] = ('mutable', self.visit(ctx.varType, env), kind)
    #     return('mutable', self.visit(ctx.varType, env), kind)

    def __init__(self,name:str,typ:Type,field:int, constant=False):
        self.name = name
        self.typ = typ
        self.field = field
        self.constant = constant

    def __eq__(self, objPar):
        if isinstance(objPar, varControl):
            return self.name == objPar.name and self.typ == objPar.typ and self.field == objPar.field
        return False

    def typeReceive(self):
        return self.typ

class attControl:

    # def visitAttributeDecl(self, ast: AttributeDecl, o: object):
    #     if type(ast.kind) is Instance:
    #         self.visit(ast.decl, ('instance', o))
    #     if type(ast.kind) is Static:
    #         self.visit(ast.decl, ('static', o))

    def __init__(self, name:str, typ:Type, checkStc = False, constant = False):
        self.name = name
        self.type = typ
        self.checkStc = checkStc
        self.constant = constant

class methodControl:

    # def visitMethodDecl(self, ctx: MethodDecl, o: object):
    #     # pass
    #     returnType = None #### this line will be deleted !!!!!!
    #     if type(ctx.kind) is Instance:
    #         kind = 'instance'
    #     if type(ctx.kind) is Static:
    #         kind = 'static'
    #     if o.get(ctx.name.name) is not None:
    #         raise Redeclared(Method(), ctx.name.name)
    #     params = ctx.param
    #     if ctx.name.name == 'main' and kind == 'static': # main
    #         returnType = None
    #     #########
    #     if returnType is not None: ###### how to check returnType (not None)?
    #         param = list(map(lambda x: self.visit(x, (None, {})), params))
    #         o[ctx.name.name] = ('method', self.visit(
    #             returnType, o), kind, param)
    #     else:
    #         param = list(map(lambda x: self.visit(x, (None, {})), params))
    #         o[ctx.name.name] = ('method', None, kind, param)

    def __init__(self, method_name:str, stc=False, para:List[VarDecl]=[], rettype=None):
        self.name = method_name
        self.paratype = list(map(lambda x: x.varType, para))
        self.rettype = rettype
        self.checkStc = stc
        self.circ = 0
        self.variable = {}
        self.field = 1
        for var in para:
            self.decParams(var.variable.name,var.varType)
        self.field = 0

    def __eq__(self, objPar):
        if isinstance(objPar, methodControl):
            return self.clsname == objPar.name and self.name == method_name and self.paratype == objPar.paratype
        return self.clsname == objPar.cls

    def inCircuit(self):
        self.circ += 1

    def outCircuit(self):
        self.circ -= 1 

    def inField(self):
        self.field += 1

    def outField(self):
        self.field -= 1
        for k, lst in self.variable.items():
            if lst and lst[-1].field > self.field:
                self.variable[k].pop()
 

    def rePaControl(self, name):
        if name in self.variable:
            if self.variable[name][-1].field == self.field:
                raise Redeclared(Parameter(),name)

    def reVaControl(self, name):
        if name in self.variable:
            if self.variable[name][-1].field == self.field:
                raise Redeclared(Variable(),name)

    def reCoControl(self, name):
        if name in self.variable:
            if self.variable[name][-1].field == self.field:
                raise Redeclared(Constant(),name)


    def mainControl(self):
        return self.name == 'main'

    def typeReceive(self):
        return self.rettype

    def decParams(self, name:str, typ:Type):
        self.rePaControl(name)
        if name not in self.variable:
            self.variable[name] = [varControl(name,typ,self.field)]
        else:
            self.variable[name] += [varControl(name,typ,self.field)]

    def decVars(self, name:str, typ:Type):
        self.reVaControl(name)
        if name not in self.variable:
            self.variable[name] = [varControl(name,typ,self.field)]
        else:
            self.variable[name] += [varControl(name,typ,self.field)]

    def decCons(self, name:str, typ:Type):
        self.reCoControl(name)
        if name not in self.variable:
            self.variable[name] = [varControl(name,typ,self.field,True)]
        else:
            self.variable[name] += [varControl(name,typ,self.field,True)]

class classControl:

    # def visitClassDecl(self, ast: ClassDecl, o: object):
    #     name = ast.classname.name
    #     if o.get(name) is not None:
    #         raise Redeclared(Class(), name)
    #     o[name] = {}
    #     for x in ast.memlist:
    #         self.visit(x, o[name])

    def __init__(self, name:str, superClass = None):
        self.att = {}
        self.method = {}
        self.env = []
        self.name = name
        self.typCst = []
        if superClass:
            self.att = superClass.att.copy()
            self.method = superClass.method.copy()
            self.env = [name] + superClass.env.copy()
        else:
            self.env = [name]

    def attPlus(self, name:str, att_type:Type, checkStc=False, const=False):
        self.reCheckAtb(name)
        self.att[name] = attControl(name,att_type,checkStc,const)

    def mtdPlus(self, name:str, checkStc=False, paratype:List[VarDecl]=[], rettype=None):
        self.reCheckMtd(name, paratype)
        self.method[name] = methodControl(name,checkStc,paratype,rettype)
        if name == 'Constructor':
            self.typCst = self.method[name].paratype

    def mtdReceive(self, method_name:str):
        if method_name not in self.method.keys(): raise Undeclared(Method(),method_name)
        return self.method[method_name]

    def attReceive(self, atrbName:str):
        if atrbName not in self.att.keys(): raise Undeclared(Attribute(),atrbName)
        return self.att[atrbName]

    def entryPointControl(self):
        return any([x.mainControl() == 'main' for x in self.method.values()])

    def reCheckMtd(self, name:str, typelst:List[VarDecl]):
        if name in self.method.keys() or name in self.att.keys():
            raise Redeclared(Method(), name)

    def reCheckAtb(self, name:str):
        if name in self.method.keys() or name in self.att.keys():
            raise Redeclared(Attribute(),name)

class classDir:
    def __init__(self):
        self.objid = {}

    # def visitClassDecl(self, ast: ClassDecl, o: object):
    #     name = ast.classname.name
    #     if o.get(name) is not None:
    #         raise Redeclared(Class(), name)
    #     o[name] = {}
    #     for x in ast.memlist:
    #         self.visit(x, o[name])

    def classPlus(self, cls_name:str, superClass:str = None):
        self.reCheckCls(cls_name)
        if superClass:
            self.unCheckCls(superClass)
            self.objid[cls_name] = classControl(cls_name, self.objid[superClass])
        else:
            self.objid[cls_name] = classControl(cls_name)

    def mtdPlus(self, cls_name:str, method_name:str, checkStc=False, paratype:List[VarDecl]=[], rettype = None):
        self.unCheckCls(cls_name)
        self.objid[cls_name].mtdPlus(method_name, checkStc, paratype, rettype)

    def attPlus(self, cls_name:str, atrbName:str,att_type:Type,checkStc:bool,const:bool):
        self.unCheckCls(cls_name)
        self.objid[cls_name].attPlus(atrbName,att_type,checkStc,const)

    def classReceive(self, preClaSml:str):
        return self.objid[preClaSml]

    def entryPointControl(self):
        if not any([x.entryPointControl() for x in self.objid.values()]):
            raise NoEntryPoint()

    def typeSctt(self, typA, typB):
        
        if type(typA) is type(typB) and type(typA) not in [ClassType, ArrayType]:
            return True
        if type(typA) is FloatType and type(typB) is IntType:
            return True
        if type(typA) is ClassType and type(typB) is ClassType and typA.classname.name in self.classReceive(typB.classname.name).env:
            return True
        if type(typA) is ArrayType and type(typB) is ArrayType:
            return typA.size == typB.size and self.typeSctt(typA.eleType,typB.eleType)
        return False

    def reCheckCls(self, name:str):
        if name in self.objid.keys():
            raise Redeclared(Class(),name)

    def unCheckCls(self, cls_name):
        if cls_name not in self.objid.keys():
            raise Undeclared(Class(),cls_name)

# class ExpUtils:
#     @ staticmethod
#     def isNaNType(expType):
#         return type(expType) not in [IntType, FloatType]

#     @ staticmethod
#     def isNotConst(expType):
#         return type(expType) in [CallExpr, NewExpr, ArrayCell, ArrayType]

#     @ staticmethod
#     def isNotAccess(expType):
#         return type(expType) not in [CallExpr, FieldAccess, CallStmt]

class StaticChecker(BaseVisitor):    
    def __init__(self,ast):
        self.ast = ast
    
    # global_envi = [
    #     Symbol("getInt", MType([], IntType())),
    #     Symbol("putIntLn", MType([IntType()], VoidType()))
    # ]

    # def __init__(self, ast):
    #     self.ast = ast

    # def check(self):
    #     return self.visit(self.ast, StaticChecker.global_envi)

    # def visitProgram(self, ast, c):
    #     env = GetEnv().visit(ast, None)
    #     return [self.visit(x, env) for x in ast.decl]

    def visit(self, ast, c):
        if isinstance(ast, IntLiteral): return self.visitIntLiteral(ast, c)
        elif isinstance(ast, FloatLiteral): return self.visitFloatLiteral(ast, c)
        elif isinstance(ast, StringLiteral): return self.visitStringLiteral(ast, c)
        elif isinstance(ast, BooleanLiteral): return self.visitBooleanLiteral(ast, c)
        elif isinstance(ast, NullLiteral): return self.visitNullLiteral(ast, c)
        elif isinstance(ast, SelfLiteral): return self.visitSelfLiteral(ast, c)
        elif isinstance(ast, ArrayLiteral): return self.visitArrayLiteral(ast, c)
        elif isinstance(ast, Assign): return self.visitAssign(ast, c)
        # elif isinstance(ast, BoolType): return self.visitBoolType(ast, c)
        # elif isinstance(ast, StringType): return self.visitStringType(ast, c)
        # elif isinstance(ast, ArrayType): return self.visitArrayType(ast, c)
        elif isinstance(ast, If): return self.visitIf(ast, c)
        elif isinstance(ast, For): return self.visitFor(ast, c)
        elif isinstance(ast, Break): return self.visitBreak(ast, c)
        elif isinstance(ast, Continue): return self.visitContinue(ast, c)
        elif isinstance(ast, Return): return self.visitReturn(ast, c)
        elif isinstance(ast, MethodDecl): return self.visitMethodDecl(ast, c)
        elif isinstance(ast, AttributeDecl): return self.visitAttributeDecl(ast, c)
        elif isinstance(ast, IntType): return self.visitIntType(ast, c)
        elif isinstance(ast, FloatType): return self.visitFloatType(ast, c)
        elif isinstance(ast, BoolType): return self.visitBoolType(ast, c)
        elif isinstance(ast, StringType): return self.visitStringType(ast, c)
        elif isinstance(ast, ArrayType): return self.visitArrayType(ast, c)
        elif isinstance(ast, ClassType): return self.visitClassType(ast, c)
        elif isinstance(ast, VoidType): return self.visitVoidType(ast, c)
        elif isinstance(ast, Program): return self.visitProgram(ast, c)
        # elif isinstance(ast, CallExpr): return self.visitCallExpr(ast, c)
        # elif isinstance(ast, NewExpr): return self.visitNewExpr(ast, c)
        # elif isinstance(ast, ArrayCell): return self.visitArrayCell(ast, c)
        elif isinstance(ast, Id): return self.visitId(ast, c)
        elif isinstance(ast, BinaryOp): return self.visitBinaryOp(ast, c)
        elif isinstance(ast, UnaryOp): return self.visitUnaryOp(ast, c)
        elif isinstance(ast, CallExpr): return self.visitCallExpr(ast, c)
        elif isinstance(ast, NewExpr): return self.visitNewExpr(ast, c)
        elif isinstance(ast, ArrayCell): return self.visitArrayCell(ast, c)
        # elif isinstance(ast, CallExpr): return self.visitCallExpr(ast, c)
        # elif isinstance(ast, NewExpr): return self.visitNewExpr(ast, c)
        # elif isinstance(ast, ArrayCell): return self.visitArrayCell(ast, c)
        elif isinstance(ast, FieldAccess): return self.visitFieldAccess(ast, c)
        elif isinstance(ast, CallStmt): return self.visitCallStmt(ast, c)
        elif isinstance(ast, VarDecl): return self.visitVarDecl(ast, c)
        elif isinstance(ast, Block): return self.visitBlock(ast, c)
        elif isinstance(ast, ConstDecl): return self.visitConstDecl(ast, c)
        elif isinstance(ast, ClassDecl): return self.visitClassDecl(ast, c)
        elif isinstance(ast, Static): return self.visitStatic(ast, c)


    def check(self):
        return self.visit(self.ast,None)

    # def visitProgram(self, ast, c):
    #     env = GetEnv().visit(ast, None)
    #     return [self.visit(x, env) for x in ast.decl]

    def visitProgram(self,ast, c=None):
        self.manageCls = classDir()
        [self.visit(x,c) for x in ast.decl]
        if not self.manageCls.entryPointControl():
            raise NoEntryPoint()

    # def visitClassDecl(self, ast: ClassDecl, o):
    #     env = {}
    #     env['current'] = ast.classname.name
    #     env['global'] = o
    #     # env['local'] = [{}]
    #     if ast.parentname is not None:
    #         if env['global'].get(ast.parentname.name) is not None:
    #             env['parent'] = ast.parentname.name
    #         else:
    #             raise Undeclared(Class(), ast.parentname.name)
    #     else:
    #         env['parent'] = None
    #     for x in ast.memlist:
    #         self.visit(x, env)

    def visitClassDecl(self, ast:ClassDecl, c=None):
        if ast.parentname: self.manageCls.classPlus(ast.classname.name,ast.parentname.name)
        else: self.manageCls.classPlus(ast.classname.name)
        [self.visit(x,(self.manageCls.classReceive(ast.classname.name),None)) for x in ast.memlist]

    # def visitAttributeDecl(self, ast: AttributeDecl, o: object):
    #     env = o
    #     if type(ast.decl) is VarDecl:
    #         self.visit(ast.decl, (Variable(), env))
    #     if type(ast.decl) is ConstDecl:
    #         self.visit(ast.decl, (Constant(), env))

    def visitAttributeDecl(self, ast, c:classControl):
        cla = c[0]
        stc = self.visit(ast.kind,c)
        const = type(ast.decl) is ConstDecl
        if type(ast.decl) is ConstDecl:
            typ = ast.decl.constType
            atrbName = ast.decl.constant.name
            typeOfEpr = self.visit(ast.decl.value,c)
            if not typeOfEpr or not typeOfEpr[1]:
                raise IllegalConstantExpression(ast.decl.value)
        else:
            typ = ast.decl.varType
            atrbName = ast.decl.variable.name
            typeOfEpr = self.visit(ast.decl.varInit,c)

        if type(typeOfEpr) is ClassType:
            if typeOfEpr.classname.name not in self.manageCls.objid:
                raise Undeclared(Class(),typeOfEpr.classname.name)

        if typeOfEpr and not self.manageCls.typeSctt(typ,typeOfEpr[0]):
            raise TypeMismatchInStatement(ast)
        cla.attPlus(atrbName,typ,stc,const)

    def visitMethodDecl(self,ast, c:classControl):
        cla = c[0]
        checkStc = type(ast.kind) is Static
        cla.mtdPlus(ast.name.name,checkStc,ast.param)
        self.visit(ast.body,(c[0],cla.mtdReceive(ast.name.name)))

    # def visitMethodDecl(self, ctx: MethodDecl, o: object):
    #     # pass
    #     returnType = None #### this line will be deleted !!!!!!
    #     if type(ctx.kind) is Instance:
    #         kind = 'instance'
    #     if type(ctx.kind) is Static:
    #         kind = 'static'
    #     if o.get(ctx.name.name) is not None:
    #         raise Redeclared(Method(), ctx.name.name)
    #     params = ctx.param        

    # def visitBlock(self, ast: Block, o):
    #     # pass
    #     inLoop, env1 = o
    #     env = {}
    #     env['global'] = env1['global']
    #     env['local'] = [{}]+env1['local']
    #     env['current'] = env1['current']
    #     env['parent'] = env1['parent']
    #     # decls = ast.decl
    #     # stmts = ast.stmt
    #     # for decl in decls:
    #     #     if type(decl) is VarDecl:
    #     #         self.visit(decl, (Variable(), env))
    #     #     if type(decl) is ConstDecl:
    #     #         self.visit(decl, (Constant(), env))
    #     # [self.visit(stmt, (inLoop, env)) for stmt in stmts]

    def visitBlock(self, ast, c:tuple):
        cla = c[0]
        mtd = c[1]
        mtd.inField()
        [self.visit(x,c) for x in ast.inst]
        mtd.outField()

    # def visitAssign(self, ast, o):
    #     inLoop, env = o
    #     print(o)
    #     # lhs = self.visit(ast.lhs, env)
    #     # exp = self.visit(ast.exp, env)
       
    #     exp = self.visit(ast.exp, env)
    #     lhs = self.visit(ast.lhs, env)

    def visitAssign(self, ast, c:tuple):
        lhs = self.visit(ast.lhs,c)
        rhs = self.visit(ast.exp,c)
        if type(lhs[0]) is ClassType and lhs[0].classname.name[-1]==',': raise Undeclared(Identifier(),lhs[0].classname.name[:-1])       
        if not isinstance(ast.lhs, LHS) or lhs[1]: raise CannotAssignToConstant(ast)
        if not self.manageCls.typeSctt(lhs[0],rhs[0]): raise TypeMismatchInStatement(ast)
        


    def visitIf(self, ast, c:tuple):
        preEnv = self.visit(ast.expr,c)
        if preEnv[0] != BoolType(): raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt,c)
        self.visit(ast.elseStmt,c)

    # def visitIf(self, ast: If, o):
    #     inLoop, env = o
    #     condType = self.visit(ast.expr, env)
    #     if condType[0] == 'mutable' or condType[0] == 'immutable' or condType[0] == 'method':
    #         if ExpUtils.isNotAccess(ast.expr):
    #             raise Undeclared(Identifier(), ast.expr.name)
    #     if type(condType[1]) is not BoolType:
    #         raise TypeMismatchInStatement(ast)
    #     self.visit(ast.thenStmt, (inLoop, env))
    #     self.visit(ast.elseStmt, (inLoop, env))        

    def visitFor(self, ast, c:tuple):
        cla = c[0]
        mtd = c[1]
        mtd.inField()
        mtd.inCircuit()
        self.visit(VarDecl(ast.id,IntType()),c)
        expr1 = self.visit(ast.expr1,c)
        expr2 = self.visit(ast.expr2,c)
        if expr1[0] != IntType() or expr2[0] != IntType(): raise TypeMismatchInStatement(ast)
        self.visit(ast.loop,c)
        mtd.outCircuit()
        mtd.outField()
    
    # def visitContinue(self, ast, o):
    #     inLoop, env = o
    #     if not inLoop:
    #         raise MustInLoop(ast)

    # def visitBreak(self, ast, o):
    #     inLoop, env = o
    #     if not inLoop:
    #         raise MustInLoop(ast)

    def visitBreak(self, ast, c:tuple):
        cla = c[0]
        mtd = c[1]
        if mtd.circ == 0: raise MustInLoop(ast)
    
    def visitContinue(self, ast, c:tuple):
        cla = c[0]
        mtd = c[1]
        if mtd.circ == 0: raise MustInLoop(ast)

    def visitReturn(self, ast, c:tuple):
        cla = c[0]
        mtd = c[1]
        mtd.rettype = self.visit(ast.expr,c)[0]

    # def visitReturn(self, ast, o):
    #     typeMethod, env = o
    #     typeReturn = self.visit(ast.expr, o)
    #     if typeReturn[0] == 'mutable' or typeReturn[0] == 'immutable' or typeReturn[0] == 'method':
    #         if ExpUtils.isNotAccess(ast.expr):
    #             raise Undeclared(Identifier(), ast.expr.name)
    #     if type(typeMethod) is not type(typeReturn[1]):
    #         if not (type(typeMethod) is FloatType and type(typeReturn[1]) is IntType):
    #             raise TypeMismatchInStatement(ast)        

    def visitCallStmt(self, ast, c=None):
        typeSml = self.visit(ast.obj,c)[0]
        if type(typeSml) is not ClassType: raise TypeMismatchInStatement(ast)
        preClaSml = typeSml.classname.name

        ise = True
        if preClaSml[-1] == ',':
            ise = False
            preClaSml = preClaSml[:-1]

        cla = self.manageCls.classReceive(preClaSml)
        mtd = cla.mtdReceive(ast.method.name)
    
        if not ise and not mtd.checkStc or ise and mtd.checkStc:
            raise IllegalMemberAccess(ast)

        if mtd.rettype: raise TypeMismatchInStatement(ast)
                    
        typPrePar = [self.visit(x,c)[0] for x in ast.param]
        if len(mtd.paratype) != len(typPrePar): raise TypeMismatchInStatement(ast)
        for x in zip(mtd.paratype,typPrePar):
            if not self.manageCls.typeSctt(x[0],x[1]): raise TypeMismatchInStatement(ast)


    def visitVarDecl(self, ast, c=None):
        cla = c[0]
        mtd = c[1]
        mtd.decVars(ast.variable.name,ast.varType)
        if type(ast.varType) is ClassType:
            if ast.varType.classname.name not in self.manageCls.objid: raise Undeclared(Class(),ast.varType.classname.name)
        varSml = self.visit(ast.varInit,c)
        if varSml and not self.manageCls.typeSctt(ast.varType,varSml[0]): raise TypeMismatchInStatement(ast)


    def visitConstDecl(self, ast, c=None):
        cla = c[0]
        mtd = c[1]
        mtd.decCons(ast.constant.name,ast.constType)
        if type(ast.constType) is ClassType:
            if ast.constType.classname.name not in self.manageCls.objid: raise Undeclared(Class(),ast.constType.classname.name)
        constSml = self.visit(ast.value,c)
        if (not constSml) or (not constSml[1]): raise IllegalConstantExpression(ast.value)
        if constSml and not self.manageCls.typeSctt(ast.constType,constSml[0]): raise TypeMismatchInConstant(ast)


    def visitBinaryOp(self, ast, c=None):
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)
        tA = left[0]
        tB = right[0]
        if ast.op in ['+','-','*','/']:
            if type(tA) not in [IntType, FloatType] or type(tB) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            if type(tA) is IntType and type(tB) is IntType: return (IntType(), left[1] and right[1])
            return (FloatType(), left[1] and right[1])
        if ast.op in ['<','<=','>','>=']:
            if type(tA) not in [IntType, FloatType] or type(tB) not in [IntType, FloatType]: raise TypeMismatchInExpression(ast)
            return (BoolType(), left[1] and right[1])
        if ast.op in ['&&','||']:
            if type(tA) is not BoolType or type(tB) is not BoolType:raise TypeMismatchInExpression(ast)
            return (BoolType(), left[1] and right[1])
        if ast.op in ['+.','==.']:
            if type(tA) is not StringType or type(tB) is not StringType:
                raise TypeMismatchInExpression(ast)
            return (StringType(), left[1] and right[1]) if ast.op == '+.' else (BoolType(), left[1] and right[1])

    def visitUnaryOp(self, ast, c=None):
        opSml = self.visit(ast.body,c)
        if ast.op in ['-'] and type(opSml[0]) not in [FloatType,IntType]: raise TypeMismatchInExpression(ast)
        elif ast.op in ['!'] and type(opSml[0]) not in [BoolType]: raise TypeMismatchInExpression(ast)
        return opSml

    def visitCallExpr(self, ast, c=None):
        typeSml = self.visit(ast.obj,c)[0]
        if type(typeSml) is not ClassType: raise TypeMismatchInExpression(ast)
        ise = True
        if typeSml.classname.name[-1] == ',':
            ise = False
            typeSml.classname.name = typeSml.classname.name[:-1]
        preClaSml = typeSml.classname.name
        cla = self.manageCls.classReceive(preClaSml)
        mtd = cla.mtdReceive(ast.method.name)
        if not ise and not mtd.checkStc or ise and mtd.checkStc: raise IllegalMemberAccess(ast)
        if not mtd.rettype: raise TypeMismatchInExpression(ast)       
        typPrePar = [self.visit(x,c)[0] for x in ast.param]
        if len(mtd.paratype) != len(typPrePar): raise TypeMismatchInExpression(ast)
        for x in zip(mtd.paratype,typPrePar):
            if not self.manageCls.typeSctt(x[0],x[1]): raise TypeMismatchInExpression(ast)
        return (mtd.rettype, False)

    def visitStatic(self,ast,c): return True

    def visitInstance(self,ast,c): return False

    def visitNewExpr(self, ast:NewExpr, c=None):
        if ast.classname.name not in self.manageCls.objid: raise Undeclared(Class(),ast.classname.name)
        if ast.param: typeOfEpr = [self.visit(x,c)[0] for x in ast.param]
        else: typeOfEpr = []
        cla = self.manageCls.classReceive(ast.classname.name)
        if len(cla.typCst) != len(typeOfEpr): raise TypeMismatchInExpression(ast)
        for x in zip(cla.typCst,typeOfEpr):
            if not self.manageCls.typeSctt(x[0],x[1]): raise TypeMismatchInExpression(ast)
        return (ClassType(ast.classname), True)

    def visitIntLiteral(self, ast:IntLiteral, c=None): return (IntType(), True)
    
    def visitFloatLiteral(self, ast:FloatLiteral, c=None): return (FloatType(), True)
    
    def visitStringLiteral(self, ast:StringLiteral, c=None): return (StringType(), True)
    
    def visitBooleanLiteral(self, ast:BooleanLiteral, c=None): return (BoolType(), True)
    
    def visitNullLiteral(self, ast:NullLiteral, c=None): return None
    
    def visitSelfLiteral(self, ast:SelfLiteral, c:tuple): return (ClassType(Id(c[0].name)), True)
    
    def visitArrayLiteral(self, ast:ArrayLiteral, c=None):
        preType = [self.visit(x,c)[0] for x in ast.value]
        if preType:
            preTypIn = preType[0]
            for i in range(len(ast.value)):
                if not self.manageCls.typeSctt(preType[i],preTypIn) or type(preType[i]) is not type(preTypIn): raise IllegalArrayLiteral(ast)
        return (ArrayType(len(preType),preTypIn), True)

    def visitId(self, ast, c:tuple):
        cla = c[0]
        mtd = c[1]
        if ast.name not in list(mtd.variable.keys()) + list(self.manageCls.objid.keys()): raise Undeclared(Identifier(),ast.name)
        if ast.name in mtd.variable: return (mtd.variable[ast.name][-1].typ, mtd.variable[ast.name][-1].constant)
        else: return (ClassType(Id(ast.name+',')), False)

    def visitArrayCell(self, ast, c=None):
        arrCell = self.visit(ast.arr,c)
        typCell = arrCell[0]
        slotSml = [self.visit(x,c)[0] for x in ast.idx]
        if type(typCell) is not ArrayType: raise TypeMismatchInExpression(ast)
        for x in slotSml:
            if type(x) is not IntType: raise TypeMismatchInExpression(ast)
        return (typCell.eleType, arrCell[1])

    # def visitFieldAccess(self, ast, o):
    #     if type(o) is tuple:
    #         checkConst, env = o
    #     else:
    #         env = o
    #     if type(ast.obj) is SelfLiteral:
    #         fieldname = self.handleAccess(
    #             ast.fieldname, (Attribute(), env, env['current']))
    #         if fieldname[2] == 'static':
    #             raise IllegalMemberAccess(ast)
    #     else:
    #         try:
    #             nameClass = self.visit(ast.obj,  env)
    #         except:
    #             if ast.obj.name in env['global']:
    #                 nameClass = ast.obj.name
    #             else:
    #                 raise Undeclared(Class(), ast.obj.name)
    #         if type(nameClass) is tuple:
    #             if type(nameClass[1]) is not ClassType:
    #                 raise TypeMismatchInExpression(ast)
    #             fieldname = self.handleAccess(
    #                 ast.fieldname, (Attribute(), env, nameClass[1].classname.name))
    #             if fieldname[2] == 'static':
    #                 raise IllegalMemberAccess(ast)
    #             if fieldname[0] == 'method':
    #                 raise TypeMismatchInExpression(ast)
    #         if type(nameClass) is str:
    #             fieldname = self.handleAccess(
    #                 ast.fieldname, (Attribute(), env, nameClass))

    #             if fieldname[2] == 'instance':
    #                 raise IllegalMemberAccess(ast)
    #             if fieldname[0] == 'method':
    #                 raise TypeMismatchInExpression(ast)
    #     return (fieldname[0], fieldname[1], None)

    def visitFieldAccess(self, ast, c:tuple):
        cla = c[0]
        mtd = c[1]
        obj = self.visit(ast.obj,c)
        typeSml = obj[0]
        if type(typeSml) is not ClassType: raise IllegalMemberAccess(ast.obj)
        ise = True
        if typeSml.classname.name[-1] == ',':
            ise = False
            typeSml.classname.name = typeSml.classname.name[:-1]
        objcls = self.manageCls.classReceive(typeSml.classname.name)
        if ast.fieldname.name not in objcls.att: raise Undeclared(Attribute(),ast.fieldname.name) 
        if not ise and not objcls.att[ast.fieldname.name].checkStc or ise and objcls.att[ast.fieldname.name].checkStc: raise IllegalMemberAccess(ast)
        att = objcls.attReceive(ast.fieldname.name)
        return (att.type, att.constant and obj[1])

    # def handleAccess(self, ast, o):
    #     kind, env, name = o
    #     if ast.name in env['global'][name]:
    #         return env['global'][name][ast.name]
    #     if env['parent'] is not None:
    #         if ast.name in env['global'][env['parent']]:
    #             return env['global'][env['parent']][ast.name]
    #     raise Undeclared(kind, ast.name)