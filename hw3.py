#Foundations of Artificial Intelligence
#read input from file
#format
'''
<NQ = NUMBER OF QUERIES>
<QUERY 1>
...
<QUERY NQ>
<NS = NUMBER OF GIVEN SENTENCES IN THE KNOWLEDGE BASE>
<SENTENCE 1>
...
<SENTENCE NS>
'''
def ReadInputFile():
    File_Ptr=open("input.txt","r")
    Input=list(map(str.strip,File_Ptr.readlines()))
    print(Input)
    #NQ=number of queries
    NQ=int(Input[0])
    #Get each query
    for i in range(1,NQ+1):
        print(Input[i])
        #Call inference algorithm
    #number of sentences in KB
    NS=int(Input[NQ+1])
    for i in range(NQ+2,NS+1):
        print(Input[i])
        #Store in KB

ReadInputFile()

