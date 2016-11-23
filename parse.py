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
'''
lexer = lex.lex()
parser = yacc.yacc()
res = parser.parse("((~a(o))=>v(p))")
print(res)
'''

#(predicate(aq,ar,aw,hg,yt)=>pcate(bw))
operators=['&','|']
def MoveNotInwards(Input):
    #print("begin",Input)
    while(Input[0]=='not' and type(Input[1]) is list ):
        #print("l",Input)
        Input=Demorgan(Input)
        #print(Input)
    #print("end",Input)
    c=1
    for i in Input[1:]:
        #print("i",i)
        if(type(i) is list):
            Input[c]=MoveNotInwards(i)
            c+=1
    return Input
def Demorgan(Input):
    #print("demorgan",Input)
    Output=[]
    if(type(Input)is not list):
        Output=Input
    elif(Input[1][0]=='not'):
        Output=Input[1][1]
    elif(Input[1][0]=='and'):
        #Output=['or',Demorgan(['not',Input[1]]),Demorgan(['not',Input[2])]
        Output=['or',['not',Input[1][1]],['not',Input[2][2]]]
    elif(Input[1][0]=='or'):
        print(Input)
        Output=['and',['not',Input[1][1]],['not',Input[1][2]]]
    elif(len(Input[1])==1):
        Output=Input
        #print("y")
    #print(Output)
    return Output
'''
def DistributeAnd(Input):
    Output=[]
    if(Input[0]=='or'):
        Input=DistributeAndHelper()

def DistributeAndHelper(Input):
    Output=['and']
    if(Input[1][0]=='and'):
        if(Input[2][0]=='and'):
            Output.append([])
 '''
def isDistributionCandidate(logic):

    if logic[0] == 'or':
        for i in range(1, len(logic)):
            if len(logic[i]) > 1:
                if logic[i][0] == 'and':
                    return True
    return False

def parseDistribution(logic):

    #Check if the logic is a candidate for distribution of OR over ANDs
    if isDistributionCandidate(logic):
        logic = distributeOR(logic)

    #For all the attributes in the logic repeat the process recursively
    for i in range(1, len(logic)):
        if len(logic[i]) > 1:
            logic[i] = parseDistribution(logic[i])

    #Check if the logic is a candidate for distribution of OR over ANDs

    if isDistributionCandidate(logic):
        logic = distributeOR(logic)

    #return distributed logic
    return logic

def distributeOR(logic):

    result = []
    #AND will propogate outwards
    result.append('and')

    #Check if both the lists are ands
    if logic[1][0] == 'and' and logic[2][0] == 'and':
        #Distribute the literals
        result.append(parseDistribution(['or', logic[1][1], logic[2][1]]))
        result.append(parseDistribution(['or', logic[1][1], logic[2][2]]))
        result.append(parseDistribution(['or', logic[1][2], logic[2][1]]))
        result.append(parseDistribution(['or', logic[1][2], logic[2][2]]))

    else:
        #Either one is and and
        if logic[1][0] == 'and':

            #Check if the second argument is a list
            if len(logic[2]) > 2:
                #check if its a candidate for distribution
                if isDistributionCandidate(logic[2]):
                    logic[2] = parseDistribution(logic[2])

                    #Distribute the literals
                    result.append(parseDistribution(['or', logic[1][1], logic[2][1]]))
                    result.append(parseDistribution(['or', logic[1][1], logic[2][2]]))
                    result.append(parseDistribution(['or', logic[1][2], logic[2][1]]))
                    result.append(parseDistribution(['or', logic[1][2], logic[2][2]]))

                else:
                    #Keep the second as it is
                    result.append(parseDistribution(['or', logic[1][1], logic[2]]))
                    result.append(parseDistribution(['or', logic[1][2], logic[2]]))

            else:
                #Keep the second as it is
                result.append(parseDistribution(['or', logic[1][1], logic[2]]))
                result.append(parseDistribution(['or', logic[1][2], logic[2]]))
        else:

            #Check if the second argument is a list
            if len(logic[1]) > 2:
                #check if its a candidate for distribution
                if isDistributionCandidate(logic[1]):
                    logic[1] = parseDistribution(logic[1])

                    #Distribute the literals
                    result.append(parseDistribution(['or', logic[1][1], logic[2][1]]))
                    result.append(parseDistribution(['or', logic[1][1], logic[2][2]]))
                    result.append(parseDistribution(['or', logic[1][2], logic[2][1]]))
                    result.append(parseDistribution(['or', logic[1][2], logic[2][2]]))
                else:
                    #Keep the second as it is
                    result.append(parseDistribution(['or', logic[1], logic[2][1]]))
                    result.append(parseDistribution(['or', logic[1], logic[2][2]]))
            else:
                #Keep the second as it is
                result.append(parseDistribution(['or', logic[1], logic[2][1]]))
                result.append(parseDistribution(['or', logic[1], logic[2][2]]))


    return result
lexer = lex.lex()
parser = yacc.yacc()
#(~((~(a(x)|b(y)))|(~c(z))))
'''
res = parser.parse("((a(z)&b(z))|(d(z)&c(z)))")
print(res)
print("*"*20)
res=MoveNotInwards(['or', ['or', 'a', 'b'], ['and', 'd', 'c']])
print(res)
res=parseDistribution(['or', ['and', 'a', 'b'], ['and', 'd', 'c']])
print(res)
'''
res = parser.parse("(((bob(z)&bill(z))|n(m))|(dull(z)&cat(z)))")
print(res)
res=MoveNotInwards(res)
print(res)
res=parseDistribution(res)
print(res)
