public class PredictTheWinner {

    int[] nums;
    int len;

    public boolean PredictTheWinner(int[] nums) {
        if (nums == null || nums.length == 0) { return false; }

        this.nums = nums;
        this.len = nums.length;

        return run(0, 0, this.len-1, 0);
    }

    /**
     * @param d, the current depth in the game tree
     * @param l, the leftmost index of subarray under consideration
     * @param r, the rightmost index of subarray under consideration
     * @param v, the current value of the game
     * @return boolean true if player1 wins game subtree
     */
    public boolean run(int d, int l, int r, int v) {
        boolean p1turn = (d % 2 == 0);  //is it player1's turn?
        if (d == this.len) { //base case
            return v >= 0;
        } else { //induction case
            boolean leftWin, rightWin;
            if (p1turn) {
                leftWin  = run(d+1, l+1, r  , v + this.nums[l]);
                rightWin = run(d+1, l  , r-1, v + this.nums[r]);
                return leftWin || rightWin;
            } else {
                leftWin  = run(d+1, l+1, r  , v - this.nums[l]);
                rightWin = run(d+1, l  , r-1, v - this.nums[r]);
                return leftWin && rightWin;
            }
        }
    }

    public static void main(String[] args) {
        int[] inputNums = new int[args.length];
        for (int i = 0; i < args.length; i++) {
            inputNums[i] = Integer.parseInt(args[i]);
        }

        PredictTheWinner ptw = new PredictTheWinner();
        System.out.println(ptw.PredictTheWinner(inputNums));
    }
}
