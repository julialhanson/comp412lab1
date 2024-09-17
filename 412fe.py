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

errorflag = False
wordArr = ["loadI", "nop", "output", "sub", "store", "load", "=>", ',', "\\n",  "", "lshift", "COMMENT", "mult", "add", "rshift"]


class IRNode:
    def __init__(self, linenum, sr1: int = None, sr2: int = None, sr3: int = None) -> None:
        self.linenum = linenum
        self.opcode = 0
        self.sr1 = sr1
        self.sr2 = sr2
        self.sr3 = sr3
        self.prev = self
        self.next = self
        pass
    
    def getOpcode(self):
        return self.opcode
    
    def insertAfter(self, node):
        self.next.prev = node
        node.next = self.next
        node.prev = self
        self.next = node
        
    def __str__(self) -> str:
        return f"{wordArr[self.opcode]}     [{self.sr1}], [{self.sr2}], [{self.sr3}]"
        pass
        
def parseLine(scanner):
    word = scanner.readWord()
    
    while word[0] == EOL:
        word = scanner.readWord()
        
    node = IRNode(scanner.getLine())
    
    if word[0] == MEMOP:
        node.opcode = word[1]
        word = scanner.readWord()
        if word[0] == REGISTER:
            node.sr1 = word[1]
            word = scanner.readWord()
            if word[0] == INTO:
                word = scanner.readWord()
                if word[0] == REGISTER:
                    node.sr3 = word[1]
                    word = scanner.readWord()
                    if word[0] == EOL:
                        return node
                    else:
                        print("ERROR " + str(node.linenum) + ": Extra words in " + scanner.wordArr[node.opcode] + " operation")
                        node.opcode = ERROR
                        errorFlag = True
                        return node
                else:
                    print("ERROR " + str(node.linenum) + ": Missing second source register in " + scanner.wordArr[node.opcode])
                    node.opcode = ERROR
                    errorFlag = True
                    return node
            else:
                print("ERROR " + str(node.linenum) + ":  Missing '=>' in " + scanner.wordArr[node.opcode])
                node.opcode = ERROR
                errorFlag = True
                return node
        else:
            print("ERROR " + str(node.linenum) + ": missing first source register in " + scanner.wordArr[node.opcode])
            node.opcode = ERROR
            errorFlag = True
            return node
    elif word[0] == LOADI:
        node.opcode = word[1]
        word = scanner.readWord()
        if word[0] == CONSTANT:
            node.sr1 = word[1]
            word = scanner.readWord()
            if word[0] == INTO:
                word = scanner.readWord()
                if word[0] == REGISTER:
                    node.sr3 = word[1]
                    word = scanner.readWord()
                    if word[0] == EOL:
                        return (node)
                    else:
                        print("ERROR " + str(node.linenum) + ": Extra words in " + scanner.wordArr[node.opcode] + " operation")
                        node.opcode = ERROR
                        errorFlag = True
                        return node
                else:
                    print("ERROR " + str(node.linenum) + ": Missing second source register in " + scanner.wordArr[node.opcode])
                    node.opcode = ERROR
                    errorFlag = True
                    return node
            else:
                print("ERROR " + str(node.linenum) + ": Missing '=>' in " + scanner.wordArr[node.opcode])
                node.opcode = ERROR
                errorFlag = True
                return node
        else:
            print("ERROR " + str(node.linenum) + ": missing first source register in " + scanner.wordArr[node.opcode])
            node.opcode = ERROR
            errorFlag = True
            return node
    elif word[0] == ARITHOP:
        node.opcode = word[1]
        word = scanner.readWord()
        if word[0] == REGISTER:
            node.sr1 = word[1]
            word = scanner.readWord()
            if word[0] == COMMA:
                word = scanner.readWord()
                if word[0] == REGISTER:
                    node.sr2 = word[1]
                    word = scanner.readWord()
                    if word[0] == INTO:
                        word = scanner.readWord()
                        if word[0] == REGISTER:
                            node.sr3 = word[1]
                            word = scanner.readWord()
                            if word[0] == EOL:
                                return (node)
                            else:
                                print("ERROR " + str(node.linenum) + ": Extra words in " + scanner.wordArr[node.opcode] + " operation")
                                node.opcode = ERROR
                                errorFlag = True
                                return node
                        else:
                            print("ERROR " + str(node.linenum) + ": Missing third source register in +" + scanner.wordArr[node.opcode])
                            node.opcode = ERROR
                            errorFlag = True
                            return node
                    else:
                        print("ERROR " + str(node.linenum) + ": Missing '=>' in " + scanner.wordArr[node.opcode])
                        node.opcode = ERROR
                        errorFlag = True
                        return node
                else:
                    print("ERROR " + str(node.linenum) + ": Missing second source register in" + scanner.wordArr[node.opcode])
                    node.opcode = ERROR
                    errorFlag = True
                    return node
            else:
                print("ERROR " + str(node.linenum) + ": Missing comma in " + scanner.wordArr[node.opcode])
                node.opcode = ERROR
                errorFlag = True
                return node
        else:
            print("ERROR " + str(node.linenum) + ": Missing first source register in " + scanner.wordArr[node.opcode])
            node.opcode = ERROR
            errorFlag = True
            return node
    elif word[0] == OUTPUT:
        node.opcode = word[1]
        word = scanner.readWord()
        if word[0] == CONSTANT:
            node.sr1 = word[1]
            word = scanner.readWord()
            if word[0] == EOL:
                return node
            else:
                print("ERROR " + str(node.linenum) + ": Extra words in " + scanner.wordArr[node.opcode] + " operation")
                node.opcode = ERROR
                errorFlag = True
                return node
        else:
            print("ERROR " + str(node.linenum) + ": Missing constant in " + scanner.wordArr[node.opcode])
            node.opcode = ERROR
            errorFlag = True
            return node
    elif word[0] == NOP:
        node.opcode = word[1]
        word = scanner.readWord()
        if word[0] == EOL:
            return (node)
        else:
            print("ERROR " + str(node.linenum) + ": Extra words in " + scanner.wordArr[node.opcode] + " operation")
            node.opcode = ERROR
            errorFlag = True
            return node
    elif word[0] == EOF:
        node.opcode = EOF
        return node
    elif word[0] == ERROR:
        # We don't print errors twice
        node.opcode = ERROR
        errorFlag = True
        return node
    else:
        print("ERROR  " + str(node.linenum) + ": Invalid starting part of speech, " + scanner.categoryArr[word[0]])
        node.opcode = ERROR
        errorFlag = True
        return node
    
            
            
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
    while not scanner.getEOF():
        if (nextWord[0] == CONSTANT or nextWord[0] == REGISTER):
            print("Line " + str(scanner.linenum) + ": [" + scanner.categoryArr[nextWord[0]] + ", " + str(nextWord[1]) + "]")
        elif (nextWord[0] != ERROR):
            print("Line " + str(scanner.linenum) + ": [" + scanner.categoryArr[nextWord[0]] + ", " + scanner.wordArr[nextWord[1]] + "]")
        nextWord = scanner.readWord()
    # print eof
    print("Line " + str(scanner.linenum) + ": [" + scanner.categoryArr[nextWord[0]] + ", " + scanner.wordArr[nextWord[1]] + "]")


def p_flag(filename):
    scanner = Scanner(filename)
    scanner.readLine()
    ir = parseLine(scanner)
    opcount = 0
    is_error = False
    while not scanner.getEOF():
        if ir.getOpcode() != ERROR:
            opcount += 1
        else:
            is_error = True
        ir = parseLine(scanner)
        
    if is_error == True:
        print("Parser found errors.")
    else:
        print("Parse succeeded. Processed " + str(opcount) + " operations.")
        

def r_flag(filename):
    scanner = Scanner(filename)
    scanner.readLine()
    ir = parseLine(scanner)

    is_error = False
    head = IRNode(-1)
    
    while not scanner.getEOF():
        if ir.getOpcode() != ERROR:
            head.prev.insertAfter(ir)
            
        else:
            is_error = True
        ir = parseLine(scanner)
        
    if is_error == True:
        print("Due to syntax errors, run terminates.")
    else:
        node = head
        while (node.next != head):
            print(node.next)
            node = node.next
    
    

def main ():
    argslst = argv
    filename = argslst[-1]
    if len(argslst) > 3:
        print("ERROR: more than one flag present. Highest priority flag will be implemented")
    if "-h" in argslst:
        h_flag(filename)
    elif "-r" in argslst:
        r_flag(filename)
    elif "-p" in argslst:
        p_flag(filename)
    else:
        s_flag(filename)
        
if __name__ == "__main__":
    main()
    
    
