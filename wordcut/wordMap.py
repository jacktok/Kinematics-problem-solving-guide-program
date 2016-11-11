from wordcut.wordFilter import Filter 
from wordcut.wordCut import WordCut
from wordcut.SearchWord import Dic
from operator import itemgetter
import re,string
class WordMap(WordCut,Filter,Dic):
	"""docstring for WordMap"""
	def __init__(self):
		super(WordMap, self).__init__()
	def includeProblem(self,txt):
		self.problem=txt
		# super(WordMap,self).set(txt)
	def tencesCut(self,problem):
		tences=self.divideTance(problem)
		words=[]
		for tence in tences:
			# print(tence)
			if tence[1]:
				self.set(tence[0])
				words+=self.wordCut()
			else:
				words.append(tence[0])
		return words
	def insertWordDescrip(self,words):
		wordDescrip=[]
		while len(words)!=0:
			tryWord=words.pop(0)
			word=tryWord
			count=0
			find=-1
			# if len(words)-1>count:
			# 	print(self.look(tryWord+words[count])," :: ",tryWord+words[count])
			while len(words)> count and self.look(tryWord+words[count])!=0 and not(self.searchWordSpec(tryWord)) and not(self.searchWordSpec(words[count])):
				tryWord+=words[count]
				print('word',tryWord)
				# self.look(tryWord)
				if self.searchDictionary():
					find=count
					# print(" :: find ")
				count+=1
				print("\n")
			for count in range(-1,find):word+=words.pop(0)
			# print(word)
			self.look(word)
			descrip=dict()
			if not(self.searchWordSpec(word)):
				descrip['type']='n/a'
				if self.isThai(word[0]):
					self.searchDictionary()
					descrip['type']=self.wordType()
				if self.isNum(word[0]):
					descrip['type']='num'
					descrip['value']=word
				descrip['word']=word
			else :
				descrip=self.searchWordSpec(word)
				# descrip['type']='special'
			wordDescrip.append(descrip)
		return wordDescrip
	def map(self):
		problem=self.problem
		words=self.tencesCut(problem)
		wordDescrip=self.insertWordDescrip(words)
		wordDescrip=self.findUnit (wordDescrip)
		return wordDescrip

	def findUnit(self,words):
		formathUnit=["si","unit","operation","num"]
		units=list()
		count=0
		eng=list()
		one=list()
		for word in words:
			# print(words)
			if word['word']=="ต่อ" or word['word']=="/":
				units.append(count)
			if word['type']=="n/a":
				eng.append(count)
			count+=1

		while eng:
			index=eng.pop(0)
			word=words[index]['word']
			divide=False
			if '/' in word:
				divide=True
			word=word.split('/')
			check=list()
			print(word)
			while word:
				unit=word.pop(0)
				
				last=len(unit)
				for indexFM in range(3,-1,-1):
					print(indexFM)
					if last==0:break
					wordSpec=self.searchTypeSpec(formathUnit[indexFM],'value')
					while wordSpec:
						pattern=wordSpec.pop(0)+"$"
						if pattern[0] in string.punctuation:pattern="\\"+pattern
						print(pattern," ::: ",unit[:last])
						match=re.search(pattern,unit[:last])
						if match:
							last=match.start()
							if indexFM==1:check.append(True)
							break
					
			if (len(check)==2 and divide) or (not(divide) and len(check)==1) :
				words[index]['type']="unit"
				words[index]['value']=words[index]['word']
			

		positionUnit=list()
		# print(units)
		while units:
			index=units.pop(0)
			# index=words.index(unit)
			# print(index)
			checkpre=False
			checkpos=False
			start=index
			finit=index
			for indexFM in range(0,4):
				# print(formathUnit[indexFM],indexFM)
				if formathUnit[indexFM]==words[finit+1]['type']:
					finit+=1
					# print("   ",words[finit]['type'],"  :: ",finit,indexFM)
					if formathUnit[indexFM]=="unit":checkpos=True
				if formathUnit[-1*(indexFM+1)]==words[start-1]['type']:
					start-=1
					if formathUnit[-1*(indexFM+1)]=="unit":checkpre=True
			# print(start,"  ::  ",finit)
			if checkpre and checkpos:positionUnit.append([start,index,finit])
		positionUnit.sort(key=itemgetter(0),reverse=True)
		print(positionUnit)
		while positionUnit:
			posi=positionUnit.pop(0)
			descrip=dict()
			descrip['value']=words[posi[0]]['value']
			descrip['word']=words[posi[0]]['word']
			descrip['type']="unit"
			# print(range(posi[0]+1,posi[2]))
			for index in range(posi[0]+1,posi[2]+1):

				if index == posi[1]:
					descrip['value']+='/'
				else :
					# print(words[index])
					descrip['value']+=words[index]['value']
				descrip['word']+=words[index]['word']
			words[posi[0]]=descrip
			for index in range(posi[2],posi[0],-1):
				# print(index)
				del words[index]
		count=0
		for word in words:
			if word['type']=="si":
				one.append(count)
			count+=1
		position=list()
		print(formathUnit)
		while one:
			once=one.pop(0)
			check=False
			si=once
			index=once
			for indexFM in range(0,4):
				# print(formathUnit[indexFM],"::",words[index+1]['type'])
				if index+1<len(words):
					if formathUnit[indexFM]==words[index+1]['type']:
						index+=1
						if formathUnit[indexFM]=="unit":check=True
			if check:position.append([si,index])
		position.sort(key=itemgetter(0),reverse=True)
		while position:
			posi=position.pop(0)
			descrip=dict()
			descrip['value']=words[posi[0]]['value']
			descrip['word']=words[posi[0]]['word']
			descrip['type']="unit"
			for index in range(posi[0]+1,posi[1]+1):
				descrip['value']+=words[index]['value']
				descrip['word']+=words[index]['word']
			words[posi[0]]=descrip
			for index in range(posi[1],posi[0],-1):
				# print(index)
				del words[index]



		return words









		