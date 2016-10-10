import PyICU
class WordCut(object):
    def set(self, sentences):
         self.sentences = sentences
    def isThai(self,chr):
        cVal = ord(chr)
        if(cVal >= 3584 and cVal <= 3711):
            return True
        return False
    def isNum(self,chr):
        cVal=ord(chr)
        if(cVal>=48 and cVal<=57):
            return True
        return False
    def warp(self,txt):
        bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
        bd.setText(txt)
        lastPos = bd.first()
        word=[]
        try:
            while(1): 
                currentPos = next(bd)
              
                word+=[txt[lastPos:currentPos]]
                lastPos = currentPos
        except StopIteration:
            pass
        return word
    def wordCut(self):
        sentences=self.sentences
        sentences=sentences.replace('\n',' ').split()
        words=[]
        for sentence in sentences:
            # print(sentence)
            if not(self.isThai(sentence[0]) or self.isNum(sentence[0])) :
                words+=[sentence] 
                pass
            else:
                words+=self.warp(sentence)[:]
        return words




# "วัตถุกำลังเคลื่อนที่ด้วยความเร็ว 40 m/s ไปทางทิศตะวันตก จากนั้นได้รับความเร่ง 10\n ไปทางทิศตะวันออกเป็นเวลา 5 วินาที จงหาความเร็วของวัตถุ"
