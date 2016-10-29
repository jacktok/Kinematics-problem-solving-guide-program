from wordcut.wordMap import WordMap
import pprint
import json
import os

pp = pprint.PrettyPrinter(indent=4)
class WordGroup(WordMap):
	"""docstring for WordGroup"""
	def __init__(self):
		super(WordGroup, self).__init__()
		self.fileLocaltion=os.getcwd()+"/data/grammar"
		self.loadGrammar()
	def loadGrammar(self):
		data=open(self.fileLocaltion,"r")
		txtData=data.read()
		data.close()
		grammar=json.loads(txtData)
		self.grammar=grammar
	def saveGrammar(self):
		data=json.dumps(self.grammar, ensure_ascii=False)
		grammar=open(self.fileLocaltion,"w")
		grammar.write(data)
		grammar.close()
		print("complit")
		
	def dumpGrammar(self,*arg):
		# paramiter grammarof typedata

		if len(arg)==0 :
			# dump all data of grammar
			# return(list:list:dict)
			return self.grammar
		if len(arg)==1 :
			# dump some grammar
			# return(list:dict)
			if arg[0] in self.grammar:
				return self.grammar[arg[0]]
			else:
				print("Error : No paramiters "+arg[0])
				return []
		if len(arg)==2:
			# dump some grammar and some type 
			# return(list:list:str)
			print("im dumpGrammmar len 2"+arg[0]+arg[1])
			if arg[0] in self.grammar:
				someGrammar=list()
				for grammar in self.grammar[arg[0]]:
					pp.pprint(grammar)
					someGrammar.append(self.dumpGrammarFM(grammar.copy(),arg[1]))
				return someGrammar
		print("Error : dump grammar")

	def dumpGrammarFM(self,*arg):
		# paramiter data(list:dict) typedata
		# return(list:str) some data of dict
		if len(arg)==2 :
			# pp.pprint(arg[0])
			if arg[1] in arg[0][0]:
				grammarFM=list()
				while arg[0]:
					grammarFM.append(arg[0].pop(0)[arg[1]])
				return grammarFM
			else :
				print("Error : "+arg[1]+" not match ")
				return []
		if len(arg)==1:
			return arg[0]
		print("Error : dump grammar FM")
	def checkGrammar(self,grammar,typeGrammar):
		# paramiter grammar(list:dict)
		# check if grammar is already return False
		grammarType=self.dumpGrammarFM(grammar.copy(),"type")
		print("aaaaaaaaa   " )
		pp.pprint(grammarType)
		pp.pprint(self.dumpGrammar('direction','type'))
		for dicTypeGrammar in self.dumpGrammar(typeGrammar,"type"):
			pp.pprint(dicTypeGrammar)
			if grammarType == dicTypeGrammar :
				return False
				break
		return True
	def addGrammar(self):
		print("-----add grammar------")
		newGrammar=list()
		x="y"
		typeGrammar=input("type :: ")
		while x=="y":
			newSubGrammar=dict()
			newSubGrammar['type']=input("Type : ")
			newSubGrammar['important']=input("important(t) : ")=="t"
			x=input("more type(y)")
			newGrammar.append(newSubGrammar)
		try:
			grammar[typeGrammar]
		except NameError:
			self.grammar[typeGrammar]=list()
		self.grammar[typeGrammar].append(newGrammar)

		# pp.pprint(newGrammar)
		# if self.checkGrammar(newGrammar,typeGrammar):
		# 	print("Complite ::")
		# else :
		# 	print("Error : grammar is already")
	def group(self):
		words=self.map()
		grammar=self.grammar.copy()
		# pp.pprint(words)
		for title in grammar: 
			# titile of grammar
			if title!="group":
				for rule in grammar[title]:
					words=self.patternWord(words,rule.copy(),title)
		for rule in grammar["group"]:
			print(rule)
			words=self.patternWord(words,rule.copy(),self.grammarFirstTrue(rule)['type'])

		pp.pprint(words)
		return words
	def grammarFirstTrue(self,rule):
		for i in rule:
			if i['important']:
				return i

	def patternWord(self,words,rule,title):
		# find word is coincide rule
		# print(words)
		titleIndex=list()
		preWord=list()
		posWord=words.copy()
		ruleIndex=self.indexTitleofRule(rule.copy(),title)
		# pp.pprint(rule)
		# pp.pprint(ruleIndex)
		while posWord:
			isTitle=False
			coincide=True
			word=posWord.pop(0)
			bufferRule=list()
			if word['type']==title:
				print("hi")
				isTitle=True
				tryGroup=list()
				tryGroup.append(word)				
				if ruleIndex>=0:
					nextStatus=True
					for index in range(1,ruleIndex+1):
	
						# type between rule[0] and befor rule[index]
						bufferWord=self.popWord(preWord,-1)
						if bufferWord['type']==rule[ruleIndex-index]['type']:
							if rule[ruleIndex-index]['important']:
								bufferRule=list()
							if not(rule[ruleIndex-index]['important']):
								bufferRule+=[rule[ruleIndex-index]['type']]
							tryGroup.insert(0,bufferWord)
						else:
							if bufferWord['type']!=self.popWord(bufferRule,0) or rule[ruleIndex-index]['important']:
								coincide=False
								break
					wordIndex=len(tryGroup)	
					bufferRule=list()
					
					for index in range(1,len(rule)-ruleIndex):
						# type between after rule[index] and rule[last]
						if nextStatus: bufferWord=self.popWord(posWord,0)
						print(":::",bufferWord['type'],rule[ruleIndex+index]['type'],rule[ruleIndex+index]['important'])

						if bufferWord['type']==rule[ruleIndex+index]['type']:
							if rule[ruleIndex+index]['important']:
								bufferRule=list()
							if not(rule[ruleIndex+index]['important']):
								bufferRule+=[rule[ruleIndex+index]['type']]
							tryGroup.append(bufferWord)
							nextStatus=True
						else:
							print("else",not(rule[ruleIndex+index]['important']))
							if not(rule[ruleIndex+index]['important']):
								print("not im")
								nextStatus=False
								pass
							
							elif bufferWord['type']!=self.popWord(bufferRule,0) :
									print("break")
									# print(bufferWord)
									tryGroup.append(bufferWord)
									coincide=False
									# isTitle=False
									break
					if coincide:
						# print("tRUEEEEEEEE",wordIndex)
						group=dict()
						group['type']='g'+title
						group['rule']=rule
						group['title']=title
						group['words']=tryGroup
						preWord.append(group)
					else:
						preWord+=tryGroup[:wordIndex]
						posWord=tryGroup[wordIndex:]+posWord
			if not(isTitle):
				preWord.append(word)
			# pp.pprint(preWord)
	
		return preWord	

		
	def popWord(self,word,index):
		if len(word)!=0:
			return word.pop(index)
		return False


	def indexTitleofRule(self,rule,title):
		# find index of title in rule
		count=0
		while rule:
			if rule.pop(0)['type']==title:
				return count
			count+=1
		return -1




			



# test=WordGroup()



# pp.pprint(test.dumpGrammar('direction','type'))
# test.addGrammar()