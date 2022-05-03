import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

##### 3.2 Program comment #########################

    def test_lexer_1(self): # Program comment
        self.assertTrue(TestLexer.test(
            """
            ##Day la comment hop le##
            """
            , """<EOF>""", 100))

    def test_lexer_2(self): # Program comment
        self.assertTrue(TestLexer.test(
            """
            ####
            """
            , """<EOF>""", 101))

    def test_lexer_3(self): # Program comment
        self.assertTrue(TestLexer.test(
            """
            ##First comment## If its == rain: return wet; ##"Second comment"##
            """
            ,"""If,its,==,rain,:,return,wet,;,<EOF>""", 102))

    def test_lexer_4(self): # Program comment
        self.assertTrue(TestLexer.test(
            """
            ## ## func ##
            """
            , """func,Error Token #""", 103))

    def test_lexer_5(self): # Program comment
        self.assertTrue(TestLexer.test(
            """
            ## This is a
            multi-line
            comment.
            ##
            """
            , """<EOF>""", 105))

    def test_lexer_6(self): # Program comment
        self.assertTrue(TestLexer.test(
            """
            ## This is a
            multi-line
            comment.
            ##
            """
            , """<EOF>""", 106))

    def test_lexer_7(self): # Program comment
        self.assertTrue(TestLexer.test(
            """
            "Hello Saigon ##" ##
            """
            , """Hello Saigon ##,Error Token #""", 107))

    def test_lexer_8(self): # Program comment
        self.assertTrue(TestLexer.test(
            """
            "xinChao ## may be a comment? ## Hanoi"
            """
            , """xinChao ## may be a comment? ## Hanoi,<EOF>""", 108))

    def test_lexer_9(self): # Program comment
        self.assertTrue(TestLexer.test(
            """
            ## xin chao ## ban ## ##
            """
            , """ban,<EOF>""", 109))

    def test_lexer_10(self): # Program comment
        self.assertTrue(TestLexer.test(
            """
            day la comment test ## vui long bo qua #
            """
            , """day,la,comment,test,Error Token #""", 110))


### 4. String ##########################################
### Test illegal escape in string #########################

    def test_lexer_11(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "xyz\\h def"
            """
            , """Illegal Escape In String: xyz\h""", 111))

    def test_lexer_12(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "nguyen van a \k le thi C"
            """
            , """Illegal Escape In String: nguyen van a \k""", 112))

    def test_lexer_13(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "helloChina \\s japan"
            """
            , """Illegal Escape In String: helloChina \s""", 113))

    def test_lexer_14(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "Vietnam \\"
            """
            , r"""Illegal Escape In String: Vietnam \"""", 114))
    

    def test_lexer_15(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "abc - xyz"
            "hello \m laos"
            """
            , """abc - xyz,Illegal Escape In String: hello \m""", 115))

    def test_lexer_16(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "Backspace testing  \\b"
            """
            , """Backspace testing  \\b,<EOF>""", 116))

    def test_lexer_17(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "this is Newline testing\\n"
            """
            , """this is Newline testing\\n,<EOF>""", 117))

    def test_lexer_18(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            please check Illegal escape in string: "\\a" 
            """
            , """please,check,Illegal,escape,in,string,:,Illegal Escape In String: \\a""", 118))

    def test_lexer_19(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            " halow viejtnang \m\\n\c\s\d\\f "
            """
            , """Illegal Escape In String:  halow viejtnang \m""", 119))

    def test_lexer_20(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "BKHCM" let me show you "learn"
            " spycier\m "
            """
            , """BKHCM,let,me,show,you,learn,Illegal Escape In String:  spycier\m""", 120))


## Test unclosed string #########################

    def test_lexer_21(self): # Unclosed string
        self.assertTrue(TestLexer.test(
            """
            "xin chao \' Singapore"
            """
            , """Unclosed String: xin chao """, 121))

    def test_lexer_22(self): # Unclosed string
        self.assertTrue(TestLexer.test(
            """
            "Line1 string
            Line2 string"
            """
            , '''Unclosed String: Line1 string''', 122))

    def test_lexer_23(self): # Unclosed string
        self.assertTrue(TestLexer.test(
            """
            " xyz/h def <EOF>
            """
            , """Unclosed String:  xyz/h def <EOF>""", 123))

    def test_lexer_24(self): # Unclosed string
        self.assertTrue(TestLexer.test(
            """
            "
            """
            , """Unclosed String: """, 124))

    def test_lexer_25(self): # Unclosed string
        self.assertTrue(TestLexer.test(
            """
            " example example
            """
            , """Unclosed String:  example example""", 125))

    def test_lexer_26(self): # Unclosed string
        self.assertTrue(TestLexer.test(
            """
            "name '"
            """
            , '''Unclosed String: name '"''', 126))

    def test_lexer_27(self): # Unclosed string
        self.assertTrue(TestLexer.test(
            """
            myVar = "abcxyz
            """
            , """myVar,=,Unclosed String: abcxyz""", 127))

    def test_lexer_28(self): # Unclosed string
        self.assertTrue(TestLexer.test(
            """
            "hi my name is Loan
            """
            , """Unclosed String: hi my name is Loan""", 128))

    def test_lexer_29(self): # Unclosed string
        self.assertTrue(TestLexer.test(
            """
            "that's a nice car!
            """
            , """Unclosed String: that""", 129))

    def test_lexer_30(self): # Unclosed string
        self.assertTrue(TestLexer.test(
            """
            "give me the pen please!
            """
            , """Unclosed String: give me the pen please!""", 130))

  

### Test normal string ################################

    def test_lexer_31(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "He asked me: '"Where is John? '" "
            """
            , """He asked me: '"Where is John? '" ,<EOF>""", 131))

    def test_lexer_32(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "Be careful driving."
            """
            , """Be careful driving.,<EOF>""", 132))

    def test_lexer_33(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "Can you translate this for me?"
            """
            , """Can you translate this for me?,<EOF>""", 133))

    def test_lexer_34(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "Everyone knows it."
            """
            , """Everyone knows it.,<EOF>""", 134))

    def test_lexer_35(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "From time to time."
            """
            , """From time to time.,<EOF>""", 135))

    def test_lexer_36(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "He likes it very much."
            """
            , """He likes it very much.,<EOF>""", 136))

    def test_lexer_37(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "I don't speak very well."
            """
            , """Unclosed String: I don""", 137))

    def test_lexer_38(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "I hope you and your wife have a nice trip."
            """
            , """I hope you and your wife have a nice trip.,<EOF>""", 138))

    def test_lexer_39(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "I'll call you when I leave."
            """
            , """Unclosed String: I""", 139))

    def test_lexer_40(self): # Illegal escape in string
        self.assertTrue(TestLexer.test(
            """
            "That's alright."
            """
            , """Unclosed String: That""", 140))

#### 3.3 Identifiers ################################

    def test_lexer_41(self): # Test Identifiers
        self.assertTrue(TestLexer.test(
            """
            myVar x _ __ _y _0 0y x9_
            """
            , """myVar,x,_,__,_y,_0,0,y,x9_,<EOF>""", 141))

    def test_lexer_42(self): # Test Identifiers
        self.assertTrue(TestLexer.test(
            """
            WriteLn, writeln, and WRITELN
            """
            , """WriteLn,,,writeln,,,and,WRITELN,<EOF>""", 142))

    def test_lexer_43(self): # Test Identifiers
        self.assertTrue(TestLexer.test(
            """
            letter (A-Z or a-z) or underscore (_),
            """
            , """letter,(,A,-,Z,or,a,-,z,),or,underscore,(,_,),,,<EOF>""", 143))

    def test_lexer_44(self): # Test Identifiers
        self.assertTrue(TestLexer.test(
            """
            It begins with a dollar sign ($)
            """
            , """It,begins,with,a,dollar,sign,(,Error Token $""", 144))

    def test_lexer_45(self): # Test Identifiers
        self.assertTrue(TestLexer.test(
            """
            Shape::$getNumOfShape();
            """
            , """Shape,::,$getNumOfShape,(,),;,<EOF>""", 145))

    def test_lexer_46(self): # Test Identifiers
        self.assertTrue(TestLexer.test(
            """
            s = r * r * Se?lf.myPI;
            """
            , """s,=,r,*,r,*,Se,Error Token ?""", 146))

    def test_lexer_47(self): # Test Identifiers
        self.assertTrue(TestLexer.test(
            """
            Val My1stCons, My2ndCons: Int = 1 + 5, 2;
            """
            , """Val,My1stCons,,,My2ndCons,:,Int,=,1,+,5,,,2,;,<EOF>""", 147))

    def test_lexer_48(self): # Test Identifiers
        self.assertTrue(TestLexer.test(
            """
            Var $x, $y : @Int = 0, 0;
            """
            , """Var,$x,,,$y,:,Error Token @""", 148))

    def test_lexer_49(self): # Test Identifiers
        self.assertTrue(TestLexer.test(
            """
            Out.printInt(*Shape::$numOfShape);
            """
            , """Out,.,printInt,(,*,Shape,::,$numOfShape,),;,<EOF>""", 149))

    def test_lexer_50(self): # Test Identifiers
        self.assertTrue(TestLexer.test(
            """
            Val $_immutableA#ttribute: Int = 0;
            """
            , """Val,$_immutableA,Error Token #""", 150))

#### 3.4 Keywords ################################

    def test_lexer_51(self): # Test Keywords
        self.assertTrue(TestLexer.test(
            """
            Break Continue If Elseif Else
            """
            , """Break,Continue,If,Elseif,Else,<EOF>""", 151))

    def test_lexer_52(self): # Test Keywords
        self.assertTrue(TestLexer.test(
            """
            Foreach True False Array In
            """
            , """Foreach,True,False,Array,In,<EOF>""", 152))

    def test_lexer_53(self): # Test Keywords
        self.assertTrue(TestLexer.test(
            """
            Int Float Boolean String Return
            """
            , """Int,Float,Boolean,String,Return,<EOF>""", 153))

    def test_lexer_54(self): # Test Keywords
        self.assertTrue(TestLexer.test(
            """
            Null Class Val Var Self
            """
            , """Null,Class,Val,Var,Self,<EOF>""", 154))

    def test_lexer_55(self): # Test Keywords
        self.assertTrue(TestLexer.test(
            """
            Constructor Destructor New By
            """
            , """Constructor,Destructor,New,By,<EOF>""", 155))


#### 3.5 Operators ################################

    def test_lexer_56(self): # Test Operators
        self.assertTrue(TestLexer.test(
            """
            + - * / %
            """
            , """+,-,*,/,%,<EOF>""", 156))

    def test_lexer_57(self): # Test Operators
        self.assertTrue(TestLexer.test(
            """
            ! && || == =
            """
            , """!,&&,||,==,=,<EOF>""", 157))

    def test_lexer_58(self): # Test Operators
        self.assertTrue(TestLexer.test(
            """
            != < <= > >=
            """
            , """!=,<,<=,>,>=,<EOF>""", 158))

    def test_lexer_59(self): # Test Operators
        self.assertTrue(TestLexer.test(
            """
            ==. +. .+ - *
            """
            , """==.,+.,.,+,-,*,<EOF>""", 159))

    def test_lexer_60(self): # Test Operators
        self.assertTrue(TestLexer.test(
            """
            :: New&& ||
            """
            , """::,New,&&,||,<EOF>""", 160))

#### 3.6 Seperators ################################

    def test_lexer_61(self): # Test Seperators
        self.assertTrue(TestLexer.test(
            """
            ( ) [ ] . , ; : { }
            """
            , """(,),[,],.,,,;,:,{,},<EOF>""", 161))

    def test_lexer_62(self): # Test Seperators
        self.assertTrue(TestLexer.test(
            """
            (x + y - z ) Arr[5] . , ; : { Return; }
            """
            , """(,x,+,y,-,z,),Arr,[,5,],.,,,;,:,{,Return,;,},<EOF>""", 162))

#### 3.7 Literals ################################

#### 1. Integer ################################

    def test_lexer_63(self): # Test Integer
        self.assertTrue(TestLexer.test(
            """
            1234 0123 0x1A 0b11111111 1_234_567
            """
            , """1234,0123,0x1A,0b11111111,1234567,<EOF>""", 163))

    def test_lexer_64(self): # Test Integer
        self.assertTrue(TestLexer.test(
            """
            3945 09345 0X9345dfds 0b10101
            """
            , """3945,0,9345,0X9345,dfds,0b10101,<EOF>""", 164))

    def test_lexer_65(self): # Test Integer
        self.assertTrue(TestLexer.test(
            """
            68659 07474 0xAAAEEE92 0B0103495 
            """
            , """68659,07474,0xAAAEEE92,0B0,103495,<EOF>""", 165))

    def test_lexer_66(self): # Test Integer
        self.assertTrue(TestLexer.test(
            """
            0 00 0x0 0b0
            """
            , """0,00,0x0,0b0,<EOF>""", 166))

    def test_lexer_67(self): # Test Integer
        self.assertTrue(TestLexer.test(
            """
            933 0xx0435 56_354_359 0b48939
            """
            , """933,0,xx0435,56354359,0,b48939,<EOF>""", 167))

    def test_lexer_68(self): # Test Integer
        self.assertTrue(TestLexer.test(
            """
            455_4543_ 0000 00x000x 0bB045FFF
            """
            , """4554543,_,00,00,00,x000x,0,bB045FFF,<EOF>""", 168))

    def test_lexer_69(self): # Test Integer
        self.assertTrue(TestLexer.test(
            """
            _57_000_FF 00xb010101 123
            """
            , """_57_000_FF,00,xb010101,123,<EOF>""", 169))

    def test_lexer_70(self): # Test Integer
        self.assertTrue(TestLexer.test(
            """
            x00FA b0101 868 00045
            """
            , """x00FA,b0101,868,00,045,<EOF>""", 170))

#### 2. Float ################################

    def test_lexer_71(self): # Test Float
        self.assertTrue(TestLexer.test(
            """
            1.234 1.2e3 7E-10 1_234.567
            """
            , """1.234,1.2e3,7E-10,1234.567,<EOF>""", 171))

    def test_lexer_72(self): # Test Float
        self.assertTrue(TestLexer.test(
            """
            59.394,4e3,e4,.,3,.e12,<EOF>
            """
            , """59.394,,,4e3,,,e4,,,.,,,3,,,.e12,,,<,EOF,>,<EOF>""", 172))

    def test_lexer_73(self): # Test Float
        self.assertTrue(TestLexer.test(
            """
            334.44,8e90,.,4,e,3.0,3.,5.6e-1,<EOF>
            """
            , """334.44,,,8e90,,,.,,,4,,,e,,,3.0,,,3.,,,5.6e-1,,,<,EOF,>,<EOF>""", 173))

    def test_lexer_74(self): # Test Float
        self.assertTrue(TestLexer.test(
            """
            e,.,2,2,e,.,3,9,ee,.,9,00,0.0,00,03,e,<EOF>
            """
            , """e,,,.,,,2,,,2,,,e,,,.,,,3,,,9,,,ee,,,.,,,9,,,00,,,0.0,,,00,,,03,,,e,,,<,EOF,>,<EOF>""", 174))

    def test_lexer_75(self): # Test Float
        self.assertTrue(TestLexer.test(
            """
            e45 3. .0 0.e 1e12 3.000_0001
            """
            , """e45,3.,.,0,0.,e,1e12,3.0,00,_0001,<EOF>""", 175))

    def test_lexer_76(self): # Test Float
        self.assertTrue(TestLexer.test(
            """
            88e9,e,8193.,_999_3,565.,e_23,<EOF>
            """
            , """88e9,,,e,,,8193.,,,_999_3,,,565.,,,e_23,,,<,EOF,>,<EOF>""", 176))

    def test_lexer_77(self): # Test Float
        self.assertTrue(TestLexer.test(
            """
            920E12,e11,-,3,7,e,*,9,93.222,_e,<EOF>
            """
            , """920E12,,,e11,,,-,,,3,,,7,,,e,,,*,,,9,,,93.222,,,_e,,,<,EOF,>,<EOF>""", 177))

    def test_lexer_78(self): # Test Float
        self.assertTrue(TestLexer.test(
            """
            2.0,00,030000,4.444,_e,-,5,<EOF>
            """
            , """2.0,,,00,,,030000,,,4.444,,,_e,,,-,,,5,,,<,EOF,>,<EOF>""", 178))

    def test_lexer_79(self): # Test Float
        self.assertTrue(TestLexer.test(
            """
            92.e+3 +3 -3 ...00
            """
            , """92.e+3,+,3,-,3,..,.,00,<EOF>""", 179))

#### 3. Boolean ################################

    def test_lexer_80(self): # Test Boolean
        self.assertTrue(TestLexer.test(
            """
            True False True True False True False True True False
            """
            , """True,False,True,True,False,True,False,True,True,False,<EOF>""", 180))

#### 5. Indexed Array ################################

    def test_lexer_81(self): # Indexed Array
        self.assertTrue(TestLexer.test(
            """
            Array(1, 5, 7, 12)
            """
            , """Array,(,1,,,5,,,7,,,12,),<EOF>""", 181))

    def test_lexer_82(self): # Indexed Array
        self.assertTrue(TestLexer.test(
            """
            Array("Kangxi", "Yongzheng", "Qianlong")
            """
            , """Array,(,Kangxi,,,Yongzheng,,,Qianlong,),<EOF>""", 182))

    def test_lexer_83(self): # Indexed Array
        self.assertTrue(TestLexer.test(
            """
            Array("Volvo", "22", "18")
            """
            , """Array,(,Volvo,,,22,,,18,),<EOF>""", 183))

    def test_lexer_84(self): # Indexed Array
        self.assertTrue(TestLexer.test(
            """
            Array("Saab", "5", "2")
            """
            , """Array,(,Saab,,,5,,,2,),<EOF>""", 184))

    def test_lexer_85(self): # Indexed Array
        self.assertTrue(TestLexer.test(
            """
            Array("Land Rover", "17", "15")
            """
            , """Array,(,Land Rover,,,17,,,15,),<EOF>""", 185))            

    def test_lexer_86(self): # Indexed Array
        self.assertTrue(TestLexer.test(
            """
            Array(3.5 2.0 4.25)
            """
            , """Array,(,3.5,2.0,4.25,),<EOF>""", 186))

    def test_lexer_87(self): # Indexed Array
        self.assertTrue(TestLexer.test(
            """
            Array(1e2 5e-12 10 55)
            """
            , """Array,(,1e2,5e-12,10,55,),<EOF>""", 187))

    def test_lexer_88(self): # Indexed Array
        self.assertTrue(TestLexer.test(
            """
            Array("hello", "hi", "good bye")
            """
            , """Array,(,hello,,,hi,,,good bye,),<EOF>""", 188))

    def test_lexer_89(self): # Indexed Array
        self.assertTrue(TestLexer.test(
            """
            Array(True, True, False, False)
            """
            , """Array,(,True,,,True,,,False,,,False,),<EOF>""", 189))

    def test_lexer_90(self): # Indexed Array
        self.assertTrue(TestLexer.test(
            """
            Array(Yes, No, Yes, Yes)
            """
            , """Array,(,Yes,,,No,,,Yes,,,Yes,),<EOF>""", 190)) 

#### 6. Multi-dimensional arrays ################################

    def test_lexer_91(self): # Multi-dimensional arrays
        self.assertTrue(TestLexer.test(
            """
            Array (
                    Array("Volvo", "22", "18"),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
            )
            """
            , """Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>""", 191))

    def test_lexer_92(self): # Multi-dimensional arrays
        self.assertTrue(TestLexer.test(
            """
            Array (
                    Array(1, 5, 7, 12),
                    Array(3.5 2.0 4.25),
                    Array("Land Rover", "17", "15")
            )
            """
            , """Array,(,Array,(,1,,,5,,,7,,,12,),,,Array,(,3.5,2.0,4.25,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>""", 192))

    def test_lexer_93(self): # Multi-dimensional arrays
        self.assertTrue(TestLexer.test(
            """
            Array (
                    Array("hello", "hi", "good bye"),
                    Array(3.5 2.0 4.25),
                    Array(1e2 5e-12 10 55)
            )
            """
            , """Array,(,Array,(,hello,,,hi,,,good bye,),,,Array,(,3.5,2.0,4.25,),,,Array,(,1e2,5e-12,10,55,),),<EOF>""", 193))

    def test_lexer_94(self): # Multi-dimensional arrays
        self.assertTrue(TestLexer.test(
            """
            Array (
                    Array(3.5 2.0 4.25),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
            )
            """
            , """Array,(,Array,(,3.5,2.0,4.25,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>""", 194))

    def test_lexer_95(self): # Multi-dimensional arrays
        self.assertTrue(TestLexer.test(
            """
            Array (
                    Array(True, True, False, False),
                    Array("Saab", "5", "2"),
                    Array(Yes, No, Yes, Yes)
            )
            """
            , """Array,(,Array,(,True,,,True,,,False,,,False,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Yes,,,No,,,Yes,,,Yes,),),<EOF>""", 195))

    def test_lexer_96(self): # Multi-dimensional arrays
        self.assertTrue(TestLexer.test(
            """
            Array (
                    Array(1e2 5e-12 10 55),
                    Array("hello", "hi", "good bye")
                    Array(3.5 2.0 4.25)
            )
            """
            , """Array,(,Array,(,1e2,5e-12,10,55,),,,Array,(,hello,,,hi,,,good bye,),Array,(,3.5,2.0,4.25,),),<EOF>""", 196))

    def test_lexer_97(self): # Multi-dimensional arrays
        self.assertTrue(TestLexer.test(
            """
            Array (
                    Array(Yes, No, Yes, Yes)
                    Array(True, True, False, False),
                    Array("Land Rover", "17", "15")
            )
            """
            , """Array,(,Array,(,Yes,,,No,,,Yes,,,Yes,),Array,(,True,,,True,,,False,,,False,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>""", 197))

    def test_lexer_98(self): # Multi-dimensional arrays
        self.assertTrue(TestLexer.test(
            """
            Array (
                    Array("hello", "hi", "good bye"),
                    Array("Saigon", "5", "2"),
                    Array("Hanoi", "NhaTrang", "15")
            )
            """
            , """Array,(,Array,(,hello,,,hi,,,good bye,),,,Array,(,Saigon,,,5,,,2,),,,Array,(,Hanoi,,,NhaTrang,,,15,),),<EOF>""", 198))

    def test_lexer_99(self): # Multi-dimensional arrays
        self.assertTrue(TestLexer.test(
            """
            Array (
                    Array("Car", "22", "18"),
                    Array("People", "Human", "2"),
                    Array("Girl", "17", "15")
            )
            """
            , """Array,(,Array,(,Car,,,22,,,18,),,,Array,(,People,,,Human,,,2,),,,Array,(,Girl,,,17,,,15,),),<EOF>""", 199))

    def test_lexer_200(self): # Multi-dimensional arrays
        self.assertTrue(TestLexer.test(
            """
            Array (
                    Array("Cr7", "M30", "18"),
                    Array("Vietnam", "5", "2"),
                    Array("Cafe", "City", "night")
            )
            """
            , """Array,(,Array,(,Cr7,,,M30,,,18,),,,Array,(,Vietnam,,,5,,,2,),,,Array,(,Cafe,,,City,,,night,),),<EOF>""", 200))