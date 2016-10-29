from operator import itemgetter
import json
import re
import os
class Filter(object):
	def __init__(self):
		super(Filter, self).__init__()
		self.fileLocaltion=os.getcwd()+"/data/wordspecial"
		self.load()
		print("loaded word special\n")
	def load(self):
		wordspec=open(self.fileLocaltion,"r")
		dic=wordspec.read()
		wordspec.close()
		dic=json.loads(dic)
		self.dic=dic
		# print("complete :: loaded\n")
	def add(self):
		word=input('{:10}:: '.format('word')).strip()
		special=input('{:10}:: '.format('type')).strip()
		value=input('{:10}:: '.format('value')).strip()
		# direction=input('{:10}:: '.format('direction')).strip()
		wordadd={"word":word,"type":special,"value":value}
		self.dic+=[wordadd]
		print("Complete :: add word\n")
	def addWord(self,word):
		special=input('{:10}:: '.format('type')).strip()
		value=input('{:10}:: '.format('value')).strip()
		# direction=input('{:10}:: '.format('direction')).strip()
		wordadd={"word":word,"type":special,"value":value}
		self.dic+=[wordadd]
		print("Complete :: add word")
	def save(self):
		self.sortDic
		data=json.dumps(self.dic, ensure_ascii=False)
		dic=open(self.fileLocaltion,"w")
		dic.write(data)
		dic.close()
		print("Complete :: saved\n")
	def sortDic():
		from operator import itemgetter
	def dump(self):
		return self.dic
	def dumpWord(self):
		word=[]
		for i in self.dic:
			word+=[i['word']]
		return word
	def dumpWord(self):
		words=[]
		for word in self.dic:
			words+=[word['word']]
		return words
	def searchWordSpec(self,wordSearch):
		for word in self.dic:
			if word['word']==wordSearch:
				return word
		return False
	def searchTypeSpec(self,typeSearch):
		words=list()
		for word in self.dic:
			if word['type']==typeSearch:
		
				words.append(word['word'])
		if words :
			return False
		return words
	def edit(self,word):
		index=-1
		for i in range(len(self.dic)):
			if self.dic[i]['word']==word:
				index=i
				break
		if index!=-1:
			print("word = ",self.dic[index]['word'],"\n----edit---")
			self.dic[index]['type']=input("Edit {:10}::".format("type"))or self.dic[index]['type']
			self.dic[index]['value']=input("Edit {:10}::".format("value"))or self.dic[index]['value']
			# self.dic[index]['direction']=input("Edit {:10}::".format("direction"))or self.dic[index]['direction']
			return True	
		return False
	# def clear(self):
	# 	self.dic=[]
	def delete(self,word):
		index=-1
		for i in range(len(self.dic)):
			if self.dic[i]['word']==word:
				index=i
				break
		if index!=-1:
			del self.dic[index]
			return True
		return False
	def divideTance(self,txt):
		# finde index of word special in txt 
		specWord=self.dumpWord()
		specWord.sort(key=len,reverse=True)
		tenceIndex=[]
		for spec in specWord:
			index=[st.start() for st in re.finditer(spec,txt)]
			if spec=="วินาที" :print(index)
			while len(index)!=0:
				startTence=index.pop(0)
				finitTence=startTence+len(spec)
				overlap=False
				# print(tenceIndex)
				if len(tenceIndex)!=0:
					for tence in tenceIndex:
						rangeTence=range(tence[0]+1,tence[1]-1)
						if (startTence in rangeTence) or (finitTence in rangeTence):
							overlap=True
							break
				if not(overlap) or (len(tenceIndex)==0):
					tenceIndex.append([startTence,finitTence])
		tenceIndex.sort(key=itemgetter(0))
		# divide txt by word special

		tences=[]
		currentIndex=0
		while len(tenceIndex)!=0:
			index=tenceIndex.pop(0)
			if currentIndex!=index[0]:
				tences.append([txt[currentIndex:index[0]],True])
			tences.append([txt[index[0]:index[1]],False])
			currentIndex=index[1]
		if currentIndex!=len(txt):
			tences.append([txt[currentIndex:],True])
		return tences




				

# a=filter()
# a.add()