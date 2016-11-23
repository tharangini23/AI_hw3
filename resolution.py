import re
############################################################################################
def is_variable(Input_Var):
    if(isinstance(Input_Var,list)):
        return False
    else:
        return  Input_Var.islower()
############################################################################################
def unify(x,y,theta):
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
        if(j==term):
            clause.remove(i)
    return clause
############################################################################################
def IsNegation(i,j):
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
    #                 1         1  2 3        3          2
    PredicatePattern='([a-zA-Z]+)\((([a-zA-Z]+,)*[a-zA-Z])\)'
    m=re.match(PredicatePattern,Input)
    l=[]
    if(m):
       return m.group(1)
    else:return ""
############################################################################################
def ReturnArgList(Input):
    if(type(Input) is list):
        Input=Input[1]
    #                 1         1  2 3        3          2
    PredicatePattern='([a-zA-Z]+)\((([a-zA-Z]+,)*[a-zA-Z])\)'
    m=re.match(PredicatePattern,Input)
    l=[]
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
    print("modified",modified)
    return modified
############################################################################################

def pl_resolution(kb, query):
    "Propositional-logic resolution: say if alpha follows from KB. [Figure 7.12]"
    kb.append(query)#not of query
    new = set()
    while True:
        resolve_pair=[]
        for i in range(0,len(kb)):
            for j in range(i+1,len(kb)):
                resolve_pair.append([kb[i],kb[j]])

        for i in resolve_pair:
            resolvents = pl_resolve(i[0], i[1])
            if False in resolvents:#none
                return True
        for c in resolvents:
            if c not in kb:
                kb.append(c)
############################################################################################
#c1=['or',a,b,c]
#c2=['or',['not',a],b,c]
def pl_resolve(c1, c2):
    """Return all clauses that can be obtained by resolving clauses ci and cj."""
    #comment
'''
    clauses = []
    for di in disjuncts(ci):
        for dj in disjuncts(cj):
            if di == ~dj or ~di == dj:
                dnew = unique(removeall(di, disjuncts(ci)) +
                              removeall(dj, disjuncts(cj)))
                clauses.append(associate('|', dnew))
    return clauses
'''
    #end comment
    clauses=['or']
    for i in c1[1:]:
        for j in c2[1:]:
            if((predicate(i)==predicate(j) and IsNegation(i,j)):#predicates match
                theta=unify(args(i),args(j))
                substitute(c1,theta)
                substitute(c2,theta)
                r1=removeMatch(clause,i)
                r2=removeMatch(clause,i)
                for k in r2:
                    if(k not in r1):
                        r1.append(k)
                clauses.append(r1)
    return clauses

############################################################################################
kb=[['or',a(x),b(x)],['not',a('John')]]
############################################################################################
substitute(['or','a(x)',['not','b(x)'],'k(x,y)'],{'x':'John'})
pl_resolution(kb, query)

