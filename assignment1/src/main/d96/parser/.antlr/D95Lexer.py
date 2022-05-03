# Generated from c:\THANH\BK\NGUYEN LY NGON NGU LAP TRINH\assignment\assignment1\src\main\d96\parser\PhongD95.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


import re
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u0288\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\6\b\u00ff\n\b\r")
        buf.write("\b\16\b\u0100\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u0109\n\t\f")
        buf.write("\t\16\t\u010c\13\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\6\n\u0115")
        buf.write("\n\n\r\n\16\n\u0116\3\13\3\13\7\13\u011b\n\13\f\13\16")
        buf.write("\13\u011e\13\13\3\f\3\f\6\f\u0122\n\f\r\f\16\f\u0123\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*")
        buf.write("\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3>")
        buf.write("\3>\3?\3?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3C\3C\3D\3D\3D\3")
        buf.write("D\3E\3E\3E\3F\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3")
        buf.write("L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3Q\3Q\5Q\u01f7\nQ\3Q\3")
        buf.write("Q\3R\3R\3R\7R\u01fe\nR\fR\16R\u0201\13R\3R\5R\u0204\n")
        buf.write("R\5R\u0206\nR\3S\3S\3S\3S\7S\u020c\nS\fS\16S\u020f\13")
        buf.write("S\3T\3T\3T\7T\u0214\nT\fT\16T\u0217\13T\3U\3U\3U\3U\7")
        buf.write("U\u021d\nU\fU\16U\u0220\13U\3V\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\5V\u022f\nV\3V\3V\3W\3W\3X\3X\3X\7X\u0238")
        buf.write("\nX\fX\16X\u023b\13X\5X\u023d\nX\3X\5X\u0240\nX\3Y\3Y")
        buf.write("\3Y\5Y\u0245\nY\3Y\3Y\3Z\3Z\7Z\u024b\nZ\fZ\16Z\u024e\13")
        buf.write("Z\3Z\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3]\3]\3]\5]\u025c\n]\3")
        buf.write("^\3^\3^\3_\3_\7_\u0263\n_\f_\16_\u0266\13_\3_\5_\u0269")
        buf.write("\n_\3_\3_\3`\3`\7`\u026f\n`\f`\16`\u0272\13`\3`\3`\3`")
        buf.write("\3a\3a\3a\5a\u027a\na\3b\3b\3c\3c\3c\3c\7c\u0282\nc\f")
        buf.write("c\16c\u0285\13c\3c\3c\4\u010a\u0283\2d\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\2K\2M\2O\2Q\2S\2U\2W")
        buf.write("\2Y\2[\2]\2_\2a\2c\2e\2g\2i\34k\35m\36o\37q s!u\"w#y$")
        buf.write("{%}&\177\'\u0081(\u0083)\u0085*\u0087+\u0089,\u008b-\u008d")
        buf.write(".\u008f/\u0091\60\u0093\61\u0095\62\u0097\63\u0099\64")
        buf.write("\u009b\65\u009d\66\u009f\67\u00a18\u00a3\2\u00a5\2\u00a7")
        buf.write("\2\u00a9\2\u00ab9\u00ad\2\u00af\2\u00b1\2\u00b3:\u00b5")
        buf.write("\2\u00b7\2\u00b9\2\u00bb\2\u00bd;\u00bf<\u00c1\2\u00c3")
        buf.write("=\u00c5>\3\2,\5\2\13\f\16\17\"\"\6\2\62;C\\aac|\3\2C\\")
        buf.write("\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2I")
        buf.write("Iii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4")
        buf.write("\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVv")
        buf.write("v\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\3")
        buf.write("\2\63;\4\2\62;aa\3\2\62;\4\2\63;CH\4\2\62;CH\3\2\639\3")
        buf.write("\2\629\3\2\62\63\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhppt")
        buf.write("tvv\7\3\n\f\16\17$$))^^\3\2^^\4\2,,\61\61\2\u027e\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00b3\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf")
        buf.write("\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\3\u00c7\3\2\2")
        buf.write("\2\5\u00cf\3\2\2\2\7\u00d7\3\2\2\2\t\u00e1\3\2\2\2\13")
        buf.write("\u00eb\3\2\2\2\r\u00f4\3\2\2\2\17\u00fe\3\2\2\2\21\u0104")
        buf.write("\3\2\2\2\23\u0112\3\2\2\2\25\u0118\3\2\2\2\27\u011f\3")
        buf.write("\2\2\2\31\u0125\3\2\2\2\33\u012b\3\2\2\2\35\u0134\3\2")
        buf.write("\2\2\37\u0137\3\2\2\2!\u013e\3\2\2\2#\u0143\3\2\2\2%\u0149")
        buf.write("\3\2\2\2\'\u0151\3\2\2\2)\u0154\3\2\2\2+\u015d\3\2\2\2")
        buf.write("-\u0162\3\2\2\2/\u0168\3\2\2\2\61\u016e\3\2\2\2\63\u0175")
        buf.write("\3\2\2\2\65\u017c\3\2\2\2\67\u017e\3\2\2\29\u0180\3\2")
        buf.write("\2\2;\u0182\3\2\2\2=\u0184\3\2\2\2?\u0186\3\2\2\2A\u0188")
        buf.write("\3\2\2\2C\u018a\3\2\2\2E\u018c\3\2\2\2G\u018e\3\2\2\2")
        buf.write("I\u0190\3\2\2\2K\u0192\3\2\2\2M\u0194\3\2\2\2O\u0196\3")
        buf.write("\2\2\2Q\u0198\3\2\2\2S\u019a\3\2\2\2U\u019c\3\2\2\2W\u019e")
        buf.write("\3\2\2\2Y\u01a0\3\2\2\2[\u01a2\3\2\2\2]\u01a4\3\2\2\2")
        buf.write("_\u01a6\3\2\2\2a\u01a8\3\2\2\2c\u01aa\3\2\2\2e\u01ac\3")
        buf.write("\2\2\2g\u01ae\3\2\2\2i\u01b0\3\2\2\2k\u01b2\3\2\2\2m\u01b4")
        buf.write("\3\2\2\2o\u01b6\3\2\2\2q\u01b8\3\2\2\2s\u01ba\3\2\2\2")
        buf.write("u\u01bc\3\2\2\2w\u01bf\3\2\2\2y\u01c2\3\2\2\2{\u01c5\3")
        buf.write("\2\2\2}\u01c7\3\2\2\2\177\u01ca\3\2\2\2\u0081\u01cc\3")
        buf.write("\2\2\2\u0083\u01cf\3\2\2\2\u0085\u01d1\3\2\2\2\u0087\u01d4")
        buf.write("\3\2\2\2\u0089\u01d8\3\2\2\2\u008b\u01db\3\2\2\2\u008d")
        buf.write("\u01de\3\2\2\2\u008f\u01e0\3\2\2\2\u0091\u01e2\3\2\2\2")
        buf.write("\u0093\u01e4\3\2\2\2\u0095\u01e6\3\2\2\2\u0097\u01e8\3")
        buf.write("\2\2\2\u0099\u01ea\3\2\2\2\u009b\u01ec\3\2\2\2\u009d\u01ee")
        buf.write("\3\2\2\2\u009f\u01f0\3\2\2\2\u00a1\u01f6\3\2\2\2\u00a3")
        buf.write("\u0205\3\2\2\2\u00a5\u0207\3\2\2\2\u00a7\u0210\3\2\2\2")
        buf.write("\u00a9\u0218\3\2\2\2\u00ab\u022e\3\2\2\2\u00ad\u0232\3")
        buf.write("\2\2\2\u00af\u0234\3\2\2\2\u00b1\u0241\3\2\2\2\u00b3\u0248")
        buf.write("\3\2\2\2\u00b5\u0252\3\2\2\2\u00b7\u0254\3\2\2\2\u00b9")
        buf.write("\u025b\3\2\2\2\u00bb\u025d\3\2\2\2\u00bd\u0260\3\2\2\2")
        buf.write("\u00bf\u026c\3\2\2\2\u00c1\u0279\3\2\2\2\u00c3\u027b\3")
        buf.write("\2\2\2\u00c5\u027d\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7\64\2\2\u00cb")
        buf.write("\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7v\2\2\u00ce")
        buf.write("\4\3\2\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7p\2\2\u00d1")
        buf.write("\u00d2\7v\2\2\u00d2\u00d3\7\64\2\2\u00d3\u00d4\7u\2\2")
        buf.write("\u00d4\u00d5\7v\2\2\u00d5\u00d6\7t\2\2\u00d6\6\3\2\2\2")
        buf.write("\u00d7\u00d8\7u\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7t")
        buf.write("\2\2\u00da\u00db\7\64\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd")
        buf.write("\7n\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7c\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0\b\3\2\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3")
        buf.write("\7n\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7\64\2\2\u00e7\u00e8\7u\2\2\u00e8")
        buf.write("\u00e9\7v\2\2\u00e9\u00ea\7t\2\2\u00ea\n\3\2\2\2\u00eb")
        buf.write("\u00ec\7u\2\2\u00ec\u00ed\7v\2\2\u00ed\u00ee\7t\2\2\u00ee")
        buf.write("\u00ef\7\64\2\2\u00ef\u00f0\7d\2\2\u00f0\u00f1\7q\2\2")
        buf.write("\u00f1\u00f2\7q\2\2\u00f2\u00f3\7n\2\2\u00f3\f\3\2\2\2")
        buf.write("\u00f4\u00f5\7d\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7q")
        buf.write("\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7\64\2\2\u00f9\u00fa")
        buf.write("\7u\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7t\2\2\u00fc\16")
        buf.write("\3\2\2\2\u00fd\u00ff\t\2\2\2\u00fe\u00fd\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102\u0103\b\b\2\2\u0103\20\3\2")
        buf.write("\2\2\u0104\u0105\7\61\2\2\u0105\u0106\7,\2\2\u0106\u010a")
        buf.write("\3\2\2\2\u0107\u0109\13\2\2\2\u0108\u0107\3\2\2\2\u0109")
        buf.write("\u010c\3\2\2\2\u010a\u010b\3\2\2\2\u010a\u0108\3\2\2\2")
        buf.write("\u010b\u010d\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e\7")
        buf.write(",\2\2\u010e\u010f\7\61\2\2\u010f\u0110\3\2\2\2\u0110\u0111")
        buf.write("\b\t\2\2\u0111\22\3\2\2\2\u0112\u0114\7&\2\2\u0113\u0115")
        buf.write("\t\3\2\2\u0114\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\24\3\2\2\2\u0118")
        buf.write("\u011c\t\4\2\2\u0119\u011b\t\3\2\2\u011a\u0119\3\2\2\2")
        buf.write("\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3")
        buf.write("\2\2\2\u011d\26\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0121")
        buf.write("\7a\2\2\u0120\u0122\t\3\2\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\u0123\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2")
        buf.write("\u0124\30\3\2\2\2\u0125\u0126\7d\2\2\u0126\u0127\5W,\2")
        buf.write("\u0127\u0128\5=\37\2\u0128\u0129\5\65\33\2\u0129\u012a")
        buf.write("\5I%\2\u012a\32\3\2\2\2\u012b\u012c\7e\2\2\u012c\u012d")
        buf.write("\5Q)\2\u012d\u012e\5O(\2\u012e\u012f\5[.\2\u012f\u0130")
        buf.write("\5E#\2\u0130\u0131\5O(\2\u0131\u0132\5]/\2\u0132\u0133")
        buf.write("\5=\37\2\u0133\34\3\2\2\2\u0134\u0135\7k\2\2\u0135\u0136")
        buf.write("\5? \2\u0136\36\3\2\2\2\u0137\u0138\7g\2\2\u0138\u0139")
        buf.write("\5K&\2\u0139\u013a\5Y-\2\u013a\u013b\5=\37\2\u013b\u013c")
        buf.write("\5E#\2\u013c\u013d\5? \2\u013d \3\2\2\2\u013e\u013f\7")
        buf.write("g\2\2\u013f\u0140\5K&\2\u0140\u0141\5Y-\2\u0141\u0142")
        buf.write("\5=\37\2\u0142\"\3\2\2\2\u0143\u0144\7y\2\2\u0144\u0145")
        buf.write("\5C\"\2\u0145\u0146\5E#\2\u0146\u0147\5K&\2\u0147\u0148")
        buf.write("\5=\37\2\u0148$\3\2\2\2\u0149\u014a\7h\2\2\u014a\u014b")
        buf.write("\5Q)\2\u014b\u014c\5W,\2\u014c\u014d\5=\37\2\u014d\u014e")
        buf.write("\5\65\33\2\u014e\u014f\59\35\2\u014f\u0150\5C\"\2\u0150")
        buf.write("&\3\2\2\2\u0151\u0152\7c\2\2\u0152\u0153\5Y-\2\u0153(")
        buf.write("\3\2\2\2\u0154\u0155\7h\2\2\u0155\u0156\5]/\2\u0156\u0157")
        buf.write("\5O(\2\u0157\u0158\59\35\2\u0158\u0159\5[.\2\u0159\u015a")
        buf.write("\5E#\2\u015a\u015b\5Q)\2\u015b\u015c\5O(\2\u015c*\3\2")
        buf.write("\2\2\u015d\u015e\7v\2\2\u015e\u015f\5W,\2\u015f\u0160")
        buf.write("\5]/\2\u0160\u0161\5=\37\2\u0161,\3\2\2\2\u0162\u0163")
        buf.write("\7h\2\2\u0163\u0164\5\65\33\2\u0164\u0165\5K&\2\u0165")
        buf.write("\u0166\5Y-\2\u0166\u0167\5=\37\2\u0167.\3\2\2\2\u0168")
        buf.write("\u0169\7c\2\2\u0169\u016a\5W,\2\u016a\u016b\5W,\2\u016b")
        buf.write("\u016c\5\65\33\2\u016c\u016d\5e\63\2\u016d\60\3\2\2\2")
        buf.write("\u016e\u016f\7f\2\2\u016f\u0170\5=\37\2\u0170\u0171\5")
        buf.write("? \2\u0171\u0172\5E#\2\u0172\u0173\5O(\2\u0173\u0174\5")
        buf.write("=\37\2\u0174\62\3\2\2\2\u0175\u0176\7t\2\2\u0176\u0177")
        buf.write("\5=\37\2\u0177\u0178\5[.\2\u0178\u0179\5]/\2\u0179\u017a")
        buf.write("\5W,\2\u017a\u017b\5O(\2\u017b\64\3\2\2\2\u017c\u017d")
        buf.write("\t\5\2\2\u017d\66\3\2\2\2\u017e\u017f\t\6\2\2\u017f8\3")
        buf.write("\2\2\2\u0180\u0181\t\7\2\2\u0181:\3\2\2\2\u0182\u0183")
        buf.write("\t\b\2\2\u0183<\3\2\2\2\u0184\u0185\t\t\2\2\u0185>\3\2")
        buf.write("\2\2\u0186\u0187\t\n\2\2\u0187@\3\2\2\2\u0188\u0189\t")
        buf.write("\13\2\2\u0189B\3\2\2\2\u018a\u018b\t\f\2\2\u018bD\3\2")
        buf.write("\2\2\u018c\u018d\t\r\2\2\u018dF\3\2\2\2\u018e\u018f\t")
        buf.write("\16\2\2\u018fH\3\2\2\2\u0190\u0191\t\17\2\2\u0191J\3\2")
        buf.write("\2\2\u0192\u0193\t\20\2\2\u0193L\3\2\2\2\u0194\u0195\t")
        buf.write("\21\2\2\u0195N\3\2\2\2\u0196\u0197\t\22\2\2\u0197P\3\2")
        buf.write("\2\2\u0198\u0199\t\23\2\2\u0199R\3\2\2\2\u019a\u019b\t")
        buf.write("\24\2\2\u019bT\3\2\2\2\u019c\u019d\t\25\2\2\u019dV\3\2")
        buf.write("\2\2\u019e\u019f\t\26\2\2\u019fX\3\2\2\2\u01a0\u01a1\t")
        buf.write("\27\2\2\u01a1Z\3\2\2\2\u01a2\u01a3\t\30\2\2\u01a3\\\3")
        buf.write("\2\2\2\u01a4\u01a5\t\31\2\2\u01a5^\3\2\2\2\u01a6\u01a7")
        buf.write("\t\32\2\2\u01a7`\3\2\2\2\u01a8\u01a9\t\33\2\2\u01a9b\3")
        buf.write("\2\2\2\u01aa\u01ab\t\34\2\2\u01abd\3\2\2\2\u01ac\u01ad")
        buf.write("\t\35\2\2\u01adf\3\2\2\2\u01ae\u01af\t\36\2\2\u01afh\3")
        buf.write("\2\2\2\u01b0\u01b1\7-\2\2\u01b1j\3\2\2\2\u01b2\u01b3\7")
        buf.write("/\2\2\u01b3l\3\2\2\2\u01b4\u01b5\7,\2\2\u01b5n\3\2\2\2")
        buf.write("\u01b6\u01b7\7\61\2\2\u01b7p\3\2\2\2\u01b8\u01b9\7\'\2")
        buf.write("\2\u01b9r\3\2\2\2\u01ba\u01bb\7#\2\2\u01bbt\3\2\2\2\u01bc")
        buf.write("\u01bd\7(\2\2\u01bd\u01be\7(\2\2\u01bev\3\2\2\2\u01bf")
        buf.write("\u01c0\7~\2\2\u01c0\u01c1\7~\2\2\u01c1x\3\2\2\2\u01c2")
        buf.write("\u01c3\7?\2\2\u01c3\u01c4\7?\2\2\u01c4z\3\2\2\2\u01c5")
        buf.write("\u01c6\7?\2\2\u01c6|\3\2\2\2\u01c7\u01c8\7#\2\2\u01c8")
        buf.write("\u01c9\7?\2\2\u01c9~\3\2\2\2\u01ca\u01cb\7@\2\2\u01cb")
        buf.write("\u0080\3\2\2\2\u01cc\u01cd\7@\2\2\u01cd\u01ce\7?\2\2\u01ce")
        buf.write("\u0082\3\2\2\2\u01cf\u01d0\7>\2\2\u01d0\u0084\3\2\2\2")
        buf.write("\u01d1\u01d2\7>\2\2\u01d2\u01d3\7?\2\2\u01d3\u0086\3\2")
        buf.write("\2\2\u01d4\u01d5\7?\2\2\u01d5\u01d6\7?\2\2\u01d6\u01d7")
        buf.write("\7\60\2\2\u01d7\u0088\3\2\2\2\u01d8\u01d9\7-\2\2\u01d9")
        buf.write("\u01da\7\60\2\2\u01da\u008a\3\2\2\2\u01db\u01dc\7?\2\2")
        buf.write("\u01dc\u01dd\7@\2\2\u01dd\u008c\3\2\2\2\u01de\u01df\7")
        buf.write("*\2\2\u01df\u008e\3\2\2\2\u01e0\u01e1\7+\2\2\u01e1\u0090")
        buf.write("\3\2\2\2\u01e2\u01e3\7]\2\2\u01e3\u0092\3\2\2\2\u01e4")
        buf.write("\u01e5\7_\2\2\u01e5\u0094\3\2\2\2\u01e6\u01e7\7<\2\2\u01e7")
        buf.write("\u0096\3\2\2\2\u01e8\u01e9\7\60\2\2\u01e9\u0098\3\2\2")
        buf.write("\2\u01ea\u01eb\7.\2\2\u01eb\u009a\3\2\2\2\u01ec\u01ed")
        buf.write("\7=\2\2\u01ed\u009c\3\2\2\2\u01ee\u01ef\7}\2\2\u01ef\u009e")
        buf.write("\3\2\2\2\u01f0\u01f1\7\177\2\2\u01f1\u00a0\3\2\2\2\u01f2")
        buf.write("\u01f7\5\u00a3R\2\u01f3\u01f7\5\u00a5S\2\u01f4\u01f7\5")
        buf.write("\u00a7T\2\u01f5\u01f7\5\u00a9U\2\u01f6\u01f2\3\2\2\2\u01f6")
        buf.write("\u01f3\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f5\3\2\2\2")
        buf.write("\u01f7\u01f8\3\2\2\2\u01f8\u01f9\bQ\3\2\u01f9\u00a2\3")
        buf.write("\2\2\2\u01fa\u0206\7\62\2\2\u01fb\u0203\t\37\2\2\u01fc")
        buf.write("\u01fe\t \2\2\u01fd\u01fc\3\2\2\2\u01fe\u0201\3\2\2\2")
        buf.write("\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0202\3")
        buf.write("\2\2\2\u0201\u01ff\3\2\2\2\u0202\u0204\t!\2\2\u0203\u01ff")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205")
        buf.write("\u01fa\3\2\2\2\u0205\u01fb\3\2\2\2\u0206\u00a4\3\2\2\2")
        buf.write("\u0207\u0208\7\62\2\2\u0208\u0209\t\34\2\2\u0209\u020d")
        buf.write("\t\"\2\2\u020a\u020c\t#\2\2\u020b\u020a\3\2\2\2\u020c")
        buf.write("\u020f\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2")
        buf.write("\u020e\u00a6\3\2\2\2\u020f\u020d\3\2\2\2\u0210\u0211\7")
        buf.write("\62\2\2\u0211\u0215\t$\2\2\u0212\u0214\t%\2\2\u0213\u0212")
        buf.write("\3\2\2\2\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216\u00a8\3\2\2\2\u0217\u0215\3\2\2\2")
        buf.write("\u0218\u0219\7\62\2\2\u0219\u021a\t\6\2\2\u021a\u021e")
        buf.write("\7\63\2\2\u021b\u021d\t&\2\2\u021c\u021b\3\2\2\2\u021d")
        buf.write("\u0220\3\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2")
        buf.write("\u021f\u00aa\3\2\2\2\u0220\u021e\3\2\2\2\u0221\u0222\5")
        buf.write("\u00adW\2\u0222\u0223\5\u00afX\2\u0223\u0224\5\u00b1Y")
        buf.write("\2\u0224\u022f\3\2\2\2\u0225\u0226\5\u00afX\2\u0226\u0227")
        buf.write("\5\u00b1Y\2\u0227\u022f\3\2\2\2\u0228\u0229\5\u00adW\2")
        buf.write("\u0229\u022a\5\u00b1Y\2\u022a\u022f\3\2\2\2\u022b\u022c")
        buf.write("\5\u00adW\2\u022c\u022d\5\u00afX\2\u022d\u022f\3\2\2\2")
        buf.write("\u022e\u0221\3\2\2\2\u022e\u0225\3\2\2\2\u022e\u0228\3")
        buf.write("\2\2\2\u022e\u022b\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0231")
        buf.write("\bV\4\2\u0231\u00ac\3\2\2\2\u0232\u0233\5\u00a3R\2\u0233")
        buf.write("\u00ae\3\2\2\2\u0234\u023f\5\u0097L\2\u0235\u0239\t!\2")
        buf.write("\2\u0236\u0238\t \2\2\u0237\u0236\3\2\2\2\u0238\u023b")
        buf.write("\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a")
        buf.write("\u023d\3\2\2\2\u023b\u0239\3\2\2\2\u023c\u0235\3\2\2\2")
        buf.write("\u023c\u023d\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u0240\t")
        buf.write("\37\2\2\u023f\u023c\3\2\2\2\u023f\u0240\3\2\2\2\u0240")
        buf.write("\u00b0\3\2\2\2\u0241\u0244\t\t\2\2\u0242\u0245\5i\65\2")
        buf.write("\u0243\u0245\5k\66\2\u0244\u0242\3\2\2\2\u0244\u0243\3")
        buf.write("\2\2\2\u0244\u0245\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247")
        buf.write("\5\u00adW\2\u0247\u00b2\3\2\2\2\u0248\u024c\5\u00b5[\2")
        buf.write("\u0249\u024b\5\u00b9]\2\u024a\u0249\3\2\2\2\u024b\u024e")
        buf.write("\3\2\2\2\u024c\u024a\3\2\2\2\u024c\u024d\3\2\2\2\u024d")
        buf.write("\u024f\3\2\2\2\u024e\u024c\3\2\2\2\u024f\u0250\5\u00b5")
        buf.write("[\2\u0250\u0251\bZ\5\2\u0251\u00b4\3\2\2\2\u0252\u0253")
        buf.write("\7$\2\2\u0253\u00b6\3\2\2\2\u0254\u0255\7)\2\2\u0255\u00b8")
        buf.write("\3\2\2\2\u0256\u025c\n\'\2\2\u0257\u0258\5\u00b7\\\2\u0258")
        buf.write("\u0259\5\u00b5[\2\u0259\u025c\3\2\2\2\u025a\u025c\5\u00bb")
        buf.write("^\2\u025b\u0256\3\2\2\2\u025b\u0257\3\2\2\2\u025b\u025a")
        buf.write("\3\2\2\2\u025c\u00ba\3\2\2\2\u025d\u025e\7^\2\2\u025e")
        buf.write("\u025f\t(\2\2\u025f\u00bc\3\2\2\2\u0260\u0264\5\u00b5")
        buf.write("[\2\u0261\u0263\5\u00b9]\2\u0262\u0261\3\2\2\2\u0263\u0266")
        buf.write("\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265")
        buf.write("\u0268\3\2\2\2\u0266\u0264\3\2\2\2\u0267\u0269\t)\2\2")
        buf.write("\u0268\u0267\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u026b\b")
        buf.write("_\6\2\u026b\u00be\3\2\2\2\u026c\u0270\5\u00b5[\2\u026d")
        buf.write("\u026f\5\u00b9]\2\u026e\u026d\3\2\2\2\u026f\u0272\3\2")
        buf.write("\2\2\u0270\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u0273")
        buf.write("\3\2\2\2\u0272\u0270\3\2\2\2\u0273\u0274\5\u00c1a\2\u0274")
        buf.write("\u0275\b`\7\2\u0275\u00c0\3\2\2\2\u0276\u0277\7^\2\2\u0277")
        buf.write("\u027a\n(\2\2\u0278\u027a\n*\2\2\u0279\u0276\3\2\2\2\u0279")
        buf.write("\u0278\3\2\2\2\u027a\u00c2\3\2\2\2\u027b\u027c\13\2\2")
        buf.write("\2\u027c\u00c4\3\2\2\2\u027d\u027e\7\61\2\2\u027e\u027f")
        buf.write("\7,\2\2\u027f\u0283\3\2\2\2\u0280\u0282\13\2\2\2\u0281")
        buf.write("\u0280\3\2\2\2\u0282\u0285\3\2\2\2\u0283\u0284\3\2\2\2")
        buf.write("\u0283\u0281\3\2\2\2\u0284\u0286\3\2\2\2\u0285\u0283\3")
        buf.write("\2\2\2\u0286\u0287\n+\2\2\u0287\u00c6\3\2\2\2\33\2\u0100")
        buf.write("\u010a\u0116\u011c\u0123\u01f6\u01ff\u0203\u0205\u020d")
        buf.write("\u0215\u021e\u022e\u0239\u023c\u023f\u0244\u024c\u025b")
        buf.write("\u0264\u0268\u0270\u0279\u0283\b\b\2\2\3Q\2\3V\3\3Z\4")
        buf.write("\3_\5\3`\6")
        return buf.getvalue()


class D95Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    WS = 7
    BLOCK_COMMENT = 8
    VPID = 9
    CID = 10
    FID = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSEIF = 15
    ELSE = 16
    WHILE = 17
    FOREACH = 18
    AS = 19
    FUNCTION = 20
    TRUE = 21
    FALSE = 22
    ARRAY = 23
    DEFINE = 24
    RETURN = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    MOD = 30
    NOT = 31
    AND = 32
    OR = 33
    EQ = 34
    ASSIGN = 35
    NE = 36
    GT = 37
    GTE = 38
    LT = 39
    LTE = 40
    ED = 41
    AD = 42
    EGT = 43
    LP = 44
    RP = 45
    LSB = 46
    RSB = 47
    COLON = 48
    DOT = 49
    COMMA = 50
    SEMI = 51
    LCB = 52
    RCB = 53
    INTLIT = 54
    FLOATLIT = 55
    STRINGLIT = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    ERROR_CHAR = 59
    UNTERMINATED_COMMENT = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'str2int'", "'int2str'", "'str2float'", "'float2str'", "'str2bool'", 
            "'bool2str'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", 
            "'==.'", "'+.'", "'=>'", "'('", "')'", "'['", "']'", "':'", 
            "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BLOCK_COMMENT", "VPID", "CID", "FID", "BREAK", "CONTINUE", 
            "IF", "ELSEIF", "ELSE", "WHILE", "FOREACH", "AS", "FUNCTION", 
            "TRUE", "FALSE", "ARRAY", "DEFINE", "RETURN", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", "ASSIGN", "NE", 
            "GT", "GTE", "LT", "LTE", "ED", "AD", "EGT", "LP", "RP", "LSB", 
            "RSB", "COLON", "DOT", "COMMA", "SEMI", "LCB", "RCB", "INTLIT", 
            "FLOATLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "WS", 
                  "BLOCK_COMMENT", "VPID", "CID", "FID", "BREAK", "CONTINUE", 
                  "IF", "ELSEIF", "ELSE", "WHILE", "FOREACH", "AS", "FUNCTION", 
                  "TRUE", "FALSE", "ARRAY", "DEFINE", "RETURN", "A", "B", 
                  "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
                  "Y", "Z", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                  "OR", "EQ", "ASSIGN", "NE", "GT", "GTE", "LT", "LTE", 
                  "ED", "AD", "EGT", "LP", "RP", "LSB", "RSB", "COLON", 
                  "DOT", "COMMA", "SEMI", "LCB", "RCB", "INTLIT", "DEC", 
                  "HEX", "OCT", "BIN", "FLOATLIT", "IP", "DP", "EP", "STRINGLIT", 
                  "DoubQ", "SignQ", "STR_CHAR", "ESC_SEQ", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    grammarFileName = "PhongD95.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[79] = self.INTLIT_action 
            actions[84] = self.FLOATLIT_action 
            actions[88] = self.STRINGLIT_action 
            actions[93] = self.UNCLOSE_STRING_action 
            actions[94] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    string = str(self.text)
                    self.text = re.sub('_','',string)
                
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                        string = str(self.text)
                        self.text = re.sub('_','',string)
                    
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			self.text=y[1:-1]
            		else:
            			self.text=y[1:]
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		self.text=y[1:]
            	
     


