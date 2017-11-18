import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Oddities {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        try {
            String line = br.readLine();
            while ((line = br.readLine()) != null) {
                if (Integer.parseInt(line) % 2 == 0) {
                    System.out.println(line + " is even");
                } else {
                    System.out.println(line + " is odd");
                }
            }
        } catch (Exception e) {
            System.out.println("Oopsie");
        }
    }
}
