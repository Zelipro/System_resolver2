
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

"""print("*************BIENVENUE*************\n")
k=int(input("Veuillez entrez le nombre d'élément d'une ligne qui est aussi egale à une colonne de la matrice:"))
l=[]
for i in range(k):
    la=[]
    for j in range(k):
        print("l[",i,"][",j,"]=",end="")
        t=int(input())
        la.append(t)
    l.append(la)

print(l)
    
for x in l:
    for o in x:
        print(o,end='\t')
    print()
    
print("Le determinant de la matrice est:",det(l))
print("*****************************************")    """    

"""equation = [[1,2,5],[3,2,-1],[0,5,3]]
for x in equation:
    for o in x:
        print(o,end='\t')
    print()
print(det(equation))"""