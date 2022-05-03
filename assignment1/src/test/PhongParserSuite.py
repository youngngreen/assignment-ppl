# Bui Thanh Phong-2020062
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_iarray1(self):
        input = """$a=array(1,5,7,12);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_iarray2(self):
        input = """$a=array(1.1,5e10,7E-12,12.);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_iarray3(self):
        input = """$a=array(\"Phong\",\"Thanh\",\"Bui\");"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
        
    def test_iarray4(self):
        input = """ 
                    $a= array(1); 
                    $b= array(1.15); 
                    $c= array(\"Phong\");"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
        
    def test_iarray5(self):
        input = """$a=array(\"Bui Thanh Phong\");"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
        
    def test_iarray6(self):
        input = """$a=array(1,1.1,1.2);"""
        expect = "Error on line 1 col 11: 1.1"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_iarray7(self):
        input = """$a=array(1,2,3,4,);"""
        expect = "Error on line 1 col 17: )"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_iarray8(self):
        input = """$a=array(123,45,1.3)"""
        expect = "Error on line 1 col 16: 1.3"
        self.assertTrue(TestParser.checkParser(input,expect,208)) 
        
    def test_iarray9(self):
        input = """$a=Array(\"Phong\");"""
        expect = "Error on line 1 col 8: ("
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_iarray10(self):
        input = """ 
                    $a=array(\"Thanh\")
                    $b=array(1,2,3);"""
        expect = "Error on line 3 col 20: $b"
        self.assertTrue(TestParser.checkParser(input,expect,210))
        
    def test_aarray1(self):
        input = """ 
                    $a=array(1 => "abc",
                            "15" => 15 + 16.1,
                            "place" => "Yanxi");"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_aarray2(self):
        input = """ $a=array(\"Phong\"=>\"24 years old\");"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_aarray3(self):
        input = """ $a=array(1=>1+2,2=>5,3=>10);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
        
    def test_aarray4(self):
        input = """ $a=array(\"Phong\"=>\"Hand some\",1=>2,3=>4);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

        
    def test_aarray5(self):
        input = """ $a=array(0x5=>15+16.1,20=>\"P\"+1);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
        
    def test_aarray6(self):
        input = """ $a=array(1.15=>456);"""
        expect = "Error on line 1 col 14: =>"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_aarray7(self):
        input = """ $a=array($P=>123);"""
        expect = "Error on line 1 col 10: $P"
        self.assertTrue(TestParser.checkParser(input,expect,217))


    def test_aarray8(self):
        input = """ $a=array(1=>$b,=>456);"""
        expect = "Error on line 1 col 16: =>"
        self.assertTrue(TestParser.checkParser(input,expect,218))
        
    def test_aarray9(self):
        input = """ $a=Array(9999=>\"Phong\");"""
        expect = "Error on line 1 col 9: ("
        self.assertTrue(TestParser.checkParser(input,expect,219)) 
        
    def test_aarray10(self):
        input = """ $a=arraY(0x999=>123,456.7=>7);"""
        expect = "Error on line 1 col 21: 456.7"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    
    def test_marray1(self):
        input = """
                    $a=array (
                        array("Volvo", "22", "18"),
                        array("a" => "BMW", "b" => 15, "c" => 13),
                        array("Saab", "5", "2"),
                        array("Land Rover", "17", "15")
                        );"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
        
    def test_marray2(self):
        input = """
                    $a=array (
                        array(0x5=>15+16.1,20=>\"P\"+1),
                        array(1,2,3)
                        );"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
        
    def test_marray3(self):
        input = """
                    $a=array (
                        array(),
                        array(),
                        array()
                        );"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
        
    def test_marray4(self):
        input = """$a=array (arraY(0x999=>123,4567=>7));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
        
    def test_marray5(self):
        input = """$a=array (arraY());"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
        
    def test_marray6(self):
        input = """
                    $a=array (
                        array(4=>5),
                        array(),
                        array(6=>\"Phong\"),
                        );"""
        expect = "Error on line 6 col 24: )"
        self.assertTrue(TestParser.checkParser(input,expect,226))
        
    def test_marray7(self):
        input = """
                    $a=array (
                        array(\"a\"=>$b),
                        array($a=>$c),
                        );"""
        expect = "Error on line 4 col 30: $a"
        self.assertTrue(TestParser.checkParser(input,expect,227))
        
    def test_marray8(self):
        input = """
                    $a=array (
                        array()
                        array(1,2,3),
                        );"""
        expect = "Error on line 4 col 24: array"
        self.assertTrue(TestParser.checkParser(input,expect,228))
        
    def test_marray9(self):
        input = """$a=array (array(1,2,3.5));"""
        expect = "Error on line 1 col 20: 3.5"
        self.assertTrue(TestParser.checkParser(input,expect,229))
        
    def test_marray10(self):
        input = """$a=array (array("Volvo",22, "18"));"""
        expect = "Error on line 1 col 24: 22"
        self.assertTrue(TestParser.checkParser(input,expect,230))
        
    def test_variable1(self):
        input = """$x = 4;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
        
    def test_variable2(self):
        input = """ 
                    $y = 5;
                    $z = 6;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
        
    def test_variable3(self):
        input = """ 
                    $a = 4.1;
                    $b = 5.e10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
        
    def test_variable4(self):
        input = """ 
                    $c = "Phong";
                    $d = "Thanh";
                    $e = "Bui";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
        
    def test_variable5(self):
        input = """ 
                    $x = "Bui"+"Thanh"+"Phong" ;
                    $y = A+2*3+$x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
        
    def test_variable6(self):
        input = """X = 4;"""
        expect = "Error on line 1 col 0: X"
        self.assertTrue(TestParser.checkParser(input,expect,236))
        
    def test_variable7(self):
        input = """ 
                    $x =1.1;
                    $y[]=2.2;"""
        expect = "Error on line 3 col 22: ["
        self.assertTrue(TestParser.checkParser(input,expect,237))
        
    def test_variable8(self):
        input = """ 
                    $x ="1"+"2";
                    $y="Phong" """
        expect = "Error on line 3 col 31: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,238))
        
    def test_variable9(self):
        input = """ 
                    _A = 100*5;
                    $y = $y+A;"""
        expect = "Error on line 2 col 20: _A"
        self.assertTrue(TestParser.checkParser(input,expect,239))
        
    def test_variable10(self):
        input = """ 
                    $c[1]  = "I";
                    $d     = "Am";
                    $e       "Phong";"""
        expect = "Error on line 2 col 22: ["
        self.assertTrue(TestParser.checkParser(input,expect,240))
        
    def test_constants1(self):
        input = """ 
                    define(A, 10);
                    define(B, "Story of Yanxi Place");"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
        
    def test_constants2(self):
        input = """ 
                    define(A, 1.2345);
                    define(B, "This too, shall pass");
                    define(C, A+B);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
        
    def test_constants3(self):
        input = """ define(Phong,"Very Handsome");"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
        
    def test_constants4(self):
        input = """ define(Thanh,$a+$b-_foo(3));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
        
    def test_constants5(self):
        input = """ 
                    define(X, 1.e10+2*4);
                    define(Y, "How wonderful life is, now you are in the world");"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
        
    def test_constants6(self):
        input = """ define($a, 10);"""
        expect = "Error on line 1 col 8: $a"
        self.assertTrue(TestParser.checkParser(input,expect,246))
        
    def test_constants7(self):
        input = """ define(_foo,"100");"""
        expect = "Error on line 1 col 8: _foo"
        self.assertTrue(TestParser.checkParser(input,expect,247))
        
    def test_constants8(self):
        input = """ 
                    define(A, 1.e5);
                    define(B, "Life is a story. Make yours the best seller");
                    define(C, A+B)"""
        expect = "Error on line 4 col 34: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,248))
        
    def test_constants9(self):
        input = """ dEfine("A", 1101);"""
        expect = "Error on line 1 col 8: A"
        self.assertTrue(TestParser.checkParser(input,expect,249))
        
    def test_constants10(self):
        input = """ 
                    define(A, 10);
                    define(B, 20);
                    define(C, 30);
                    define(D, 40);
                    define(E, 50;"""
        expect = "Error on line 6 col 32: ;"
        self.assertTrue(TestParser.checkParser(input,expect,250))
        
    def test_function1(self):
        input = """ 
                    function _foo() {
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
        
    def test_function2(self):
        input = """ 
                    function _foo($a, $b) {
                    return 0;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
        
    def test_function3(self):
        input = """ 
                    function _ABC() {
                        $u = $i + 1;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
        
    def test_function4(self):
        input = """ 
                    define(A,10);
                    function _Phong() {
                        $B=20;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
        
    def test_function5(self):
        input = """ 
                    function _Phong($a,$b) {
                        $A=9;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
        
    def test_function6(self):
        input = """ 
                    function Foo($a, $b) {
                    }"""
        expect = "Error on line 2 col 29: Foo"
        self.assertTrue(TestParser.checkParser(input,expect,256))
        
    def test_function7(self):
        input = """ 
                    function _Phong(A,B) {
                        A+B=0;
                    }"""
        expect = "Error on line 2 col 36: A"
        self.assertTrue(TestParser.checkParser(input,expect,257))
        
    def test_function8(self):
        input = """ 
                    function _xyz() {
                        function _abc(){}
                    }"""
        expect = "Error on line 3 col 24: function"
        self.assertTrue(TestParser.checkParser(input,expect,258))
        
    def test_function9(self):
        input = """ 
                    Function _123() {
                        $a="Phong";
                    }"""
        expect = "Error on line 2 col 20: Function"
        self.assertTrue(TestParser.checkParser(input,expect,259))
        
    def test_function10(self):
        input = """ 
                    function _Phong($a,$b[[[2]]]) {
                        A+B=9;
                    }"""
        expect = "Error on line 2 col 41: ["
        self.assertTrue(TestParser.checkParser(input,expect,260))
        
    def test_expressions1(self):
        input = """ 
                    function _foofoo() {
                        $a[3 + _foo(2)] = $a[$b[2]["place"]] + 4;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
        
    def test_expressions2(self):
        input = """ 
                    function _foo($a,$b) {
                        $a[3]=10;
                        $b[5][6][$c[9]] = $a[3]+A;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_expressions3(self):
        input = """ 
                    function _foofoo($a,$b) {
                        $a[2] = _foo(2) + _foo(_bar(2, 3));
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_expressions4(self):
        input = """ 
                    function _foofoo($a,$b) {
                        $a[1][2] = _foo(_foo(_foo(2)));
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_expressions5(self):
        input = """ 
                    function _foo($a,$b) {
                        $a = str2int(15)+str2float(1.5);
                        $b = str2bool(True);
                        $c = $a+$b;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_expressions6(self):
        input = """ 
                    function _foo() {
                        $a[B[1]] = 10/15;
                        B[1] = 9;
                        C = 5;
                    }"""
        expect = "Error on line 5 col 26: ="
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_expressions7(self):
        input = """ 
                    function _foo($a,$b) {
                        [$a[3]]=10;
                    }"""
        expect = "Error on line 3 col 24: ["
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_expressions8(self):
        input = """ 
                    function _foofoo($a,$b) {
                        $a[2] = Foo(2) + _foo(3);
                    }"""
        expect = "Error on line 3 col 35: ("
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_expressions9(self):
        input = """ 
                    function _foofoo($a,$b) {
                        $bx[2] = _foo(2) + _foo[3];
                    }"""
        expect = "Error on line 3 col 47: ["
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_expressions10(self):
        input = """ 
                    function _foo($a,$b) {
                        $a = str(5)+str2float(0.5);
                    }"""
        expect = "s"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_statements1(self):
        input = """ 
                    define(A,10);
                    define(B,20);
                    $a=1+A;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
        
    def test_statements2(self):
        input = """ 
                    function _foo($x,$y,$z) {
                        $x = 1;
                        $y = 2;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_statements3(self):
        input = """ 
                    function _foo($x,$y) {
                        $x = A+B;
                        $y = Z+T;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_statementss4(self):
        input = """ 
                    function _foo() {
                        if (A==B) {$a=$b;}
                        else {$a=$c;}
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_statements5(self):
        input = """ 
                    function _foo() {
                        if (A==B) {$Max="A and B";}
                        elseif (A>B) {$Max="A";}
                        elseif (A<B) {$Max="B";}
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_statements6(self):
        input = """ 
                    function _foo() {
                        if (A==1) {$Result="A is 1";}
                        elseif (A==2) {$Result="A is 2";}
                        elseif (A==3) {$Result="A is 3";}
                        elseif (A==4) {$Result="A is 4";}
                        elseif (A==5) {$Result="A is 5";}
                        else {$Result="A is greater than 5";}
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_statements7(self):
        input = """ 
                    function _foo() {
                        foreach ($a as $key => $value) {
                        _echo((("Element " +. int2str($key)) +. ": ") +. int2str($value));
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_statements8(self):
        input = """ 
                    function _foo() {
                        $sum=0;
                        foreach ($array as $key => $value) {
                            $sum=$sum+$value;
                        }
                        return $sum;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_statements9(self):
        input = """ 
                    function _foo() {
                        $a=0;
                        while ($a<5){
                            $a=$a+1;
                            _echo($a);
                        }
                        return 0;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_statements10(self):
        input = """ 
                    function _foo() {
                        while (1){}
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_statements11(self):
        input = """ 
                    function _foo() {
                        if (A<B) {
                            if (A==10) {break;}
                            $a=A;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
        
    def test_statements12(self):
        input = """ 
                    function _foo() {
                        foreach ($A as $key => $value) {
                            if ($value<5){continue;}
                            else {break;}
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_statements13(self):
        input = """ 
                    function _foo($a) {
                        if ($a<5){
                            _echo("a less than 5");
                        }
                        else {
                            _echo("a greater than 5");
                        }
                        return 0;
                    }
                    $check=_foo(1);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_statements14(self):
        input = """ 
                    define(A,10);
                    $a=1+A;
                    define(B,20);"""
        expect = "Error on line 4 col 20: define"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_statements15(self):
        input = """ 
                    function _foo($x,$y,$z) {
                        $x = 1;
                        A  = 5;
                        $y = 2;
                    }"""
        expect = "Error on line 4 col 27: ="
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_statements16(self):
        input = """ 
                    function _foo() {
                        if () {$a=$b;}
                    }"""
        expect = "Error on line 3 col 28: )"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_statements17(self):
        input = """ 
                    function _foo() {
                        if (A==B) {$Max="A and B";}
                        elseif (A>B) {$Max="A";}
                        else {break;}
                        elseif (A<B) {$Max="B";}
                    }"""
        expect = "Error on line 6 col 24: elseif"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_statements18(self):
        input = """ 
                    function _foo() {
                        foreach ($a as $key) {
                            _echo($key);
                        }
                    }"""
        expect = "Error on line 3 col 43: )"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_statements19(self):
        input = """ 
                    function _foo() {
                        while ($a<5) Do {
                            $a=$a+1;
                        }
                        return 0;
                    }"""
        expect = "Error on line 3 col 37: Do"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_statements20(self):
        input = """ function _foo($a){}
                    function _foo1($a){}
                    $check=_foo(1)+_foo1[2];"""
        expect = "Error on line 3 col 40: ["
        self.assertTrue(TestParser.checkParser(input,expect,290))
        
    def test_program1(self):
        input = """
                /*This function calculate factorial of a number*/
                function _fact($n){
                    if ($n > 1){
                        return $n * _fact($n - 1); 
                    } 
                    else {return $n;}
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
        
    def test_program2(self):
        input = """
            define(A, 10);
            define(B, "Story of Yanxi Place");
            function _foo($a, $b) {
                $i = 0;
                while ($i < 5) {
                    A[$i] = ($b + 1) * $a;
                    $u = $i + 1;
                    if ($a[$u] == 10) {
                        return $b;
                    }
                    $i = $i + 1;
                }
                return B + ": Done";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
        
    def test_program3(self):
        input = """
                /*Swap a,b*/
                function _swap($a,$b){
                    $tmp = $a;
                    $a = $b;
                    $b = $tmp;
                    $result = array();
                    $result[1]=$a;
                    $result[2]=$b;
                    return $result;
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
        
    def test_program4(self):
        input = """
                define(A,20);
                $a = array(1, 2, 3);
                function _foo()
                {
                    foreach ($a as $key => $value) {
                        _echo(A + $value +"\\n");
                    }
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
        
    def test_program5(self):
        input = """
                /*combined_dict*/
                function _combined_dict($a,$b){
                    $resul=array();
                    foreach ($a as $key => $value) {
                        $result = $result + $value;
                    } 
                    foreach ($b as $key => $value) {
                        $result = $result + $value;
                    }
                    return $result; 
                }            
                $dict_1 = array("apple","banana");
                $dict_2 = array("orange"); 
                function _print(){
                    $result=_combined_dict($dict_1,$dict_2);
                    foreach ($result as $key => $value) {
                        _echo($value +" ");
                    } 
                }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
        
    def test_program6(self):
        input = """
                /*This function calculate factorial of a number*/
                function _fact($n){
                    if ($n > 1){
                        return $n * _fact($n - 1); 
                    } 
                    else {return $n;}
                
        """
        expect = "Error on line 9 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,296))
        
    def test_program7(self):
        input = """
            define(A, 10);
            define(B, "Story of Yanxi Place");
            function _foo($a, $b) {
                i = 0;
                while ($i < 5) {
                    A[$i] = ($b + 1) * $a;
                    $u = $i + 1;
                    if ($a[$u] == 10) {
                        return $b;
                    }
                    $i = $i + 1;
                }
                return B + ": Done";
            }
        """
        expect = "i"
        self.assertTrue(TestParser.checkParser(input,expect,297))
        
    def test_program8(self):
        input = """
                /*Swap a,b*/
                function _swap($a,$b){
                    $tmp = $a;
                    $a = $b;
                    $b = $tmp;
                    $result = array($a,$b);
                    return $result;
                }
        """
        expect = "Error on line 7 col 36: $a"
        self.assertTrue(TestParser.checkParser(input,expect,298))
        
    def test_program9(self):
        input = """
                define(A,20);
                $a = array(1, 2, 3);
                foreach ($a as $key => $value) {
                    _echo(A + $value +"\\n");
                }
        """
        expect = "Error on line 4 col 16: foreach"
        self.assertTrue(TestParser.checkParser(input,expect,299))
        
    def test_program10(self):
        input = """
                /*combined_dict*/
                function _combined_dict($a,$b){
                    $resul=array();
                    foreach ($a as $key => $value) {
                        $result = $result + $value;
                    } 
                    foreach ($b as $key => $value) {
                        $result = $result + $value;
                    }
                    return $result; 
                }            
                $dict_1 = array("apple","banana");
                $dict_2 = array("orange"); 
                $result=_combined_dict($dict_1,$dict_2);
                foreach ($result as $key => $value) {
                    _echo($value +" ");
                }      
        """
        expect = "Error on line 16 col 16: foreach"
        self.assertTrue(TestParser.checkParser(input,expect,300))

