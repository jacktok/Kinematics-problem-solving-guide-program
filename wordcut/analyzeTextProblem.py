# from SearchWord import Dic
# from wordCut import WordCut

class AnalyzeText(Dic,WordCut):
	"""docstring for AnalyzeText"""
	def __init__(self, Text):
		super(AnalyzeText, self).__init__()
		super(AnalyzeText,self).set(Text)
		self.Text = Text

		wordList=super(AnalyzeText,self).wordCut()
		words=[]
		for word in wordList:
			wordtype="none"
			if super(AnalyzeText,self).isThai(word[0]):
				super(AnalyzeText,self).search(word)
				wordtype=super(AnalyzeText,self).wordType()
			if super(AnalyzeText,self).isNum(word[0]):
				wordtype="num"
			words+=[{"word":word,"type":wordtype}]
		for i in words:
			print(i['word']," :: ",i['type'],end='\n')
AnalyzeText("วัตถุกำลังเคลื่อนที่ด้วยความเร็ว 40 m/s ไปทางทิศตะวันตก จากนั้นได้รับความเร่ง 10\n ไปทางทิศตะวันออกเป็นเวลา 5 วินาที จงหาความเร็วของวัตถุ")