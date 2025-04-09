import time
from random import shuffle
def  gauss(equ,result):
    def New(things = equ, result = result):
        Lis = []
        for elmt in things:
            Lis2 = []
            for x in elmt:
                Lis2.append(x)
            Lis2.append(result[things.index(elmt)])
            Lis.append(Lis2)
             
        return Lis
    depart = New(equ,result)
    ii = 0
    Ind = len(depart)
    for i in range(len(equ)-1):
        ref = []
        for elmt in depart:
            eq = []
            for elmt2 in elmt:
                eq.append(elmt2)
            ref.append(eq)
            verif = True
        for elmt in range(Ind-1):
            if ref[elmt+ii][ii] == 0:
                resu = New(equ,result)
                shuffle(resu)
                EQU =[resu[x][:-1] for x in range(len(resu))]
                Res = [resu[x][-1] for x in range(len(resu))]
                verif = False 
                return gauss(EQU,Res)
            else:
                verif = True
                coef = ref[elmt+1+ii][ii]/ref[elmt+ii][ii]
                Mult = []
                for elmt1 in ref[elmt+ii]:
                    Mult.append(elmt1*coef)  
                    
                for iii,elmt2 in zip(range(len(depart[elmt+1+ii])),Mult):
                    depart[elmt+1+ii][iii] -= elmt2 
        if not verif :
            break
        ii+=1
        Ind -= 1
    #print(depart) 
        #print()
    return Resolve(depart)
        
        

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

def MAIN(equation,result):
    tim1 = time.time()
    rep = gauss(equation,result)
    tim2 = time.time()
    return rep,tim2 -tim1


"""equation = [[1,2,5],[3,2,-1],[0,5,3]]
result = [1,1/2,1]
#equation = [[2,6,2,8],[1,4,2,2],[1,1,2,4],[1,1,1,1]]
#result = [16,5,9,2]
tim1 = time.time()
rep = gauss(equation,result)
tim2 = time.time()

print(f"La solution est : {rep} et la durée est {(tim2 - tim1)*1000} milliseconde")"""
            
    
        