from wordMap import WordMap 
from wordFilter import Filter
# txt="วัตถุกำลังเคลื่อนที่ด้วยความเร็ว 40 m/s ไปทางทิศตะวันตก  จากนั้นได้รับความเร่ง 10 เมตรต่อวินาทียกกำลังสอง\n ไปทางทิศตะวันออกเป็นเวลา 5 วินาที จงหาความเร็วของวัตถุ"
# txt="เชิงเส้น เชิงมุม ความถี่ คาบ แรง มวล สัมประสิทธิ์ความเสียดทาน สถิต จลน์ เริ่มต้น ต้น ปลาย ท้าย สุดท้าย คงที่ เฉลี่ย ไปทาง ทาง แนวราบ แนวดิ่ง แนวระนาบ แนวระดับ แนวตั้ง ทะแยง"
txt="วัตถุมวล 10 kg เคลื่อนที่เป็นเส้นตรงมีความเร็วต้น 20 m/s มีความเร่ง 5 เมตรต่อวินาทียกกำลังสอง ถ้าให้เคลื่อนที่เป็นเวลา 20 s จะมีความเร็วเท่าไร"
a=WordMap()
a.includeProblem(txt)
word=a.map()
for i in word:
	print("{:40}{:20}".format(i['word'],i['type']))
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
			
 
