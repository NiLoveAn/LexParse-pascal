import ply.yacc as yacc
from lex import tokens

class Node:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append( str( part ) )
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts

# Определение грамматики языка
#################################################################################

def p_program(p):
    '''program : PROGRAM SEMICOLON body'''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = p[3]

def p_body(p):
    '''body :
            | body sbody fbody'''
    if len(p) > 1:
        if p[1] is None:
            p[1] = Node('body', [])
        p[0] = p[1].add_parts([p[2]])
    else:
        p[0] = Node('body', [])

#################################################################################

def p_sbody(p):
    '''sbody : var variables'''

def p_var(p):
    'var  : VAR'
    p[0] = Node('var', [p[1]])

def p_variables(p):
    'variables : perem types'

def p_perem(p):
    ''' perem : IDENTIFIER
            | IDENTIFIER COMMA perem'''
    p[0] = p[1]

def p_types(p):
    '''types : COLON INTEGER SEMICOLON
            | COLON DOUBLE SEMICOLON '''


#################################################################################

def p_fbody(p):
    'fbody : BEGIN pascalbody END DOT '

def p_pascalbody(p):
    '''pascalbody : pascalline pascalcolons pascalbody
            | pascalline pascalcolons'''

def p_pascalcolons(p):
    '''pascalcolons : SEMICOLON
                 | pascalcolons SEMICOLON'''

def p_pascalline(p):
    '''pascalline : assign
                | func
                | expression
                | WRITE args'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('writeln', [p[2]])

#################################################################################

def p_assign(p):
    '''assign : IDENTIFIER ASSIGN expr'''
    p[0] = Node('assign', [p[1], p[3]])

def p_expression(p):
    '''expression : for
                  | if
                  | while'''

def p_expr(p):
    ''' expr : fact
            | expr PLUS fact
            | expr MINUS fact
        fact : term
            | fact MULTIPLY term
            | fact DIVIDE term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node(p[2], [p[1], p[3]])

def p_term(p):
    '''term : arg
            | LPAREN expr RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_func(p):
    '''func : IDENTIFIER LPAREN args RPAREN'''
    p[0] = Node('func', [p[1], p[3]])


def p_args(p):
    '''args :
            | expr
            | args COMMA expr'''
    if len(p) == 1:
        p[0] = Node('args', [])
    elif len(p) == 2:
        p[0] = Node('args', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])



def p_arg(p):
    '''arg : NUMBER
            | IDENTIFIER
            | func
            | NOT'''
    p[0] = Node('arg', [p[1]])

def p_for(p):
    'for : FOR IDENTIFIER ASSIGN NUMBER TO NUMBER DO BEGIN function END '

def p_if(p):
    '''if : IF arg operand arg THEN BEGIN function else END '''

def p_else(p):
    ''' else :
                | ELSE function '''

def p_while(p):
    'while : WHILE arg operand arg DO BEGIN function END '

def p_operand(p):
    '''operand : AND
                | XOR
                | OR
                | BOLEE
                | MENEE'''

def p_function(p):
    ''' function : assign SEMICOLON
                | func SEMICOLON
                | expression SEMICOLON
                | WRITE args SEMICOLON
                | assign SEMICOLON function
                | func SEMICOLON function
                | expression SEMICOLON function
                | WRITE args SEMICOLON function
                | BREAK SEMICOLON
                | CONTINUE SEMICOLON'''

#################################################################################

def p_error(p):
    print(p ,"Ошибка синтаксического анализа")

parser = yacc.yacc()

def build_tree(code):
    return parser.parse(code)

#################################################################################