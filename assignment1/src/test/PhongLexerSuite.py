# Bui Thanh Phong-2020062
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # def test_variable(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("$abc ab","$abc,<EOF>",101))

    # def test_keyword(self):
    #     self.assertTrue(TestLexer.checkLexeme("array False","array,<EOF>",102))

    # def test_wrong_token(self):
    #     self.assertTrue(TestLexer.checkLexeme("$ab?svn","ab,Error Token ?",103))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme("15_123_128","15123128,<EOF>",104))
    def test_identifier1(self):
        self.assertTrue(TestLexer.checkLexeme("$a15_","$a15_,<EOF>",101))
        
    def test_identifier2(self):
        self.assertTrue(TestLexer.checkLexeme("$a15_ aaA ","$a15_,aaA,<EOF>",102))
        
    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("aZsa b123 c_d","aZsa,b123,c_d,<EOF>",103))
        
    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("a_1 bCd eE","a_1,bCd,eE,<EOF>",104))
        
    def test_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("a124 $567","a124,$567,<EOF>",105))
        
    def test_identifier6(self):
        self.assertTrue(TestLexer.checkLexeme("Aabcdef","Error Token A",106))
        
    def test_identifier7(self):
        self.assertTrue(TestLexer.checkLexeme("afbd A1234","afbd,Error Token A",107))
        
    def test_identifier8(self):
        self.assertTrue(TestLexer.checkLexeme("_124abc def","Error Token _",108))
        
    def test_identifier9(self):
        self.assertTrue(TestLexer.checkLexeme("$10 A1567","$10,Error Token A",109))
        
    def test_identifier10(self):
        self.assertTrue(TestLexer.checkLexeme("z11 _21","z11,Error Token _",110))
        
    def test_keyword1(self):
        self.assertTrue(TestLexer.checkLexeme("bReak cOntinue iF","bReak,cOntinue,iF,<EOF>",111))
        
    def test_keyword2(self):
        self.assertTrue(TestLexer.checkLexeme("else elsE iF whIle","else,elsE,iF,whIle,<EOF>",112))
        
    def test_keyword3(self):
        self.assertTrue(TestLexer.checkLexeme("foREACH as function tRUE","foREACH,as,function,tRUE,<EOF>",113))
        
    def test_keyword4(self):
        self.assertTrue(TestLexer.checkLexeme("fALSe aRRAY define","fALSe,aRRAY,define,<EOF>",114))
        
    def test_keyword5(self):
        self.assertTrue(TestLexer.checkLexeme("iF else iF if eLse elsE","iF,else,iF,if,eLse,elsE,<EOF>",115))
        
    def test_keyword6(self):
        self.assertTrue(TestLexer.checkLexeme("Break and","Error Token B",116))
        
    def test_keyword7(self):
        self.assertTrue(TestLexer.checkLexeme("if else If if","if,else,Error Token I",117))
        
    def test_keyword8(self):
        self.assertTrue(TestLexer.checkLexeme("truE False","truE,Error Token F",118))
        
    def test_keyword9(self):
        self.assertTrue(TestLexer.checkLexeme("array Define aS","array,Error Token D",119))
        
    def test_keyword10(self):
        self.assertTrue(TestLexer.checkLexeme("ARRAY IF ELSE AS","Error Token A",120))
        
    def test_integer1(self):
        self.assertTrue(TestLexer.checkLexeme("1234 4231 567910","1234,4231,567910,<EOF>",121))
        
    def test_integer2(self):
        self.assertTrue(TestLexer.checkLexeme("01234 05678 0456789","01234,0567,8,04567,89,<EOF>",122))
        
    def test_integer3(self):
        self.assertTrue(TestLexer.checkLexeme("0x1A 0X0123 0xABCDEF","0x1A,0X0123,0xABCDEF,<EOF>",123))
        
    def test_integer4(self):
        self.assertTrue(TestLexer.checkLexeme("0b1101 0B0011 0b0001","0b1101,0B0011,0b0001,<EOF>",124)) 
               
    def test_integer5(self):
        self.assertTrue(TestLexer.checkLexeme("123_456_789 0b11011997 30_4_1997","123456789,0b11011,997,3041997,<EOF>",125))   
             
    def test_integer6(self):
        self.assertTrue(TestLexer.checkLexeme("0x 0B423","0,x,0,Error Token B",126))    
            
    def test_integer7(self):
        self.assertTrue(TestLexer.checkLexeme("0B234 12345","0,Error Token B",127))
        
    def test_integer8(self):
        self.assertTrue(TestLexer.checkLexeme("1X 2 3 4 5 0","1,Error Token X",128)) 
               
    def test_integer9(self):
        self.assertTrue(TestLexer.checkLexeme("0x123_456 0B110_1","0x123,Error Token _",129))   
             
    def test_integer10(self):
        self.assertTrue(TestLexer.checkLexeme("01234567 0b11011_","01234567,0b11011,Error Token _",130))  
        
    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme("1.234e456 2.e+421 3.999e-534","1.234e456,2.e+421,3.999e-534,<EOF>",131))  
        
    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme("0.15 .4_5_6e1_2_3 .1_2e55","0.15,.456e123,.12e55,<EOF>",132))  
        
    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme("110197e456 30041997E-5","110197e456,30041997E-5,<EOF>",133))  
        
    def test_float4(self):
        self.assertTrue(TestLexer.checkLexeme("0.001 123. 567.8_9","0.001,123.,567.89,<EOF>",134))
                                              
    def test_float5(self):
        self.assertTrue(TestLexer.checkLexeme("1.2345.6789.101112.13_4567_999e+123","1.2345,.,6789.101112,.134567999e+123,<EOF>",135))  

    def test_float6(self):
        self.assertTrue(TestLexer.checkLexeme("e-10 E0123","e,-,10,Error Token E",136))  
        
    def test_float7(self):
        self.assertTrue(TestLexer.checkLexeme(".4_5_67e .99E-",".,4567,e,.,99,Error Token E",137))  
        
    def test_float8(self):
        self.assertTrue(TestLexer.checkLexeme("0.12345e^50001","0.12345,e,Error Token ^",138))  
        
    def test_float9(self):
        self.assertTrue(TestLexer.checkLexeme("0.001e- 1234E+","0.001,e,-,1234,Error Token E",139)) 
        
    def test_float10(self):
        self.assertTrue(TestLexer.checkLexeme("1.245248.541548.418118____E_1","1.245248,.,541548.418118,Error Token E",140))  
        
    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a string containing tab \\t\"","This is a string containing tab \\t,<EOF>",141))  
        
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme("\"He asked me: '\"Where is John?'\"\"","He asked me: '\"Where is John?'\",<EOF>",142))  
        
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme("\"Hi, my name is Phong.\"","Hi, my name is Phong.,<EOF>",143))  
        
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme("\"Hello World!!!\"","Hello World!!!,<EOF>",144)) 
        
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme("\"He is Phong \\n He very handsome!!!! \"","He is Phong \\n He very handsome!!!! ,<EOF>",145))  
        
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme("\"Everything you can imagine is real.","Unclosed String: Everything you can imagine is real.",146))  
        
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme("\"Reality continues to ruin my life.\\a\"","Illegal Escape In String: Reality continues to ruin my life.\\a",147))  
        
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme("This too, shall pass.","Error Token T",148)) 
    
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme("\"Life's too mysterious to take too serious.\"","Unclosed String: Life",149)) 
    
    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme("\"Be where \byour feet are\"","Unclosed String: Be where ",150)) 
        
    def test_iarray1(self):
        self.assertTrue(TestLexer.checkLexeme("array(1,5,7,12)","array(1,5,7,12),<EOF>",151)) 

    def test_iarray2(self):
        self.assertTrue(TestLexer.checkLexeme("array(1.1,5e10,7E-12,12.)","array(1.1,5e10,7E-12,12.),<EOF>",152)) 

    def test_iarray3(self):
        self.assertTrue(TestLexer.checkLexeme("array(\"Phong\",\"Thanh\",\"Bui\")","array(\"Phong\",\"Thanh\",\"Bui\"),<EOF>",153)) 
        
    def test_iarray4(self):
        self.assertTrue(TestLexer.checkLexeme("array(1) array(1.15) array(\"Phong\")","array(1),array(1.15),array(\"Phong\"),<EOF>",154)) 
        
    def test_iarray5(self):
        self.assertTrue(TestLexer.checkLexeme("array(\"Bui Thanh Phong\")","array(\"Bui Thanh Phong\"),<EOF>",155)) 
        
    def test_iarray6(self):
        self.assertTrue(TestLexer.checkLexeme("array(1,1.1,1.2)","array,(,1,,,1.1,,,1.2,),<EOF>",156)) 

    def test_iarray7(self):
        self.assertTrue(TestLexer.checkLexeme("array(1,2,3,4,)","array,(,1,,,2,,,3,,,4,,,),<EOF>",157)) 

    def test_iarray8(self):
        self.assertTrue(TestLexer.checkLexeme("arra(123,45,1.3)","arra,(,123,,,45,,,1.3,),<EOF>",158)) 
        
    def test_iarray9(self):
        self.assertTrue(TestLexer.checkLexeme("Array(\"Phong\")","Error Token A",159)) 
        
    def test_iarray10(self):
        self.assertTrue(TestLexer.checkLexeme("array(\"Thanh\",)","array,(,Thanh,,,),<EOF>",160)) 
        
    def test_aarray1(self):
        self.assertTrue(TestLexer.checkLexeme("array(1=>abc)","array(1=>abc),<EOF>",161)) 

    def test_aarray2(self):
        self.assertTrue(TestLexer.checkLexeme("array(\"Phong\"=>24 years old)","array(\"Phong\"=>24 years old),<EOF>",162)) 

    def test_aarray3(self):
        self.assertTrue(TestLexer.checkLexeme("array(1=>abc,2=>def,3=>10)","array(1=>abc,2=>def,3=>10),<EOF>",163)) 
        
    def test_aarray4(self):
        self.assertTrue(TestLexer.checkLexeme("array(\"Phong\"=>\"Hand some\",1=>2,3=>4)","array(\"Phong\"=>\"Hand some\",1=>2,3=>4),<EOF>",164)) 
        
    def test_aarray5(self):
        self.assertTrue(TestLexer.checkLexeme("array(0x5=>15+16.1,20=>P+1)","array(0x5=>15+16.1,20=>P+1),<EOF>",165)) 
        
    def test_aarray6(self):
        self.assertTrue(TestLexer.checkLexeme("array(1.15=>abc)","array,(,1.15,=,>,abc,),<EOF>",166)) 

    def test_aarray7(self):
        self.assertTrue(TestLexer.checkLexeme("array($P=>xyz)","array,(,$P,=,>,xyz,),<EOF>",167)) 

    def test_aarray8(self):
        self.assertTrue(TestLexer.checkLexeme("array(1=>abc,=>456)","array,(,1,=,>,abc,,,=,>,456,),<EOF>",168)) 
        
    def test_aarray9(self):
        self.assertTrue(TestLexer.checkLexeme("Array(9999=>Phong)","Error Token A",169)) 
        
    def test_aarray10(self):
        self.assertTrue(TestLexer.checkLexeme("arraY(0x999=>abc,456.7=>7)","arraY,(,0x999,=,>,abc,,,456.7,=,>,7,),<EOF>",170)) 
    
    def test_marray1(self):
        self.assertTrue(TestLexer.checkLexeme("aRRay(array(1,2,4),array(5,6,7))","aRRay(array(1,2,4),array(5,6,7)),<EOF>",171)) 
        
    def test_marray2(self):
        self.assertTrue(TestLexer.checkLexeme("array(array(1.1,5e10,7E-12,12.),array(\"Phong\",\"Thanh\",\"Bui\"))","array(array(1.1,5e10,7E-12,12.),array(\"Phong\",\"Thanh\",\"Bui\")),<EOF>",172)) 
        
    def test_marray3(self):
        self.assertTrue(TestLexer.checkLexeme("aRray(arraY(1=>2,2=>3),array(4,5,6))","aRray(arraY(1=>2,2=>3),array(4,5,6)),<EOF>",173)) 
        
    def test_marray4(self):
        self.assertTrue(TestLexer.checkLexeme("array(array(1.1,1.2,1.3))","array(array(1.1,1.2,1.3)),<EOF>",174)) 
        
    def test_marray5(self):
        self.assertTrue(TestLexer.checkLexeme("array(array(\"Phong\"=>123))","array(array(\"Phong\"=>123)),<EOF>",175)) 
        
    def test_marray6(self):
        self.assertTrue(TestLexer.checkLexeme("array(array())","array,(,array,(,),),<EOF>",176)) 
        
    def test_marray7(self):
        self.assertTrue(TestLexer.checkLexeme("ARRay(array(1,2,4),Array(5,6,7))","Error Token A",177)) 
        
    def test_marray8(self):
        self.assertTrue(TestLexer.checkLexeme("array(array(1,2,3,4),)","array,(,array(1,2,3,4),,,),<EOF>",178)) 
        
    def test_marray9(self):
        self.assertTrue(TestLexer.checkLexeme("array(array(1,2.999,3),array(1=>b))","array,(,array,(,1,,,2.999,,,3,),,,array(1=>b)),<EOF>",179)) 
        
    def test_marray10(self):
        self.assertTrue(TestLexer.checkLexeme("aRRAY(array(array()))","aRRAY,(,array,(,array,(,),),),<EOF>",180)) 
        
    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("/*The trick in life is learning\\ how to deal with it*/","<EOF>",181)) 
        
    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("/*If you want to go fast, go alone.\tIf you want to go far, go together*/","<EOF>",182)) 
        
    def test_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("/*It's OK to not be OK, \n as long as you don't stay that way.*/","<EOF>",183)) 
        
    def test_comment4(self):
        self.assertTrue(TestLexer.checkLexeme("/*I can be changed by what happens to me but \t I refuse to be reduced by it.*/","<EOF>",184)) 
        
    def test_comment5(self):
        self.assertTrue(TestLexer.checkLexeme("/*Believe you can and you're halfway there.*/","<EOF>",185)) 
        
    def test_comment6(self):
        self.assertTrue(TestLexer.checkLexeme("/*Defeat is simply a signal to press onward.","Unterminated Comment",186)) 
        
    def test_comment7(self):
        self.assertTrue(TestLexer.checkLexeme("/*Not how long, but how well you have lived is the main thing.*","Unterminated Comment",187)) 
        
    def test_comment8(self):
        self.assertTrue(TestLexer.checkLexeme("(The heart, like the stomach, wants a varied diet.*/","(,Error Token T",188)) 
        
    def test_comment9(self):
        self.assertTrue(TestLexer.checkLexeme("The trick in life is learning how to deal with it.","Error Token T",189)) 
        
    def test_comment10(self):
        self.assertTrue(TestLexer.checkLexeme("(Life is really simple, but we insist on making it complicated.*/","(,Error Token L",190)) 
        
    def test_random1(self):
        self.assertTrue(TestLexer.checkLexeme("1+2<3!=100 break \"Phong\" 1.9999e888","1,+,2,<,3,!=,100,break,Phong,1.9999e888,<EOF>",191)) 
        
    def test_random2(self):
        self.assertTrue(TestLexer.checkLexeme("array(1,2,3,4) /*This is commnent*/ 0b1101 ==. +. true ","array(1,2,3,4),0b1101,==.,+.,true,<EOF>",192)) 
        
    def test_random3(self):
        self.assertTrue(TestLexer.checkLexeme("faLse $567_abcv 12_346_810 &&%||*foReach as","faLse,$567_abcv,12346810,&&,%,||,*,foReach,as,<EOF>",193)) 
        
    def test_random4(self):
        self.assertTrue(TestLexer.checkLexeme("cONTINUE false = 100+1 - array(array(1))","cONTINUE,false,=,100,+,1,-,array(array(1)),<EOF>",194)) 
        
    def test_random5(self):
        self.assertTrue(TestLexer.checkLexeme("\"Bui '\"Thanh'\" Phong\" if 1+1 else 0.5 (3+4) 9999 123e10","Bui '\"Thanh'\" Phong,if,1,+,1,else,0.5,(,3,+,4,),9999,123e10,<EOF>",195)) 
        
    def test_random6(self):
        self.assertTrue(TestLexer.checkLexeme("456 array(1=>1111) 0 0 0 0xABCD 0.9e15 \"Phong","456,array(1=>1111),0,0,0,0xABCD,0.9e15,Unclosed String: Phong",196)) 
        
    def test_random7(self):
        self.assertTrue(TestLexer.checkLexeme("_9123 Phong Thanh Bui \\ \t \f \b","Error Token _",197)) 
        
    def test_random8(self):
        self.assertTrue(TestLexer.checkLexeme("/*Commnent is an unterminated comment.) + - * / <= >=","Unterminated Comment",198)) 
        
    def test_random9(self):
        self.assertTrue(TestLexer.checkLexeme("\"Code is my life \\n\" 100% real false deFine break","Code is my life \\n,100,%,real,false,deFine,break,<EOF>",199)) 
        
    def test_random10(self):
        self.assertTrue(TestLexer.checkLexeme("\"THE END!!! Wishing you all the best!\"","THE END!!! Wishing you all the best!,<EOF>",200)) 