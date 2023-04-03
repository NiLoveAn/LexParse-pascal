import sys
import ply.lex as lex

tokens = (
    'VAR', 'PROGRAM', 'BEGIN', 'END', 'INTEGER', 'DOUBLE', 'AND', 'OR', 'XOR', 'BREAK', 'CONTINUE', 'WRITE',
    'IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'FOR', 'TO', 'NOT', 'IDENTIFIER', 'NUMBER', 'PLUS', 'MINUS',
    'MULTIPLY', 'DIVIDE', 'ASSIGN', 'BOLEE', 'MENEE', 'SEMICOLON', 'LPAREN', 'RPAREN', 'DOT', 'COMMA', 'COLON'
)

t_IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9_]*|(?<![0-9])[0-9]+[a-zA-Z_]+'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_ASSIGN = r':='
t_BOLEE = r'\>'
t_MENEE = r'\<'
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_COMMA = r','
t_COLON = r':'


t_ignore = ' \t'
t_ignore_COMMENT = '//.*'


def t_PROGRAM(t):
    'program\s+[a-zA-Z][a-zA-Z0-9_]*|(?<![0-9])[0-9]+[a-zA-Z_]+'
    t.value = str(t.value)
    return t

def t_BEGIN(t):
    'begin'
    t.value = str(t.value)
    return t

def t_END(t):
    'end'
    t.value = str(t.value)
    return t

def t_INTEGER(t):
    'integer'
    t.value = str(t.value)
    return t

def t_DOUBLE(t):
    'double'
    t.value = str(t.value)
    return t

def t_AND(t):
    'and'
    t.value = str(t.value)
    return t

def t_OR(t):
    'or'
    t.value = str(t.value)
    return t

def t_XOR(t):
    'xor'
    t.value = str(t.value)
    return t

def t_BREAK(t):
    'break'
    t.value = str(t.value)
    return t

def t_CONTINUE(t):
    'continue'
    t.value = str(t.value)
    return t

def t_WRITE(t):
    'writeln'
    t.value = str(t.value)
    return t

def t_IF(t):
    'if'
    t.value = str(t.value)
    return t

def t_THEN(t):
    'then'
    t.value = str(t.value)
    return t

def t_ELSE(t):
    'else'
    t.value = str(t.value)
    return t

def t_WHILE(t):
    'while'
    t.value = str(t.value)
    return t

def t_DO(t):
    'do'
    t.value = str(t.value)
    return t

def t_FOR(t):
    'for'
    t.value = str(t.value)
    return t

def t_TO(t):
    'to'
    t.value = str(t.value)
    return t

def t_NOT(t):
    'not'
    t.value = str(t.value)
    return t

def t_VAR(t):
    'var'
    t.value = str(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("line %d: illegal character '%s'" %(t.lineno, t.value[0]) )
    t.lexer.skip(1)




lexer = lex.lex()

try:
    with open('test.pas', 'r') as reader:
        lexer.input(reader.read())
        for token in lexer:
            print("line %d: %s(%s)" %(token.lineno, token.type, token.value))

except OSError as error:
    print("Error: {0}".format(error))

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise