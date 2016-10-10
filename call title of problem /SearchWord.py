# document of code
# usage
# 	from SearchWord import Dic
# 	a=Dic()
# 	a.search('อย่างไร')
# 	print(a.lookup())
# base on NECTEC
# Development by Jack Tok

import json
class Dic(object):
	def __init__(self):
		f=open("newdic","r")
		a=f.read()
		f.close()
		self.dic=json.loads(a)
		self.wordlist=[]
	def search(self,word):
		self.wordlist=[]
		for i in self.dic:
			# in the dictionary have space in the words
			try:
				i['tsearch']
			except Exception:
				pass
			else:
				if i['tsearch'] == word :
					self.wordlist.append(i.copy())
	def lookup(self):
		return self.wordlist	
	def dicData(self):
		return self.dic
	def wordType(self):
		try:
			return self.wordlist[0]['tcat']
		except Exception as e:
			return "none"

		