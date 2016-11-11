import calculation.findEquationMuti as findE
import calculation.calculation as changE
import calculation.selectCalValue as cal
import string,re,os
class controllCalculation():
        """docstring for controllCalculation"""
        def __init__(self):
                super(controllCalculation, self).__init__()
                
        def set(self,value,cost,find):
                self.value=value
                self.find=find
                self.cost=cost
        def test(self):
                self.value=['v']
                self.find='v'
                self.cost=[2,90]
        def loade(self):
                fileLocaltion=os.getcwd()+"/data/formula/equation"
                data=open(fileLocaltion,"r")
                txtData=data.read()
                data.close()
                self.equation=txtData.split('\n')
         


        def update(self):
                self.loade()
                equation=self.equation
                for index in range(len(equation)):
                        equation[index]='/'.join([i for i in equation[index].split()if (not(i in string.punctuation) and not( re.match('[0-9]+|sin|cos',i) ))])
                equation='\n'.join(equation)
                fileLocaltion=os.getcwd()+"/data/formula/variable"
                data=open(fileLocaltion,"w")
                data.write(equation)
                data.close()

        def calculate(self):
                # value=list:str 
                # cost= list:float
                # valueFind = str
                value=self.value
                cost=self.cost
                valueFind=self.find
                show="problem give variable : "+" ".join(value)

                select=[]
                print("data")
                print(value)
                print(cost)
                print(valueFind)
                listE=findE.getIndex(value,valueFind)
                print(listE)
                miss=[]
                if len(listE)==0:return []
                for i in range(len(listE)):
                                
                        miss=list(set(findE.getEuationIndex(listE[i]))-set(value))
                        selec="Use equation "+''.join(changE.getEquationOrigin(listE[i]))+" for find "+miss[0]+" value\n"
                        Echange=changE.getEquationChange(listE[i],miss)
                        selec+="Formatting equation : " +''.join(Echange)+" for calculation \n"
                        cost+=[cal.select(Echange,value,cost)]
                        value+=miss
                        selec+="\n้have "+miss[0]+" = "+str(cost[-1])+"\n\n"
                        select+=[selec]
                        
                textshow=show+"\n\n" + '\n'.join(select)
                print(textshow)  

                return cost

a=controllCalculation()
a.update()
a.test()
print(a.calculate())
