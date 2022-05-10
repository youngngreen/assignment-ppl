import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {foo();}"""
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn();
    #     }"""
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,405))


#################################################

    # def test_1(self):
    #     """Simple program: int main() {} """
    #     input = """
    #         Class A {}
    #         Class B{}
    #         Class A{}

    #     """
    #     expect = "Redeclared Class: A"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_2(self):
    #     input = """
    #         Class A {
    #             Var numOfShape: Int = 0;
    #             Var numOfShape: Int;
    #         }
    #     """
    #     expect = "Redeclared Attribute: numOfShape"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_3(self): # not OK, please check return type of method????
    #     input = """
    #         Class A {
    #             Var $numOfShape: Int = 0;
    #             numOfShape(){}
    #         }
    #     """
    #     expect = "Redeclared Method: numOfShape"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_5(self):
    #     input = """
    #         Class A {
    #             Val $numOfShape : Int = 0;
    #             Val immuAttribute: Int = 0;
    #             test(n: Int){
    #                 Val n: Int = 5;
    #             }
    #         }
    #     """
    #     expect = "Redeclared Constant: n"
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_6(self):
    #     input = """
    #         Class A {
    #             Val $numOfShape : Int = 0;
    #             Val immuAttribute: Int = 0;
    #             test(n : Int){
    #                 Var n: Int;
    #             }
    #         }
    #     """
    #     expect = "Redeclared Variable: n"
    #     self.assertTrue(TestChecker.test(input, expect, 406))

    # def test_7(self):
    #     """Simple program: int main() {} """
    #     input = """
    #         Class A {
    #             Val $numOfShape : Int = 0;
    #             Val immuAttribute: Int = 0;
    #             test(n: Int){
    #                 Var a: Int;
    #                 Var a: Int = 6;
    #             }
    #         }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test_8(self):
    #     input = """
    #         Class B{}
    #         Class A {
    #             Var c: C ;
    #         }
    #     """
    #     expect = "Undeclared Class: C"
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test_9(self):
    #     input = """
    #         Class B{}
    #         Class A {
    #             foo(){
    #                 Var test: C;
    #             }

    #         }
    #     """
    #     expect = "Undeclared Class: C"
    #     self.assertTrue(TestChecker.test(input, expect, 409))

    def test_10(self): ## not OK, please check block {{{{}}}}
        input = """
            Class B{}
            Class A {
                int foo(){
                    {
                        {
                            {
                                {
                                    Var test: C;
                                }
                            }
                        }
                    }
                }

            }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 410))

    # def test_11(self):
    #     input = """
    #         Class B{}
    #         Class A {
    #             foo(){
    #                 Val a: Int = 0;
    #                 a = 1;
    #             }
    #         }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 411))

####################  BKEL test cases ##############################

#     def test_12(self):
#         input = Program(
#     [
#         ClassDecl(
#             Id("Program"),
#             [
#                 MethodDecl(
#                     Static(),
#                     Id("main"),
#                     [],
#                     Block([])
#                 ),
#                 AttributeDecl(
#                     Instance(),
#                     VarDecl(
#                         Id("myVar"),
#                         StringType(),
#                         StringLiteral("Hello World")
#                     )
#                 ),
#                 AttributeDecl(
#                     Instance(),
#                     VarDecl(
#                         Id("myVar"),
#                         IntType()
#                     )
#                 )
#             ]
#         )
#     ]
# )
#         expect = "Redeclared Attribute: myVar"
#         self.assertTrue(TestChecker.test(input, expect, 412))

#     def test_13(self):
#         input = Program(
#     [
#         ClassDecl(
#             Id("Program"),
#             [
#                 MethodDecl(
#                     Static(),
#                     Id("main"),
#                     [],
#                     Block(
#                         [
#                             Assign(
#                                 Id("myVar"),
#                                 IntLiteral(10)
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#     ]
# )
#         expect = "Undeclared Identifier: myVar"
#         self.assertTrue(TestChecker.test(input, expect, 413))


#     def test_14(self):
#         input = Program(
#     [
#         ClassDecl(
#             Id("Program"),
#             [
#                 MethodDecl(
#                     Static(),
#                     Id("main"),
#                     [],
#                     Block([
#                         ConstDecl(
#                             Id("myVar"),
#                             IntType(),
#                             IntLiteral(5)
#                         ),
#                         Assign(
#                             Id("myVar"),
#                             IntLiteral(10)
#                         )]
#                     )
#                 )
#             ]
#         )
#     ]
# )
#         expect = "Cannot Assign To Constant: AssignStmt(Id(myVar),IntLit(10))"
#         self.assertTrue(TestChecker.test(input, expect, 414))

#     def test_15(self):
#         input = Program(
#     [
#         ClassDecl(
#             Id("Program"),
#             [
#                 MethodDecl(
#                     Static(),
#                     Id("main"),
#                     [],
#                     Block(
#                         [
#                             Break()
#                         ]
#                     )
#                 )
#             ]
#         )
#     ]
# )
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 415))

#     def test_16(self):
#         input = Program(
#     [
#         ClassDecl(
#             Id("Program"),
#             [
#                 MethodDecl(
#                     Static(),
#                     Id("main"),
#                     [],
#                     Block(
#                         [
#                             ConstDecl(
#                                 Id("myVar"),
#                                 IntType(),
#                                 FloatLiteral(1.2)
#                             )
#                         ]
#                     )
#                 )
#             ]
#         )
#     ]
# )
#         expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(myVar),IntType,FloatLit(1.2))"
#         self.assertTrue(TestChecker.test(input, expect, 416))

######################### End BKEL test cases ################################

"""
    def test_13(self):
        input = 
        expect = "Undeclared Identifier: myVar"
        self.assertTrue(TestChecker.test(input, expect, 413))

"""
