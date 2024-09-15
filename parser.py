import io
import sys
from scanner import Scanner

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

linecount = 1

class Irepresentation():
    def __init__(self) -> None:
        self.head = None
    
    def createIR(self):
        self.line = linecount
        self.opcode = 0
        self.sr1 = 0
        self.vr1 = 0
        self.pr1 = 0
        self.nu1 = 0
        self.sr2 = 0
        self.vr2 = 0
        self.pr2 = 0
        self.nu2 = 0
        self.sr3 = 0
        self.vr3 = 0
        self.pr3 = 0
        self.nu3 = 0
        
        
    
def parseLine():
    word = Scanner.readWord()
    
    while word != (9, "EOF"):
        if word[0] == MEMOP:
            word = scanner.readWord()
            if word[0] == REGISTER:
                word = scanner.readWord()
                if word[0] == INTO:
                    word = scanner.readWord()
                    if word[0] == REGISTER:
                        self.opcode = 4
                        self.sr1 = 2
                        self.createIR
                    else:
                        throw
                else:
                    throw
            else:
                throw
        elif word[0] == LOADI:
            word = scanner.readWord()
            if word[0] == CONSTANT:
                const = word[1]
                word = scanner.readWord()
                if word[0] == INTO:
                    word = scanner.readWord()
                    if word[0] == REGISTER:
                        reg = word[1]
                        return(0,0)
                    else:
                        throw
                else:
                    throw
            else:
                throw
        elif word[0] == ARITHOP:
            word = scanner.readWord()
            if word[0] == REGISTER:
                word = scanner.readWord()
                if word[0] == COMMA:
                    word = scanner.readWord()
                    if word[0] == REGISTER:
                        word = scanner.readWord()
                        if word[0] == INTO:
                            word = scanner.readWord()
                            if word[0] == REGISTER:
                                createIR()
                                return
                            else:
                                throw
                        else:
                            throw
                    else:
                        throw
                else:
                    throw
            else:
                throw
        elif word[0] == OUTPUT:
            word = scanner.readWord()
            if word[0] == CONSTANT:
                createIR()
                return
            else:
                throw
        elif word[0] == NOP:
            createIR()
            return
                    
                
                 
                
            