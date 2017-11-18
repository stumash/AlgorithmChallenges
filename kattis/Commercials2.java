import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class AnotherWay {
    public static void main(String[] args) {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String currLine;
        StringTokenizer st;

        int numBreaks; // number of commercial breaks in a day
        int breakPrice; // price of one commercial break
        int[] profitPerBreak; // profit, in swedish crowns, per commercial break
        int max, prev; // for use in maximum subarray problem

        try {
            while ((currLine = br.readLine()) != null) {

                // read in numBreaks and breakPrice
                st = new StringTokenizer(currLine);
                numBreaks = Integer.parseInt(st.nextToken());
                breakPrice = Integer.parseInt(st.nextToken());

                // read in profit per break which is revenue per break - break price
                st = new StringTokenizer(currLine = br.readLine());
                profitPerBreak = new int[numBreaks];
                for (int i = 0; i < profitPerBreak.length; i++)
                    profitPerBreak[i] = Integer.parseInt(st.nextToken()) - breakPrice;

                // maximum subarray problem
                max = 0; prev = profitPerBreak[0];
                for (int i = 1; i < profitPerBreak.length; i++) {

                }

                System.out.println(max);
            }
        } catch(Exception e){
            e.printStackTrace();
        }
    }
}
