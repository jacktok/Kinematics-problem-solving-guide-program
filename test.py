# from wordMap import WordMap 
# from wordFilter import Filter
from wordcut.wordGroup import WordGroup
import pprint
# txt="วัตถุกำลังเคลื่อนที่ด้วยความเร็ว 40 m/s ไปทางทิศตะวันตก  จากนั้นได้รับความเร่ง 10 เมตรต่อวินาทียกกำลังสอง\n ไปทางทิศตะวันออกเป็นเวลา 5 วินาที จงหาความเร็วของวัตถุ"
txt="วัตถุมวล 10 kg เคลื่อนที่เป็นเส้นตรงมีความเร็วต้น 20 m/s มีความเร่ง 5 เมตรต่อวินาทียกกำลังสอง ถ้าให้เคลื่อนที่เป็นเวลา 20 s จะมีความเร็วเท่าไร"
# txt="วัตถุกำลังเคลื่อนที่ด้วยความเร็ว 4 เมตร/วินาที ไปทางทิศตะวันตก จากนั้นได้รับความเร่ง 5 เมตร/วินาทียกกำลังสอง ไปทางทิศตะวันออกเป็นเวลา 5 วินาที จงหาความเร็วของวัตถุ"
a=WordGroup()
# a.includeProblem(txt)
# word=a.group()
a.addGrammar()
a.saveGrammar()

pp = pprint.PrettyPrinter(indent=10)
# pp.pprint(word)


# for i in word:
# 	print("{:40}{:20}".format(i['type'],i['word']))
# b=Filter()
# fil=b.dumpWord()
# #for i in word:
# #	if not(i['word'] in fil):
# #		ans=input("import :: "+i['word']+" y/n? ")
# #		if ans=='y':
# #			b.addWord(i['word'])
# for i in txt.split():
# 	if not(i in fil):
# 		ans=input("import :: "+i+" y/n? ")
# 		if ans=='y':
# 			b.addWord(i)

# ans=input('save')
# if ans=='yes':b.save()
			
 
