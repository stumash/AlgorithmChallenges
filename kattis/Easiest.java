import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Easiest {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;

        try {
            while (!(line = br.readLine()).equals("0")) {
                System.out.println(getPFromN(Integer.parseInt(line)));
            } 
        } catch (Exception e) {
            System.out.println("Oopsie");
        }
    }

    // return the smallest p> where sumOfDigits(n*p)==sumOfDigits(n)
    public static int getPFromN(int n) {
        int nd = sumOfDigits(n);
        for (int p = 11;;p++) {
            if (sumOfDigits(n*p)==nd)
                return p;
        }
    }

    public static int sumOfDigits(int num) {
        int sum = 0;

        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }

        return sum;
    }
}
