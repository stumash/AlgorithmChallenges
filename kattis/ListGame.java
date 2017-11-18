import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ListGame {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            int n = Integer.parseInt(br.readLine());
            System.out.println(k(n));
        } catch(Exception e){
            e.printStackTrace();
        }
    }
    private static int k(int n) {
        int count = 0;
        boolean composite = true;
        outer:
        while (composite) {
            for (int i = 2; i <= (int)Math.sqrt(n); i++) {
                if (n % i == 0) {
                    count++;
                    n /= i;
                    continue outer;
                }
            }
            composite = false;
        }
        return count + 1;
    }
}
