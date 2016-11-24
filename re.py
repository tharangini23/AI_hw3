import re
#returns list where first element is predicate name and second list of arguments
PredicateTable={}
def ReturnPredicateNameAndArgList1(Input):
    #                 12  2         1   34        4        3
    PredicatePattern='((~?)[a-zA-Z]+)\((([a-zA-Z]+,)*[a-zA-Z])\)'
    m=re.match(PredicatePattern,Input)
    Negetive=0
    if(m):
        if(m.group(2)):
            Negetive=1
        l=[m.group(),m.group(1),list(m.group(3).split(','))]#full match,predicate name,arguments
        if(m.group(1) not in PredicateTable.keys() ):
            PredicateTable[m.group(1)]=[[],[],[],[]]#True,Not True,Premise,Conclusion
        if(Negetive):
            PredicateTable[m.group(1)][1].append(list(m.group(3).split(',')))
        else:
            PredicateTable[m.group(1)][0].append(list(m.group(3).split(',')))
    else:
        l=[]
    print(PredicateTable)
    return l
'''
def Tell():
    pass
def Ask():
    pass

#check if sentence is a implication
def Implication(Input):
    ImplicationPattern='(.+)=>(.+)'
    m=re.match(ImplicationPattern,Input)
    if(m):
        print(m.group())
        #premise
            m.group(1)
        #conclusion
        m.group(2)
        return True
    else:return False
#p=>q ----~p|q
def Convert():
    ImplicationPattern='(.+)=>(.+)'
    m=re.match(ImplicationPattern,Input)
    Simplify(m.group(1))+"|"+Simplify(m.group(2))



def Simplify(Input):
    operators1='[~|&]'
    operators2='=>'
    if(re.match(operators2,Input)):
        Convert(Input):

    else :
        return Input
def CNF(Input):
    #move not
    pattern='~(.+)'
    m=re.match(pattern,Input)
    if(m):
        #
        m1=m.group(1)#input without ~
        pattern1='.+\(.+\)[&|]'
        m2=re.sub(pattern1,'~'+pattern1m1)


'''




def ReturnPredicateName(Input):
    #                 1         1
    PredicatePattern='([a-zA-Z]+)\('
    m=re.match(PredicatePattern,Input)
    l=[]
    if(m):
       return m.group(1)
    else:return ""
def ReturnArgList(Input):
    #                 1         1  2 3        3          2
    PredicatePattern='([a-zA-Z]+)\((([a-zA-Z]+,)*[a-zA-Z]*)\)'
    m=re.match(PredicatePattern,Input)
    l=[]
    if(m):
        return list(m.group(2).split(','))
    else :return []
Subject=['Ajk(jjkj)','Bing(abkjkj,bkjk)','C(l,)','A(z)']
for i in Subject:
    print(ReturnPredicateName(i))
    print(ReturnArgList(i))
Subject2=['A(x)=>Bing(a,b)','C(l,)']
