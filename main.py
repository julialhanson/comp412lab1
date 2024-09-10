from sys import argv
from scanner import Scanner

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
    while nextWord[0] != 9:
        print(nextWord)
        nextWord = scanner.readWord()

def p_flag():
    print("P flag worked")


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
        p_flag()
    else:
        s_flag(filename)
        
if __name__ == "__main__":
    main()