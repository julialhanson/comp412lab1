import io
import sys
# Array to represent the words:
# 0: store, 1: sub, 2: load, 3: loadl, 4: lshift, 5: rshift, 6: mult,
# 7: add, 8: nop, 9: output, 10: =>, 11: ',', 12: EOL, 13: EOF

# change this 
wordArr = ["loadI", "nop", "output", "sub", "store", "load", "=>", ',', "\\n",  "", "lshift", "rshift", "mult", "add"]
##loadi, nop, output defined in other constants

SUB = 3
STORE = 4
LOAD = 5
# INTO, COMMA, EOL, EOF shared
LSHIFT = 10
RSHIFT = 11
MULT = 12
ADD = 13

# add constant category that is just number

LOADI = 0
NOP = 1
OUTPUT = 2
ARITHOP = 3
MEMOP = 4
CONSTANT = 5
INTO = 6
COMMA = 7
EOL = 8
EOF = 9
REGISTER = 10
COMMENT = 11

ERROR = -1

# Array to represent the categories, it goes like so:
categoryArr = ["LOADI", "NOP", "OUTPUT", "ARITHOP", "MEMOP",  "CONSTANT", "INTO", "COMMA", "EOL", "EOF", "REGISTER", "COMMENT"]
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
        
        if self.line[self.i] == 's':
            if self.line[self.i] == 'u':
                self.i += 1
                if self.line[self.i] == 'b':
                    self.i += 1
                    if self.line[self.i].isspace():
                        return (ARITHOP, SUB)
                    else:
                        return self.handleError()
                else:
                    return self.handleError()
            elif self.line[self.i] == 't':
                self.i += 1
                if self.line[self.i] == 'o':
                    self.i += 1
                    if self.line[self.i] == 'r':
                        self.i += 1
                        if self.line[self.i] == 'e':
                            self.i += 1
                            if self.line[self.i].isspace():
                                return (MEMOP, STORE)
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
        elif self.line[self.i] == 'l':
            self.i += 1
            if self.line[self.i] == 's':
                self.i += 1
                if self.line[self.i] == 'h':
                    self.i += 1
                    if self.line[self.i] == 'i':
                        self.i += 1
                        if self.line[self.i] == 'f':
                            self.i += 1
                            if self.line[self.i] == 't':
                                self.i += 1
                                if self.line[self.i].isspace():
                                    return (ARITHOP, LSHIFT)
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
            elif self.line[self.i] == 'o':
                self.i += 1
                if self.line[self.i] == 'a':
                    self.i += 1
                    if self.line[self.i] == 'd':
                        self.i += 1
                        if self.line[self.i] == 'I':
                            self.i += 1
                            if self.line[self.i].isspace():
                                return (LOADI, LOADI)
                            else:
                                return self.handleError()
                        elif self.line[self.i].isspace():
                            return (MEMOP, LOAD)
                        else:
                            return self.handleError()
            else: 
                return self.handleError()
        elif self.line[self.i] == 'r':
            if self.line[self.i] == 's':
                self.i += 1
                if self.line[self.i] == 'h':
                    self.i += 1
                    if self.line[self.i] == 'i':
                        self.i += 1
                        if self.line[self.i] == 'f':
                            self.i += 1
                            if self.line[self.i] == 't':
                                self.i += 1
                                if self.line[self.i].isspace():
                                    return (ARITHOP, RSHIFT)
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
            elif ord(self.line[self.i]) >= 48 and ord(self.line[self.i]) <= 57:
                print("CHAR IS " + self.line[self.i])
                regstr = ""
                while self.i < len(self.line) and (ord(self.line[self.i]) >= 48 and ord(self.line[self.i]) <= 57):
                    regstr = regstr + self.line[self.i]
                    self.i += 1
                if(self.i == len(self.line)):
                    self.readLine()
                    return(REGISTER, int(regstr))
                elif(self.line[self.i].isspace()):
                    return(REGISTER, int(regstr))
                else:
                    print("BREAK 1")
                    return self.handleError("Register Error")
            else:
                print("BREAK 2")
                return self.handleError()
        elif self.line[self.i] == 'm':
            if self.line[self.i] == 'u':
                self.i += 1
                if self.line[self.i] == 'l':
                    self.i += 1
                    if self.line[self.i] == 't':
                        self.i += 1
                        if self.line[self.i].isspace():
                            return (ARITHOP, MULT)
                        else:
                            return self.handleError()
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
                    self.i += 1
                    if self.line[self.i].isspace():
                        return (ARITHOP, ADD)
                    else:
                        print("add error")
                        return self.handleError()
                else:
                    return self.handleError()
            else:
                return self.handleError()
        elif self.line[self.i] == 'n':
            if self.line[self.i] == 'o':
                self.i += 1
                if self.line[self.i] == 'p':
                    self.i += 1
                    if self.line[self.i].isspace():
                        return (NOP, NOP)
                    else:
                        return self.handleError()
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
                                self.i += 1
                                if self.line[self.i].isspace():
                                    return (OUTPUT, OUTPUT)
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
            else:
                return self.handleError()
        elif self.line[self.i] == '=':
            print("goes into equal")
            self.i += 1
            if self.line[self.i] == '>':
                self.i += 1
                if self.line[self.i].isspace():
                    return (INTO, INTO)
            else:
                return self.handleError()
        elif self.line[self.i] == ',':
            print("goes into comma")
            self.i += 1
            if self.line[self.i].isspace():
                return (COMMA, COMMA)
            else:
                return self.handleError()
        elif self.line[self.i] == '/':
            self.i += 1
            if self.line[self.i] == '/':
                while self.i < len(self.line):
                    self.i += 1
                self.readLine()
                return (COMMENT, COMMENT)
        elif self.line[self.i] == 'EOL':
            self.readLine()
            return (EOL, EOL) 
        elif self.line[self.i] == ' ':
            self.i += 1
        elif ord(self.line[self.i]) <= 57 and ord(self.line[self.i]) >= 48:
            constr = ""
            while ord(self.line[self.i]) <= 57 and ord(self.line[self.i]) >= 48:
                constr = constr + self.line[self.i]
                self.i += 1
            if self.line[self.i].isspace():
                return (CONSTANT, int(constr))   
            else:
                print("Constant testing broke at char " + self.line[self.i])
                return self.handleError()                 
        else:
            print("error char = " + self.line[self.i])
            return self.handleError()
    # if(self.i == len(self.line)):
    #     self.readLine()
    #     if self.line == '':
    #         return [9, 13]
        
    def handleError(self):
        self.readLine()
        errorMessage = "ERROR"
        return (11, errorMessage)
    
    