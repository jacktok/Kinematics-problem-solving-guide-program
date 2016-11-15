from wordcut.controller import ControllWord
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
			return maped[0]
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
		print("im calculateeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
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
			cost[the]=calculate.calculate('result')[-1]

			calculate.set(['value','the'],cos,'value|y')
			cost[value]=calculate.calculate('result')[-1]
			des[the]='dirx'
			des[value]='diry'
			if len(variable[value])==3:variable[value]+='sta'
			variable[the]=variable[value]
			unit[the]=unit[value]
		print("-*-*-*-*-*-*-*-*-*-")
		pp.pprint([variable,cost,unit,des,find,title])

		# if 'dirx' in des and 'diry' in des:
		variableX=list()
		costX=list()
		variableY=list()
		costY=list()
		if True:
			

			
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
				costY.append(-9.8)

			#  map variable for formula
			variableXmap=self.mapsVariable(variableX)
			variableYmap=self.mapsVariable(variableY)
			fdes=self.getlist(title)
			print("titleeeeeeeeeeeeeeeeeeeeee")
			print(title)
			fdes='' if fdes ==[] else fdes[0]
		find = find[0] if type(find)==list else find
		find=self.mapsVariable(find)
		lastStep=list()
		step=list()
		val =list()
		equation=[]
		if(fdes=='dirx'):
			calculate.set(variableXmap.copy(),costX.copy(),find)
			equation+=calculate.getFormula()
			step=[calculate.calculate('solving')+['x']]
			val +=self.mapvariableForUI(variableXmap,'x');
			cost=costX
		elif (fdes=='diry'):
			calculate.set(variableYmap.copy(),costY.copy(),find)	
			equation+=calculate.getFormula()
			step=[calculate.calculate('solving')+['y']]
			val =self.mapvariableForUI(variableYmap,'y');
			cost=costY
		else:
			print([variableX.copy(),variableY.copy(),find])
			calculate.set(variableXmap.copy(),costX.copy(),find)
			equation+=calculate.getFormula()
			equationX=equation
			stepX=[calculate.calculate('solving')+['x']]
			equation=[]
			print("sddasdzxczxczxcxc")
			pp.pprint([variableYmap,costY])
			calculate.set(variableYmap.copy(),costY.copy(),find)	
			equation+=calculate.getFormula()
			stepY=[calculate.calculate('solving')+['y']]
			equationY=equation
			if self.isVariableCore(find,['u','v','a','F','s']):
				if equationY!=[] and equationX!=[]:
					equation=equationY+equationX 
					step=stepX+stepY
					calculate.set(["value|x","value|y"],[stepX[0][-2][0],stepX[0][-2][0]],"value")
					# stepX[0][-2][0] is last cost of step
					lastStep=calculate.calculate('solving')
					lastStep[0]=[find+"x",find+"y"]
					lastStep[1]=[stepX[0][-2][0],stepY[0][-2][0]]
					lastStep[2]=[find,"+","(","(",find+"x","^","2",")","+","(",find+"y","^","2",")",")","^","0.5"]
					lastStep.append(find)
					pp.pprint(lastStep)
				else :
					equation=[]
					step=[]

				val =self.mapvariableForUI(variableYmap,'y');
				val +=self.mapvariableForUI(variableXmap,'x');
				cost=costY+costX

			else:
				if equationX==[]:
					equation=equationY
					step=stepY
					val =self.mapvariableForUI(variableYmap,'y');
					cost=costY
				else:
					equation=equationX
					step=stepX
					val +=self.mapvariableForUI(variableXmap,'x');
					cost=costX
					
			

		# insert core x and y for user inrterface
		

		print(fdes)
		find+=fdes[3] if 'dir' in fdes else ''
		
		[val,cost]=self.cutVariable(val,cost)
		print([val,cost])


		return [[val,cost],equation,find,step,lastStep]











	def cutVariable(self,variable,cost):
		val=list()
		cos=list()
		for index in range(len(variable)):
			if not(variable[index] in val):
				val.append(variable[index])
				cos.append(cost[index])
		return [val,cos]
















	def returnVariable(self):
		print("im return variableeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
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
			cost[the]=calculate.calculate('result')[-1]

			calculate.set(['value','the'],cos,'value|y')
			cost[value]=calculate.calculate('result')[-1]
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
				costY.append(-9.8)

			#  map variable for formula
			variableXmap=self.mapsVariable(variableX)
			variableYmap=self.mapsVariable(variableY)
			fdes=self.getlist(title)
			fdes='' if fdes ==[] else fdes[0]
		find = find[0] if type(find)==list else find
		find=self.mapsVariable(find)

		equation=[]
		if(fdes=='dirx'):
			calculate.set(variableXmap,[],find)
			equation+=calculate.getFormula()
		elif (fdes=='diry'):
			calculate.set(variableYmap,[],find)	
			equation+=calculate.getFormula()
		else:
			print([variableX,variableY,find])
			calculate.set(variableXmap,[],find)
			equation+=calculate.getFormula()
			equationX=equation
			equation=[]
			calculate.set(variableYmap,[],find)	
			equation+=calculate.getFormula()
			equationY=equation
			if self.isVariableCore(find,['u','v','a','F','s']):
				equation=equationY+equationX if equationY!=[] and equationX!=[] else []
			else:
				if equationX==[]:
					equation=equationY
				else:
					equation=equationX
			

		# insert core x and y for user inrterface
		val =list()
		val =self.mapvariableForUI(variableYmap,'y');
		val +=self.mapvariableForUI(variableXmap,'x');
		val=list(set(val))
		print(fdes)
		find+=fdes[3] if 'dir' in fdes else ''

		return [val,equation,find]

	def mapvariableForUI(self,variable,core):
		val=list()
		for value in variable:
			if self.isVariableCore(value,['u','v','a','F','s']):
				val.append(value+core)
			else:
				val.append(value)
		return val