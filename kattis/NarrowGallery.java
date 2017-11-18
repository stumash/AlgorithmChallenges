import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class NarrowGallery {

    // utiliities
    private static BufferedReader br;
    private static StringTokenizer st;
    private static String currLine;

    // algo variables
    private static int nrows; // number of rows in galleryInstance
    private static int nToRem; // number of rooms to remove from galleryInstance
    private static int[][] rooms; // 2D array to hold the art galleryInstance info
    private static int[][][] dp; // 3D array DP table

    /* The recurrence relation:
     *
     * dp[i][j][0] ≡ maxval of art galleryInstance of first i rows when removing a set
     *      of j rooms that doesn't include either rooms[i][0] or rooms[i][1]
     *             ≡ rooms[i][0] + rooms[i][1]
     *               + max(dp[i-1][j][0], dp[i-1][j][1], dp[i-1][j][2])
     *
     * dp[i][j][1] ≡ maxval of art galleryInstance of first i rows when removing a set
     *      of j rooms that includes rooms[i][0]
     *             ≡ rooms[i][1]
     *               + max(dp[i-1][j-1][0], dp[i-1][j-1][1])
     *
     * dp[i][j][2] ≡ maxval of art galleryInstance of first i rows when removing a set
     *      of j rooms that includes rooms[i][1]
     *             ≡ rooms[i][0]
     *               + max(dp[i-1][j-1][0], dp[i-1][j-1][2])
     */

    public static void main(String[] args) {
        br = new BufferedReader(new InputStreamReader(System.in));

        try {

            while (!(currLine = br.readLine()).equals("0 0")) {

                readNarrowArtGalleryInstance();

                dp = new int[nrows + 1][nToRem + 1][3];
                for (int row = 1; row < nrows + 1; row++)
                    for (int rem = 0; rem < nToRem + 1; rem++)
                        for (int nlr = 0; nlr < 3; nlr++)
                            dp[row][rem][nlr] = dp(row, rem, nlr);

                System.out.println(
                    max(dp[nrows][nToRem][0],dp[nrows][nToRem][1],dp[nrows][nToRem][2])
                );

                //printDP();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Computes the correct value for dp[row][rem][nlr] using recurrence from above
     * @param nlr the values 0,1,2 correspond to removing none, left, or right room
     */
    public static int dp(int row, int rem, int nlr) {
        if (rem > row)
            return 0;

        if (nlr == 0) {
            if (row == rem)
                return 0;

            return rooms[row][0] + rooms[row][1] +
                max(dp[row-1][rem][0],dp[row-1][rem][1],dp[row-1][rem][2]);
        } else {
            if (rem == 0)
                return 0;

            if (nlr == 1) {
                return rooms[row][1] + max(dp[row-1][rem-1][0],dp[row-1][rem-1][1]);
            } else {
                return rooms[row][0] + max(dp[row-1][rem-1][0],dp[row-1][rem-1][2]);
            }
        }
    }

    // HELPERS

    public static void readNarrowArtGalleryInstance() throws IOException {
        st = new StringTokenizer(currLine);
        nrows = Integer.parseInt(st.nextToken());
        nToRem = Integer.parseInt(st.nextToken());
        rooms = new int[nrows + 1][2];
        for (int i = 1; i <= nrows; i++) {
            st = new StringTokenizer(br.readLine());
            rooms[i][0] = Integer.parseInt(st.nextToken());
            rooms[i][1] = Integer.parseInt(st.nextToken());
        }
    }
    public static int max(int a, int b) {
        return (a > b)? a: b;
    }
    public static int max(int a, int b, int c) {
        int maxab = max(a,b);
        return (maxab > c)? maxab: c;
    }

    // FOR DEBUGGING

    public static void printDP() {
        for (int row = 0; row <= nrows; row++) {
            for (int x = 0; x < 3; x++) {
                for (int rem = 0; rem <= nToRem; rem++) {
                    System.out.print(dp[row][rem][x] + "\t");
                }
                System.out.print("\t\t");
            }
            System.out.println();
        }
        System.out.println();
    }
}
