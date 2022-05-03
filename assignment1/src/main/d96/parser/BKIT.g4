// 1812783

grammar BKIT;

@lexer::header {
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

program  : var_dec_stmt* func_dec* EOF ;

// ----------PARSER----------
func_dec: FUNCTION COLON IDENTIFIER param_dec? body;
param_dec: PARAMETER COLON param_list;
param_list: param (COMMA param)*;
param: IDENTIFIER dimension?;
body: BODY COLON var_dec_stmt* stmt* ENDBODY DOT;
stmt: ass_stmt|if_stmt|for_stmt|while_stmt|do_while_stmt|call_stmt|return_stmt;

// -----EXPRESSION-----
// ---ARITHMETIC OPERATOR---
// arithm_op: PLUS|MINUS|MUL|DIV|REM;
// float_arithm_op: FLOAT_PLUS|FLOAT_MINUS|FLOAT_MUL|FLOAT_DIV;

// ---BOOLEAN OPERATOR---
// bool_op: NEG|CONJ|DISJ;

// ---RELATIONAL OPERATOR---
// rel_op: EQEQ|NOTEQEQ|LESS|GREATER|LESSOREQ|GREATEROREQ;
// float_rel_op: FLOAT_NOTEQEQ|FLOAT_LESS|FLOAT_GREATER|FLOAT_LESSOREQ|FLOAT_GREATEROREQ;

// ---INDEX OPERATOR---
ele_expr: expr idx_op;
idx_op
    : LSB integer_expr RSB
    | LSB integer_expr RSB idx_op
    ;

// ---FUNCTION CALL---
func_call
    : IDENTIFIER LP argument_list? RP
    | type_coer_func
    | 'printLn' LP RP
    | 'print' LP STRING RP
    | 'printStrLn' LP STRING RP
    | 'read' LP RP
    ;
argument_list: (expr|STRING) (COMMA (expr|STRING))*;

// ---OPERATOR PRECEDENCE AND ASSOCIATIVITY---
//expr
//    : LP expr RP
//    | func_call
//    | IDENTIFIER idx_op                 // IDENTIFIER
//    | sign expr                         // INTEGER|FLOAT
//    | logical_neg expr                  // BOOLEAN
//    | expr multiplying expr             // INTEGER|FLOAT
//    | expr adding expr                  // INTEGER|FLOAT
//    | expr logical expr                 // BOOLEAN
//    | expr relational expr              // INTEGER|FLOAT
//    | (INTEGER|FLOAT|BOOLEAN)
//    | IDENTIFIER
//    ;

expr
    : integer_expr
    | float_expr
    | boolean_expr
    ;
integer_expr
    : LP expr RP
    | func_call
    | IDENTIFIER idx_op
    | MINUS integer_expr
    | integer_expr (MUL|DIV) integer_expr
    | integer_expr (PLUS|MINUS) integer_expr
    | integer_expr (EQEQ|NOTEQEQ|LESS|GREATER|LESSOREQ|GREATEROREQ) integer_expr
    | INTEGER
    | IDENTIFIER
    ;
float_expr
    : LP expr RP
    | func_call
    | IDENTIFIER idx_op
    | FLOAT_MINUS float_expr
    | float_expr (FLOAT_MUL|FLOAT_DIV) float_expr
    | float_expr (FLOAT_PLUS|FLOAT_MINUS) float_expr
    | float_expr (FLOAT_NOTEQEQ|FLOAT_LESS|FLOAT_GREATER|FLOAT_LESSOREQ|FLOAT_GREATEROREQ) float_expr
    | FLOAT
    | IDENTIFIER
    ;
boolean_expr
    : LP expr RP
    | func_call
    | IDENTIFIER idx_op
    | NEG boolean_expr
    | boolean_expr (CONJ|DISJ) boolean_expr
    | (integer_expr (EQEQ|NOTEQEQ|LESS|GREATER|LESSOREQ|GREATEROREQ) integer_expr | float_expr (FLOAT_NOTEQEQ|FLOAT_LESS|FLOAT_GREATER|FLOAT_LESSOREQ|FLOAT_GREATEROREQ) float_expr)
    | BOOLEAN
    | IDENTIFIER
    ;

//sign: MINUS|FLOAT_MINUS;
//logical_neg: NEG;
//multiplying: MUL|FLOAT_MUL|DIV|FLOAT_DIV|REM;
//adding: PLUS|FLOAT_PLUS|MINUS|FLOAT_MINUS;
//logical: CONJ|DISJ;
//relational: EQEQ|NOTEQEQ|LESS|GREATER|LESSOREQ|GREATEROREQ|FLOAT_NOTEQEQ|FLOAT_LESS|FLOAT_GREATER|FLOAT_LESSOREQ|FLOAT_GREATEROREQ;

// ---TYPE COERCION---
type_coer_func
    : 'int_of_float' LP float_expr RP
    | 'float_to_int' LP integer_expr RP
    | 'int_of_string' LP STRING RP
    | 'string_of_int' LP integer_expr RP
    | 'float_of_string' LP STRING RP
    | 'string_of_float' LP float_expr RP
    | 'bool_of_string' LP STRING RP
    | 'string_of_bool' LP boolean_expr RP
    ;

// ---EVALUATION ORDER---

// -----STATEMENT-----
// ---VARIABLE DECLARATION STATEMENT---
var_dec_stmt: VAR COLON var_list SEMICOLON;
var_list: var (COMMA var)*;
var
    : IDENTIFIER (EQUAL (INTEGER|FLOAT|BOOLEAN|STRING))?
    | IDENTIFIER dimension (EQUAL array)?
    ;
dimension: LSB INTEGER RSB dimension*;

// ---ASSIGNMENT STATEMENT---
ass_stmt: IDENTIFIER idx_op? EQUAL (expr|STRING) SEMICOLON;

// ---IF STATEMENT---
if_stmt: IF expr THEN var_dec_stmt* stmt* (ELSEIF expr THEN var_dec_stmt* stmt*)* (ELSE var_dec_stmt* stmt*)? ENDIF DOT;

// ---FOR STATEMENT---
for_stmt: FOR LP IDENTIFIER EQUAL init_expr COMMA condition_expr COMMA update_expr RP DO var_dec_stmt* (stmt|break_stmt|continue_stmt)* ENDFOR DOT;
init_expr: integer_expr;
condition_expr: boolean_expr;
update_expr: integer_expr;

// ---WHILE STATEMENT---
while_stmt: WHILE expr DO var_dec_stmt* (stmt|break_stmt|continue_stmt)* ENDWHILE DOT;

// ---DO-WHILE STATEMENT---
do_while_stmt: DO var_dec_stmt* (stmt|break_stmt|continue_stmt)* WHILE expr ENDDO DOT;

// ---BREAK STATEMENT---
break_stmt: BREAK SEMICOLON;

// ---CONTINUE STATEMENT---
continue_stmt: CONTINUE SEMICOLON;

// ---CALL STATEMENT---
call_stmt: func_call SEMICOLON;

// ---RETURN STATEMENT---
return_stmt: RETURN expr? SEMICOLON;

// ----------LEXER----------

WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs, newlines

COMMENT: '**' .*? '**' -> skip;

IDENTIFIER: [a-z][A-Za-z_0-9]*;

BOOLEAN: TRUE|FALSE; // MOVE THIS TOKEN FROM BELOW TO HERE (BEFORE THE 2 TOKENS TRUE AND FALSE) ELSE IT WOULD NOT RECOGNIZE TOKEN BOOLEAN IN PARSER PART ABOVE

BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return'; 
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
TRUE: 'True';
FALSE: 'False';
ENDDO: 'EndDo';

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '\\';
REM: '%';
FLOAT_PLUS: '+.';
FLOAT_MINUS: '-.';
FLOAT_MUL: '*.';
FLOAT_DIV: '\\.';

NEG: '!';
CONJ: '&&';
DISJ: '||';

EQEQ: '==';
NOTEQEQ: '!=';
LESS: '<';
GREATER: '>';
LESSOREQ: '<=';
GREATEROREQ: '>=';
FLOAT_NOTEQEQ: '=/=';
FLOAT_LESS: '<.';
FLOAT_GREATER: '>.';
FLOAT_LESSOREQ: '<=.';
FLOAT_GREATEROREQ: '>=.';

//SEPERATOR: LP|RP|LSB|RSB|COLON|DOT|COMMA|LCB|RCB;
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
COLON: ':';
DOT: '.';
COMMA: ',';
SEMICOLON: ';';
LCB: '{';
RCB: '}';

EQUAL: '='; // NO EXPLICIT DESCRIPTION IN THE SPECIFICATION

INTEGER: Decimal|Hexadecimal|Octal;
fragment Decimal: '0'|[1-9][0-9]*;
fragment Hexadecimal: '0'[xX][1-9A-F][0-9A-F]*;
fragment Octal: '0'[oO][1-7][0-7]*;

FLOAT: [0-9]+(Decimal_part|Exponent_part|Decimal_part Exponent_part);
fragment Decimal_part: '.'[0-9]*;
fragment Exponent_part: [eE][+-]?[0-9]+;

//BOOLEAN: TRUE|FALSE;

STRING
    : '"' (Esc|'\'''"'|~('\\'|'\''))*? '"'
    {self.text = self.text[1:-1]}
    ;
fragment Esc: '\\'[bfrnt'\\];

//ARRAY: LCB [ ]* literal [ ]* (COMMA [ ]* literal)* [ ]* RCB;
array: LCB literal (COMMA literal)* RCB;

literal: INTEGER|FLOAT|BOOLEAN|STRING|array;


UNCLOSE_STRING
    : '"' (Esc|'\'''"'|~('\\'|'\''|'"'))*? EOF
    {self.text = self.text[1:]}
    ;
ILLEGAL_ESCAPE
    : '"' (Esc|'\'''"'|~('\\'|'\''|'"'))*? (('\\'((~[bfrnt'\\])|EOF))|'\''((~'"')|EOF))
    {self.text = self.text[1:]}
    ;
UNTERMINATED_COMMENT: '**' ('*'(~'*'|EOF)|~'*')*? EOF;
ERROR_CHAR: .;