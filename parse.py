import ply.lex as lex
import ply.yacc as yacc

#strore sentence number,
count=1
KB={}
Table=[]
tokens = ('NAME','AND','OR','IMPLIES','NOT','OB','CB','COMMA')
t_AND=r'&'
t_NOT=r'~'
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
                  | OB NOT expression CB

    """
    if(p[3]=='=>'):
        #p[0] = '('+'~'+p[2]+'|'+ p[4]+')'
        p[0]=['or',['not',p[2]],p[4]]
    elif(p[3]=='&'):
        p[0]=['and',p[2],p[4]]
    elif(p[3]=='|'):
        p[0]=['or',p[2],p[4]]
    elif(p[2]=='~'):
        p[0]=['not',p[3]]
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
count=1
lexer = lex.lex()
parser = yacc.yacc()
res = parser.parse("((~a(o))=>v(p))")
print(res)
#(predicate(aq,ar,aw,hg,yt)=>pcate(bw))
operators=['&','|']
def Convert_To_CNF(Input):
    if(Input[0] not in operators and len(Input[1])==1 and len(Input[2])==1 ):
        return True
    if(Input[0]=='and'):
        return (Convert_To_CNF(Input[1])and Convert_To_CNF(Input[2]))
    if(Input[0]=='not' and Input[1][0]=='not'):
        Input=
