import ply.lex as lex
import ply.yacc as yacc
tokens = ('NAME','AND','OR','IMPLIES','NOT','OB','CB','COMMA')
t_AND=r'&'
t_OR=r'\|'
t_IMPLIES=r'=>'
t_OB='\('
t_CB=r'\)'
t_COMMA=r','
#t_NAME=r'\[a-z]+'

def t_NAME(t):
    r'[a-z]+'
    print(t.value,"name")
    return t
'''
def p_arguments(p):
    """
    arguments : NAME COMMA NAME
    """
'''


def p_expression(p):
    """expression : expression AND expression
                  | expression OR expression
                  | expression IMPLIES expression
                  | OB expression OR expression CB
                  | OB expression AND expression CB
                  | OB expression IMPLIES expression CB
    """
    print(p[0],p[1],p[2],p[3])

    print(p[1])
    p[0] = p[1]
    return p[0]
def p_predicate(p):
    """expression : NAME OB expression CB
    """
    print(p[1])
    p[0]=p[1]
def p_arguments(p):
    """
    expression : expression COMMA expression
               | NAME
    """
lexer = lex.lex()
parser = yacc.yacc()
res = parser.parse("a(c,a,x)&b(a)")
print(res)
