import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class PermutEncrypt {
    public static void main(String[] args) {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[] ekey; // encryption key
        String line; // temp var for each line read
        int rightPad; // # of spaces to right-pad input 
        char[] message; // holds string input as char array

        try {
            while (!(line = br.readLine()).equals("0")) {

               // load encryption key
                st = new StringTokenizer(line, " ");
                ekey = new int[Integer.parseInt(st.nextToken())];

                for (int i = 0; i < ekey.length; i++)
                    ekey[i] = Integer.parseInt(st.nextToken()) - 1;

               // load message
                line = br.readLine();

                if (line.length() % ekey.length == 0)
                    rightPad = 0;
                else
                    rightPad = ekey.length - line.length() % ekey.length;

                message = new char[line.length() + rightPad];

                for (int i = 0; i < line.length(); i++)
                    message[i] = line.charAt(i);
                for (int i = line.length(); i < message.length; i++)
                    message[i] = ' ';

               // encrypt and print message
                System.out.print("'");
               
                for (int i = 0; i < message.length; i++)
                    System.out.print(message[  ekey[i%ekey.length] +  i - i%ekey.length  ]);

                System.out.println("'");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
