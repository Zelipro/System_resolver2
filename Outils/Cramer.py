"""Ce code est ecrite par Elisee ATIKPO
"""
def det(l):
    dt=0
    s=0
    for x in l:
        s+=1
    if s==2:
       return l[0][0]*l[1][1]-l[0][1]*l[1][0]
    elif l == [[l[0][0]]]:
        return l[0][0]
    else:
       for i in range(s):
               na=[]
               n=[]
               v=0
               for t in range(s):
                   for h in range(s):
                       if t!=0 and h!=i:
                           n.append(l[t][h])
                           v+=1
                       if v==(s-1):
                            na.append(n)
                            n=[]
                            v=0
               dt+=(l[0][i]) *(-1)**(i)*det(na)
       return dt
       

import time
def Possible(equ):                                                
    return det(equ) 

def cramer(equ,result):
    Pos = Possible(equ)
    if not Pos:
       return "L'Impossible car determinant est egale a zero"
    else:
        List2 = []
        
        def New():
            departi = []
            for elmt in equ:
                departi.append(elmt)
            
            return departi
        
        depart = New()
        
        for elmt in depart:
            indice = depart.index(elmt)
            depa = [] 
            for ii in range (len(depart)):
                List = []
                for elmt in depart[ii]:
                   List.append(elmt)
                List[indice] = result[ii]
                depa.append(List)
            List2.append(det(depa)/Pos) 
            depart = New()
        return List2  

def TIME(tim1):
    H,M,S = tim1.split(" ")
    return 3600*int(H) + 60*int(M)  + int(S)

def MAIN(equation,result):
    tim1 = time.time()
    crame = cramer(equation,result)
    tim2= time.time()
    return crame,tim2-tim1
"""equation = [[1,2,5],[3,2,-1],[0,5,3]]
#equation = [[2,6,2,8],[1,4,2,2],[1,1,2,4],[1,1,1,1]]
#result = [16,5,9,2]
result = [1,1/2,1]

tim1 = time.time()
crame = cramer(equation,result)
tim2= time.time()

print(f"rep = {crame}, time = {(tim2-tim1)*1000} milliseconde")"""
    
