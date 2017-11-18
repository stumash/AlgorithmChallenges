import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

// O(n log(n) + n m) -- can do better? (at best O(n m) but is it possible to avoid the sort?)
public class ClosestSums {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String currLine;
        int[] nums;
        int[] queries;
        int caseCount = 1;
        int currQuery, currSum, closestSum, left, right;

        try {
            while ((currLine = br.readLine()) != null) {
                System.out.println("Case " + (caseCount++) + ":");

                // read in data numbers. O(n)
                nums = new int[Integer.parseInt(currLine)];
                for (int i = 0; i < nums.length; i++)
                    nums[i] = Integer.parseInt(br.readLine());
                Arrays.sort(nums); // O(n log(n))

                // read in query numbers. O(m)
                queries = new int[Integer.parseInt(br.readLine())];
                for (int i = 0; i < queries.length; i++)
                    queries[i] = Integer.parseInt(br.readLine());

                // look for a closest sum for each query. O(n m)
                for (int i = 0; i < queries.length; i++) {

                    currQuery = queries[i];
                    left = 0; right = nums.length - 1;
                    closestSum = nums[left] + nums[right];

                    while (left < right) {
                        currSum = nums[left] + nums[right];

                        if (Math.abs(currSum - currQuery) < Math.abs(closestSum - currQuery))
                            closestSum  = currSum;

                        if (currSum > currQuery) {
                            right--;
                        } else if (currSum < currQuery) {
                            left++;
                        } else {
                            break;
                        }
                    }

                    System.out.println("Closest sum to " + currQuery + " is " + closestSum + ".");
                }
            }
        } catch(Exception e){
            e.printStackTrace();
        }
    }
}
