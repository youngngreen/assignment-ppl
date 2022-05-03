# Huỳnh Bảo Minh -2020047
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """Class MyClass_61 {
                myMethod_61(){
                    a = (c == d) <= (b != 0);   
                }
            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_2(self):
        input = """
            CLass Rectangle{
            Val a : Int =12;
        }

        """
        expect = "Error on line 2 col 12: CLass"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_3(self):
        input = """CLass Rectangle{
            Val a : Int =12+3*3/2;
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_4(self):
        input = """CLass Rectangle{
            Val a : Int =b[3] + c[2];
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_5(self):
        input = """CLass Rectangle{
            Val a : Int =b[3][2] + c[1][2];
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_6(self):
        input = """CLass Rectangle{
            Val a : Int =2 - (3 + 2);
            b= TruE;
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_7(self):
        input = """CLass Rectangle{
            Val a : int =2 - (3 + 2);
            
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_8(self):
        input = """CLaSS _ectangle{
            VaL a : ArRay[Int,5];
            
        }
        """
        expect = "Error on line 1 col 0: CLaSS"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_9(self):
        
        input = """cLass Rectangle{
            Val a : Array[Int,5];
            
        }
        """
        expect = "Error on line 1 col 0: cLass"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_10(self):
        input = """CLass Rectangle{
            Val a : String= "Hello" +. "World";
            
        }
        """
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_11(self):
        input = """Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_12(self):
        input = """Class Shape {
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_13(self):
        input = """
        CLass Rectangle: Shape {
                getArea() {
            Return Self.length * Self.width; }
            }
        """
        expect = "Error on line 2 col 8: CLass"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_14(self):
        input = """
        Class Program {
            main() {
        Out.printInt(Shape::$numOfShape); }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_15(self):
        input = """
        Class Program {
            main() {
                a= New People("Peter",23,"IT");
                
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_16(self):
        input = """
        Class Program {
            main() {
                a= New People("Peter",23,"IT");   
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_17(self):
        input = """
        Class Program {
            main() {
                a= New Vehicle();
                a.branch="BMW";
                a.model="i5";
                a.cost=100000;
                a.country="Germany" ;  
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_18(self):
        input = """
        Class Program {
            main() {
                Var a : Array[String,3]=Array("Kangxi", "Yongzheng", "Qianlong");
                a[1]="Minh";
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_19(self):
        input = """
        Class Program {
            main() {
                Var a : Array[Int,4]=Array(1, 5, 7, 12);
                a[1]=a[2]+a[3];
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_20(self):
        input = """
        Class Program {
            main() {
                Var a : Array[Array[String,3],3]=Array (
                    Array("Volvo", "22", "18"),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
            );
                
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_21(self):
        input = """
        Class Program {
            main() {
                Var a : Array[Boolean,3]=array(True,False,true); 
        }
        }
        """
        expect = "Error on line 4 col 46: ("
        self.assertTrue(TestParser.test(input,expect,221))
    def test_22(self):
        input = """
        Class Program {
            main() {
                Var a : Float=12.0e-123; 
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_23(self):
        
        input = """
        Class Program {
            main() {
                Var a : Float=1_234.567; 
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_24(self):
        
        input = """
        Class Program {
            main() {
                Var a : Float=7E-10 * 0.13e2 + 1_34.2; 
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_25(self):
        
        input = """
        Class Program {
            main() {
                Var a : String="He asked me: '"Where is John?'""; 
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_26(self):
        
        input = """
        Class Program {
            main() {
                If(a==True)
                {Return "Hi";}
                Else
                {ReturN "Hello";}
        }
        }
        """
        expect = "Error on line 7 col 31: ;"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_27(self):
        
        input = """
        Class Program {
            main() {
                If(a[3][2]==."Hello")
                {Return b;}
                Else
                {ReturN c;}
        }
        }
        """
        expect = "Error on line 7 col 25: ;"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_28(self):
        
        input = """
        Class Program {
            main() {
                If((a[3][2]==."Hello") && (b==2))
                {Return 3;}
                Else
                {ReturN 5;}
        }
        }
        """
        expect = "Error on line 7 col 25: ;"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_29(self):
        
        input = """
        Class Program {
            main() {
                If((a.Name ==."World") || (c==2))
                {Return True;}
                Else
                {ReturN False;}
        }
        }
        """
        expect = "Error on line 7 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_30(self):
        
        input = """
        Class Program {
            main() {
                If(!(a.Name ==."World"))
                {Return True;}
                Else
                {ReturN False;}
        }
        }
        """
        expect = "Error on line 7 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_31(self):
        
        input = """
        Class Program {
            main() {
                If(a.Count>= 18)
                {a.Name="Adult";}
                Else
                {a.Name="Teen";}
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_32(self):
        
        input = """
        Class Program {
            main() {
                If((a.Count>= 18) && (a.Address ==. "HCM"))
                {a.isWork=TruE;}
                Else
                {a.isWork=False;}
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_33(self):
        
        input = """
        Class Program {
            main() {
                If((a.Count > 18))
                {Return "More than 18";}
                Elseif (a.Count == 18)
                {Return "Equal 18";}
                Elseif (a.Count <12)
                {Return "Less than 12";}
                Else
                {Return "Others";}
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_34(self):
        
        input = """
        Class Program {
            main() {
                Foreach(i In 1 .. 10 By 2)
                {Out.printInt(i);}
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_35(self):
        
        input = """
        Class Program {
            main() {
                Foreach(x In 1 .. 10)
                {Out.printInt(arr[i]);}
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_36(self):
        
        input = """
        Class Program {
            main() {
                Foreach(x In 1 .. 10 By 2)
                {
                    If(x==3)
                    {Break;}
                    Else
                    {
                        Out.printInt(arr[i]);
                    }
                }
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_37(self):
        
        input = """
        Class Program {
            main() {
                Foreach(x In 1 .. 10 By 2)
                {
                    If(x==3)
                    {Continue;}
                    Else
                    {
                        Out.printInt(arr[i]);
                    }
                }
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_38(self):
        
        input = """
        Class Program {
            main() {
                Out.printInt(3);
                Return ;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_39(self):
        
        input = """
        Class Program {
            main() {
                Shape::$getNumOfShape();
                Return ;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_40(self):
        
        input = """
        Class Program {
            main() {
                s = r * r * Self.myPI;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_41(self):
        
        input = """
        Class Program {
            main() {
                var r, s: Int;
                r = 2.0;
                var a, b: Array[Int, 5];
                }
        }
        """
        expect = "Error on line 4 col 21: ,"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_42(self):
        
        input = """
        Class Hello {
            Destructor() {
                
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_43(self):
        
        input = """
        Class Hello {
            Constructor() {
                
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_44(self):
        
        input = """
        Class Hello {
            Val a : Int= b +c[3];
            remove()
            {
                a=Null;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_45(self):
        
        input = """
        Class Hello {
            Val a : String;
            Contructor()
            {
                Self.Intro="Hello";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_46(self):
        
        input = """
        Class Hello {
            Val a : Int= b +c[3];
            Var $numSay : String="Hello";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_47(self):
        
        input = """
        Class Hello {
            Val a : Int= b +c[3];
            Var $numSay : String="Hello";
            increase(b:Int){
                a=b+3;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_48(self):
        
        input = """
        Class Hello {
            Val a : Int= 10;
            Var $numSay : String="Hello";
            condition(c:Int; d: String){
                If(c<a)
                {
                    Return d;
                }
                Else
                {
                    Return;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_49(self):
        
        input = """
        Class Hello {
            Val a : Int= 10;
            
            setValue(c:Int){
                a=c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_50(self):
        
        input = """
        Class Hello {
            Val a : Int= 10;
            
            Alert(){
               Return "THis is information";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_51(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_52(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_53(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_54(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_55(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_56(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Int,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_57(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_58(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
                ID=1234567;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_59(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
                ID=1234567;
                major="IT";
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_60(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_61(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            setName(a:Int)
            {
                self.name=a;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_62(self):
        
        input = """
        Class Student {
            Var name : String;
            Var degree: Array[Float,10];
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                degree=Array(2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,0.0);
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            setName(a:Int)
            {
                self.name=a;
            }
            getName()
            {
                Return self.name;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_63(self):
        
        input = """
        Class Student {
            Var name : String;
            Var age: Int;
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                age=22;
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            setName(a:String)
            {
                self.name=a;
            }
            getName()
            {
                Return self.name;
            }
            setAge(a:Int)
            {
                self.age=a;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_64(self):
        
        input = """
        Class Student {
            Var name : String;
            Var age: Int;
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                age=22;
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            setName(a:String)
            {
                self.name=a;
            }
            getName()
            {
                Return self.name;
            }
            setAge(a:Int)
            {
                self.age=a;
            }
            getAge()
            {
                Return self.age;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_65(self):
        
        input = """
        Class Student {
            Var name : String;
            Var age: Int;
            Var address: String;
            Var ID: Int;
            Var major: String;
            Var birthday : String;
            Student (){
                name="Nguyen Van A";
                age=22;
            address="HCM";
                ID=1234567;
                major="IT";
                birthday="1/1/2020";
            }
            setName(a:String)
            {
                self.name=a;
            }
            getName()
            {
                Return self.name;
            }
            setAge(a:Int)
            {
                If(a<=0)
                {
                    Out.printLn("So tuoi khong dung!!");
                }
                self.age=a;
            }
            getAge()
            {
                Return self.age;
            }
            setMajor(a:String){
                self.major=a;
            }
            getMajor()
            {
                Return self.major;
            }
            Destructor()
            {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_66(self):
        
        input = """
        Class Animal {
            Var Weight : Float;
            Var Height : Float;
            Info(){
                Out.printLn("Height: " +. Height + "Weight: " +. Weight );
            }
        }
        """
        expect = "Error on line 6 col 62: +."
        self.assertTrue(TestParser.test(input,expect,266))
    def test_67(self):
        
        input = """
        Class Animal {
            Var Weight : Float;
            Var Height : Float;
            Info(){
                Out.printLn("Height: " +. Height + "Weight: " +. Weight );
            }

        }
        Class Program{
            main(){
                Dog= New Animal();
                Dog.Weight=2;## don vi kg##
                Dog.Height=50;## don vi cm##
                Dog.Info();
            }
        }
        """
        expect = "Error on line 6 col 62: +."
        self.assertTrue(TestParser.test(input,expect,267))
    def test_68(self):
        
        input = """
        
        Class Cat{
            Var Weight : Float;
            Var Height : Float;
            Cat(){
                Weight = 800;
                Height = 10;
            }
            Cat(w:Int; h:Int)
            {

            Weight = w;
            Height = h;

            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))
    def test_69(self):
        
        input = """
        
        Class Cat{
            Var Weight : Float;
            Var Height : Float;
            Cat(){
                Weight = 800;
                Height = 10;
            }
            Cat(w:Int; h:Int)
            {

            Weight = w;
            Height = h;

            }
        }
        Class Program{
            main(){
                BlackCat = New Cat();
                BlackCat.Info();
                WhiteCat = New Cat(1200, 30);
                WhiteCat.Info();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_70(self):
        
        input = """
        
        Class SinhVien
    {
        Var MASV:String;
        Var HoTen:String;
        Var DiemToan:Float;
        Var DiemVan:Float;

        InThongTinDiemTB()
        {
            Var DTB :Float = (DiemToan + DiemVan) / 2;
            Console.WriteLine(" Sinh vien " +. HoTen );
            Console.WriteLine("co diem TB la: " +. DTB);
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_71(self):
        
        input = """
        
        Class SinhVien
    {
        Var MASV:String;
        Var HoTen:String;
        Var DiemToan:Float;
        Var DiemVan:Float;

        setDiemToan(a:Float)
        {
            DiemToan=a;
        }
        setDiemVan(a:Float)
        {
            DiemVan=a;
        }

    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_72(self):
        
        input = """
        
        Class SinhVien
    {
        Var MASV:String;
        Var HoTen:String;
        Var DiemToan:Float;
        Var DiemVan:Float;

        setDiemToan(a:Float)
        {
            DiemToan=a;
        }
        setDiemVan(a:Float)
        {
            DiemVan=a;
        }
        result(){
            If((DiemToan>=8)&&(DiemVan>=8))
            {
                Out.printLn("Hoc sinh gioi");
            }
            Elseif((DiemToan>=7)&&(DiemVan>=7))
            {
                Out.printLn("Hoc sinh Kha");
            }
            Elseif((DiemToan>=5)&&(DiemVan>=5))
            {
                Out.printLn("Hoc sinh Trung binh kha");
            }
            Else{
                Out.printLn("Hoc sinh Yeu");
            }

        }

    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_73(self):
        
        input = """
        
        Class Animal
    {
        Var Weight : Float;
        Var Height : Float;
        Var Legs : Int;

        Info()
        {
            Console.WriteLine(" Weight: " + Weight + " Height: " + Height + " Legs: " + Legs);
        }
    }


    Class Cat : Animal
    {
        Cat()
        {
            
            Weight = 500;
            Height = 20;
            Legs = 2;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_74(self):
        
        input = """
        
        Class Animal
    {
        Var Weight : Float;
        Var Height : Float;
        Var Legs : Int;

        Info()
        {
            Console.WriteLine(" Weight: " + Weight + " Height: " + Height + " Legs: " + Legs);
        }
    }


    Class Cat : Animal
    {
        Cat()
        {
            
            Weight = 500;
            Height = 20;
            Legs = 2;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_75(self):
        
        input = """
        
        Class Animal
    {

        Speak()
        {
            Console.WriteLine(" Animal is speaking. . .");
        }
    }


    Class Cat : Animal
    {
        Speak()
        {
            Console.WriteLine(" Cat is speaking. . .");
        }
    }


    Class Dog : Animal
    {
        Speak()
        {
            Console.WriteLine(" Dog is speaking. . .");
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_76(self):
        
        input = """
        
       Class Program{
           main(){
               Return a+3;
           }
       }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_77(self):
        
        input = """
        
       Class Program{
           main(){
               Foreach(x IN 1 .. 3)
               {
                   a[x]=x;
               }
           }
       }
        """
        expect = "Error on line 5 col 25: IN"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_78(self):
        
        input = """
        
       Class Program{
           main(){
               Foreach(x IN 1 .. 3)
               {
                   If(a[x]==1)
                   {
                       Out.printLn("Equal");
                   }
               }
           }
       }
        """
        expect = "Error on line 5 col 25: IN"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_79(self):
        
        input = """
        
       Class Program{
           main(){
            Var r, s: Int;
            r = 2.0;
            Var a, b: Array[Int, 5]; 
            s = r * r * Self.myPI; 
            a[0] = s;
           }
       }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_80(self):
        
        input = """
        
       Class Program{
           main(){
            Var r, s: Float=1.3,2.4;
            
            Var a, b: Array[String, 5]; 
           
           }
       }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_81(self):
        
        input = """
        
       Class Dog: Pet {
                getWeight() {
                    x = Self.weight;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_82(self):
        
        input = """
        
       Class Dog: Pet {
                getWeight() {
                    x = Self.weight;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_83(self):
        
        input = """
        
       Class Dog: Pet {
                Info() {
                    Out.printLn("Gau gau");
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_84(self):
        
        input = """
            Class Dog {
            Constructor(name:String; birthday:Int) {
                Self.name = name;
                Self.birthday = birthday;
            }

            ##Declare private variables##
            _attendance = 0;

            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_85(self):
        
        input = """
            Class Dog {
            getAge() {
                ##Getter##
                Return Self.calcAge();
            }

            calcAge() {
                ##calculate age using today's date and birthday##
                Return Date.now() - Self.birthday;
    }

            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_86(self):
        
        input = """
            Class Dog {
            calcAge() {
                ##calculate age using today's date and birthday##
                Return Date.now() - Self.birthday;
    }

            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_87(self):
        
        input = """
            Class MyClass {      
            Val myNum : Int;        
            Var myString : String;  
        }
            Class Program{
                main() {
            myObj=New MyClass();  
            myObj.myNum = 15; 
            myObj.myString = "Some text";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_88(self):
        
        input = """
            Class Car {
            Var brand:String;   
            Var model:String;
            Var year:Int;
            }
            Class Program{
                main() {
            carObj1=New Car();  
           carObj1.brand = "BMW";
            carObj1.model = "X5";
            carObj1.year = 1999;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_89(self):
        
        input = """
            Class MyClass {
            myMethod() {  ##Method/function defined inside the class##
                Out.printLn("Hello World!");
                }
            }
            Class Program{
                main() {
            myObj=New MyClass();     ##Create an object of MyClass##
            myObj.myMethod();  ##all the method##
            Return 0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_90(self):
        
        input = """
            Class MyClass {
            Var brand:String;  ## Attribute##
            Var model:String;  ##Attribute##
            Var year:Int;      ## Attribute##
            Car(x, y:String; z:Int) { ## Constructor with parameters##
            brand = x;
            model = y;
            year = z;
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
    def test_91(self):
        
        input = """
            Class Program {
            main(){
                Var x:Int=2+3.6E12;
                Val $metsa:String="asdasd" +. "asd";
                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_92(self):
        
        input = """
            Class Program {
            main(){
                Return x+y/c*c*(a-x);
                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_93(self):
        
        input = """
            Class Program {
            main(){
                If(a=="2")
                {
                    a="23";
                }

                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_94(self):
        
        input = """
            Class Program {
            main(){
                Foreach(asdf In 1 ... 3)
                {

                }

                
    }
        }
        """
        expect = "Error on line 4 col 36: ."
        self.assertTrue(TestParser.test(input,expect,294))
    def test_95(self):
        
        input = """
            Class Program {
            main(){
               Return Break;

                
    }
        }
        """
        expect = "Error on line 4 col 22: Break"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_96(self):
        
        input = """
            Class Program {
            main(){
               a[a[3].3]=3;

                
    }
        }
        """
        expect = "Error on line 4 col 22: 3"
        self.assertTrue(TestParser.test(input,expect,296))
    def test_97(self):
        
        input = """
            Class Program {
            main(){
               Var a :Array[Array[Array[Int,3],4],5];

                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_98(self):
        
        input = """
            Class Program {
            main(){
               Foreach (a In 1 .. 2 )
               {
                   If(b[a]==1)
                   {
                       Break;
                   }
               }

                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_99(self):
        
        input = """
            Class Program {
            main(){
               If(ac[3].a[3]==1)
               {

               }

                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_100(self):
        
        input = """
            Class Program {
            main(){
               a=d.x +c[3-3]/2+(1-3)*3;

                
    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))
#     def test_program_1(self): # Valid class
#         input = """Class Car {}"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,201))
    
#     def test_program_2(self): # Valid class
#         input = """
#             Class Car {}
#             Class People {}
#             Class animal {}
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,202))

#     def test_program_3(self): # Valid class
#         input = """
#             Class fOOtbaLL{
#                 Val My1stCons, My2ndCons: Int = 1 + 5, 2;
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,203))

#     def test_program_4(self): # Attribute declaration is outside class.
#         input = """
#             Var $name, age: Int;
#             Class Dog{}
#         """
#         expect = "Error on line 2 col 12: Var"
#         self.assertTrue(TestParser.test(input,expect,204))

#     def test_program_5(self): # Valid class
#         input = """
#             Class Cat{
#                 Var weight, $height: Float;
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,205))

#     def test_program_6(self): # No keyword "Class".
#         input = """
#             People{
#             }
#         """
#         expect = "Error on line 2 col 12: People"
#         self.assertTrue(TestParser.test(input,expect,206))

#     def test_program_7(self): # Missing LCB "{".
#         input = """
#             Class Animal
#                 Var weight, $height: Float;
#             }
#         """
#         expect = "Error on line 3 col 16: Var"
#         self.assertTrue(TestParser.test(input,expect,207))
    
#     def test_program_8(self): # Missing RCB "}".
#         input = """
#             Class Country{
#         """
#         expect = "Error on line 3 col 8: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,208))

#     def test_program_9(self): # Missing class name.
#         input = """
#             Class {}
#         """
#         expect = "Error on line 2 col 18: {"
#         self.assertTrue(TestParser.test(input,expect,209))

#     def test_program_10(self): # Wrong keyword "class".
#         input = """
#             class Sea{}
#         """
#         expect = "Error on line 2 col 12: class"
#         self.assertTrue(TestParser.test(input,expect,210))

# # Test attribute declaration ###############################

#     def test_program_11(self): # Valid attribute
#         input = """
#             Class Sea{
#                 Val My1stCons, My2ndCons: Int = 1 + 5, 2;
#                 Var $x, $y : Int = 0, 0;
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,211))

#     def test_program_12(self): # Valid attribute
#         input = """
#             Class Color{
#                 Var $yellow, red: String;
#                 Val blue, $Orange: String;
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,212))

#     def test_program_13(self): # Valid attribute
#         input = """
#             Class footbalPlayer{
#                 Var height: Float = 180.5;
#                 Val $age: Int = 24;
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,213))

#     def test_program_14(self): # Missing type of attribute.
#         input = """
#             Class Vietnam{
#                 Var Capital = Saigon;
#             }
#         """
#         expect = "Error on line 3 col 28: ="
#         self.assertTrue(TestParser.test(input,expect,214))

#     def test_program_15(self): # Missing value after "=".
#         input = """
#             Class food{
#                 Val $taste: String =;
#             }
#         """
#         expect = "Error on line 3 col 36: ;"
#         self.assertTrue(TestParser.test(input,expect,215))

#     def test_program_16(self): # Wrong keyword "Val/Var".
#         input = """
#             Class People{
#                vaL $height: Float = 170.0;
#             }
#         """
#         expect = "Error on line 3 col 19: $height"
#         self.assertTrue(TestParser.test(input,expect,216))

#     def test_program_17(self): # Missing colon ":".
#         input = """
#             Class Truck{
#                 Var $size, $color String = big, red;
#             }
#         """
#         expect = "Error on line 3 col 34: String"
#         self.assertTrue(TestParser.test(input,expect,217))

#     def test_program_18(self): # Missing comma "," between attribute names.
#         input = """
#             Class Restaurant{
#                 Val star location: Int;
#             }
#         """
#         expect = "Error on line 3 col 25: location"
#         self.assertTrue(TestParser.test(input,expect,218))

#     def test_program_19(self): # Missing semicolon at the end of attribute statement.
#         input = """
#             Class province{
#                 Var $population, $area: Int = 97_000_000, 300_000
#             }
#         """
#         expect = "Error on line 4 col 12: }"
#         self.assertTrue(TestParser.test(input,expect,219))

#     def test_program_20(self): # Missing comma between initial values.
#         input = """
#             Class Animal{
#                 Val weight, long: Float = 50.25 130.5;
#             }
#         """
#         expect = "Error on line 3 col 48: 130.5"
#         self.assertTrue(TestParser.test(input,expect,220))

# # Test Method declaration ####################################################

#     def test_program_21(self): # Valid method
#         input = """
#             Class Dog: Pet {
#                 getWeight(a, b, c: Int; x, y, z: Float) {
#                     Return;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,221))

#     def test_program_22(self): # Valid method
#         input = """
#             Class People {
#                 setAge() {}
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,222))

#     def test_program_23(self): # Valid method
#         input = """
#             Class Car {
#                 setColor(color: String) {
#                     $color[1][2] = red;
#                     Return True;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,223))

#     def test_program_24(self): # Method missing "()"
#         input = """
#             Class sport {
#                 $football{
#                     Return;
#                 }
#             }
#         """
#         expect = "Error on line 3 col 25: {"
#         self.assertTrue(TestParser.test(input,expect,224))

#     def test_program_25(self): # Method missing "("
#         input = """
#             Class Fish {
#                 tuna( {
#                     Return color;
#                 }
#             }
#         """
#         expect = "Error on line 3 col 22: {"
#         self.assertTrue(TestParser.test(input,expect,225))

#     def test_program_26(self): # Method missing ")"
#         input = """
#             Class House {
#                 roof ) {
#                     Return color;
#                 }
#             }
#         """
#         expect = "Error on line 3 col 21: )"
#         self.assertTrue(TestParser.test(input,expect,226))

#     def test_program_27(self): # Method missing "{}"
#         input = """
#             Class building {
#                 $wall();
#             }
#         """
#         expect = "Error on line 3 col 23: ;"
#         self.assertTrue(TestParser.test(input,expect,227))

#     def test_program_28(self): # missing type of parameters.
#         input = """
#             Class City {
#                 $District(x, $y; z, t){
#                     Return x + True;
#                 }
#             }
#         """
#         expect = "Error on line 3 col 31: ;"
#         self.assertTrue(TestParser.test(input,expect,228))

#     def test_program_29(self): # error: semicomma ";" in list of parameters.
#         input = """
#             Class Country {
#                 $province(x, y, z: String;){
#                     x = y + z;
#                 }
#             }
#         """
#         expect = "Error on line 3 col 42: )"
#         self.assertTrue(TestParser.test(input,expect,229))

#     def test_program_30(self): # error: semicomma ";" at the end of the method.
#         input = """
#             Class myClass_30 {
#                 myMethod_30(){
#                     Return myReturn;
#                 };
#             }
#         """
#         expect = "Error on line 5 col 17: ;"
#         self.assertTrue(TestParser.test(input,expect,230))

# # Test Constructor & Destructor declaration ############

#     def test_program_31(self): # Valid Constructor & Destructor.
#         input = """
#             Class myClass_31 {
#                 Constructor(color, size: String; x, y: Int){}
#                 Destructor(){}
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,231))

#     def test_program_32(self): # Valid Constructor & Destructor.
#         input = """
#             Class myClass_32 {
#                 Constructor(a, b: Float){
#                     y = x % z;
#                 }
#                 Destructor(){
#                     z = z + 2 - z;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,232))

#     def test_program_33(self): # error: parameters in Destructor
#         input = """
#             Class myClass_33 {
#                 Constructor(x, y: Int){}
#                 Destructor(y, z: Array; u, v: Boolean){}
#             }
#         """
#         expect = "Error on line 4 col 27: y"
#         self.assertTrue(TestParser.test(input,expect,233))

# # Test Array Literal #######################

#     def test_program_34(self): # valid array declaration.
#         input = """
#             Class myClass_34 {
#                 $myMethod_34(){
#                     Var yourArray_34: Array[Int, 4];
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,234))

#     def test_program_35(self): # valid indexed array.
#         input = """
#             Class myClass_35 {
#                 $myMethod_35(){
#                     yourArray_34 = Array (1, 4, 3, 5);
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,235))

#     def test_program_36(self): # valid multi-dimensional array.
#         input = """
#             Class myClass_36 {
#                 $myMethod_36(){
#                     myArr = Array (
#                                 Array("Volvo", "22", "18"),
#                                 Array("Saab", "5", "2"),
#                                 Array("Land Rover", "17", "15")
#                             );
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,236))

#     def test_program_37(self): # valid array declaration.
#         input = """
#             Class myClass_37 {
#                 $myMethod_37(){
#                     Val myArray_37: Array[Int, 4] = Array(1, 5, 3, 2);
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,237))

#     def test_program_38(self): # array error: size = 0.
#         input = """
#             Class myClass_38 {
#                 $myMethod_38(){
#                     Val myArray_38: Array[Boolean, 0];
#                 }
#             }
#         """
#         expect = "Error on line 4 col 51: 0"
#         self.assertTrue(TestParser.test(input,expect,238))

#     def test_program_39(self): # array error: elements different type (float, float, int)
#         input = """
#             Class myClass_39 {
#                 $myMethod_39(){
#                     Val myArray_39: Array[Float, 3] = Array(1.5, 3.25, 5);
#                     x = arr[0];
#                 }
#             }
#         """
#         expect = "Error on line 4 col 71: 5"
#         self.assertTrue(TestParser.test(input,expect,239))

#     def test_program_40(self): # array error: has no element.
#         input = """
#             Class MyClass_40 {
#                 $MyMethod_40(){
#                     Val myArray_40: Array[Int, 8] = Array();
#                 }
#             }
#         """
#         expect = "Error on line 4 col 58: )"
#         self.assertTrue(TestParser.test(input,expect,240))

#     def test_program_41(self): # array error: element list has comma "," at the end
#         input = """
#             Class MyClass_41 {
#                 $MyMethod_41(){
#                     Var myArray_41: Array[String, 5] = Array("Lan", "Hong", "Cuc",);
#                 }
#             }
#         """
#         expect = "Error on line 4 col 82: )"
#         self.assertTrue(TestParser.test(input,expect,241))

#     def test_program_42(self): # array error: element list has comma "," at the end
#         input = """
#             Class MyClass_42 {
#                 $MyMethod_42(){
#                     Var myArray_42: Array[String, 5] = Array (
#                                                             Array("Volvo", "22", "18"),
#                                                             Array("Saab", "5", "2"),
#                                                             "Toyota"
#                                                             );
#                 }
#             }
#         """
#         expect = "Error on line 7 col 60: Toyota"
#         self.assertTrue(TestParser.test(input,expect,242))

# # Test class type (object creation) #########################################

#     def test_program_43(self): # Object creation: valid.
#         input = """
#             Class MyClass_43 {
#                 $MyMethod_43(){
#                     x = New Car(5, 7);
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,243))

#     def test_program_44(self): # Object creation: valid.
#         input = """
#             Class MyClass_44 {
#                 myMethod_44(){
#                     y = New dog();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,244))

#     def test_program_45(self): # Object creation: valid.
#         input = """
#             Class MyClass_45 {
#                 myMethod_45(){
#                     z = New Animal(x + 2, New Car("color", "size"), Array(1, 3, 5));
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,245))

#     def test_program_46(self): # Object creation error: "new" not "New".
#         input = """
#             Class MyClass_46 {
#                 myMethod_46(){
#                     Val a : Null = new People();
#                 }
#             }
#         """
#         expect = "Error on line 4 col 39: People"
#         self.assertTrue(TestParser.test(input,expect,246))

#     def test_program_47(self): # Object creation error: no "()".
#         input = """
#             Class MyClass_47 {
#                 myMethod_47(){
#                     Var newObject: Null = New aniMal;
#                 }
#             }
#         """
#         expect = "Error on line 4 col 52: ;"
#         self.assertTrue(TestParser.test(input,expect,247))

#     def test_program_48(self): # Object creation error: no class name after "New".
#         input = """
#             Class MyClass_48 {
#                 myMethod_48(){
#                     Var yourObject: People = New (x - 3, True);
#                 }
#             }
#         """
#         expect = "Error on line 4 col 49: ("
#         self.assertTrue(TestParser.test(input,expect,248))

#     def test_program_49(self): # Object creation error: invalid argument.
#         input = """
#             Class MyClass_49 {
#                 myMethod_49(){
#                     Val hisObject: Null = New Car(x, *);
#                 }
#             }
#         """
#         expect = "Error on line 4 col 53: *"
#         self.assertTrue(TestParser.test(input,expect,249))

#     def test_program_50(self): # Object creation error: no "New".
#         input = """
#             Class MyClass_50 {
#                 myMethod_50(){
#                     Var thatObject: Null = Car(x, y, z);
#                 }
#             }
#         """
#         expect = "Error on line 4 col 46: ("
#         self.assertTrue(TestParser.test(input,expect,250))

# # Test Self #######################################

#     def test_program_51(self): # Self: valid.
#         input = """
#             Class MyClass_51 {
#                 myMethod_51(){
#                     y = x * Self.myPI;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,251))

# # Test Statements ########################################
# # Variable and Constant Declaration Statement

#     def test_program_52(self): # Variable declararion: Valid.
#         input = """
#             Class MyClass_52 {
#                 myMethod_52(){
#                     Var x: Int;
#                     Var y: Float = 5.25;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,252))

#     def test_program_53(self): # Constant declaration: Valid.
#         input = """
#             Class MyClass_53 {
#                 myMethod_53(){
#                     Val a: String = "vieTnaM";
#                     Val size: Int;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,253))

#     def test_program_54(self): # Variable declaration error: missing type.
#         input = """
#             Class MyClass_54 {
#                 myMethod_54(){
#                     Var myVal;
#                 }
#             }
#         """
#         expect = "Error on line 4 col 29: ;"
#         self.assertTrue(TestParser.test(input,expect,254))

#     def test_program_55(self): # Variable declaration error: must be ID, not dollar ID in var/const declaration.
#         input = """
#             Class MyClass_55 {
#                 myMethod_55(){
#                     Var $yourVal: String = "Hanoi";
#                 }
#             }
#         """
#         expect = "Error on line 4 col 24: $yourVal"
#         self.assertTrue(TestParser.test(input,expect,255))

#     def test_program_56(self): # Constant declaration error: missing type.
#         input = """
#             Class MyClass_56 {
#                 myMethod_56(){
#                     Val newConst = 10e12;
#                 }
#             }
#         """
#         expect = "Error on line 4 col 33: ="
#         self.assertTrue(TestParser.test(input,expect,256))

#     def test_program_57(self): # Constant declaration error: ID not dollar ID.
#         input = """
#             Class MyClass_57 {
#                 myMethod_57(){
#                     Val $lastConst: String = "Good bye!";
#                 }
#             }
#         """
#         expect = "Error on line 4 col 24: $lastConst"
#         self.assertTrue(TestParser.test(input,expect,257))
    
# #   Test Assignment Statement #############################################

#     def test_program_58(self): # Assignment Statement: valid.
#         input = """
#             Class MyClass_58 {
#                 myMethod_58(){
#                     x = y + z * Self.mean - a[2][x-y];
#                     m[n][y * k % f] = v.length();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,258))

#     def test_program_59(self): # Assignment Statement error: no right hand side.
#         input = """
#             Class MyClass_59 {
#                 myMethod_59(){
#                     k =;
#                 }
#             }
#         """
#         expect = "Error on line 4 col 23: ;"
#         self.assertTrue(TestParser.test(input,expect,259))

#     def test_program_60(self): # Assignment Statement error: no left hand side.
#         input = """
#             Class MyClass_60 {
#                 myMethod_60(){
#                     = c.getSize();
#                 }
#             }
#         """
#         expect = "Error on line 4 col 20: ="
#         self.assertTrue(TestParser.test(input,expect,260))

# #   Test If statement ###################################################

#     def test_program_61(self): # If statement: valid.
#         input = """
#             Class MyClass_61 {
#                 myMethod_61(){
#                     If (a == 20 && True) {c = a + b;}
#                     Elseif (d >= 2) {Return c;}
#                     Elseif (b == c)
#                         {
#                             b = c % a;
#                             c = c - b;
#                         }
#                     Else {Return False;}    
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,261))

#     def test_program_62(self): # If statement: valid.
#         input = """
#             Class MyClass_62 {
#                 myMethod_62(){
#                     If (x != 5) {}
#                     Elseif (d >= 0) {}
#                     Else {}    
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,262))

#     def test_program_63(self): # If statement: valid.
#         input = """
#             Class MyClass_63 {
#                 myMethod_63(){
#                     If (True && False) {}
#                     Else {}    
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,263))

#     def test_program_64(self): # If statement: valid.
#         input = """
#             Class MyClass_64 {
#                 myMethod_64(){
#                     If (True && False) {}
#                     Elseif(False) {}    
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,264))

#     def test_program_65(self): # If statement: valid.
#         input = """
#             Class MyClass_65 {
#                 myMethod_65(){
#                     If (True) {}
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,265))

#     def test_program_66(self): # If statement error: no "If" keyword.
#         input = """
#             Class MyClass_66 {
#                 myMethod_66(){
#                     Elseif (True) {}
#                 }
#             }
#         """
#         expect = "Error on line 4 col 20: Elseif"
#         self.assertTrue(TestParser.test(input,expect,266))

#     def test_program_67(self): # If statement error: No condition expression in "()" after "If".
#         input = """
#             Class MyClass_67 {
#                 myMethod_67(){
#                     If () {Return x;}
#                     Elseif (b > 0) {Return y;}
#                     Else {Return z;} 
#                 }
#             }
#         """
#         expect = "Error on line 4 col 24: )"
#         self.assertTrue(TestParser.test(input,expect,267))

#     def test_program_68(self): # If statement error: No condition expression in "()" after "Elseif".
#         input = """
#             Class MyClass_68 {
#                 myMethod_68(){
#                     If (True || False && True) {}
#                     Elseif ()
#                     {
#                         x = y + 2;
#                         return x;
#                     }
#                     Else {} 
#                 }
#             }
#         """
#         expect = "Error on line 5 col 28: )"
#         self.assertTrue(TestParser.test(input,expect,268))

#     def test_program_69(self): # If statement error: "()" after "Else".
#         input = """
#             Class MyClass_69 {
#                 myMethod_69(){
#                     If (a || b) {}
#                     Elseif (x && y) {}
#                     Else (True) {} 
#                 }
#             }
#         """
#         expect = "Error on line 6 col 25: ("
#         self.assertTrue(TestParser.test(input,expect,269))

#     def test_program_70(self): # If statement error: no block statement after "If".
#         input = """
#             Class MyClass_70 {
#                 myMethod_70(){
#                     If (False) Return x + y;
#                     Elseif (a == 0) {Return;}
#                     Else {Return;} 
#                 }
#             }
#         """
#         expect = "Error on line 4 col 31: Return"
#         self.assertTrue(TestParser.test(input,expect,270))

# # Test Foreach/ In statement ##########################################

#     def test_program_71(self): # Foreach/ In: valid.
#         input = """
#             Class MyClass_71 {
#                 myMethod_71(){
#                     Foreach (i In 1 .. 100 By 2) {
#                         Out.printInt(i);
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,271))

#     def test_program_72(self): # Foreach/ In: valid.
#         input = """
#             Class MyClass_72 {
#                 myMethod_72(){
#                     Foreach (x In 5 .. 2) {
#                         Out.printInt(arr[x]);
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,272))

#     def test_program_73(self): # Foreach/ In error: "Foreach" not "foreach".
#         input = """
#             Class MyClass_73 {
#                 myMethod_73(){
#                     foreach (i In 0 .. 10) {
#                         arr[i] = i + 1;
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 4 col 28: ("
#         self.assertTrue(TestParser.test(input,expect,273))

#     def test_program_74(self): # Foreach/ In error: "In" not "in".
#         input = """
#             Class MyClass_74 {
#                 myMethod_74(){
#                     Foreach (x in 2 .. 8) {
#                         y = y * x;
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 4 col 31: in"
#         self.assertTrue(TestParser.test(input,expect,274))

#     def test_program_75(self): # Foreach/ In error: ".." not "." after the first number of range.
#         input = """
#             Class MyClass_75 {
#                 myMethod_75(){
#                     Foreach (x In 1 . 100) {
#                         Out.print(x + 1);
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 4 col 36: ."
#         self.assertTrue(TestParser.test(input,expect,275))

#     def test_program_76(self): # Foreach/ In error: no scalar variable after "Foreach (".
#         input = """
#             Class MyClass_76 {
#                 myMethod_76(){
#                     Foreach (In 0..50) {
#                         Return;
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 4 col 29: In"
#         self.assertTrue(TestParser.test(input,expect,276))

#     def test_program_77(self): # Foreach/ In error: no range "(...)" after "Foreach".
#         input = """
#             Class MyClass_77 {
#                 myMethod_77(){
#                     Foreach {
#                         Return;
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 4 col 28: {"
#         self.assertTrue(TestParser.test(input,expect,277))

#     def test_program_78(self): # Foreach/ In error: nothing in range "()" after "Foreach".
#         input = """
#             Class MyClass_78 {
#                 myMethod_78(){
#                     Foreach () {
#                         x = x + 1;
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 4 col 29: )"
#         self.assertTrue(TestParser.test(input,expect,278))

#     def test_program_79(self): # Foreach/ In error: no block statement "{}" after range "(...)".
#         input = """
#             Class MyClass_79 {
#                 myMethod_79(){
#                     Foreach (x In 1 .. 10)
#                 }
#             }
#         """
#         expect = "Error on line 5 col 16: }"
#         self.assertTrue(TestParser.test(input,expect,279))

# # Test Break statement ############################

#     def test_program_80(self): # Break statement: valid.
#         input = """
#             Class MyClass_80 {
#                 myMethod_80(){
#                     Foreach (x In 1 .. 10)
#                     {
#                         Out.printInt(arr[x]);
#                         If (x > 5)
#                         {
#                             Break;
#                         }
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,280))
    
#     def test_program_81(self): # Break statement: valid.
#         input = """
#             Class MyClass_81 {
#                 myMethod_81(){
#                     Foreach (i In 0 .. 25)
#                     {
#                         Break;
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,281))

#     def test_program_82(self): # Break statement error: "Break" not "break".
#         input = """
#             Class MyClass_82 {
#                 myMethod_82(){
#                     Foreach (x In 1 .. 10)
#                     {
#                         break;
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 6 col 29: ;"
#         self.assertTrue(TestParser.test(input,expect,282))

#     def test_program_83(self): # Break statement error: no semicomma ";" after "Break".
#         input = """
#             Class MyClass_83 {
#                 myMethod_83(){
#                     Foreach (x In 1 .. 100)
#                     {
#                         Break
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 7 col 20: }"
#         self.assertTrue(TestParser.test(input,expect,283))

# # Test Continue statement #################################

#     def test_program_84(self): # Continue statement: valid.
#         input = """
#             Class MyClass_84 {
#                 myMethod_84(){
#                     Foreach (x In 1 .. 10)
#                     {
#                         x = x + 1;
#                         If (x > 5)
#                         {
#                             Continue;
#                         }
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,284))
    
#     def test_program_85(self): # Continue statement: valid.
#         input = """
#             Class MyClass_85 {
#                 myMethod_85(){
#                     Foreach (i In 0 .. 150)
#                     {
#                         Continue;
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,285))

#     def test_program_86(self): # Continue statement error: "Continue" not "continue".
#         input = """
#             Class MyClass_86 {
#                 myMethod_86(){
#                     Foreach (x In 1 .. 200)
#                     {
#                         continue;
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 6 col 32: ;"
#         self.assertTrue(TestParser.test(input,expect,286))

#     def test_program_87(self): # Continue statement error: no semicomma ";" after "Continue".
#         input = """
#             Class MyClass_87 {
#                 myMethod_87(){
#                     Foreach (x In 1 .. 100)
#                     {
#                         Continue
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 7 col 20: }"
#         self.assertTrue(TestParser.test(input,expect,287))

# # Test Return statement ########################

#     def test_program_88(self): # Return statement: valid.
#         input = """
#             Class MyClass_88 {
#                 myMethod_88(){
#                     Foreach (x In 1 .. 10)
#                     {
#                         x = x + 1;
#                         If (x > 5)
#                         {
#                             Return;
#                         }
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,288))
    
#     def test_program_89(self): # Return statement: valid.
#         input = """
#             Class MyClass_89 {
#                 myMethod_89(){
#                     Foreach (i In 0 .. 150)
#                     {
#                         Return x - y + Self.length;
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,289))

#     def test_program_90(self): # Return statement error: "Return" not "continue".
#         input = """
#             Class MyClass_90 {
#                 myMethod_90(){
#                     Foreach (x In 1 .. 200)
#                     {
#                         return;
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 6 col 30: ;"
#         self.assertTrue(TestParser.test(input,expect,290))

#     def test_program_91(self): # Return statement error: no semicomma ";" after "Return".
#         input = """
#             Class MyClass_91 {
#                 myMethod_91(){
#                     Foreach (x In 1 .. 100)
#                     {
#                         Return
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 7 col 20: }"
#         self.assertTrue(TestParser.test(input,expect,291))

# # Test Method Invocation statement #############################

#     def test_program_92(self): # Method Invocation statement: valid.
#         input = """
#             Class MyClass_92 {
#                 myMethod_92(){
#                     Shape::$getNumOfShape();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,292))

#     def test_program_93(self): # Method Invocation statement: valid.
#         input = """
#             Class MyClass_93 {
#                 myMethod_93(){
#                     get.size();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,293))

#     def test_program_94(self): # Method Invocation statement error: missing "$" for static method.
#         input = """
#             Class MyClass_94 {
#                 myMethod_94(){
#                     rectangular::getSize();
#                 }
#             }
#         """
#         expect = "Error on line 4 col 33: getSize"
#         self.assertTrue(TestParser.test(input,expect,294))

#     def test_program_95(self): # Method Invocation statement error: "ID", not "$ID" after dot "." for instance method.
#         input = """
#             Class MyClass_95 {
#                 myMethod_95(){
#                     let.$changeName();
#                 }
#             }
#         """
#         expect = "Error on line 4 col 24: $changeName"
#         self.assertTrue(TestParser.test(input,expect,295))

# # Test block statement ##################################

#     def test_program_96(self): # Block statement: valid.
#         input = """
#             Class MyClass_96 {
#                 myMethod_96()
#                 {
#                     Var r, s: Int;
#                     r = 2.0;
#                     Var a, b: Array[Int, 5];
#                     s = r * r * Self.myPI;
#                     a[0] = s;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,296))

#     def test_program_97(self): # Block statement: valid.
#         input = """
#             Class MyClass_96 {
#                 myMethod_96()
#                 {
#                     Val a, b: String = "hello", "hi";
#                     s = y + z - v % i;
#                     {
#                         a = b && c;
#                         Var c: Int = 5;
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,297))

#     def test_program_98(self): # Block statement: valid.
#         input = """
#             Class MyClass_98 {
#                 myMethod_98()
#                 {
#                     If (a == 20 && True)
#                     {
#                         c = a + b;
#                         Return c;
#                     }
#                     Else
#                     {
#                         x = x + 1;
#                         Return False;
#                     } 
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,298))

#     def test_program_99(self): # Block statement: valid.
#         input = """
#             Class MyClass_99 {
#                 myMethod_99()
#                 {
#                     {}
#                     If (True)
#                     {
#                         {}
#                         Return;
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,299))

#     def test_program_100(self): # Block statement: valid.
#         input = """
#             Class MyClass_100 {
#                 myMethod_100()
#                 {
#                     Foreach (i In 0 .. 10)
#                     {
#                         arr[i] = i + 1;
#                         {
#                             a = b % c;
#                             c = Self.length;
#                         }
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,300))

