// Bui Thanh Phong-2020062
grammar PhongD95;

@lexer::header {
import re
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}
/*
 * Assignment2
 */

program: constdecls decls EOF;

//**** PARSER ****

constdecls:constdecl constdecls|;

decls: (vardecl|funcdecl)decls| ;

vardecl: VPID ASSIGN expr SEMI;

constdecl: DEFINE LP CID COMMA expr RP SEMI;

funcdecl: FUNCTION FID LP (paramslist|) RP body ;

paramslist:VPID COMMA paramslist|VPID;

body: LCB stmts RCB;

stmts: (vardecl|ass_stmt|if_stmt|foreach_stmt|while_stmt|break_stmt|cont_stmt|call_stmt|return_stmt) stmts|;

//**** Expressions ****

//Index operators
idx_op
    : LSB expr RSB 
    | LSB expr RSB idx_op
    ;

//Function call
func_call: FID LP (argument_list | ) RP;

argument_list: expr COMMA argument_list | expr;

//Operator precedence and associativity
// expr
//     | func_call
//     | expr idx_op
//     | SUB expr
//     | NOT expr
//     | expr (MUL|DIV|MOD) expr
//     | expr (ADD|SUB) expr
//     | expr (AND|OR) expr
//     | expr (EQ|NE|LT|GT|LTE|GTE) expr 
//     | expr (AD|ED) expr
//     | expr EGT expr
//     | (INTLIT|FLOATLIT|BOOLEANLIT|STRINGLIT|iar|aar|mar)
//     | VPID(idx_op|) | CID (idx_op|) | type_coer_func
//     ;

expr:   expr1 EGT expr1|expr1;

expr1:  expr2 (AD|ED) expr2|expr2;

expr2:  expr3 (EQ|NE|LT|GT|LTE|GTE) expr3|expr3;

expr3:  expr3 (AND|OR) expr4|expr4; 

expr4:  expr4 (ADD|SUB) expr5|expr5;

expr5:  expr5 (MUL|DIV|MOD) expr6|expr6;

expr6:  NOT expr6|expr7;

expr7:  SUB expr7|expr8;

expr8:  (VPID|CID) idx_op|expr9;

expr9:  func_call|type_coer_func|operands;

operands
	: (INTLIT|FLOATLIT|booleanlit|STRINGLIT|array)
	| VPID | CID 
    | LP expr RP
	;
    
//Type coercions
type_coer_func: ('str2int'|'int2str'|'str2float'|'float2str'|'str2bool'|'bool2str') LP expr RP;

//**** Statements ****

//Asignment Statement
ass_stmt :(VPID|CID) idx_op ASSIGN expr SEMI;

//If Statement
if_stmt: IF stmt_if (elseif_stmts | ) (ELSE LCB stmts RCB | );

stmt_if: LP expr RP LCB stmts RCB;

elseif_stmts: ELSEIF stmt_if elseif_stmts | ELSEIF stmt_if;

//Foreach Statement
foreach_stmt: FOREACH LP expr AS VPID EGT VPID RP LCB stmts RCB;

//While Statement
while_stmt: WHILE LP expr RP LCB stmts RCB;

//Break Statement
break_stmt: BREAK SEMI;

//Continue Statement
cont_stmt: CONTINUE SEMI;

//Call Statement
call_stmt: func_call SEMI;

//Return Statement
return_stmt: RETURN (expr| ) SEMI;


/*
 * Assignment1
 */

// skip spaces, tabs, newlines
WS : [ \t\r\n\f]+ -> skip ; 

// Skip comments
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;

/*
 * Identifiers
 */

VPID: '$'[A-Za-z_0-9]+;

CID: [A-Z][A-Za-z0-9_]*;

FID: '_'[A-Za-z0-9_]+;

/*
 *Keywords
 */

BREAK:'b' R E A K;          CONTINUE:'c' O N T I N U E;     IF:'i' F;                

ELSEIF:'e' L S E I F;       ELSE:'e' L S E;                 WHILE:'w' H I L E;          

FOREACH:'f' O R E A C H;    AS:'a' S;                       FUNCTION:'f' U N C T I O N;    

TRUE:'t' R U E;             FALSE:'f' A L S E;              ARRAY:'a' R R A Y;          

DEFINE:'d' E F I N E;       RETURN:'r' E T U R N;

fragment A: [aA];   fragment B: [bB];   fragment C: [cC];
fragment D: [dD];   fragment E: [eE];   fragment F: [fF];
fragment G: [gG];   fragment H: [hH];   fragment I: [iI];
fragment J: [jJ];   fragment K: [kK];   fragment L: [lL];
fragment M: [mM];   fragment N: [nN];   fragment O: [oO];
fragment P: [pP];   fragment Q: [qQ];   fragment R: [rR];
fragment S: [sS];   fragment T: [tT];   fragment U: [uU];
fragment V: [vV];   fragment W: [wW];   fragment X: [xX];
fragment Y: [yY];   fragment Z: [zZ];

/*
 *Operators
 */

ADD:'+';    SUB:'-';    MUL:'*';    DIV:'/';

MOD:'%';    NOT:'!';    AND:'&&';   OR:'||';

EQ:'==';    ASSIGN:'=';    NE:'!=';    GT:'>';

GTE:'>=';   LT:'<';     LTE:'<=';   ED:'==.';

AD:'+.';    EGT:'=>';

/*
 *Seperators
 */
 
LP: '(';        RP: ')';        LSB: '[';       RSB: ']'; 
COLON: ':';     DOT: '.';       COMMA: ',';     SEMI: ';';
LCB: '{';       RCB: '}'; 

/*
 *Literals
 */

/* Integer*/
INTLIT: (DEC|HEX|OCT|BIN)
    {
        string = str(self.text)
        self.text = re.sub('_','',string)
    };

fragment DEC:'0'|[1-9]([0-9_]*[0-9])?;

fragment HEX:'0'[xX][1-9A-F][0-9A-F]*;

fragment OCT:'0' [1-7][0-7]*;

fragment BIN:'0' [bB] '1'[01]* ;

/* Float*/
FLOATLIT
        :(IP DP EP
        |DP EP
        |IP EP
        |IP DP)
        {
            string = str(self.text)
            self.text = re.sub('_','',string)
        };

fragment IP:DEC;

fragment DP:DOT (([0-9][0-9_]*)?[1-9])?;

fragment EP:[eE] (ADD|SUB)? IP;

/* Boolean*/
booleanlit: TRUE|FALSE;

/* String*/
STRINGLIT: DoubQ STR_CHAR* DoubQ
	{
		y = str(self.text)
		self.text = y[1:-1]
	};
    
fragment DoubQ:'"';

fragment SignQ:'\'';

fragment STR_CHAR: ~[\b\t\n\f\r"'\\] |SignQ DoubQ|ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;

/*ARRAY */
array:iar|aar|mar;

/* Indexed Array*/
iar:ARRAY LP (aints|afloats|astrings|abools|) RP;

aints: INTLIT COMMA aints | INTLIT;

afloats: FLOATLIT COMMA afloats | FLOATLIT;

astrings: STRINGLIT COMMA astrings | STRINGLIT;

abools: booleanlit COMMA abools | booleanlit;

/* Associative Array*/
aar:ARRAY LP aarraylists RP;

aarraylists: aarraylist COMMA aarraylists|aarraylist;

aarraylist: (INTLIT|STRINGLIT) EGT expr;

/* Multi-dimensional arrays*/
mar:ARRAY LP marraylists RP;

marraylists: (iar|aar|mar) COMMA marraylists| (iar|aar|mar);

/*
 *lexical errors
 */

 /* UNCLOSE_STRING */
UNCLOSE_STRING: DoubQ STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			self.text=y[1:-1]
		else:
			self.text=y[1:]
	};

/* ILLEGAL_ESCAPE*/
ILLEGAL_ESCAPE: DoubQ STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		self.text=y[1:]
	};

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;

/* ERROR_CHAR*/
ERROR_CHAR:.;

/*UNTERMINATED_COMMENT*/
UNTERMINATED_COMMENT: '/*' .*? ~[*/];



