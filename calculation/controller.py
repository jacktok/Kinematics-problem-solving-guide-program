import findEquationMuti as findE
import calculation as changE
import selectCalValue as cal
def getInput(problem):
        def printE(E):
                s=""
                for i in E:
                        s+=i
                return s

        problem=problem.split("\n")
        value=[]
        cost=[]
        show="problem give variable : "
               
        #print(problem)
        for i in range(len(problem)):
                problem[i]=problem[i].split("=")
                
                if(problem[i][1]=="?"):
                        valueFind=problem[i][0]
                else:
                        value+=[problem[i][0]]
                        cost+=[float(problem[i][1])]
        for i in value:
                show+=i+"  "
        select=[]
        #print(value)
        listE=findE.getIndex(value,valueFind)
        #print(listE)
        miss=[]
        for i in range(len(listE)):
                        
                miss=list(set(findE.getEuationIndex(listE[i]))-set(value))
                #print("use equation ",printE(changE.getEquationOrigin(listE[i]))," for find ",miss[0]," \n")
                selec="Use equation "+printE(changE.getEquationOrigin(listE[i]))+" for find "+miss[0]+" value\n"
                #print(miss,listE[i],type(miss))
                Echange=changE.getEquationChange(listE[i],miss)
                #print(Echange,value,cost)
                #print("chaged Equation is " ,printE(Echange))
                selec+="Formatting equation : " +printE(Echange)+" for calculation"
                cost+=[cal.select(Echange,value,cost)]
                #print(Echange)
                value+=miss
                selec+="\n้have "+miss[0]+" = "+str(cost[-1])+"\n\n"
                #print(value,cost)
                select+=[selec]
                        
        textshow=show+"\n\n"
        for i in select:
                textshow+=i
        return textshow
       
def getChangE(problem):
        def printE(E):
                s=""
                for i in E:
                        s+=i
                return s

        problem=problem.split("\n")
        value=[]
        cost=[]
        show="problem give variable : "
               
        #print(problem)
        for i in range(len(problem)):
                problem[i]=problem[i].split("=")
                
                if(problem[i][1]=="?"):
                        valueFind=problem[i][0]
                else:
                        value+=[problem[i][0]]
                        cost+=[float(problem[i][1])]
        for i in value:
                show+=i+"  "
        select=[]
        #print(value)
        listE=findE.getIndex(value,valueFind)
        #print(listE)
        miss=[]
        for i in range(len(listE)):
                        
                miss=list(set(findE.getEuationIndex(listE[i]))-set(value))
                #print("use equation ",printE(changE.getEquationOrigin(listE[i]))," for find ",miss[0]," \n")
                selec="Use equation "+printE(changE.getEquationOrigin(listE[i]))+" for find "+miss[0]+" value\n"
                #print(miss,listE[i],type(miss))
                Echange=changE.getEquationChange(listE[i],miss)
                #print(Echange,value,cost)
                #print("chaged Equation is " ,printE(Echange))
                selec+="Formatting equation : " +printE(Echange)+" for calculation \n"
                cost+=[cal.select(Echange,value,cost)]
                #print(Echange)
                value+=miss
                #selec+="\n้have "+miss[0]+" = "+str(cost[-1])+"\n\n"
                #print(value,cost)
                select+=[selec]
                        
        textshow=show+"\n\n"
        for i in select:
                textshow+=i+"\n"
                
        return textshow
def getE(problem):
        def printE(E):
                s=""
                for i in E:
                        s+=i
                return s

        problem=problem.split("\n")
        value=[]
        cost=[]
        show="problem give variable : "
               
        #print(problem)
        for i in range(len(problem)):
                problem[i]=problem[i].split("=")
                        
                if(problem[i][1]=="?"):
                        valueFind=problem[i][0]
                else:
                        value+=[problem[i][0]]
                        cost+=[float(problem[i][1])]
        for i in value:
                show+=i+"  "
        select=[]
        #print(value)
        listE=findE.getIndex(value,valueFind)
        #print(listE)
        miss=[]
        for i in range(len(listE)):
                        
                miss=list(set(findE.getEuationIndex(listE[i]))-set(value))
                #print("use equation ",printE(changE.getEquationOrigin(listE[i]))," for find ",miss[0]," \n")
                selec="Use equation "+printE(changE.getEquationOrigin(listE[i]))+" for find "+miss[0]+" value\n"
                #print(miss,listE[i],type(miss))
                Echange=changE.getEquationChange(listE[i],miss)
                #print(Echange,value,cost)
                #print("chaged Equation is " ,printE(Echange))
                #selec+="Formatting equation : " +printE(Echange)+" for calculation \n"
                cost+=[cal.select(Echange,value,cost)]
                #print(Echange)
                value+=miss
                #selec+="\n้have "+miss[0]+" = "+str(cost[-1])+"\n\n"
                #print(value,cost)
                select+=[selec]
                
        textshow=show+"\n\n"
        for i in select:
                textshow+=i+"\n"                
        return textshow
        
