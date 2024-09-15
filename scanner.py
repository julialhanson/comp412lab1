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

okEndChars = ['\n', '/']

# Array to represent the categories, it goes like so:
categoryArr = ["LOADI", "NOP", "OUTPUT", "ARITHOP", "MEMOP",  "CONSTANT", "INTO", "COMMA", "EOL", "EOF", "REGISTER", "COMMENT"]
class Scanner():
    def __init__(self, filename):
        self.filename = filename
        self.buffer = open(filename, "r", encoding="utf-8")
        self.line = ""
        self.i = 0
        self.error = ""
        pass

    def readLine(self):
        print("Reading a new line")
        self.line = self.buffer.readline()
        self.i = 0
        
    def readWord(self):
        if(len(self.line) == 0):
            return (9, "EOF") 
        
        word = ""
        
        # handling the words sub, store
        if self.line[self.i] == 's':
            self.i += 1
            if self.line[self.i] == 'u':
                self.i += 1
                if self.line[self.i] == 'b':
                    self.i += 1
                    if self.line[self.i].isspace():
                        return (ARITHOP, SUB)
                    else:
                        self.error = "Error 1"
                        return self.handleError()
                else:
                    self.error = "Error 2"
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
                                self.error = "Error 3"
                                return self.handleError()
                        else:
                            self.error = "Error 4"
                            return self.handleError()
                    else:
                        self.error = "Error 5"
                        return self.handleError()
                else:
                    self.error = "Error 6"
                    return self.handleError()
            else:
                self.error = "Error 7"
                return self.handleError()
        # handling words lshift, loadI, load
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
                                    self.error = "Error 8"
                                    return self.handleError()
                            else:
                                self.error = "Error 9"
                                return self.handleError()
                        else:
                            self.error = "Error 10"
                            return self.handleError()
                    else:
                        self.error = "Error 11"
                        return self.handleError()
                else:
                    self.error = "Error 12"
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
                                self.error = "Error 13"
                                return self.handleError()
                        elif self.line[self.i].isspace():
                            return (MEMOP, LOAD)
                        else:
                            self.error = "Error 14"
                            return self.handleError()
            else: 
                self.error = "Error 15"
                return self.handleError()
        #handling rshift and registers
        elif self.line[self.i] == 'r':
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
                                    return (ARITHOP, RSHIFT)
                                else: 
                                    self.error = "Error 16"
                                    return self.handleError()
                            else:
                                self.error = "Error 17"
                                return self.handleError()
                        else:
                            self.error = "Error 18"
                            return self.handleError()
                    else:
                        self.error = "Error 19"
                        return self.handleError()
                else:
                    self.error = "Error 20"
                    return self.handleError()
            #handling consonants
            elif ord(self.line[self.i]) >= 48 and ord(self.line[self.i]) <= 57:
                
                regstr = ""
                while self.i < len(self.line) and (ord(self.line[self.i]) >= 48 and ord(self.line[self.i]) <= 57):
                    regstr = regstr + self.line[self.i]
                    self.i += 1
                if(self.i == len(self.line)):
                    self.readLine()
                    return(REGISTER, int(regstr))
                elif(self.line[self.i].isspace() or self.line[self.i] == '=' or self.line[self.i] == ','):
                    return(REGISTER, int(regstr))
                elif self.line[self.i] in okEndChars:
                    print("OK end chars")
                    return(REGISTER, int(regstr))
                else:
                    self.error = "Error 21"
                    return self.handleError()
            else:
                self.error = "Error 22"
                return self.handleError()
        elif self.line[self.i] == 'm':
            self.i += 1
            if self.line[self.i] == 'u':
                self.i += 1
                if self.line[self.i] == 'l':
                    self.i += 1
                    if self.line[self.i] == 't':
                        self.i += 1
                        if self.line[self.i].isspace():
                            return (ARITHOP, MULT)
                        else:
                            self.error = "hit in mult"
                            return self.handleError()
                    else:
                        self.error = "Error 23"
                        return self.handleError()
                else:
                    self.error = "Error 24"
                    return self.handleError()
            else:
                self.error = "Error 25"
                return self.handleError()
        elif self.line[self.i] == 'a':
            self.i += 1
            if self.line[self.i] == 'd':
                self.i += 1
                if self.line[self.i] == 'd':
                    self.i += 1
                    if self.line[self.i].isspace():
                        return (ARITHOP, ADD)
                    else:
                        self.error = "Error 26"
                        return self.handleError()
                else:
                    self.error = "Error 27"
                    return self.handleError()
            else:
                self.error = "Error 28"
                return self.handleError()
        elif self.line[self.i] == 'n':
            self.i += 1
            if self.line[self.i] == 'o':
                self.i += 1
                if self.line[self.i] == 'p':
                    self.i += 1
                    if self.line[self.i].isspace():
                        return (NOP, NOP)
                    else:
                        self.error = "Error 29"
                        return self.handleError()
                else:
                    self.error = "Error 30"
                    return self.handleError()
            else:
                self.error = "Error 31"
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
                                    self.error = "Error 32"
                                    return self.handleError()
                            else:
                                self.error = "Error 33"
                                return self.handleError()
                        else:
                            self.error = "Error 34"
                            return self.handleError()
                    else:
                        self.error = "Error 35"
                        return self.handleError()
                else:
                    self.error = "Error 36"
                    return self.handleError()
            else:
                self.error = "Error 37"
                return self.handleError()
        elif self.line[self.i] == '=':
            self.i += 1
            if self.line[self.i] == '>':
                self.i += 1
                if self.line[self.i].isspace():
                    return (INTO, INTO)
            else:
                self.error = "Error 38"
                return self.handleError()
        elif self.line[self.i] == ',':
            self.i += 1
            return (COMMA, COMMA)
        elif self.line[self.i] == '/':
            self.i += 1
            if self.line[self.i] == '/':
                while self.i < len(self.line):
                    self.i += 1
                self.readLine()
                return (COMMENT, COMMENT)
        elif self.line[self.i] == '\n':
            self.readLine()
            return (EOL, EOL) 
        elif self.line[self.i] == ' ':
            self.i += 1
        elif ord(self.line[self.i]) <= 57 and ord(self.line[self.i]) >= 48:
            constr = ""
            while ord(self.line[self.i]) <= 57 and ord(self.line[self.i]) >= 48:
                constr = constr + self.line[self.i]
                self.i += 1
            if self.line[self.i].isspace() or self.line[self.i] == '=':
                return (CONSTANT, int(constr))
            else:
                # print("Constant testing broke at char " + self.line[self.i])
                return self.handleError()                 
        else:
            self.i += 1
            # print(self.line[self.i])
            self.error = "Error 40"
            return self.handleError()
    
        
    def handleError(self):
        errorstr = ""
        while not self.line[self.i].isspace():
            errorstr = errorstr + self.line[self.i]
            self.i += 1
        print("ERROR: not a valid string: " + errorstr)
        return (self.line[self.i], self.error)
    
    