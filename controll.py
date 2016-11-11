from controller import ControllWord
from calculation.controller import controllCalculation
import re,pprint,os,json,string,math
pp = pprint.PrettyPrinter(indent=10)

class Controll(ControllWord):
	"""docstring for Controll"""
	def __init__(self):
		super(Controll, self).__init__()
	def mapsVariable(self,variable):
	
		maps={"velsta":"u"}
		maps.update({"velfin":"v"})
		maps.update({"acc":"a"})
		maps.update({"dis":"s"})
		maps.update({"velavg":"vav"})
		maps.update({"tim":"t"})
		maps.update({"for":"F"})
		maps.update({"mas":"m"})
		maps.update({"vel":"v"})
		
		maped=list()
		if type(variable)==list:
			for value in variable:
				if value in maps:
					maped.append(maps[value])
				else:
					maped.append(value)
			
		elif type(variable)==str:
			if variable in maps:
				maped.append(maps[variable])
			else:
				maped.append(variable)
		return maped

	def isVariableCore(self,value,core):
		for cor in core:
			if cor in value:
				return True
		return False
	def variableOfCore(self,variable,cost,des):
		
		return [[variableY,costY],[variableX.costX]]
	def matchThe(self,variable,cost,unit,muticore):
		
		return [variable,cost,unit,des]
	def calulate(self):
		calculate=controllCalculation()
		[variable,cost,unit,des,find,title]=self.variable()
		pp.pprint([variable,cost,unit,des,find,title])
		mutiCore=['vel','acc','for']
		noDir=['tim']
		indexDir=list()
		
		for index in range(len(variable)):
			if 'the' in variable[index]:
				matchIndex=[index-1,index+1]
				for match in matchIndex:
					isMatch=False
					for value in mutiCore:
						try:
							variable[match]
						except Exception as e:
							pass
						else:
							if value in variable[match]:
								indexDir.append([index,match])
								isMatch=True
								break 
					if isMatch:break
		print(indexDir)
		for indexMatch in indexDir:
			the=indexMatch[0]
			value=indexMatch[1]
			cos=[cost[value],cost[the]]
			calculate.update()

			calculate.set(['value','the'],cos,'value|x')
			cost[the]=calculate.calculate()[-1]

			calculate.set(['value','the'],cos,'value|y')
			cost[value]=calculate.calculate()[-1]
			des[the]='dirx'
			des[value]='diry'
			if len(variable[value])==3:variable[value]+='sta'
			variable[the]=variable[value]
			unit[the]=unit[value]
		print("-*-*-*-*-*-*-*-*-*-")
		pp.pprint([variable,cost,unit,des,find,title])

		# if 'dirx' in des and 'diry' in des:
		if True:
			

			variableX=list()
			costX=list()
			variableY=list()
			costY=list()
			for indexDes in range(len(des)) :
				if des[indexDes]=='dirx' or des[indexDes]=='':
					variableX.append(variable[indexDes])
					costX.append(cost[indexDes])
				if des[indexDes]=='diry' or des[indexDes]=='':
					variableY.append(variable[indexDes])
					costY.append(cost[indexDes])
		
			for i in range(len(variableX)):
				if 'vel' in variableX[i] and not('acc' in variableX):
					variableX.append('velavg')
					costX.append(costX[i])
					break
			hasAcc=False
			for i in range(len(variableY)):
				if 'acc' in variableY:
					hasAcc=True
			if not(hasAcc):
				variableY.append('acc')
				costY.append(9.8)
			variableX=self.mapsVariable(variableX)
			variableY=self.mapsVariable(variableY)
			fdes=['']
			print('mappppppppppppppppppp')
			print(variableY)
			print(variableX)
			print(find)
			find = find[0] if type(find)==list else find
			print(find)
		if True:
			if self.isVariableCore(find,mutiCore) :
				# pass
				print("muticoreeeeeeeeeeeeeeeeeeeee")
				find=self.mapsVariable(find)[0]
				calculate.set(variableX,costX,find)
				findx=calculate.calculate()
				calculate.set(variableY,costY,find)
				findy=calculate.calculate()
				if '|x' in fdes:
					print(findx[-1])
					return findx
				elif '|y' in fdes:
					# print(findy)
					return findy
				else :
					if findy!=[] and findx!=[]:
						calculate.set(['value|x','value|y'],[findx,findy],'value')
						answer=calculate.calculate()[-1]
						print(answer)
					else :
						print("ERRORRRRRRRRRRRRRRRRRRRRRRRRRR")
			else:
				find=self.mapsVariable(find)[0]
				print("testtttttttt")
				print(find)
				calculate.set(variableX,costX,find)
				tryFindByX=calculate.calculate()
				calculate.set(variableY,costY,find)
				tryFindByY=calculate.calculate()
				answer=[i[-1] for i in [tryFindByX,tryFindByY] if i!=[]]
				print("answerrrrrrrrrrrrrrrrrrrrrrr")
				print(answer)
				if len(answer)==1:
					print(answer)
					return answer[0]

				elif len(answer)==2:
					if answer[0]==answer[1]:
						print(answer)
						return answer[0]
					else:
						print("ERRORwithNOTequation")
				else:
					print("canFind")
	def returnVariable(self):
		calculate=controllCalculation()
		[variable,cost,unit,des,find,title]=self.variable()
		pp.pprint([variable,cost,unit,des,find,title])
		mutiCore=['vel','acc','for']
		noDir=['tim']
		indexDir=list()
		
		for index in range(len(variable)):
			if 'the' in variable[index]:
				matchIndex=[index-1,index+1]
				for match in matchIndex:
					isMatch=False
					for value in mutiCore:
						try:
							variable[match]
						except Exception as e:
							pass
						else:
							if value in variable[match]:
								indexDir.append([index,match])
								isMatch=True
								break 
					if isMatch:break
		print(indexDir)
		for indexMatch in indexDir:
			the=indexMatch[0]
			value=indexMatch[1]
			cos=[cost[value],cost[the]]
			calculate.update()

			calculate.set(['value','the'],cos,'value|x')
			cost[the]=calculate.calculate()[-1]

			calculate.set(['value','the'],cos,'value|y')
			cost[value]=calculate.calculate()[-1]
			des[the]='dirx'
			des[value]='diry'
			if len(variable[value])==3:variable[value]+='sta'
			variable[the]=variable[value]
			unit[the]=unit[value]
		print("-*-*-*-*-*-*-*-*-*-")
		pp.pprint([variable,cost,unit,des,find,title])

		# if 'dirx' in des and 'diry' in des:
		if True:
			

			variableX=list()
			costX=list()
			variableY=list()
			costY=list()
			for indexDes in range(len(des)) :
				if des[indexDes]=='dirx' or des[indexDes]=='':
					variableX.append(variable[indexDes])
					costX.append(cost[indexDes])
				if des[indexDes]=='diry' or des[indexDes]=='':
					variableY.append(variable[indexDes])
					costY.append(cost[indexDes])
		
			for i in range(len(variableX)):
				if 'vel' in variableX[i] and not('acc' in variableX):
					variableX.append('velavg')
					costX.append(costX[i])
					break
			hasAcc=False
			for i in range(len(variableY)):
				if 'acc' in variableY:
					hasAcc=True
			if not(hasAcc):
				variableY.append('acc')
				costY.append(9.8)
			variableX=self.mapsVariable(variableX)
			variableY=self.mapsVariable(variableY)
			fdes=['']
			
		val =list()
		for i in variableY:
			if self.isVariableCore(i,['u','v','a','F']):
				val.append(i+"x")
			else:
				val.append(i)
		for i in variableX:
			if self.isVariableCore(i,['u','v','a','F']):
				val.append(i+"x")
			else:
				val.append(i)

		val=[i for i in val if not(i in val)]
		return val

