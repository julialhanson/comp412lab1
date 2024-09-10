import io
import sys
# Array to represent the words:
# 0: store, 1: sub, 2: load, 3: loadl, 4: lshift, 5: rshift, 6: mult,
# 7: add, 8: nop, 9: output, 10: =>, 11: ',', 12: EOL, 13: EOF
wordArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Array to represent the categories, it goes like so:
# 0: MEMOP, 1: LOADI, 2: ARITHOP, 3: OUTPUT, 4: NOP, 5: CONSTANT
# 6: REGISTER, 7: COMMA, 8: INTO, 9: EOF, 10: EOL, 11: ERROR, 12: COMMENT
categoryArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
class Scanner():
    def __init__(self, filename):
        self.filename = filename
        self.buffer = open(filename, "r", encoding="utf-8")
        self.line = ""
        self.i = 0
        pass

    def readLine(self):
        self.line = self.buffer.readline()
        self.i = 0
        
    def readWord(self):
        if(len(self.line) == 0):
            return (9, "EOF") 
        word = ""
        while (self.i < len(self.line)):
            if self.line[self.i] == 's':
                if self.line[self.i] == 'u':
                    self.i += 1
                    if self.line[self.i] == 'b':
                        return (2, 1)
                    else:
                        return self.handleError()
                elif self.line[self.i] == 't':
                    self.i += 1
                    if self.line[self.i] == 'o':
                        self.i += 1
                        if self.line[self.i] == 'r':
                            self.i += 1
                            if self.line[self.i] == 'e':
                                return (0,5)
                            else:
                                return self.handleError()
                        else:
                            return self.handleError()
                    else:
                        return self.handleError()
                else:
                    while self.i < len(self.line) and (ord(self.line[self.i]) >= 48 or ord(self.line[self.i]) <= 57):
                        self.i += 1
                    if(self.i == len(self.line)):
                        self.readLine()
                        return("Register something")
                    elif(self.line[self.i] == ' '):
                        self.i+= 1
                        return("register something")
                    else:
                        return self.handleError()
            elif self.line[self.i] == 'l':
                self.i += 1
                if self.line[self.i] == 's':
                    self.i += 1
                    if self.line[self.i] == 'h':
                        self.i += 1
                        if self.line[self.i] == 'self.i':
                            self.i += 1
                            if self.line[self.i] == 'f':
                                self.i += 1
                                if self.line[self.i] == 't':
                                    return (0,5)
                                else:
                                    return self.handleError()
                            else:
                                return self.handleError()
                        else:
                            return self.handleError()
                    else:
                        return self.handleError()
                elif self.line[self.i] == 'o':
                    self.i += 1
                    if self.line[self.i] == 'a':
                        self.i += 1
                        if self.line[self.i] == 'd':
                            if self.line[self.i + 1] == 'I':
                                self.i += 1
                                return (1,3)
                            else:
                                return (0,2)
                else: 
                    return self.handleError()
            elif self.line[self.i] == 'r':
                if self.line[self.i] == 's':
                    self.i += 1
                    if self.line[self.i] == 'h':
                        self.i += 1
                        if self.line[self.i] == 'self.i':
                            self.i += 1
                            if self.line[self.i] == 'f':
                                self.i += 1
                                if self.line[self.i] == 't':
                                    return (0,5)
                                else:
                                    return self.handleError()
                            else:
                                return self.handleError()
                        else:
                            return self.handleError()
                    else:
                        return self.handleError()
                else:
                    while self.i < len(self.line) and (ord(self.line[self.i]) >= 48 or ord(self.line[self.i]) <= 57):
                        self.i += 1
                    if(self.i == len(self.line)):
                        self.readLine()
                        return("Register something")
                    elif(self.line[self.i] == ' '):
                        self.i+= 1
                        return("register something")
                    else:
                        return self.handleError()
            elif self.line[self.i] == 'm':
                if self.line[self.i] == 'u':
                    self.i += 1
                    if self.line[self.i] == 'l':
                        self.i += 1
                        if self.line[self.i] == 't':
                            return (2,6)
                        else:
                            return self.handleError()
                    else:
                        return self.handleError()
                else:
                    return self.handleError()
            elif self.line[self.i] == 'a':
                if self.line[self.i] == 'd':
                    self.i += 1
                    if self.line[self.i] == 'd':
                        return (2,7)
                    else:
                        return self.handleError()
                else:
                    return self.handleError()
            elif self.line[self.i] == 'n':
                if self.line[self.i] == 'o':
                    self.i += 1
                    if self.line[self.i] == 'p':
                        return (4,8)
                    else:
                        return self.handleError()
                else:
                    return self.handleError()
            elif self.line[self.i] == 'o':
                self.i += 1
                if self.line[self.i] == 'u':
                    self.i += 1
                    if self.line[self.i] == 't':
                        self.i += 1
                        if self.line[self.i] == 'p':
                            self.i += 1
                            if self.line[self.i] == 'u':
                                self.i += 1
                                if self.line[self.i] == 't':
                                    return (3,9)
                                else:
                                    return self.handleError()
                            else:
                                return self.handleError()
                        else:
                            return self.handleError()
                    else:
                        return self.handleError()
                else:
                    return self.handleError()
            elif self.line[self.i] == '=':
                self.i += 1
                if self.line[self.i] == '>':
                    return (8,10)
                else:
                    return self.handleError()
            elif self.line[self.i] == ',':
                return (7,11)
            elif self.line[self.i] == '/':
                self.i += 1
                if self.line[self.i] == '/':
                    while self.i < len(self.line):
                        self.i += 1
                    self.readLine()
                    return (12, "COMMENT")
            elif self.line[self.i] == 'EOL':
                self.readLine()
                return (10,12) 
            elif self.line[self.i] == ' ':
                self.i += 1
            else:
                return self.handleError()
        # if(self.i == len(self.line)):
        #     self.readLine()
        #     if self.line == '':
        #         return [9, 13]
        
    def handleError(self):
        self.readLine()
        return (11, "ERROR")
    