import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import java.util.Iterator;
import java.util.LinkedList;

import java.io.IOException;

public class Orders {

    // necessary utilities
    private static BufferedReader br;
    private static StringTokenizer st;
    private static LinkedList<Integer> coinCombo;

    // algo variables
    private static int coins[]; // the coin values
    private static int prices[]; // the prices to make change for
    private static int[][] dp; // the dynamic programming table

    boolean first = true;

    public static void main(String[] args) {
        try {
            readProblemInstance();

            // use dynamic programming to solve coin change problem
            dp = new int[coins.length][maxOfArray(prices)+1];
            for (int i = 0; i < coins.length; i++)
                dp[i][0] = 1;
            for (int price = 1; price < dp[0].length; price++)
                for (int coin = 0; coin < dp.length; coin++)
                    dp[coin][price] = dp(coin,price);

            // output change for each price
            for (int price : prices) {
                if (dp[coins.length-1][price] < 1 )
                    System.out.println("Impossible");
                else if (dp[coins.length-1][price] > 1)
                    System.out.println("Ambiguous");
                else {
                    coinCombo = new LinkedList<Integer>();
                    getCoinCombo(coins.length - 1, price);
                    Iterator<Integer> iter = coinCombo.iterator();
                    while (iter.hasNext())
                        System.out.print(iter.next() + " ");
                    System.out.println();
                }
            }
        } catch(Exception e){
            e.printStackTrace();
        }
    }

    private static int dp(int coin, int price) {
        int sum = 0;
        if (coin - 1 >= 0)
            sum += dp[coin - 1][price];
        if (price - coins[coin] >= 0)
            sum += dp[coin][price - coins[coin]];
        if (sum > 1) sum = 2;
        return sum;
    }

    private static void getCoinCombo(int coin, int price) {
        while (coin >= 0 && price >= 0) {
            if (coin-1 >= 0 && dp[coin-1][price] == 1)
                coin--;
            else if (price-coins[coin] >= 0 && dp[coin][price-coins[coin]] == 1) {
                price -= coins[coin];
                coinCombo.addFirst(coin + 1);
            }else
                break;
        }
    }

    // helpers
    private static void readProblemInstance() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        // read coins from input
        coins = new int[Integer.parseInt(br.readLine())];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < coins.length; i++)
            coins[i] = Integer.parseInt(st.nextToken());

        // read prices from input
        prices = new int[Integer.parseInt(br.readLine())];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < prices.length; i++)
            prices[i] = Integer.parseInt(st.nextToken());
    }
    private static int maxOfArray(int[] arr) {
        int max = 0;
        for (int elem : arr)
            if (elem > max) max = elem;
        return max;
    }

    // for debugging
    private static void printArray(int[] arr) {
        if (arr.length > 0) System.out.print(arr[0]);
        for (int i = 1; i < arr.length; i++)
            System.out.print("\t" + arr[i]);
        System.out.println();
    }
    private static void printIndices(int[] arr) {
        if (arr.length > 0) System.out.print(0);
        for (int i = 1; i < arr.length; i++)
            System.out.print("\t" + i);
        System.out.println();
    }
}
