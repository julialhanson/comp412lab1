from sys import argv
from scanner import Scanner


# Constants from other file
SUB = 3
STORE = 4
LOAD = 5
# INTO, COMMA, EOL, EOF shared
LSHIFT = 10
RSHIFT = 14
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


class IRNode:
    def __init__(self, opcode, sr1, sr2, sr3) -> None:
        self.opcode = opcode
        self.sr1 = sr1
        self.sr2 = sr2
        self.sr3 = sr3
        self.prev = None
        self.next = None
        
        pass
def parseLine(linelst):
    word = scanner.readWord()
    
    while word != (9, "EOF"):
        opcode = ""
        sr1 = ""
        sr2 = ""
        sr3 = ""
        if word[0] == MEMOP:
            opcode = Scanner.categoryArr[word[1]]
            word = Scanner.readWord()
            if word[0] == REGISTER:
                self.sr1 = "sr" + str(word[1])
                word = Scanner.readWord()
                if word[0] == INTO:
                    word = Scanner.readWord()
                    if word[0] == REGISTER:
                        self.sr3 = "sr" + str(word[1])
                        word = Scanner.readWord()
                        if word[0] == EOL:
                            newIR = IRNode(opcode, sr1, sr2, sr3)
                            return (opcode, sr1, sr2, sr3)
                        else:
                            print("ERROR: Extra words in " + str(opcode) + " operation")
                            return(ERROR, ERROR)
                    else:
                        print("ERROR: Missing second source register in " + str(opcode))
                        return(ERROR, ERROR)
                else:
                    print("ERROR: Missing '=>' in " + str(opcode))
                    return(ERROR, ERROR)
            else:
                print("ERROR: missing first source register in " + str(opcode))
                return(ERROR, ERROR)
        elif word[0] == LOADI:
            opcode = Scanner.categoryArr[word[1]]
            word = Scanner.readWord()
            if word[0] == CONSTANT:
                sr1 = "val " + str(word[1])
                word = Scanner.readWord()
                if word[0] == INTO:
                    word = Scanner.readWord()
                    if word[0] == REGISTER:
                        sr3 = "sr" + str(word[1])
                        word = Scanner.readWord()
                        if word[0] == EOL:
                            return (opcode, sr1, sr2, sr3)
                        else:
                            print("ERROR: Extra words in " + str(opcode) + " operation")
                            return(ERROR, ERROR)
                    else:
                        print("ERROR: Missing second source register in " + str(opcode))
                        return(ERROR, ERROR)
                else:
                    print("ERROR: Missing '=>' in " + str(opcode))
                    return(ERROR, ERROR)
            else:
                print("ERROR: missing first source register in " + str(opcode))
                return(ERROR, ERROR)
        elif word[0] == ARITHOP:
            opcode = Scanner.categoryArr[word[1]]
            word = Scanner.readWord()
            if word[0] == REGISTER:
                sr1 = "sr" + str(word[1])
                word = Scanner.readWord()
                if word[0] == COMMA:
                    word = Scanner.readWord()
                    if word[0] == REGISTER:
                        sr2 = "sr" + str(word[1])
                        word = Scanner.readWord()
                        if word[0] == INTO:
                            word = Scanner.readWord()
                            if word[0] == REGISTER:
                                sr3 = "sr" + str(word[1])
                                word = Scanner.readWord()
                                if word[0] == EOL:
                                    return (opcode, sr1, sr2, sr3)
                                else:
                                    print("ERROR: Extra words in " + str(self.opcode) + " operation")
                                    return(ERROR, ERROR)
                            else:
                                print("ERROR: Missing third source register in +" + opcode)
                                return(ERROR, ERROR)
                        else:
                            print("ERROR: Missing '=>' in " + opcode)
                            return(ERROR, ERROR)
                    else:
                        print("ERROR: Missing second source register in" + opcode)
                        return(ERROR, ERROR)
                else:
                    print("ERROR: Missing comma in " + opcode)
                    return(ERROR, ERROR)
            else:
                print("ERROR: Missing first source register in " + opcode)
                return(ERROR, ERROR)
        elif word[0] == OUTPUT:
            opcode = Scanner.categoryArr[word[1]]
            word = Scanner.readWord()
            if word[0] == CONSTANT:
                sr1 = "val " + str(word[1])
                word = Scanner.readWord()
                if word[0] == EOL:
                    return (opcode, sr1, sr2, sr3)
                else:
                    print("ERROR: Extra words in " + str(self.opcode) + " operation")
                    return(ERROR, ERROR)
            else:
                print("ERROR: Missing constant in " + opcode)
                return(ERROR, ERROR)
        elif word[0] == NOP:
            opcode = Scanner.categoryArr[word[1]]
            word = Scanner.readWord()
            if word[0] == EOL:
                return (opcode, sr1, sr2, sr3)
            else:
                print("ERROR: Extra words in " + str(self.opcode) + " operation")
                return(ERROR, ERROR)
        elif word[0] == ERROR:
            return ("ERROR: Semantic error")
            
            
def h_flag(filename):
    print("Valid Command Line Arguments:")
    print("\n")
    print("Filename: " + filename)
    print("-h: produces a list of valid command-line arguments and includes descriptions of all command-line arguments")
    print("-r: reads the file specified by <name>, scans, parses, builds the IR, and prints the information in the IR")
    print("-p: the default behavior, reads the file specified by <name>, scans, parses, builds the IR, and reports success or errors found in the input file. If the parse succeeds, the front end must report “Parse succeeded. Processed k operations.”, where k is the number of operations the front end handled, printed without commas. If it finds errors, it must print “Parse found errors.”")
    print("-s: reads the file specified by <name> and prints a list of the tokens that the scanner found to the standard output stream")


def s_flag(filename):
    print("S flag flagged")
    scanner = Scanner(filename)
    scanner.readLine()
    nextWord = scanner.readWord()
    while nextWord != (9,'EOF'):
        if (nextWord[0] == CONSTANT or nextWord[0] == REGISTER):
            print("Line " + str(scanner.linenum) + ": [" + scanner.categoryArr[nextWord[0]] + ", " + str(nextWord[1]) + "]")
        elif (nextWord[0] != ERROR):
            print("Line " + str(scanner.linenum) + ": [" + scanner.categoryArr[nextWord[0]] + ", " + scanner.wordArr[nextWord[1]] + "]")
        nextWord = scanner.readWord()

def p_flag(filename):
    scanner = Scanner(filename)
    scanner.readLine()
    nextWord = scanner.readWord()
    while nextWord != (9, "EOF"):
        
        parseLine(nextWord)
        

def r_flag():
    print("R flag worked")
    

def main ():
    argslst = argv
    filename = argslst[-1]
    if len(argslst) > 3:
        print("ERROR: more than one flag present. Highest priority flag will be implemented")
    if "-h" in argslst:
        h_flag(filename)
    elif "-r" in argslst:
        r_flag()
    elif "-p" in argslst:
        p_flag(filename)
    else:
        s_flag(filename)
        
if __name__ == "__main__":
    main()
    
    
