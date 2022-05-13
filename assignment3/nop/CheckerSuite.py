import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_01(self):
        """Simple program: int main() {} """
        input = """
            Class A {}
            Class B{}
            Class A{}

        """
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_02(self):
        input = """
            Class A {
                Var numOfShape: Int = 0;
                Var numOfShape: Int;
            }
        """
        expect = "Redeclared Attribute: numOfShape"
        self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_03(self): # fail
    #     input = """
    #         Class A {
    #             Var $numOfShape: Int = 0;
    #             numOfShape(){}
    #         }
    #     """
    #     expect = "Redeclared Method: numOfShape"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    def test_05(self):
        input = """
            Class A {
                Val $numOfShape : Int = 0;
                Val immuAttribute: Int = 0;
                test(n: Int){
                    Val n: Int = 5;
                }
            }
        """
        expect = "Redeclared Constant: n"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_06(self):
        input = """
            Class A {
                Val $numOfShape : Int = 0;
                Val immuAttribute: Int = 0;
                test(n : Int){
                    Var n: Int;
                }
            }
        """
        expect = "Redeclared Variable: n"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_07(self):
        """Simple program: int main() {} """
        input = """
            Class A {
                Val $numOfShape : Int = 0;
                Val immuAttribute: Int = 0;
                test(n: Int){
                    Var a: Int;
                    Var a: Int = 6;
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    # def test_08(self): # fail
    #     input = """
    #         Class B{}
    #         Class A {
    #             Var c: C ;
    #         }
    #     """
    #     expect = "Undeclared Class: C"
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    def test_09(self):
        input = """
            Class B{}
            Class A {
                def(){
                    Var test: C;
                }

            }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 409))

    # def test_10(self): ## not OK, please check block {{{{}}}}
    #     input = """
    #         Class B{}
    #         Class A {
    #             int def(){
    #                 {
    #                     {
    #                         {
    #                             {
    #                                 Var test: C;
    #                             }
    #                         }
    #                     }
    #                 }
    #             }

    #         }
    #     """
    #     expect = "Undeclared Class: C"
    #     self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """
            Class B{}
            Class A {
                def(){
                    Val a: Int = 0;
                    a = 1;
                }
            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 411))

####################  BKEL test cases ##############################

    def test_12(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block([])
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        Id("myVar"),
                        StringType(),
                        StringLiteral("Hello World")
                    )
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        Id("myVar"),
                        IntType()
                    )
                )
            ]
        )
    ]
)
        expect = "Redeclared Attribute: myVar"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block(
                        [
                            Assign(
                                Id("myVar"),
                                IntLiteral(10)
                            )
                        ]
                    )
                )
            ]
        )
    ]
)
        expect = "Undeclared Identifier: myVar"
        self.assertTrue(TestChecker.test(input, expect, 413))


    def test_14(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block([
                        ConstDecl(
                            Id("myVar"),
                            IntType(),
                            IntLiteral(5)
                        ),
                        Assign(
                            Id("myVar"),
                            IntLiteral(10)
                        )]
                    )
                )
            ]
        )
    ]
)
        expect = "Cannot Assign To Constant: AssignStmt(Id(myVar),IntLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block(
                        [
                            Break()
                        ]
                    )
                )
            ]
        )
    ]
)
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_16(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block(
                        [
                            ConstDecl(
                                Id("myVar"),
                                IntType(),
                                FloatLiteral(1.2)
                            )
                        ]
                    )
                )
            ]
        )
    ]
)
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(myVar),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 416))

######################### End BKEL test cases ################################

    def test_17(self):
        """Simple program: int main() {} """
        input = """ 
                        Class B{
                            Var b:Int = 1;
                            c(){}
                        }
                        Class A:B{
                        }
                        Class C{
                            e(){
                                Var a:A;
                                a.b= 2;
                                a.c();
                                a.e();
                            }
                        }"""
        expect = "Undeclared Method: e"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Val a:Int = 2;
                                a=3;
                            }
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 2;
                                Var b:Array[Int,5];
                                b[1]=1;
                                a[1]=1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 2;
                                Var b:Array[Int,5];
                                b[1.2]=1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),[FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 1+2;
                                Var b:Float = 1+2.2;
                                Var c:Float = 1+True;
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 421))


    def test_23(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var c:Float = 1.22;
                                Var d:Boolean = (("abc" +. "def") ==. "ghi") || False;
                                Var e:Boolean = 0==False;
                                Var f:Boolean = "abc"||1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(||,StringLit(abc),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var c:Float = --------1.22;
                                Var d:Boolean = !((("abc" +. "def") ==. "ghi") || False);
                                Var e:Float = !!!!--1.22;
                            }
                        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,UnaryOp(-,UnaryOp(-,FloatLit(1.22))))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        input = """
            Class A {
                Var numOfShape: Int = 0;
                Var numOfShape: Int;
            }
        """
        expect = "Redeclared Attribute: numOfShape"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                Var e:String = a.c(1.1,2);
                            }
                        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(c),[FloatLit(1.1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """
            Class A {
                Val $numOfShape : Int = 0;
                Val immuAttribute: Int = 0;
                test(n: Int){
                    Val n: Int = 5;
                }
            }
        """
        expect = "Redeclared Constant: n"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                Var e:String = a.c(1,2);
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(e),StringType,CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        input = """
            Class A {
                Val $numOfShape : Int = 0;
                Val immuAttribute: Int = 0;
                test(n : Int){
                    Var n: Int;
                }
            }
        """
        expect = "Redeclared Variable: n"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                a.d();
                                Var e:Float = a.b;
                                Var f:Float = a.d;
                            }
                        }"""
        expect = "Undeclared Attribute: d"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        """Simple program: int main() {} """
        input = """
            Class A {
                Val $numOfShape : Int = 0;
                Val immuAttribute: Int = 0;
                test(n: Int){
                    Var a: Int;
                    Var a: Int = 6;
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                Val e:String = a.c(1,2);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_33(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Val a : Int = 1.2;
                            }
                        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 433))


    def test_35(self):
        input = """
            Class B{}
            Class A {
                def(){
                    Var test: C;
                }

            }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                a.d(1,2,"a");
                                a.d(1,2,3);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """
            Class B{}
            Class A {
                def(){
                    Val a: Int = 0;
                    a = 1;
                }
            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                a.d(1+2,2--2.0,"a"==."bcd");
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block([])
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        Id("myVar"),
                        StringType(),
                        StringLiteral("Hello World")
                    )
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        Id("myVar"),
                        IntType()
                    )
                )
            ]
        )
    ]
)
        expect = "Redeclared Attribute: myVar"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class A{}
                        Class C{
                            e(){
                                Var a:B = New B();
                                a = New A();
                            }
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),NewExpr(Id(A),[]))"
        self.assertTrue(TestChecker.test(input, expect, 440))


    def test_42(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Val a:Int = 1;
                                Val b:Float = 1;
                                Val c:Float = a+b;
                                Val d:Int = a+b;
                            }
                        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(d),IntType,BinaryOp(+,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 1;
                                Var b:Float = 1;
                                Var c:Float = a+b;
                                Var d:Int = a+b;
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(d),IntType,BinaryOp(+,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 1;
                                Var b:Int = 1;
                                If (True){
                                    Var a:Int = 2;
                                }
                                Elseif(True){
                                    Var a:Int = 2;
                                }
                                Else{
                                    Var a:Int = 2;
                                }
                                Var b:Int = 2 ;
                            }
                        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 1;
                                Var b:Int = 1;
                                Var i:Int = 0;
                                Foreach(i In 1 .. 10 By 1){
                                    Var a:Int = 1;
                                    Break;
                                    If (True){
                                        Var a:Int = 1;
                                        Continue;
                                    }
                                }
                                Var b:Int = 2 ;
                            }
                        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var i:Int = 0;
                                Foreach(i In 1 .. 10 By 1){
                                    Var a:Int = 1;
                                    Break;
                                    If (True){
                                        Var a:Int = 1;
                                        Continue;
                                    }
                                }
                                Break;
                            }
                        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var i:Int = 0;
                                Foreach(i In 1 .. 10 By 1){
                                    Var a:Int = 1;
                                    Break;
                                    If (True){
                                        Var a:Int = 1;
                                        Continue;
                                    }
                                }
                                Continue;
                            }
                        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_48(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 0;
                                Val b:Int = 1;
                                Val c:Float = b+1;
                                Val d:Float = a+1;
                            }
                        }"""
        expect = "Illegal Constant Expression: BinaryOp(+,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_49(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 0;
                                Val b:Int = 1;
                                Val c:Float = b+1;
                                Val d:Float = a + "abc";
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 0;
                                Val b:Int = 1;
                                Val c:Float = b+1;
                                Val d:Float = a + "abc";
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 0;
                                Val b:Int = 1;
                                Val c:Float = b+1;
                            }
                        }
                         Class Car {
                            Var a : Int = 10;
                            def() {
                                Var x : Int = Self.a;
                                Var y : Int = a;
                            }
                        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_53(self):
        """Simple program: int main() {} """
        input = """         
                        Class B{
                        myMethod(){
                            count.def();
                        }
                        }"""
        expect = "Undeclared Identifier: count"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_54(self):
        """Simple program: int main() {} """
        input = """
                        Class A{
                            Var $a:Int = 5;
                            Var b:Int = 4;
                        }         
                        Class B{
                        myMethod(){
                            Var b:Int = A::$a;
                            b = count.def();
                        }
                        }"""
        expect = "Undeclared Identifier: count"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_55(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            Var $a:Int = 5;
                            Var b:Int = 4;
                        }         
                        Class B{
                        myMethod(){
                            Var b:Int = A::$a;
                            b = A.b;
                        }
                        }"""
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_56(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            Var $a:Int = 5;
                            Var b:Int = 4;
                        }         
                        Class B{
                        myMethod(){
                            Var b:A = New A();
                            Var c:Int = b.b;
                            Var d:Int = b::$a;
                        }
                        }"""
        expect = "Illegal Member Access: FieldAccess(Id(b),Id($a))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){}
                            b(){}
                        }         
                        Class B{
                        myMethod(){
                            A::$a();
                            Var b:A = New A();
                            b.b();
                            b::$a();
                        }
                        }"""
        expect = "Illegal Member Access: Call(Id(b),Id($a),[])"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_58(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){}
                            b(){}
                        }         
                        Class B{
                        myMethod(){
                            A::$a();
                            Var b:A = New A();
                            b.b();
                            A.b();
                        }
                        }"""
        expect = "Illegal Member Access: Call(Id(A),Id(b),[])"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_59(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        }         
                        Class B{
                        myMethod(){
                            Var b:A = New A();
                            Var c:Int = A::$a();
                            c = b.b();
                            c = A.b();
                        }
                        }"""
        expect = "Illegal Member Access: CallExpr(Id(A),Id(b),[])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_60(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        }         
                        Class B{
                        myMethod(){
                            Var b:A = New A();
                            Var c:Int = A::$a();
                            c = b.b();
                            c = b::$a();
                        }
                        }"""
        expect = "Illegal Member Access: CallExpr(Id(b),Id($a),[])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_62(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            c(){
                                Return 1;
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_63(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            $main(){
                                Return 1;
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_64(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            $main(a:Int){
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_65(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            main(){}
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_66(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            Var a:Int = 1;
                            def(){
                                Var b:Int = Self.a;
                                Var c:Int = a;
                            }
                        } """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_67(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                        Val y:Int=10;
                        }
                        Class B{
                        Var x:A;
                        myMethod (){
                            Val z:Int=Self.x.y;
                        }
                        } """
        expect = "Illegal Constant Expression: FieldAccess(FieldAccess(Self(),Id(x)),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_68(self):
        """Simple program: int main() {} """
        input = """     
                        Class B{
                        Var x:Int = 1;
                        def(){
                            Return 1;
                        }
                        myMethod (){
                            Var a:Int = Self.x;
                            a = Self.def();
                            Var b:String = Self.def();
                        }
                        } """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),StringType,CallExpr(Self(),Id(def),[]))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_69(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block(
                        [
                            ConstDecl(
                                Id("myVar"),
                                IntType(),
                                FloatLiteral(1.2)
                            )
                        ]
                    )
                )
            ]
        )
    ]
)
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(myVar),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           myMethod() {                        
                           }                        
                        }                        
                        Class Test{                        
                          test() {                        
                                Var e: E = New E();                        
                                Return e.myMethod;                       
                          }                        
                        } """
        expect = "Undeclared Attribute: myMethod"
        self.assertTrue(TestChecker.test(input, expect, 470))


    def test_73(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           $myMethod() {                        
                           } 
                           Constructor(a:Int){
                           }                       
                        }                        
                        Class Test{ 
                            cak(){                     
                                E::$myMethod();   
                                E::$def();                             
                            }
                        }"""
        expect = "Undeclared Method: $def"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_74(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           $myMethod() { 
                                Return 1;                       
                           } 
                           Constructor(a:Int){
                           }                       
                        }                        
                        Class Test{ 
                            cak(){                     
                                Var a:Int = E::$myMethod();   
                                Var b:Int = E::$def();                             
                            }
                        }"""
        expect = "Undeclared Method: $def"
        self.assertTrue(TestChecker.test(input, expect, 474))


    def test_76(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;                      
                        }                        
                        Class B{ 
                            Var b:A = New A(); 
                        }
                        Class C{
                            def(){
                                Var c:B = New B();
                                Var e:Int = c.b.a;
                                Var f:Int = c.g.a;
                            }
                        }"""
        expect = "Undeclared Attribute: g"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;                      
                        }                        
                        Class B{ 
                            Var $b:A = New A(); 
                        }
                        Class C{
                            def(){
                                Var c:B = New B();
                                Var e:Int = B::$b.a;
                                Var f:Int = B::$b.g;
                            }
                        }"""
        expect = "Undeclared Attribute: g"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_78(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;                      
                        }                        
                        Class B{ 
                            Var $b:A = New A(); 
                        }
                        Class C{
                            def(){
                                Var c:B = New B();
                                Var e:Int = B::$b.a;
                                Var f:Int = B::$g.a;
                            }
                        }"""
        expect = "Undeclared Attribute: $g"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_79(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           def(){
                                Return 1;
                           }                      
                        }                        
                        Class B{ 
                            Var b:A = New A();
                            def(){
                                Return New A();
                            }
                        }
                        Class C{
                            def(){
                                Var c:B = New B();
                                Var e:Int = c.b.a;
                                e = c.b.def();
                                e = c.def().a;
                                e = c.def().def();
                                Var f:Int = c.def();
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(f),IntType,CallExpr(Id(c),Id(def),[]))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_80(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           def(x:Float; y:String){
                           }                      
                        }                        
                        Class B{ 
                            Var b:A = New A();
                            def(){
                                Return New A();
                            }
                        }
                        Class C{
                            def(){
                                Var c:B = New B();
                                c.def().def(1,"a");
                                c.b.def(1.2,"a");
                                c.b.def(1,1.2);
                            }
                        }"""
        expect = "Type Mismatch In Statement: Call(FieldAccess(Id(c),Id(b)),Id(def),[IntLit(1),FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input, expect, 480))


    def test_82(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           defExp(x:Float; y:String){
                                Return 1;
                           }  
                           defCall(x:Float; y:String){}                    
                        }                        
                        Class B{ 
                            Var b:A = New A();
                            def(){
                                Return New A();
                            }
                            def2(){
                                Var e:Int = Self.b.a;
                                e = Self.b.defExp(1, "a");
                                e = Self.def().a;
                                e = Self.def().defExp(1, "a");
                                Self.b.defCall(1, "a");
                                Self.def().defCall(1, "a");
                                Self.g().defCall(1, "a");
                            }
                        }"""
        expect = "Undeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           $defExp1(x:Float; y:String){
                                Return Self.a;
                           } 
                           $defExp2(x:Float; y:String){
                                Return x;
                           }  
                           $defExp3(x:Float; y:String){
                                Return y;
                           }               
                        }                        
                        Class B{
                            def2(){
                                Var e:Float = (New A()).a;
                                e = A::$defExp1(1, "a");
                                e = A::$defExp2(1, "a");
                                Var f:String = A::$defExp3(1, "a");
                                Var g:Float = A::$defExp3(1, "a");
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(g),FloatType,CallExpr(Id(A),Id($defExp3),[IntLit(1),StringLit(a)]))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_84(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block(
                        [
                            Break()
                        ]
                    )
                )
            ]
        )
    ]
)
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_85(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $defExp1(x:Float; y:String){
                                Var a:Array[Int, 2] = Array(1,1);
                                a = Array(1,1,1);
                           }               
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_86(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $defExp1(x:Float; y:String){
                                Var a:Array[Int, 2] = Array(1,1);
                                a = Array("a", "b");
                           }               
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[StringLit(a),StringLit(b)])"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block([
                        ConstDecl(
                            Id("myVar"),
                            IntType(),
                            IntLiteral(5)
                        ),
                        Assign(
                            Id("myVar"),
                            IntLiteral(10)
                        )]
                    )
                )
            ]
        )
    ]
)
        expect = "Cannot Assign To Constant: AssignStmt(Id(myVar),IntLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $defExp1(x:Float; y:String){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                Var b: Array[Array[Int, 2],2] = Array(Array("a","a"),Array("a","abc"));
                           }               
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(b),ArrayType(2,ArrayType(2,IntType)),[[StringLit(a),StringLit(a)],[StringLit(a),StringLit(abc)]])"
        self.assertTrue(TestChecker.test(input, expect, 488))


    def test_91(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $defExp1(){
                                Val a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                a[1] = Array(1,1);
                           }               
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(a),[IntLit(1)]),[IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                        Val a:Int = 2;
                           $defExp1(){
                                Self.a = "abc";
                           }               
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 492))



    def test_95(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block(
                        [
                            Assign(
                                Id("myVar"),
                                IntLiteral(10)
                            )
                        ]
                    )
                )
            ]
        )
    ]
)
        expect = "Undeclared Identifier: myVar"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input = """
                        Class A
                        {
                        }
                        Class B:A
                        {
                            Var a: A = New C();
                        }
            """

        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 496))

