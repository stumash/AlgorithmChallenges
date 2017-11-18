import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * This code solves the problem at
 * https://open.kattis.com/problems/numbertree
 */

public class NumberTree {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = "";
        try { 
            while ((line = br.readLine()) != null) {
                String[] inputTokens = line.split(" ");

                long bh1 = (long)Math.pow(2, Integer.parseInt(inputTokens[0]) + 1); 
                long nodeLabel = 1;

                if (inputTokens.length > 1) {
                    String path = inputTokens[1];
                    for (int i = 0; i < path.length(); i++) {
                        nodeLabel *= 2;
                        if (path.charAt(i) == 'R') {
                            nodeLabel++;
                        }
                    }
                }
                System.out.println(bh1 - nodeLabel);
            }
        } catch(Exception e) { 
            e.printStackTrace();
        }
    }
}

/* ALGORITHM DESCRIPTION:
 * 
 * For the two trees below:
 *                          height
 *                         ---------
 *              3                                3
 *
 *                          root at
 *                        ------------
 *              1                                15
 *
 *                     increase direction
 *                    ---------------------
 *          top down                         bottom up
 *       left to right                     right to left
 *
 */
/*              1                               15
 *          /       \                        /      \
 *      2               3                14            13 
 *    /   \           /   \            /    \        /    \
 *   4     5         6     7         12      11    10      9
 *  8 9  10 11     12 13 14 15      8  7    6  5  4  5    2  1 
 */
/* In the left tree, if you're at node x and you go left:
 *      You'll be at node x*2
 * But if, at x, you go right:
 *      You'll be at node (x*2)+1
 */
/* Whatever node l you're at in the left tree, the node r you'd
 * be at in the right tree is defined as:
 *                            r = 16 - l
 * where 16 is
 *                        2 ^ (treeHeight + 1)
 */
