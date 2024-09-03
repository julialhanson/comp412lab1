
import java.util.HashSet;


public class Main {
    static String filename;
    public static void main(String[] args){
        String filename = args[0];
        if (args.length > 2) {
            System.out.println("ERROR: more than one flag present. Highest priority flag will be implemented");
            HashSet <String> commandset = new HashSet<String>(args);
            if (commandset.contains("-h")) {
                h_flag();
            } else if (commandset.contains("-r")) {
                r_flag();
            } else if (commandset.contains("-p")) {
                p_flag();
            } else {
                s_flag();
            }
        }
    }
    
    public static void h_flag() {
        System.out.println("Valid Command Line Arguments:");
        System.out.println("\n");
        System.out.println("Filename: " + filename);
        System.out.println("-h: produces a list of valid command-line arguments and includes descriptions of all command-line arguments");
        System.out.println("-r: reads the file specified by <name>, scans, parses, builds the IR, and prints the information in the IR");
        System.out.println("-p: the default behavior, reads the file specified by <name>, scans, parses, builds the IR, and reports success or errors found in the input file. If the parse succeeds, the front end must report “Parse succeeded. Processed k operations.”, where k is the number of operations the front end handled, printed without commas. If it finds errors, it must print “Parse found errors.”");
        System.out.println("-s: reads the file specified by <name> and prints a list of the tokens that the scanner found to the standard output stream");
    }

    public static void s_flag() {
        System.out.println("S flag flagged");
    }

    public static void p_flag() {
        System.out.println("P flag worked");
    }

    public static void r_flag() {
        System.out.println("R flag worked");
    }
    

}