import re
def CNF(Input):
    #move not
    pattern='~(.+)'
    m=re.match(pattern,Input)
    if(m):
        #
        m1=m.group(1)#input without ~
        print(m1)
        pattern1='\(.+\(.+\)[&|]\)'
        pattern11='[a-z]+\([a-z]+\)'
        #m2=re.sub(pattern11,m1)
        #print(m2)
#CNF('~(a(x)|b(y))')
def RemoveImplication(Input):
    ImplicationPattern='((.+)=>(.+))+'
    ImplicationPattern='.+((.+)=>(.+))*=>(.+)'
    m=re.match(ImplicationPattern,Input)
    if(m):
        #print(m.group())
        #premise
        #    m.group(1)
        #conclusion
        print(m.group())
        print(m.group(1))
RemoveImplication("P&E=>E=>o=>Q")
