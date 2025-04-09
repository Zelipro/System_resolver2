import time
X = "X"
def Return_L_U(Equ,B):
    L,U = [],[]
    for i in range(len(Equ)):
       L.append([X]*i + [1] + [0]*(len(Equ[0])-i-1))
       U.append([0]*i + [X]*(len(Equ[0])-i))
    U[0] = Equ[0]
    UU = []
    for i in range(len(U)):
        u = []
        for elmt in U:
            u.append(elmt[i]) 
        UU.append(u)
    
    refair = True
    while refair :
        refair = False
        for i in range(len(L)):
            for j in range(len(UU)):
                som = 0
                garde = ()
                for elmt1 in range(len(L[i])):
                    if L[i][elmt1] == X and UU[j][elmt1] != X:
                        if UU[j][elmt1] == 0:
                            som += 0
                        else:
                              garde = (L,i,elmt1,j,UU)
                    elif L[i][elmt1] != X and UU[j][elmt1] == X:
                        if L[i][elmt1] == 0:
                            som += 0
                        else:
                             garde = (UU,j,elmt1,i,L)
                    elif L[i][elmt1] == X and UU[j][elmt1] == X:
                        refair = True
                        break
                    else:
                        som += L[i][elmt1]*UU[j][elmt1]
                if len(garde) > 0:
                    garde[0][garde[1]][garde[2]] = (Equ[i][j] - som)/garde[4][garde[3]][garde[2]]
    
    UUU = []
    for i in range(len(UU)):
        List = []
        for elmt in UU:
                List.append(elmt[i])
        UUU.append(List)
            
    return LU(L,UUU,B)
    

def Resolve(List):
    if Triangulation_Sup(List):
        List = List[::-1]
        Rep = ["X"]*len(List)
        for elmt in List:
            elmt2 = elmt[:-1]
            som = 0
            garde = ()
            for i in range(len(Rep)):
                    if Rep[i] == "X" and elmt2[i] != 0:
                        garde = (i,i)
                    elif Rep[i] == "X" and elmt2[i] == 0:
                        som += 0
                    else:
                        som += Rep[i]*elmt2[i]
            if len(garde) >0:
                Rep[garde[0]] = (elmt[-1] - som) / elmt2[garde[1]]
        return Rep
    elif Triangulation_Sup(List[::-1]):
        Rep = ["X"]*len(List)
        for elmt in List:
            elmt2 = elmt[:-1]
            som = 0
            garde = ()
            for i in range(len(Rep)):
                    if Rep[i] == "X" and elmt2[i] != 0:
                        garde = (i,i)
                    elif Rep[i] == "X" and elmt2[i] == 0:
                        som += 0
                    else:
                        som += Rep[i]*elmt2[i]
            if len(garde) >0:
                Rep[garde[0]] = (elmt[-1] - som) / elmt2[garde[1]]
        return Rep
    else:
        return "Le systeme n'est pas triangulé"
        

def Triangulation_Sup(List):
    nbr_zero = 0
    for elmt in List:
        if elmt.count(0) < nbr_zero:
            return False
        else:
            nbr_zero += 1
    return True      
def LU(L,U,B):
    for elmt1,elmt2 in zip(L,B):
        elmt1.append(elmt2)
    
    rep = Resolve(L)
    
    for elmt1,emlt2 in zip(U,rep):
        elmt1.append(emlt2)

    return Resolve(U)

def Produit(L,U):
    UU = []
    for i in range(len(U)):
        u = []
        for elmt in U:
            u.append(elmt[i]) 
        UU.append(u)   
    ret = []
    for x in range(len(L)):
        List = []
        for y in range(len(UU)):
            List2 = []
            for i in range(len(L[x])):
               if isinstance(L[x][i],str) or isinstance(UU[y][i],str):
                   if 0 not in [L[x][i],UU[y][i]]:
                       List2.append(f"{L[x][i]}*{UU[y][i]}")
                   else:
                       List2.append(0)
               else:
                  List2.append(L[x][i]*UU[y][i])
            som = 0
            char_som = ""
            for elt in List2:
                if isinstance(elt,int) or isinstance(elt,float):
                    som += elt 
                else:
                    char_som += elt if char_som == "" else  "+"+elt 
            if char_som == "":      
                 List.append(som)
            elif som == 0:
                 List.append(char_som)
            else:
                List.append(f"{char_som}+{som}")
        ret.append(List)
    return ret 

def MAIN(Equ,B):
    tim1 = time.time()
    rep = Return_L_U(Equ,B)
    tim2 = time.time()
    return rep, tim2-tim1

"""#print(Produit([["CF",1,1],[0,1,0],[0,0,1]],[[2,0,0],[0,2,0],[0,0,2]]))
#Equ = [[1,2,5],[3,2,-1],[0,5,3]]
#Equ = [[2,6,2,8],[1,4,2,2],[1,1,2,4],[1,1,1,1]]
#B = [16,5,9,2]
Equ= [[1,2,5],[3,2,-1],[0,5,3]]
B = [1,1/2,1]
tim1 = time.time()
rep = Return_L_U(Equ,B)
tim2 = time.time()
print(f"La solution est : {rep} et la durée est {(tim2 - tim1)*1000} milliseconde")"""
       