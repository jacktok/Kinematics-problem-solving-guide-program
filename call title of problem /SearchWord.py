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
class Dic(object):
	def __init__(self):
		super(Dic, self).__init__()
		f=open("newdic","r")
		a=f.read()
		f.close()
		self.dictionary=json.loads(a)
		self.wordlist=list()
		self.wordSearch=str()
		print("loaded dictionary\n")
	def look(self,word):
		self.wordSearch=word
		pattern='^'+word
		# print(pattern)
		self.wordlist=list()
		for wordDic in self.dictionary:
			# in the dictionary have space in the words
			try:
				wordDic['tsearch']
			except Exception:
				pass
			else:
				if re.match(pattern,wordDic['tsearch']) :
					self.wordlist.append(wordDic.copy())
		# if not(word in self.lookWord()):
		# 	self.wordlist=list()
		return len(self.wordlist)
	def search(self):
		words=list()
		for word in self.wordlist:
			if word['tsearch']==self.wordSearch:
				words.append(word)
		self.wordlist=words 
		return self.wordSearch in self.lookWord()
	def lookup(self):
		return self.wordlist	
	def lookWord(self):
		words=list()
		for word in self.wordlist:
			words.append(word['tsearch'])
		return words
	def dicData(self):
		return self.dictionary
	def wordType(self):
		try:
			return self.wordlist[0]['tcat']
		except Exception as e:
			return "none"

		