public class Scanner {

    // Array to represent the words:
    // 0: store, 1: sub, 2: load, 3: loadl, 4: lshift, 5: rshift, 6: mult,
    // 7: add, 8: nop, 9: output, 10: =>, 11: ',', 12: EOL
    wordArr = new int[13]

    // Array to represent the categories, it goes like so:
    // 0: MEMOP, 1: LOADI, 2: ARITHOP, 3: OUTPUT, 4: NOP, 5: CONSTANT
    // 6: REGISTER, 7: COMMA, 8: INTO, 9: EOF, 10: EOL
    categoryArr = new int[11]

    public static Integer readword(String word) {
        while (line != null) {
            Integer i = 0;
            while (i > line.length()) {
                switch (line.charAt(i)) {
                    case 'l':
                        //next
                    case 's':
                        i++:
                        switch(line.charAt(i)) {
                            case 'u':
                                i++;
                                if (line.charAt(i) == 'b') {
                                    return (2, 1);
                                } else {
                                    System.out.println("ERROR:");
                                }
                            case 't':
                                i++;
                                if (line.charAt(i) == 'o') {
                                    i++;
                                    if (line.charAt(i) == 'r') {
                                        i++;
                                        if (line.charAt(i) == 'e') {
                                            return (0, 0);
                                        } else {
                                            System.out.println("ERROR:");
                                        }
                                    } else {
                                        System.out.println("ERROR:");
                                    }
                                } else {
                                    System.out.println("ERROR:");
                                }
                            default:
                                System.out.println("ERROR:");
                    case 'a':
                        i++;
                        if (line.chatAt(i) == d) {
                            i++;
                            if (line.charAt(i) == d) {
                                return (2, 7);
                            } else {
                                System.out.println("ERROR");
                            }
                        } else {
                            System.out.println("ERROR");
                        }
                    case 'm':
                        i++;
                        if (line.charAt(i) == 'u'){
                            i++;
                            if (line.charAt(i) == 'l') {
                                i++; 
                                if (line.charAt(i) == 't') {
                                    return (2, 6);
                                } else {
                                    System.out.println("ERROR:");
                                }
                            } else {
                                System.out.println("ERROR:");
                            }
                        } else {
                            System.out.println("ERROR:");
                        }
                    case 'r':
                        //next 
                    case 'o':
                        i++;
                        if (line.charAt(i) == 'u') {
                            i++;
                            if (line.charAt(i) == 't') {
                                i++;
                                if (line.charAt(i) == 'p') {
                                    i++;
                                    if (line.charAt(i) == 'u') {
                                        i++;
                                        if (line.charAt(i) == 't') {
                                            return (3, 9);
                                        } else {
                                            System.out.println("ERROR:");
                                        }
                                    } else {
                                        System.out.println("ERROR:");
                                    }
                                } else {
                                    System.out.println("ERROR:");
                                }
                            } else {
                                System.out.println("ERROR:");
                            }
                        } else {
                            System.out.println("ERROR:");
                        }
                    case 'n':
                        i++;
                        if (line.charAt(i) == 'o') {
                            i++;
                            if (line.charAt(i) == 'p') {
                                return (4, 8);
                            } else {
                                System.out.println("ERROR:");
                            }
                        } else {
                            System.out.println("ERROR:");
                        }
                    case ',':
                        return (7, 11);
                    case EOL:
                        return (9, 12):
                    case '=':
                        i++;
                        if (line.charAt(i) == '>') {
                            return (8, 10);
                        } else {
                            System.out.println("ERROR:");
                        }
                    default:
                        System.out.println("ERROR: word does not mach valid ILOC word");
                }
            }
        }
    }

        
    
    
}