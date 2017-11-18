import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Peragrams {

    private static final int ASCII_a = 97;

    public static void main(String[] args) {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] charCount; // # of times each char occurs in input string
        String line; // String to hold each line of input
        int oddCount; // number of chars in input string that occur odd # of times

        try {
            while ((line = br.readLine()) != null) {

                // handle empty String -- not defined as necessary by problem description
                if (line.length() == 0) {
                    System.out.println();
                    continue;
                }

                // one count of occurence for each letter of alphabet
                charCount = new int[26]; // initialized to 0

                // loop through line recording charCounts
                for (int i = 0; i < line.length(); i++) {
                    charCount[line.charAt(i) - ASCII_a]++; // ascii for 'a' is 
                }

                // count number of letters with odd # of occurences
                oddCount = 0;
                for (int i = 0; i < charCount.length; i++) {
                    if (charCount[i] % 2 != 0) oddCount++;
                }

                if (oddCount <= 1)
                    System.out.println(0);
                else
                    System.out.println(oddCount - 1);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
