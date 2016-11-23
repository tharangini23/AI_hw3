import re
#kb-[['or',a,b,c],...]
'''
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
            if False in resolvents:
                return True
            new = new.union(set(resolvents))
        if new.issubset(set(clauses)):
            return False
        for c in new:
            if c not in clauses:
                clauses.append(c)

#c1=['or',a,b,c]
#c2=['or',['not',a],b,c]
def pl_resolve(c1, c2):
    """Return all clauses that can be obtained by resolving clauses ci and cj."""
    #comment

    clauses = []
    for di in disjuncts(ci):
        for dj in disjuncts(cj):
            if di == ~dj or ~di == dj:
                dnew = unique(removeall(di, disjuncts(ci)) +
                              removeall(dj, disjuncts(cj)))
                clauses.append(associate('|', dnew))
    return clauses

    #end comment
    clauses=['or']
    for i in c1[1:]:
        for j in c2[1:]:
            if((predicate(i)==predicate(j) and IsNegation(i,j)):#predicates match
                unify(args(i),args(j))
                r1=removeMatch(clause,i)
                r2=removeMatch(clause,i)
                for k in r2:
                    if(k not in r1):
                        r1.append(k)
                clauses.append(r1)
    return clauses
'''
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
def IsNegation(i,j):
    if((type(i) is list) and (type(j) is list)):
        return False
    elif(type(i) is list):
        return True
    elif(type(j) is list):
        return True
    else :return False

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
def substitute(c1,c2,theta):
    modified=""
    for i in range(1,len(c1)):
        print(c1[i])
        predicate_name=ReturnPredicateName(c1[i])
        Arg_list=ReturnArgList(c1[i])
        for j in range(0,len(Arg_list)):
            if(Arg_list[j] in theta.keys()):
                Arg_list[j]=theta[Arg_list[j]]#substitue
        modified=predicate_name+"("+','.join(Arg_list)+")"
        print("modified",modified)

substitute(['or','a(x)','b(x)','k(x,y)'],['not','a(John)'],{'x':'John'})

