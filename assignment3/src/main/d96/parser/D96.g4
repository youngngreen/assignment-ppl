// Le Nam Tien Thanh
// 2020088

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// Program structure
program: classdecls EOF;
classdecls: classdecl classdecls | classdecl;
classdecl: CLASS ID (COLON ID | ) LCB (memberlist | ) RCB;
memberlist: member memberlist | member;
member: attribute | method;

// Attribute declaration
attribute: mu_attribute | im_attribute;
mu_attribute: VAR att_names COLON typ (ASSIGN exprlist | ) SEMICOLON ;
im_attribute: VAL att_names COLON typ (ASSIGN exprlist | ) SEMICOLON ;
att_names: att_id COMMA att_names | att_id;
att_id: ID | DOLLARID;

// Method declaration
method: regularmethod | specialmethod;
// Regular method
regularmethod: (ID | DOLLARID) LP (paramlist | ) RP blockstm;

// Special methods
specialmethod: constructor | destructor;
constructor: CONSTRUCTOR LP (paramlist | ) RP blockstm;
destructor: DESTRUCTOR LP RP blockstm; // no return statement => next assignments

// List of parameter
paramlist: paramdecl SEMICOLON paramlist | paramdecl;
paramdecl: idlist COLON typ;
idlist: (ID | DOLLARID) COMMA idlist | (ID | DOLLARID);

// Type name
typ: INT | FLOAT | STRING | BOOLEAN | arraytype | ID; // ID is class type

// Array type
arraytype: ARRAY LSB typ COMMA NONZEROINT RSB;

// 5. Expressions

// 5.7. Object creation
objectcreation: ID LP (exprlist | ) RP; // association: RIGHT, but teacher's comfirmation is: no test case for this association.

// 5.9. Operator precedence and associativity
expr: expr1 (ADDSTR | EQUALSTR) expr1 | expr1; // association: NONE

expr1: expr2 (EQUAL | NEQ | LT | GT | LTE | GTE) expr2 | expr2; // association: NONE

expr2: expr2 (AND | OR) expr3 | expr3; // association: LEFT

expr3: expr3 (ADD | SUB) expr4 | expr4; // association: LEFT

expr4: expr4 (MUL | DIV | MOD) expr5 | expr5; // association: LEFT

expr5: NOT expr5 | expr6; // association: RIGHT

expr6: SUB expr6 | expr7; // association: RIGHT

//expr7: (ID | DOLLARID) indexopr | expr8; // check association: LEFT
expr7: expr7 indexopr | expr8; // check association: LEFT

expr8:
	expr8 DOT ID // Instance attribute access
	| expr8 DOT ID LP (exprlist | ) RP  // Instance method access
	| expr9 ; // check association: LEFT

expr9:
	ID DOUBLECOLON DOLLARID // Static attribute access
	| ID DOUBLECOLON DOLLARID LP (exprlist | ) RP // Static method invocation
	| expr10; // check association: NONE

expr10: NEW objectcreation| expr11; // association: RIGHT, but teacher's comfirmation is: no test case for this association.

expr11: LP expr RP | ID | DOLLARID | literal;

literal: intlit | FLOATLIT | booleanlit | STRINGLIT | arraylit | NULL | SELF;

// 5.10. Type coercions ??? this assignment?

// 5.11. Evaluation orders ??? this assignment?

exprlist: expr COMMA exprlist | expr; // not completed, please check!!!

// 6. Statements
statement: vardecl | constdecl | assignmentstm | ifstm | foreachstm | breakstm | continuestm | returnstm | methodinvostm | blockstm;
statementlist: statement statementlist | statement;

// 6.1 Variable and Constant declaration statement
vardecl: VAR varnames COLON typ (ASSIGN exprlist | ) SEMICOLON ;
constdecl: VAL varnames COLON typ (ASSIGN exprlist | ) SEMICOLON ;
varnames: ID COMMA varnames | ID;

// 6.2. Assignment statement
// assignmentstm: lhs ASSIGN expr SEMICOLON;
// lhs: ID | DOLLARID | expr indexopr;
assignmentstm: expr ASSIGN expr SEMICOLON;

// Index operators
indexopr: LSB expr RSB indexopr | LSB expr RSB; // association: LEFT???

// 6.3. If statement
ifstm: IF LP expr RP blockstm (else_stms | );
else_stms: elseif_stm else_stms | elseif_stm | else_stm;
elseif_stm: ELSEIF LP expr RP blockstm;
else_stm: ELSE blockstm;

// 6.4. Foreach - In statement
foreachstm: FOREACH LP ID IN expr DOUBLEDOT expr (BY expr | ) RP blockstm;

// 6.5. Break statement
breakstm: BREAK SEMICOLON;

// 6.6. Continue statement
continuestm: CONTINUE SEMICOLON;

// 6.7. Return statement
returnstm: RETURN (expr | ) SEMICOLON;


// 6.8. Method Invocation statement
methodinvostm: insmethodstm | stamethodstm;
insmethodstm: expr DOT ID LP (exprlist | ) RP SEMICOLON;
stamethodstm: ID DOUBLECOLON DOLLARID LP (exprlist | ) RP SEMICOLON;

// 6.9. Block statement
blockstm: LCB (statementlist | ) RCB;

// 7. Scope: how to treat scope? Does it belong to this assignment???

// Lexical structure

// Program comment
COMMENT: '##' .*? '##' -> skip;

// Keywords
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
SELF: 'Self';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN: '=';
NEQ: '!=';
GT: '>';
LT: '<';
GTE: '>=';
LTE: '<=';
EQUALSTR: '==.';
ADDSTR: '+.';
DOUBLECOLON: '::';

// Seperators
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
DOT: '.';
DOUBLEDOT: '..';
COMMA: ',';
COLON: ':'; // used in class declaration - superclass name
SEMICOLON: ';';
LCB: '{';
RCB: '}';

// Literals

// Integer literal
ZEROINT:  ZDEC | ZHEX | ZOCT | ZBIN;

fragment ZDEC: '0';
fragment ZHEX: '0' [xX] '0';
fragment ZOCT: '00';
fragment ZBIN: '0' [bB] '0';

NONZEROINT: (NDEC | NHEX | NOCT | NBIN)
	{
        string2=str(self.text)
        self.text=string2.replace("_","")
    }
;

fragment NDEC: [1-9] ([0-9_]* [0-9])?;
fragment NHEX: '0' [xX] [1-9A-F] ([0-9A-F_]* [0-9A-F])?;
fragment NOCT: '0' [1-7] ([0-7_]* [0-7])?;
fragment NBIN: '0' [bB] '1' ([01_]* [0-1])?;

intlit: ZEROINT | NONZEROINT;

// Float literal
FLOATLIT: (INTPART (DECPART EXPART | DECPART | EXPART) | DECPART EXPART)
	{
        string2=str(self.text)
        self.text=string2.replace("_","")
    }
;

fragment INTPART: ZDEC | NDEC;
//fragment DECPART: DOT (ZDEC | NDEC | );
fragment DECPART: DOT [0-9]*;
fragment EXPART: [eE] (ADD | SUB)? (ZDEC | NDEC);

// Boolean literal
booleanlit: TRUE | FALSE;

// Array literal
arraylit: idxarray | mularray;

// Indexed array
idxarray: ARRAY LP idxarraycontent RP;
idxarraycontent: intarr | floatarr | boolarr | stringarr;
intarr: intlit COMMA intarr | intlit;
floatarr: FLOATLIT COMMA floatarr | FLOATLIT;
stringarr: STRINGLIT COMMA stringarr | STRINGLIT;
boolarr: booleanlit COMMA boolarr | booleanlit;

// Multi-dimensional arrays
mularray: ARRAY LP mularraycontent RP;
mularraycontent: arraylit COMMA mularraycontent | arraylit;

// Identifiers
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

// Dollar identifiers
DOLLARID: '$' [a-zA-Z_0-9]+;

WS: [ \t\b\f\r\n]+ -> skip; // skip spaces, tabs, newlines

// lexical errors

// error token
ERROR_TOKEN: .
	{
		raise ErrorToken(self.text)
	}
;

// String literal
STRINGLIT: DQUOTE STRCONTENT* DQUOTE
	{
		string = str(self.text)
		self.text = string[1:-1]
	}
;

fragment DQUOTE: '"';
fragment SQUOTE: '\'';
// fragment STRCONTENT: ~[\b\f\r\n\t'\\] | SQUOTE DQUOTE | ESCSEQ;
fragment STRCONTENT: ~[\b\f\r\n\t"'\\] | SQUOTE DQUOTE | ESCSEQ;
// fragment ESCSEQ: [\b\f\r\n\t'\\];
//fragment ESCSEQ: '\\' [bfrnt"'\\] ;
fragment ESCSEQ: '\\' [bfrnt'\\] ;

// unclose string
//UNCLOSE_STRING: DQUOTE STRCONTENT* ( [\b\t\n\f\r"'\\] | EOF ) // please review?????
UNCLOSE_STRING: DQUOTE STRCONTENT* ( [\b\t\n\f\r'\\] | EOF ) // please review?????
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
;

// illegal escape
ILLEGAL_ESCAPE: DQUOTE STRCONTENT* ILGESC // waiting for teacher's comfirmation
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
;
//fragment ILGESC: '\\' ~[btnfr"'\\] | ~'\\' ; // please review?????
fragment ILGESC: '\\' ~[btnfr'\\] | ~'\\' ; // please review?????
