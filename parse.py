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
    #print(t.value,"name")
    return t



def p_expression(p):
    """expression :  OB expression OR expression CB
                  | OB expression AND expression CB
                  | OB expression IMPLIES expression CB

    """
    if(p[3]=='=>'):
        p[0] = '('+'~'+p[2]+'|'+ p[4]+')'
        #print(a)
    else:
        p[0]=p[1]+p[2]+p[3]+p[4]+p[5]
    return p[0]
def p_predicate(p):
    """expression : NAME OB expression CB
    """
    print("predicate",p[0],p[1],p[2],p[3],p[4])
    p[0]=p[1]+p[2]+p[3]+p[4]
def p_arguments(p):
    """
    expression : expression COMMA expression
    """
    #print(p.lexer.type,'l')
    if(len(p)>2):
        print("arguments",p[0],p[1],p[2],p[3])
        p[0]=p[1]+p[2]+p[3]
def p_name(p):
    """
    expression : NAME
    """
    #print("name",p[1])
    p[0]=p[1]
lexer = lex.lex()
parser = yacc.yacc()
res = parser.parse("(((a(x)&d(o))=>b(y))=>c(z))")
print(res)
#(predicate(aq,ar,aw,hg,yt)=>pcate(bw))
