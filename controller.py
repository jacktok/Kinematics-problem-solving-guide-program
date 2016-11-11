from wordcut.wordGroup import WordGroup
import re,pprint,os,json,string,math
pp = pprint.PrettyPrinter(indent=10)
class ControllWord(WordGroup):
	"""docstring for controll"""
	def __init__(self):
		super(ControllWord, self).__init__()
		self.loadUnit()
	def loadUnit(self):
		fileLocaltion=os.getcwd()+"/data/unit"
		data=open(fileLocaltion,"r")
		txtData=data.read()
		data.close()
		self.unit=json.loads(txtData)
		fileLocaltion=os.getcwd()+"/data/si"
		data=open(fileLocaltion,"r")
		txtData=data.read()
		data.close()
		self.si=json.loads(txtData)
	def variable(self):
		tence=self.group()
		myValue=list()
		for value in tence:
			try:
				value['rule']
			except Exception as e:
				pass
			else:
				myValue.append(value)		
		newmyValue=list()
		
		newmyValue=self.recur(myValue.copy())
		# pp.pprint(newmyValue)
		value=self.findeValue(newmyValue.copy())


		return self.getListvalue(value)

		
	def recur(self,myValue):
		ans=list()

		for value in myValue:
			try:
				value['title']
			except Exception as e:
				pass
			else:
				if value['title'][0]=='g':
					ans.append(self.recur(value['words'].copy()))
				else:
					data={"word":"","type":"","value":""}
					if value['title']=="question":
						data["value"]+="?"
					for word in value['words']:
						for key in word:
							data[key]+=word[key]
					
					ans.append(data)
		return ans
	def findeValue(self,ans):
		val=list()
		for value in ans:
			if type(value)!=dict:
				subv=""
				for sub in value:
					subv+=sub['value']+"|"
				val.append(subv)
			else:
				val.append(value['value'])
		for index in range(0,len(val)):
			if len(val[index].split("|"))>1:
				val[index]=val[index].split("|")
				buf=""
				for i in range(0,len(val[index])):
					match=re.search("[0-9]+",val[index][i])
					if match:
						if match.start()==0:
							
							buf+=self.findValueByUnit(val[index][i][match.end():])
							buf+=match.group()+val[index][i][match.end():]+"|"
						else:
							buf+=val[index][i]+"|"
					else:
							buf+=val[index][i]+"|"
				val[index]=buf
			else:
				match=re.search("[0-9]+",val[index])
				if match:		
					if match.start()==0:
						val[index]=self.findValueByUnit(val[index][match.end():])+match.group()+val[index][match.end():]

			
		return val

	def findValueByUnit(self,unit):
		print(type(unit))
		unit=unit.split('/')
		unitOne=list()
		unitTwo=list()
		for u in self.unit:
			more=False
			for char in u['unit']:
				if char in string.punctuation:
					more=True
			if more:
				unitTwo.append(u)
			else:
				unitOne.append(u)
		self.unitOne=unitOne
		bufUnitTwo=list()
		added=list()
		pp.pprint(unitTwo)
		while unitTwo:
			find=False
			unitt=unitTwo.pop()
			for one in unitOne:
				buf=unitt.copy()
				if re.search(one['value'],buf['unit']):
					find=True
					# if one['value'] in added:
					# 	unitTwo.append(unit.replace(one['value'],unit['unit']))
					# else:
					buf['unit']=buf['unit'].replace(one['value'],one['unit'])
					unitTwo.append(buf)
			if not(find) and not(unitt in bufUnitTwo):
				bufUnitTwo.append(unitt)

		unitTwo=bufUnitTwo
		if len(unit)==1:
			unit=self.cutSI(unit)

			for unitD in unitOne:
				if unit==unitD['unit']:
					return unitD['value']
		else:
			unit=self.cutSI(unit[0])+"/"+self.cutSI(unit[1])
			for unitD in unitTwo:
				if unit==unitD['unit']:
					return unitD['value']

		print(unit)
		
		return "ERROR!!"


	def cutSI(self,unit):
		unitspec=self.searchTypeSpec("unit","value")
		if type(unit)==list:
			unit=unit[0]

		for uspec in unitspec :
			pattern=uspec
			match=re.search(pattern,unit)
			if match:
				unit=unit[match.start():]
				return unit 
		return unit

	def changeUnit(self,old,cost):
		for spli in ['/','*','^']:
			if type(old)==list:
				old=''.join(old)
			old=old.split(spli)
			
			if len(old)>1:
				newUnit=old.copy()
				cos=1
				if spli=='/':
					for index in range (0,len(old)):
						[old[index],newUnit[index],subcos]=self.changeUnit(old[index],1)
						# pp.pprint\
						if index==0:
							cos*=subcos
						else:
							cos/=subcos
					print(cos)
				elif spli=='*':
					for index in range (0,len(old)):
						[old[index],newUnit[index],subcos]=self.changeUnit(old[index],1)
						cos*=subcos
				else:
					if len(newUnit)==2:
						cos=[0,0]
						[old[0],newUnit[0],cos[0]]=self.changeUnit(old[0],1)
						[old[1],newUnit[1],cos[1]]=self.changeUnit(old[1],1)
						print("powerrrrrrrrrrr")
						pp.pprint([old[0],newUnit[0],cos[0]])
						pp.pprint([old[1],newUnit[1],cos[1]])
						cos=cos[0]**cos[1]
						print(cos)
				newUnit = [ x for x in newUnit if x!=[]]
				old = [ x for x in old if x!=[]]
				return [spli.join(old),spli.join(newUnit),cost*cos]
		if len(old)==1:
			old=old[0]
			try:
			 	float(old)
			except Exception as e:
			 	newUnit = self.cutSI(old)
			 	match=re.search(newUnit+"$",old)
			 	print(match)
			 	si=old[:match.start()]
			 	cos=1
			 	for s in self.si:
			 		if si == s['value']:
			 			cos=10**s['cost']
			 			break
			 	timeUnit=[x for x in self.unit if x['value']=='tim']
			 	cost*=cos
			 	for time in timeUnit:
			 		if newUnit==time['unit']:
			 			return [old,'sec',cost*time['cost']]
			 	return [old,newUnit,cost]

			else:
			 	return [str(old),str(old),float(old)]
		

				# si=self.searchTypeSpec("si","value")


	def changDir(self,value,descrip):
		bufdesIndex=0.1
		for index in range(0,len(descrip)):
			for desIndex in range(0,len(descrip[index])):
				match=re.search("^dir-",descrip[index][desIndex])
				if match:
					descrip[index][desIndex]=descrip[index][desIndex].replace("dir-",'dir')
					value[index]*=-1
					if descrip[index][desIndex][0:4]=='dir-':
						try:
							descrip[index][bufdesIndex]
						except Exception as e:
							descrip[index][desIndex]=[]
							value[index]=math.fabs(value[index])
							if value[index-1]>0:
								value[index]*=-1

						else:
							if descrip[index-1][bufdesIndex][0:3]=="dir":
								descrip[index][desIndex]=descrip[index-1][bufdesIndex]
								value[index]*=-1
							else:
								del descrip[index][desIndex]
								value[index]=math.fabs(value[index])
								if value[index-1]>0:
									value[index]*=-1
				if "dir" in descrip[index][desIndex]: bufdesIndex=desIndex
			descrip[index]=[x for x in descrip[index] if x]
		return [value,descrip]



	def getListvalue(self,value):
		
		print("sssqqqqwwwee")
		variable=list()
		cost=list()
		find=list()
		unit=list()
		descrip=list()
		title=list()
		for val in value:
			if val[0]=="?":
				find.append(val[1:])
				pass
			else:
				val=[word for word in val.split("|") if word!='']
				# print(val)
				isValue=False
				des=list()
				for data in val:
					print(data)
					match=re.search("[0-9]+",data)
					if match:
						isValue=True
						val=data[:match.start()]
						cos=float(data[match.start():match.end()])
						uni=data[match.end():]
					else:
						des.append(data)
				if isValue:
					variable.append(val)
					cost.append(cos)
					unit.append(uni)
					descrip.append(des)
				else:
					title.append(des)
		buf=list()
		buff=list()
		for index in range(0,len(variable)):
			if variable[index]=='the':
				buf.append(cost[index])
				buf.append(descrip[index].copy())
				buf.append(index)
				del cost[index]
				del descrip[index]
				buff.append(buf)

	
		pp.pprint(buff)
		[cost,descrip]=self.changDir(cost,descrip)
		while buff:
			buf=buff.pop(0)
			cost.insert(buf[2],buf[0])
			descrip.insert(buf[2],buf[1])
		pp.pprint([variable,cost,unit,descrip,find,title])
		old=list()
		for index in range(0,len(cost)):
			print(index)
			pp.pprint([unit[index],cost[index]])
			[o,unit[index],cost[index]]=self.changeUnit(unit[index],cost[index])
			old.append(o)
		
		# pp.pprint([variable,cost,unit,descrip,find,title])
		cost=[self.rounding(x) for x in cost]

		# pp.pprint([old,unit,cost])	
		# return([variable,cost,unit,descrip,find,title])	

		for index in range(len(cost)):
			for des in descrip[index]:
				if 'dir'in des:
					descrip[index]=des
					break
			if type(descrip[index])==list:
				descrip[index]=''
		print("last")
		pp.pprint([variable,cost,unit,descrip,find,title])	
		return([variable,cost,unit,descrip,find,title])	
		




	
	def rounding(self,cost):
		if cost==0:
			return 0
		return round(cost,int(math.fabs(round(math.log10(math.fabs(cost))))+10))


			# five formula
				# title=projec
			# velx=velavg
			# # a=-9.8
			# if not(('acc' in value)):
			# 	pass
			# 	# variable.append('acc')


			# if vel==1 and vell==1:
			# 	index=variable.index('vel')
			# 	vvariable[index]='velsta'
			# 	# elif velfin:velfin=0
			# elif vel==2:

			# 	if vell==1:
					
			# 	velstarx
			# 	velstary
			# else: !!ERROR
			# f+liner
		# elif ang in ex:
		# 	title=angular
		# 	pass
		# else :liner
	