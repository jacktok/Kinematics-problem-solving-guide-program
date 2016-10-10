from SearchWord import Dic
a=Dic()
a.search('ความเร็ว')
# print(type(a.dica()))
# mydic=a.dica()
d=a.lookup()
for i in d:
	print(i,end='\n')
