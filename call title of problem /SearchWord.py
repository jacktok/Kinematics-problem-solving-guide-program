import json
class Dic(object):
	def __init__(self):
		f=open("newdic","r")
		a=f.read()
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
