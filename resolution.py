import re
############################################################################################
def is_variable(Input_Var):
    if(isinstance(Input_Var,list)):
        return False
    else:
        return  Input_Var.islower()
############################################################################################
def unify(x,y,theta):
    #print("unify",x,y,theta)
    if(x==y):
        return theta
    elif(is_variable(x)):
        return unify_var(x,y,theta)
    elif(is_variable(y)):
        return unify_var(y,x,theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:],y[1:],unify(x[0],y[0],theta))
    else:
        return None
############################################################################################
def unify_var(var,x,theta):
    if var in theta.keys():
        return unify(theta[var],x,theta)
    elif x in theta.keys():
        return unify(theta[var],x,theta)
    #elif occur_check(var,x):
    #    return none
    else:
        theta[var]=x
    return theta
############################################################################################
#theta={x:'John',y:'pam'}
#c1=['or',a(hj),b(fdf),c(fffd)]

def removeMatch(clause,term):
    if(type(term) is list):
        term=term[1]
    for i in clause:
        j=i
        if(type(i) is list):
            j=i[1]
        if(ReturnPredicateName(j)==ReturnPredicateName(term)):
            clause.remove(i)
    return clause
############################################################################################
def IsNegation(i,j):
    #print("negetion",i,j)
    if((type(i) is list) and (type(j) is list)):
        return False
    elif(type(i) is list):
        return True
    elif(type(j) is list):
        return True
    else :return False
############################################################################################
def ReturnPredicateName(Input):
    if(type(Input) is list):
        Input=Input[1]

    #                 1         1
    PredicatePattern='([a-zA-Z]+)\('
    m=re.match(PredicatePattern,Input)
    l=[]
    #print(Input,"innnn",m)
    if(m):
       return m.group(1)
    else:return ""
############################################################################################
def ReturnArgList(Input):

    if(type(Input) is list):
        Input=Input[1]
    #                 1         1  2 3        3          2
    PredicatePattern='([a-zA-Z]+)\((([a-zA-Z]+,)*[a-zA-Z]*)\)'
    m=re.match(PredicatePattern,Input)
    l=[]
    #print("arglist",Input,m)
    if(m):
        return list(m.group(2).split(','))
    else :return []
#print(removeMatch(['or',['not','a'],'b','c'],'a'))
############################################################################################
def substitute(c1,theta):
    modified=[]
    n=0
    for i in range(1,len(c1)):
        if(type(c1[i]) is list ):
            n=1
        predicate_name=ReturnPredicateName(c1[i])
        Arg_list=ReturnArgList(c1[i])
        for j in range(0,len(Arg_list)):
            if(Arg_list[j] in theta.keys()):
                Arg_list[j]=theta[Arg_list[j]]#substitue
        if(n):
            modified.append(['not',predicate_name+"("+','.join(Arg_list)+")"])
        else:
            modified.append(predicate_name+"("+','.join(Arg_list)+")")
        n=0
    if(len(modified)>1):
        modified.insert(0,'or')
        #print("modified",modified,c1)
    return modified
############################################################################################

def pl_resolution(kb):
    "Propositional-logic resolution: say if alpha follows from KB. [Figure 7.12]"
    #kb.append(query)#not of query
    new = set()
    print(kb)
    a=3
    while a:
        resolve_pair=[]
        for i in range(0,len(kb)):
            for j in range(i+1,len(kb)):
                resolve_pair.append([kb[i],kb[j]])
        resolvents=[]
        for i in resolve_pair:
            resolvents.append(pl_resolve(i[0], i[1]))
            print("pairs",i)
            print("resolvents",resolvents)
            if False in resolvents:#none
                return True
        for c in resolvents:
            if c not in kb:
                kb.append(c)
        a-=1
        print("kb",kb)
############################################################################################
#c1=['or',a,b,c]
#c2=['or',['not',a],b,c]
def pl_resolve(c1, c2):
    """Return all clauses that can be obtained by resolving clauses ci and cj."""
    clauses=[]
    #print("clauses",c1,c2)
    m=1
    n=1
    if(len(c1)==2):
        c1=[c1]
        m=0
    if(len(c2)==2):
        c2=[c2]
        n=0
    print("clauses",c1,c2)
    for i in c1[m:]:
        for j in c2[n:]:
            #print(i,j)
            #print(i,j,ReturnPredicateName(i),ReturnPredicateName(j),IsNegation(i,j))
            if((ReturnPredicateName(j)==ReturnPredicateName(i)) and IsNegation(i,j)):#predicates match
                theta=unify(ReturnArgList(i),ReturnArgList(j),{})
                c1=substitute(c1,theta)
                c2=substitute(c2,theta)
                r1=removeMatch(c1,i)
                r2=removeMatch(c2,i)
                if(len(r2)==0 and len(r1)==0):
                    print("&"*60)
                r3=['or']
                for k in r2[1:]:
                    if(k not in r3):
                        r3.append(k)
                if(len(r3)>1):
                    r3.insert(0,'or')
                clauses.append(r3)
    print(clauses)
    return clauses

############################################################################################
kb=[['or','a(x)','b(x)',],['not','a(John)'],['not','b(z)']]
############################################################################################
#substitute(['or','a(x)',['not','b(x)'],'k(x,y)'],{'x':'John'})
pl_resolution(kb)

