from operator import itemgetter
import json
import re
class filter(object):
	def __init__(self):
		self.fileLocaltion="../data/wordspecial"
		self.load()
	def load(self):
		wordspec=open(self.fileLocaltion,"r")
		dic=wordspec.read()
		wordspec.close()
		dic=json.loads(dic)
		self.dic=dic
		# print("complete :: loaded\n")
	def add(self):
		word=input('{:10}:: '.format('word')).strip()
		special=input('{:10}:: '.format('special')).strip()
		value=input('{:10}:: '.format('value')).strip()
		direction=input('{:10}:: '.format('direction')).strip()
		wordadd={"word":word,"special":special,"value":value,"direction":direction}
		self.dic+=[wordadd]
		print("Complete :: add word\n")
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
	def search(self,wordSearch):
		for word in self.dic:
			if word['word']==wordSearch:
				return word
		return False
	def edit(self,word):
		index=-1
		for i in range(len(self.dic)):
			if self.dic[i]['word']==word:
				index=i
				break
		if index!=-1:
			print("word = ",self.dic[index]['word'],"\n----edit---")
			self.dic[index]['special']=input("Edit {:10}::".format("special"))or self.dic[index]['special']
			self.dic[index]['value']=input("Edit {:10}::".format("value"))or self.dic[index]['value']
			self.dic[index]['direction']=input("Edit {:10}::".format("direction"))or self.dic[index]['direction']
			return True	
		return False
	def clear(self):
		self.dic=[]
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
			while len(index)!=0:
				startTence=index.pop(0)
				finitTence=startTence+len(spec)
				overlap=False
				print(tenceIndex)
				if len(tenceIndex)!=0:
					for tence in tenceIndex:
						rangeTence=range(tence[0],tence[1])
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
				tences.append(txt[currentIndex:index[0]])
			tences.append(txt[index[0]:index[1]])
			currentIndex=index[1]
		if currentIndex!=len(txt):
			tences.append(txt[currentIndex:])
		return tences




				

# a=filter()
# a.add()