import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_1(self):
        input = """Class Program {}"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,301))
        
    def test_2(self):
        input = """Class Rectangle : Shape {}"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"
        self.assertTrue(TestAST.test(input,expect,302))

    def test_3(self):
        input = """
        Class Rectangle {
            Var length: Int;
        }
        """
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,303))

    def test_4(self):
        input = """
        Class Rectangle {
            Val $x: Int = 10;
        }
        """
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10)))])])"
        self.assertTrue(TestAST.test(input,expect,304))

    def test_5(self):
        input = """
        Class myCla5 {
            Var a, b : Int;
        }
        """
        expect = "Program([ClassDecl(Id(myCla5),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,305))

    def test_6(self):
        input = """
        Class myCla6 {
            Val $c, d : Boolean = True, False;
        }
        """
        expect = "Program([ClassDecl(Id(myCla6),[AttributeDecl(Static,ConstDecl(Id($c),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(d),BoolType,BooleanLit(False)))])])"
        self.assertTrue(TestAST.test(input,expect,306))

    def test_7(self):
        input = """
            Class Shape {
                Val $numOfShape: Int = 0;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;
            }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,307))

    def test_8(self): # simple method
        input = """
            Class Shape {
                myMethod8() {}
            }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(myMethod8),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,308))

    def test_9(self): # simple static method
        input = """
            Class myClass9 {
                $myMethod9() {}
            }
        """
        expect = "Program([ClassDecl(Id(myClass9),[MethodDecl(Id($myMethod9),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,309))

    def test_10(self): # method with just one parameter.
        input = """
            Class myCla10 {
                $myMetd10(x : Int) {}
            }
        """
        expect = "Program([ClassDecl(Id(myCla10),[MethodDecl(Id($myMetd10),Static,[param(Id(x),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,310))  
        
    def test_11(self): # method with many parameters
        input = """
            Class myCla11 {
                $myMetd11(x, y : Int) {}
            }
        """
        expect = "Program([ClassDecl(Id(myCla11),[MethodDecl(Id($myMetd11),Static,[param(Id(x),IntType),param(Id(y),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,311))

    def test_12(self): # method with many parameters
        input = """
            Class myCla12 {
                $myMetd12(a, b : String; x, y, z: Float) {}
            }
        """
        expect = "Program([ClassDecl(Id(myCla12),[MethodDecl(Id($myMetd12),Static,[param(Id(a),StringType),param(Id(b),StringType),param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,312))

    def test_13(self): # Special method: Constructor
        input = """
            Class myCla13 {
                Constructor (x, y: Int; a: Boolean) {}
            }
        """
        expect = "Program([ClassDecl(Id(myCla13),[MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType),param(Id(a),BoolType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,313))

    def test_14(self): # Special method: Destructor
        input = """
            Class myCla14 {
                Destructor () {}
            }
        """
        expect = "Program([ClassDecl(Id(myCla14),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,314))

    def test_15(self): # Array type
        input = """
            Class myCla15 {
                Var a: Array[Int, 5];
            }
        """
        expect = "Program([ClassDecl(Id(myCla15),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType)))])])"
        self.assertTrue(TestAST.test(input,expect,315))

    def test_16(self): # Class type
        input = """
            Class myCla16 {
                Var myCar : Car;
            }
        """
        expect = "Program([ClassDecl(Id(myCla16),[AttributeDecl(Instance,VarDecl(Id(myCar),ClassType(Id(Car)),NullLiteral()))])])"
        self.assertTrue(TestAST.test(input,expect,316))


### 5. Expressions ##################

    def test_17(self): # Index operators
        input = """
            Class myCla17 {
                Var a: Int = myArr[x+2][5][y-6];
            }
        """
        expect = "Program([ClassDecl(Id(myCla17),[AttributeDecl(Instance,VarDecl(Id(a),IntType,ArrayCell(Id(myArr),[BinaryOp(+,Id(x),IntLit(2)),IntLit(5),BinaryOp(-,Id(y),IntLit(6))])))])])"
        self.assertTrue(TestAST.test(input,expect,317))


    def test_18(self): # Return
        input = """
            Class myCla18 {
                myMetd18(a: Int) {
                    Return a + b % 2;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla18),[MethodDecl(Id(myMetd18),Instance,[param(Id(a),IntType)],Block([Return(BinaryOp(+,Id(a),BinaryOp(%,Id(b),IntLit(2))))]))])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test_19(self): # Block
        input = """
            Class myCla19 {
                myMetd19() {
                    Break;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla19),[MethodDecl(Id(myMetd19),Instance,[],Block([Break]))])])"
        self.assertTrue(TestAST.test(input,expect,319))

    def test_20(self): # Continue
        input = """
            Class myCla20 {
                myMetd20() {
                    Continue;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla20),[MethodDecl(Id(myMetd20),Instance,[],Block([Continue]))])])"
        self.assertTrue(TestAST.test(input,expect,320))

    def test_21(self): # Break, Continue, Return
        input = """
            Class myCla21 {
                myMetd21() {
                    Break;
                    Continue;
                    Return x + y / 5;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla21),[MethodDecl(Id(myMetd21),Instance,[],Block([Break,Continue,Return(BinaryOp(+,Id(x),BinaryOp(/,Id(y),IntLit(5))))]))])])"
        self.assertTrue(TestAST.test(input,expect,321))  

    def test_22(self): # For/In
        input = """
            Class myCla22 {
                myMetd22() {
                    Foreach (i In 1 .. 10 By 2) {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla22),[MethodDecl(Id(myMetd22),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(2),Block([])])]))])])"
        self.assertTrue(TestAST.test(input,expect,322))

    def test_23(self): # For/In with no "By"
        input = """
            Class myCla23 {
                myMetd23() {
                    Foreach (i In 1 .. 10) {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla23),[MethodDecl(Id(myMetd23),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([])])]))])])"
        self.assertTrue(TestAST.test(input,expect,323))

    def test_24(self): # If statement: If - Elseif - Elseif - Else
        input = """
            Class myCla24 {
                myMetd24() {
                    If (a == 0) {}
                    Elseif (b < 0) {}
                    Elseif (c > 0) {}
                    Else {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla24),[MethodDecl(Id(myMetd24),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(0)),Block([]),If(BinaryOp(<,Id(b),IntLit(0)),Block([]),If(BinaryOp(>,Id(c),IntLit(0)),Block([]),Block([]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,324)) 

    def test_25(self): # If statement: If only
        input = """
            Class myCla25 {
                myMetd25() {
                    If (a == 0) {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla25),[MethodDecl(Id(myMetd25),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(0)),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,325)) 

    def test_26(self): # If statement: If - Else
        input = """
            Class myCla26 {
                myMetd26() {
                    If (a == 0) {}
                    Else {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla26),[MethodDecl(Id(myMetd26),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(0)),Block([]),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,326)) 

    def test_27(self): # If statement: If - Elseif - Elseif
        input = """
            Class myCla27 {
                myMetd27() {
                    If (a == 0) {}
                    Elseif (c > d) {}
                    Elseif (e <= f) {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla27),[MethodDecl(Id(myMetd27),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(0)),Block([]),If(BinaryOp(>,Id(c),Id(d)),Block([]),If(BinaryOp(<=,Id(e),Id(f)),Block([]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,327)) 

    def test_28(self): # If statement: If with block statements.
        input = """
            Class myCla28 {
                myMetd28() {
                    If (x == True)
                    {
                        x = x + 5;
                        Return x;
                    }
                    Elseif (False)
                    {
                        Return y;
                    }
                    Elseif (y >= 2)
                    {
                        Break;
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla28),[MethodDecl(Id(myMetd28),Instance,[],Block([If(BinaryOp(==,Id(x),BooleanLit(True)),Block([AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(5))),Return(Id(x))]),If(BooleanLit(False),Block([Return(Id(y))]),If(BinaryOp(>=,Id(y),IntLit(2)),Block([Break]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,328)) 

    def test_29(self): # Vardecl: one variable with no initial value.
        input = """
            Class myCla29 {
                myMetd29() {
                    Var a : Int;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla29),[MethodDecl(Id(myMetd29),Instance,[],Block([VarDecl(Id(a),IntType)]))])])"
        self.assertTrue(TestAST.test(input,expect,329))

    def test_30(self): # Vardecl: 2 variables with no initial value.
        input = """
            Class myCla30 {
                myMetd30() {
                    Var x, y : Boolean;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla30),[MethodDecl(Id(myMetd30),Instance,[],Block([VarDecl(Id(x),BoolType),VarDecl(Id(y),BoolType)]))])])"
        self.assertTrue(TestAST.test(input,expect,330)) 

    def test_31(self): # Vardecl: 2 variables with 2 initial values.
        input = """
            Class myCla31 {
                myMetd31() {
                    Var u, v: String = "Vietnam", "Saigon";
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla31),[MethodDecl(Id(myMetd31),Instance,[],Block([VarDecl(Id(u),StringType,StringLit(Vietnam)),VarDecl(Id(v),StringType,StringLit(Saigon))]))])])"
        self.assertTrue(TestAST.test(input,expect,331))

    def test_32(self): # Vardecl: one variable with one initial value.
        input = """
            Class myCla32 {
                myMetd32() {
                    Var z: Float = 5e12;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla32),[MethodDecl(Id(myMetd32),Instance,[],Block([VarDecl(Id(z),FloatType,FloatLit(5000000000000.0))]))])])"
        self.assertTrue(TestAST.test(input,expect,332))

    def test_33(self): # Vardecl: two or more lines of declaration.
        input = """
            Class myCla33 {
                myMetd33() {
                    Var a, b, c: Int;
                    Var x, t: Boolean = True, False;
                    Var c: Float;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla33),[MethodDecl(Id(myMetd33),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(x),BoolType,BooleanLit(True)),VarDecl(Id(t),BoolType,BooleanLit(False)),VarDecl(Id(c),FloatType)]))])])"
        self.assertTrue(TestAST.test(input,expect,333))

    def test_34(self): # Constdecl
        input = """
            Class myCla34 {
                myMetd34() {
                    Val m, n: String = "myConst", "yourConst";
                    Val x: Int;
                    Val a: Boolean = False;
                    Val h, i, k: Int = 3, 7, 8;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla34),[MethodDecl(Id(myMetd34),Instance,[],Block([ConstDecl(Id(m),StringType,StringLit(myConst)),ConstDecl(Id(n),StringType,StringLit(yourConst)),ConstDecl(Id(x),IntType,None),ConstDecl(Id(a),BoolType,BooleanLit(False)),ConstDecl(Id(h),IntType,IntLit(3)),ConstDecl(Id(i),IntType,IntLit(7)),ConstDecl(Id(k),IntType,IntLit(8))]))])])"
        self.assertTrue(TestAST.test(input,expect,334))

    def test_35(self): # Constdecls and Vardecls
        input = """
            Class myCla35 {
                myMetd35() {
                    Val i, j , k: Int;
                    Var a: Boolean = False;
                    Val x: Float = 0.25;
                    Var u, v: String;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla35),[MethodDecl(Id(myMetd35),Instance,[],Block([ConstDecl(Id(i),IntType,None),ConstDecl(Id(j),IntType,None),ConstDecl(Id(k),IntType,None),VarDecl(Id(a),BoolType,BooleanLit(False)),ConstDecl(Id(x),FloatType,FloatLit(0.25)),VarDecl(Id(u),StringType),VarDecl(Id(v),StringType)]))])])"
        self.assertTrue(TestAST.test(input,expect,335))

    def test_36(self): # Method invocation statement.
        input = """
            Class myCla36 {
                myMetd36() {
                    Shape::$getArea();
                    (x + y / 2).myAtt();
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla36),[MethodDecl(Id(myMetd36),Instance,[],Block([Call(Id(Shape),Id($getArea),[]),Call(BinaryOp(+,Id(x),BinaryOp(/,Id(y),IntLit(2))),Id(myAtt),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,336))

    def test_37(self): # Method invocation expression.
        input = """
            Class myCla37 {
                myMetd37() {
                    a = Car::$getColor();
                    m = (u - v).getSize();
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla37),[MethodDecl(Id(myMetd37),Instance,[],Block([AssignStmt(Id(a),CallExpr(Id(Car),Id($getColor),[])),AssignStmt(Id(m),CallExpr(BinaryOp(-,Id(u),Id(v)),Id(getSize),[]))]))])])"
        self.assertTrue(TestAST.test(input,expect,337))

    def test_38(self): # Attribute access.
        input = """
            Class myCla38 {
                myMetd38() {
                    a = Pet::$getHeight;
                    b = (m + n - a).getSize;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla38),[MethodDecl(Id(myMetd38),Instance,[],Block([AssignStmt(Id(a),FieldAccess(Id(Pet),Id($getHeight))),AssignStmt(Id(b),FieldAccess(BinaryOp(-,BinaryOp(+,Id(m),Id(n)),Id(a)),Id(getSize)))]))])])"
        self.assertTrue(TestAST.test(input,expect,338))

    def test_39(self): # Method and Attribute access.
        input = """
            Class myCla39 {
                myMetd39() {
                    Food::$getKind();
                    m.myAtt();
                    Animal::$getSize();
                    m = (u - v).Size;
                    a = Pet::$getVoid;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla39),[MethodDecl(Id(myMetd39),Instance,[],Block([Call(Id(Food),Id($getKind),[]),Call(Id(m),Id(myAtt),[]),Call(Id(Animal),Id($getSize),[]),AssignStmt(Id(m),FieldAccess(BinaryOp(-,Id(u),Id(v)),Id(Size))),AssignStmt(Id(a),FieldAccess(Id(Pet),Id($getVoid)))]))])])"
        self.assertTrue(TestAST.test(input,expect,339))


    def test_40(self): # index operator
        input = """
            Class myCla40 {
                myMetd40() {
                    a[1][2] = 0;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla40),[MethodDecl(Id(myMetd40),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,340))

    def test_41(self): # index operator
        input = """
            Class myCla41 {
                myMetd41() {
                    a[1][b[3]]="abc";
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla41),[MethodDecl(Id(myMetd41),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(b),[IntLit(3)])]),StringLit(abc))]))])])"
        self.assertTrue(TestAST.test(input,expect,341))

    def test_42(self): # index operator
        input = """
            Class myCla42 {
                myMetd42() {
                    (x + y - z)[u*v][5] = True && False;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla42),[MethodDecl(Id(myMetd42),Instance,[],Block([AssignStmt(ArrayCell(BinaryOp(-,BinaryOp(+,Id(x),Id(y)),Id(z)),[BinaryOp(*,Id(u),Id(v)),IntLit(5)]),BinaryOp(&&,BooleanLit(True),BooleanLit(False)))]))])])"
        self.assertTrue(TestAST.test(input,expect,342))

    def test_43(self): # Null
        input = """
            Class myCla43 {
                myMetd43() {
                    x = Null;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla43),[MethodDecl(Id(myMetd43),Instance,[],Block([AssignStmt(Id(x),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input,expect,343))

    def test_44(self): # Null (uninitialized variable in class type)
        input = """
            Class myCla44 {
                myMetd44() {
                    Var dog: Pet;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla44),[MethodDecl(Id(myMetd44),Instance,[],Block([VarDecl(Id(dog),ClassType(Id(Pet)),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input,expect,344))

    def test_45(self): # kind of main method (static or instance)
        input = """
                Class Program{
                    main() {}
                    main(x,y : Int) {}
                }
                Class notAProgram{
                    main() {}
                }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([]))]),ClassDecl(Id(notAProgram),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,345))                            

    def test_46(self): # String literal
       input = """
            Class myCla46 {
                myMetd46() {
                    Var pig: String = "hi" +. "hello";
                }
            }
       """
       expect = "Program([ClassDecl(Id(myCla46),[MethodDecl(Id(myMetd46),Instance,[],Block([VarDecl(Id(pig),StringType,BinaryOp(+.,StringLit(hi),StringLit(hello)))]))])])"
       self.assertTrue(TestAST.test(input,expect,346))

    def test_47(self): # String literal
       input = """
            Class myCla47 {
                myMetd47() {
                    Val car : Boolean = "Kim" ==. ("Yong" ==. "Un");
                }
            }
       """
       expect = "Program([ClassDecl(Id(myCla47),[MethodDecl(Id(myMetd47),Instance,[],Block([ConstDecl(Id(car),BoolType,BinaryOp(==.,StringLit(Kim),BinaryOp(==.,StringLit(Yong),StringLit(Un))))]))])])"
       self.assertTrue(TestAST.test(input,expect,347))

    def test_48(self): # New
       input = """
            Class myCla48 {
                Var x:Int = New Car();
            }
       """
       expect = "Program([ClassDecl(Id(myCla48),[AttributeDecl(Instance,VarDecl(Id(x),IntType,NewExpr(Id(Car),[])))])])"
       self.assertTrue(TestAST.test(input,expect,348))

    def test_49(self): # Null literal
       input = """
            Class myCla49 {
                Val c : String  = Null;
            }
       """
       expect = "Program([ClassDecl(Id(myCla49),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,NullLiteral()))])])"
       self.assertTrue(TestAST.test(input,expect,349))


    def test_50(self): # New expression with parameters
       input = """
       Class A {
           Val u : Int = New M(x, y + 5);
       }
       """
       expect = "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(u),IntType,NewExpr(Id(M),[Id(x),BinaryOp(+,Id(y),IntLit(5))])))])])"
       self.assertTrue(TestAST.test(input,expect,350))

    def test_51(self): # Float Literal
       input = """
       Class myCla51 {
           Var $x:Float = 7.25;
       }
       """
       expect = "Program([ClassDecl(Id(myCla51),[AttributeDecl(Static,VarDecl(Id($x),FloatType,FloatLit(7.25)))])])"
       self.assertTrue(TestAST.test(input,expect,351))

    def test_52(self): # Member access
       input = """
       Class myCla52 {
           foo(){
               x.y.z = "hello world";
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla52),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(FieldAccess(FieldAccess(Id(x),Id(y)),Id(z)),StringLit(hello world))]))])])"
       self.assertTrue(TestAST.test(input,expect,352))

    def test_53(self): # Member access
       input = """
       Class myCla53 {
           myMetd53(){
               x.y.z[0]=k.l.m(5, 4-2);
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla53),[MethodDecl(Id(myMetd53),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(x),Id(y)),Id(z)),[IntLit(0)]),CallExpr(FieldAccess(Id(k),Id(l)),Id(m),[IntLit(5),BinaryOp(-,IntLit(4),IntLit(2))]))]))])])"
       self.assertTrue(TestAST.test(input,expect,353))

    def test_54(self): # Member access
       input = """
       Class myCla54 {
           myMetd54(){
               Var x: Car = x.y.z(1,2+3) + 2;
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla54),[MethodDecl(Id(myMetd54),Instance,[],Block([VarDecl(Id(x),ClassType(Id(Car)),BinaryOp(+,CallExpr(FieldAccess(Id(x),Id(y)),Id(z),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]),IntLit(2)))]))])])"
       self.assertTrue(TestAST.test(input,expect,354))

    def test_55(self): # Array type
       input = """
       Class myCla55 {
           myMetd55(){
               Var myArr:Array[Array[Float,10],20];
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla55),[MethodDecl(Id(myMetd55),Instance,[],Block([VarDecl(Id(myArr),ArrayType(20,ArrayType(10,FloatType)))]))])])"
       self.assertTrue(TestAST.test(input,expect,355))

    def test_56(self): # New
       input = """
       Class myCla56 {
           myMetd56(){
               x = New x(5 - 1 * 3 / 2).m.n();
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla56),[MethodDecl(Id(myMetd56),Instance,[],Block([AssignStmt(Id(x),CallExpr(FieldAccess(NewExpr(Id(x),[BinaryOp(-,IntLit(5),BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(3)),IntLit(2)))]),Id(m)),Id(n),[]))]))])])"
       self.assertTrue(TestAST.test(input,expect,356))

    def test_57(self): # Self
       input = """
       Class myCla57 {
           myMetd57(){
               Return Self.getSize();
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla57),[MethodDecl(Id(myMetd57),Instance,[],Block([Return(CallExpr(Self(),Id(getSize),[]))]))])])"
       self.assertTrue(TestAST.test(input,expect,357))

    def test_58(self): # Array Literal: Index array
       input = """
       Class myCla58 {
           myMetd58(){
               Var myArr : Array[Int, 4] = Array(5, 6, 7, 8);
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla58),[MethodDecl(Id(myMetd58),Instance,[],Block([VarDecl(Id(myArr),ArrayType(4,IntType),[IntLit(5),IntLit(6),IntLit(7),IntLit(8)])]))])])"
       self.assertTrue(TestAST.test(input,expect,358))


    def test_59(self): # Array Literal: Index array
       input = """
       Class myCla59 {
           myMetd59(){
               Var myArr : Array[Array[Int,3],2] = Array(Array(3,4,5),Array(7,8,9));
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla59),[MethodDecl(Id(myMetd59),Instance,[],Block([VarDecl(Id(myArr),ArrayType(2,ArrayType(3,IntType)),[[IntLit(3),IntLit(4),IntLit(5)],[IntLit(7),IntLit(8),IntLit(9)]])]))])])"
       self.assertTrue(TestAST.test(input,expect,359))

    def test_60(self): # Array Literal: Multidimension array
       input = """
       Class myCla60 {
           myMetd60(){
               Var myArr : Array[Array[Int,3],2] = Array(Array(3,4,5),Array(7,8,9));
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla60),[MethodDecl(Id(myMetd60),Instance,[],Block([VarDecl(Id(myArr),ArrayType(2,ArrayType(3,IntType)),[[IntLit(3),IntLit(4),IntLit(5)],[IntLit(7),IntLit(8),IntLit(9)]])]))])])"
       self.assertTrue(TestAST.test(input,expect,360))

    def test_61(self): # Foreach
       input = """
       Class myCla61 {
           myMetd61(){
               Foreach (i In 1 .. 100 By 2) {
                    Var a:Boolean = True;
               }
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla61),[MethodDecl(Id(myMetd61),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([VarDecl(Id(a),BoolType,BooleanLit(True))])])]))])])"
       self.assertTrue(TestAST.test(input,expect,361))


    def test_62(self): # Foreach
       input = """
       Class myCla62 {
           myMetd62(){
               Foreach (x In 3-2 .. 5+6 By a.foo(1+2*5,"abc"+.9+8)){}
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla62),[MethodDecl(Id(myMetd62),Instance,[],Block([For(Id(x),BinaryOp(-,IntLit(3),IntLit(2)),BinaryOp(+,IntLit(5),IntLit(6)),CallExpr(Id(a),Id(foo),[BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(5))),BinaryOp(+.,StringLit(abc),BinaryOp(+,IntLit(9),IntLit(8)))]),Block([])])]))])])"
       self.assertTrue(TestAST.test(input,expect,362))

    def test_63(self): # Foreach
       input = """
       Class myCla63 {
           myMetd63(){
                Foreach (i In x::$y() .. m.g.c.g By v::$fun){
                    Foreach (i In x::$y() .. m.g.c.g By v::$fun){}
                }
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla63),[MethodDecl(Id(myMetd63),Instance,[],Block([For(Id(i),CallExpr(Id(x),Id($y),[]),FieldAccess(FieldAccess(FieldAccess(Id(m),Id(g)),Id(c)),Id(g)),FieldAccess(Id(v),Id($fun)),Block([For(Id(i),CallExpr(Id(x),Id($y),[]),FieldAccess(FieldAccess(FieldAccess(Id(m),Id(g)),Id(c)),Id(g)),FieldAccess(Id(v),Id($fun)),Block([])])])])]))])])"
       self.assertTrue(TestAST.test(input,expect,363))

    def test_64(self): # Main method: static or instance
       input = """
       Class myCla64 {
           main (){}
       }
       Class Program {
           main (a, b: Float){}
           main (){Return;}
           main (x: String){}
       }
       """
       expect = "Program([ClassDecl(Id(myCla64),[MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([])),MethodDecl(Id(main),Static,[],Block([Return()])),MethodDecl(Id(main),Instance,[param(Id(x),StringType)],Block([]))])])"
       self.assertTrue(TestAST.test(input,expect,364))

    def test_65(self): # Main method: static or instance
       input = """
       Class myCla65 {
            myMetd65() {
               X.x.y.z.view();
               (a.a[1][2][3]).row();
               Car::$ab.get();
               (Pet::$a.a[1][2]).size();
           }
       }
       """
       expect = "Program([ClassDecl(Id(myCla65),[MethodDecl(Id(myMetd65),Instance,[],Block([Call(FieldAccess(FieldAccess(FieldAccess(Id(X),Id(x)),Id(y)),Id(z)),Id(view),[]),Call(ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),Id(row),[]),Call(FieldAccess(Id(Car),Id($ab)),Id(get),[]),Call(ArrayCell(FieldAccess(FieldAccess(Id(Pet),Id($a)),Id(a)),[IntLit(1),IntLit(2)]),Id(size),[])]))])])"
       self.assertTrue(TestAST.test(input,expect,365))
    

    def test_66(self):
        input = """Class Program {}"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,366))
        
    def test_67(self):
        input = """Class Rectangle : Shape {}"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"
        self.assertTrue(TestAST.test(input,expect,367))

    def test_68(self):
        input = """
        Class Rectangle {
            Var length: Int;
        }
        """
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,368))

    def test_69(self):
        input = """
        Class Rectangle {
            Val $x: Int = 10;
        }
        """
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10)))])])"
        self.assertTrue(TestAST.test(input,expect,369))

    def test_70(self):
        input = """
        Class myCla70 {
            Var a, b : Int;
        }
        """
        expect = "Program([ClassDecl(Id(myCla70),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,370))

    def test_71(self):
        input = """
        Class myCla71 {
            Val $c, d : Boolean = True, False;
        }
        """
        expect = "Program([ClassDecl(Id(myCla71),[AttributeDecl(Static,ConstDecl(Id($c),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(d),BoolType,BooleanLit(False)))])])"
        self.assertTrue(TestAST.test(input,expect,371))

    def test_72(self):
        input = """
            Class Shape {
                Val $numOfShape: Int = 0;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;
            }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,372))

    def test_73(self): # simple method
        input = """
            Class Shape {
                myMethod8() {}
            }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(myMethod8),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,373))

    def test_74(self): # simple static method
        input = """
            Class myClass74 {
                $myMethod74() {}
            }
        """
        expect = "Program([ClassDecl(Id(myClass74),[MethodDecl(Id($myMethod74),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,374))

    def test_75(self): # method with just one parameter.
        input = """
            Class myCla75 {
                $myMetd75(x : Int) {}
            }
        """
        expect = "Program([ClassDecl(Id(myCla75),[MethodDecl(Id($myMetd75),Static,[param(Id(x),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,375))  
        
    def test_76(self): # method with many parameters
        input = """
            Class myCla76 {
                $myMetd76(x, y : Int) {}
            }
        """
        expect = "Program([ClassDecl(Id(myCla76),[MethodDecl(Id($myMetd76),Static,[param(Id(x),IntType),param(Id(y),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,376))

    def test_77(self): # method with many parameters
        input = """
            Class myCla77 {
                $myMetd77(a, b : String; x, y, z: Float) {}
            }
        """
        expect = "Program([ClassDecl(Id(myCla77),[MethodDecl(Id($myMetd77),Static,[param(Id(a),StringType),param(Id(b),StringType),param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,377))

    def test_78(self): # Special method: Constructor
        input = """
            Class myCla78 {
                Constructor (x, y: Int; a: Boolean) {}
            }
        """
        expect = "Program([ClassDecl(Id(myCla78),[MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType),param(Id(a),BoolType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,378))

    def test_79(self): # Special method: Destructor
        input = """
            Class myCla79 {
                Destructor () {}
            }
        """
        expect = "Program([ClassDecl(Id(myCla79),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,379))

    def test_80(self): # Array type
        input = """
            Class myCla80 {
                Var a: Array[Int, 5];
            }
        """
        expect = "Program([ClassDecl(Id(myCla80),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType)))])])"
        self.assertTrue(TestAST.test(input,expect,380))

    def test_81(self): # Class type
        input = """
            Class myCla81 {
                Var myCar : Car;
            }
        """
        expect = "Program([ClassDecl(Id(myCla81),[AttributeDecl(Instance,VarDecl(Id(myCar),ClassType(Id(Car)),NullLiteral()))])])"
        self.assertTrue(TestAST.test(input,expect,381))


    def test_82(self): # Index operators
        input = """
            Class myCla82 {
                Var a: Int = myArr[x+2][5][y-6];
            }
        """
        expect = "Program([ClassDecl(Id(myCla82),[AttributeDecl(Instance,VarDecl(Id(a),IntType,ArrayCell(Id(myArr),[BinaryOp(+,Id(x),IntLit(2)),IntLit(5),BinaryOp(-,Id(y),IntLit(6))])))])])"
        self.assertTrue(TestAST.test(input,expect,382))


    def test_83(self): # Return
        input = """
            Class myCla83 {
                myMetd83(a: Int) {
                    Return a + b % 2;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla83),[MethodDecl(Id(myMetd83),Instance,[param(Id(a),IntType)],Block([Return(BinaryOp(+,Id(a),BinaryOp(%,Id(b),IntLit(2))))]))])])"
        self.assertTrue(TestAST.test(input,expect,383))

    def test_84(self): # Block
        input = """
            Class myCla84 {
                myMetd84() {
                    Break;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla84),[MethodDecl(Id(myMetd84),Instance,[],Block([Break]))])])"
        self.assertTrue(TestAST.test(input,expect,384))

    def test_85(self): # Continue
        input = """
            Class myCla85 {
                myMetd85() {
                    Continue;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla85),[MethodDecl(Id(myMetd85),Instance,[],Block([Continue]))])])"
        self.assertTrue(TestAST.test(input,expect,385))

    def test_86(self): # Break, Continue, Return
        input = """
            Class myCla86 {
                myMetd86() {
                    Break;
                    Continue;
                    Return x + y / 5;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla86),[MethodDecl(Id(myMetd86),Instance,[],Block([Break,Continue,Return(BinaryOp(+,Id(x),BinaryOp(/,Id(y),IntLit(5))))]))])])"
        self.assertTrue(TestAST.test(input,expect,386))  

    def test_87(self): # For/In
        input = """
            Class myCla87 {
                myMetd87() {
                    Foreach (i In 1 .. 10 By 2) {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla87),[MethodDecl(Id(myMetd87),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(2),Block([])])]))])])"
        self.assertTrue(TestAST.test(input,expect,387))

    def test_88(self): # For/In with no "By"
        input = """
            Class myCla88 {
                myMetd88() {
                    Foreach (i In 1 .. 10) {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla88),[MethodDecl(Id(myMetd88),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([])])]))])])"
        self.assertTrue(TestAST.test(input,expect,388))

    def test_89(self): # If statement: If - Elseif - Elseif - Else
        input = """
            Class myCla89 {
                myMetd89() {
                    If (a == 0) {}
                    Elseif (b < 0) {}
                    Elseif (c > 0) {}
                    Else {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla89),[MethodDecl(Id(myMetd89),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(0)),Block([]),If(BinaryOp(<,Id(b),IntLit(0)),Block([]),If(BinaryOp(>,Id(c),IntLit(0)),Block([]),Block([]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,389)) 

    def test_90(self): # If statement: If only
        input = """
            Class myCla90 {
                myMetd90() {
                    If (a == 0) {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla90),[MethodDecl(Id(myMetd90),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(0)),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,390)) 

    def test_91(self): # If statement: If - Else
        input = """
            Class myCla91 {
                myMetd91() {
                    If (a == 0) {}
                    Else {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla91),[MethodDecl(Id(myMetd91),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(0)),Block([]),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,391)) 

    def test_92(self): # If statement: If - Elseif - Elseif
        input = """
            Class myCla92 {
                myMetd92() {
                    If (a == 0) {}
                    Elseif (c > d) {}
                    Elseif (e <= f) {}
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla92),[MethodDecl(Id(myMetd92),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(0)),Block([]),If(BinaryOp(>,Id(c),Id(d)),Block([]),If(BinaryOp(<=,Id(e),Id(f)),Block([]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,392)) 

    def test_93(self): # If statement: If with block statements.
        input = """
            Class myCla93 {
                myMetd93() {
                    If (x == True)
                    {
                        x = x + 5;
                        Return x;
                    }
                    Elseif (False)
                    {
                        Return y;
                    }
                    Elseif (y >= 2)
                    {
                        Break;
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla93),[MethodDecl(Id(myMetd93),Instance,[],Block([If(BinaryOp(==,Id(x),BooleanLit(True)),Block([AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(5))),Return(Id(x))]),If(BooleanLit(False),Block([Return(Id(y))]),If(BinaryOp(>=,Id(y),IntLit(2)),Block([Break]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,393)) 

    def test_94(self): # Vardecl: one variable with no initial value.
        input = """
            Class myCla94 {
                myMetd94() {
                    Var a : Int;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla94),[MethodDecl(Id(myMetd94),Instance,[],Block([VarDecl(Id(a),IntType)]))])])"
        self.assertTrue(TestAST.test(input,expect,394))

    def test_95(self): # Vardecl: 2 variables with no initial value.
        input = """
            Class myCla95 {
                myMetd95() {
                    Var x, y : Boolean;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla95),[MethodDecl(Id(myMetd95),Instance,[],Block([VarDecl(Id(x),BoolType),VarDecl(Id(y),BoolType)]))])])"
        self.assertTrue(TestAST.test(input,expect,395)) 

    def test_96(self): # Vardecl: 2 variables with 2 initial values.
        input = """
            Class myCla96 {
                myMetd96() {
                    Var u, v: String = "Vietnam", "Saigon";
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla96),[MethodDecl(Id(myMetd96),Instance,[],Block([VarDecl(Id(u),StringType,StringLit(Vietnam)),VarDecl(Id(v),StringType,StringLit(Saigon))]))])])"
        self.assertTrue(TestAST.test(input,expect,396))

    def test_97(self): # Vardecl: one variable with one initial value.
        input = """
            Class myCla97 {
                myMetd97() {
                    Var z: Float = 5e12;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla97),[MethodDecl(Id(myMetd97),Instance,[],Block([VarDecl(Id(z),FloatType,FloatLit(5000000000000.0))]))])])"
        self.assertTrue(TestAST.test(input,expect,397))

    def test_98(self): # Vardecl: two or more lines of declaration.
        input = """
            Class myCla98 {
                myMetd98() {
                    Var a, b, c: Int;
                    Var x, t: Boolean = True, False;
                    Var c: Float;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla98),[MethodDecl(Id(myMetd98),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(x),BoolType,BooleanLit(True)),VarDecl(Id(t),BoolType,BooleanLit(False)),VarDecl(Id(c),FloatType)]))])])"
        self.assertTrue(TestAST.test(input,expect,398))

    def test_99(self): # Constdecl
        input = """
            Class myCla99 {
                myMetd99() {
                    Val m, n: String = "myConst", "yourConst";
                    Val x: Int;
                    Val a: Boolean = False;
                    Val h, i, k: Int = 3, 7, 8;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla99),[MethodDecl(Id(myMetd99),Instance,[],Block([ConstDecl(Id(m),StringType,StringLit(myConst)),ConstDecl(Id(n),StringType,StringLit(yourConst)),ConstDecl(Id(x),IntType,None),ConstDecl(Id(a),BoolType,BooleanLit(False)),ConstDecl(Id(h),IntType,IntLit(3)),ConstDecl(Id(i),IntType,IntLit(7)),ConstDecl(Id(k),IntType,IntLit(8))]))])])"
        self.assertTrue(TestAST.test(input,expect,399))

    def test_100(self): # Constdecls and Vardecls
        input = """
            Class myCla100 {
                myMetd100() {
                    Val i, j , k: Int;
                    Var a: Boolean = False;
                    Val x: Float = 0.25;
                    Var u, v: String;
                }
            }
        """
        expect = "Program([ClassDecl(Id(myCla100),[MethodDecl(Id(myMetd100),Instance,[],Block([ConstDecl(Id(i),IntType,None),ConstDecl(Id(j),IntType,None),ConstDecl(Id(k),IntType,None),VarDecl(Id(a),BoolType,BooleanLit(False)),ConstDecl(Id(x),FloatType,FloatLit(0.25)),VarDecl(Id(u),StringType),VarDecl(Id(v),StringType)]))])])"
        self.assertTrue(TestAST.test(input,expect,400))