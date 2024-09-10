import io

# Array to represent the words:
# 0: store, 1: sub, 2: load, 3: loadl, 4: lshift, 5: rshift, 6: mult,
# 7: add, 8: nop, 9: output, 10: =>, 11: ',', 12: EOL
wordArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Array to represent the categories, it goes like so:
# 0: MEMOP, 1: LOADI, 2: ARITHOP, 3: OUTPUT, 4: NOP, 5: CONSTANT
# 6: REGISTER, 7: COMMA, 8: INTO, 9: EOF, 10: EOL
categoryArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
class Scanner():
    
    def __init__(self, filename):
        self.filename = filename
        self.buffer = open(filename, "r", encoding="utf-8")
        self.line = ""
        pass

    def readLine(self):
        self.line = self.buffer.readline()
        
    def readWord(self):
        i = 0
        word = ""
        while(i < len(self.line) and self.line[i] != ' '):
            word = word + self.line[i]
            i += 1
        if(i == len(self.line)):
            self.readLine()
        return word
    
        