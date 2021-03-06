# document of code
# usage
# 	from SearchWord import Dic
# 	a=Dic()
# 	a.search('อย่างไร')
# 	print(a.lookup())
# base on NECTEC
# Development by Jack Tok

import json
import re
import os
print(os.getcwd())
# print(re.search("/$",os.getcwd()))
class Dic(object):
	def __init__(self):
		super(Dic, self).__init__()
		f=open(os.getcwd()+"/data/newdic","r")
		a=f.read()
		f.close()
		self.dictionary=json.loads(a)
		self.wordlist=list()
		self.wordSearch=str()
		print("loaded dictionary\n")
	def look(self,word):
		self.wordSearch=word
		pattern='^'+word
		self.wordlist=list()
		count=0
		for wordDic in self.dictionary:
			# in the dictionary have space in the words
			try:
				wordDic['tsearch']
			except Exception:
				pass
			else:
				if re.match(pattern,wordDic['tsearch']) :
					count+=1
					self.wordlist.append(wordDic.copy())
					if count==20:
						break
		return len(self.wordlist)
	def searchDictionary(self):
		words=list()
		for word in self.wordlist:
			if word['tsearch']==self.wordSearch:
				words.append(word)
		self.wordlist=words 
		return self.wordSearch in self.lookup('word')
	def lookup(self,*arg):
		if len(arg)==0 or arg[0]=="all":
			return self.wordlist	
		if arg[0]=="word":
			words=list()
			for word in self.wordlist:
				words.append(word['tsearch'])
			return sorted(words,key=len)

	def dicData(self):
		return self.dictionary
	def wordType(self):
		try:
			return self.wordlist[0]['tcat']
		except Exception as e:
			return "none"
	# def find(self,type,txt):
	# 	