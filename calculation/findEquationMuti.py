import os
def find(equation,value,valueFind,valueMainFind,checkLoopInfinit,result):
	#print( "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ",result)
	#print(type(valueFind),valueMainFind,value)
	if(checkLoopInfinit==0):
		return False
	checkLoopInfinit-=1

	#print("หา ",valueFind ," check : ",checkLoopInfinit)
	#print(equation)

	equationState=setEquationState(equation[:])
	for i in range(len(equation)):
		if(valueFind in equation[i]):
			equationState[i][1]=True
	for i in value:
		for j in range(len(equation)):
			if(equationState[j][1] and i in equation[j]):
				equationState[j][0]-=1
	#p(equation,equationState)

	for missing in range(1,5):

		for NumEquation in range(len(equation)):
		

			#print(missing ,"::",NumEquation,"::",checkLoopInfinit,"::",valueFind)
			if(equationState[NumEquation][1] and equationState[NumEquation][0]==missing):

				#p(equation,equationState)
				#print("ใช้สมการ ",equation[NumEquation])
				if(missing==1):
					#print("หาได้")
					result+=[equation[NumEquation]]
					return True
				else:
					status=1
					s=set([])
					s.add(valueFind)
					setValueFindNext=set(equation[NumEquation])
					setValueFindNext-=set(value)
					setValueFindNext-=s
					#print("",setValueFindNext)
					if(not(valueMainFind in setValueFindNext)):
						#print(setValueFindNext)
						for findValue in setValueFindNext:
							if(not find(equation[:],value,findValue,valueMainFind,checkLoopInfinit,result)):#return false
								status=0
								break
								
						if(status==1):
							result+=[equation[NumEquation]]
							#print("หาได้ eiei" ,valueFind)
							return True
	#p(equation,equationState)
	#print("หาไม่ได้")
	result=[]

	#deleteResultError(result,checkLoopInfinit)
	return False
				
def deleteResultError(result,checkLoopInfinit):
	##("delet!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	for i in range(len(result)):
		if(len(result)!=1   and result[i][0]<=checkLoopInfinit):
			del result[i]
		if(len(result)==1 and result[0]<=checkLoopInfinit):
			result=[]
def IOEquation():
	f=open(os.getcwd()+"/data/formula/variable")
	return f.read().split()

def setEquationState(equationState):
	for i in range(len(equationState)):
		equationState[i]=[len(equationState[i])]+[False]
	return equationState

def p(equation,equationState):
	for i in range(len(equationState)):
		print(equation[i],equationState[i] ,end=' | ')
	print("")
def splitValueIO(equation):
	for i in range(len(equation)):
		equation[i]=equation[i].split('/')
	equation=[ list(set(eq)) for eq in equation.copy() ]
	return equation


def getResult(value,valuefind):
	equation=IOEquation()
	equation=splitValueIO(equation)
	result=[]

	if(find(equation,value,valuefind[:],valuefind[:],4,result)):
		return result
	else:
		return []
def getIndex(value,valuefind):
        equation=IOEquation()
        equation=splitValueIO(equation)
        result=[]
        for i in getResult(value,valuefind):
                
                result+=[equation.index(i)]
        return result
def getEuationIndex(index):
        equation=IOEquation()
        equation=splitValueIO(equation)
      
        return equation[index]
