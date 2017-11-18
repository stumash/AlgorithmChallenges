import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.ArrayDeque;
import java.util.Collections;

public class GuessTheDataStructure {

    public static void main(String[] args) {

        boolean canBeStack;
        boolean canBeQueue;
        boolean canBePriQueue;

        ArrayDeque<Integer> s;
        ArrayDeque<Integer> q;
        PriorityQueue<Integer> pq;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = null;
        String[] tokens = null;
        int numOps;

        try {
            while ( (line = br.readLine()) != null ) {

                numOps = Integer.parseInt(line);

                canBeStack = true;
                canBeQueue = true;
                canBePriQueue = true;

                s = new ArrayDeque<Integer>();
                q = new ArrayDeque<Integer>();
                pq = new PriorityQueue<Integer>(8, Collections.reverseOrder()); //maxheap, not default minheap

                for (int i = 0; i < numOps; i++) {

                    line = br.readLine();
                    tokens = line.split(" ");

                    if (tokens[0].equals("1")) { //if insert operation, insert into all dstructs
                        if (canBeStack)
                            s.push(Integer.parseInt(tokens[1]));
                        if (canBeQueue)
                            q.addFirst(Integer.parseInt(tokens[1]));
                        if (canBePriQueue)
                            pq.add(Integer.parseInt(tokens[1]));
                    } else { //if remove operation, check if datastructs are empty or wrong
                        if (s.isEmpty() || !s.pop().equals(Integer.parseInt(tokens[1])))
                            canBeStack = false;
                        if (q.isEmpty() || !q.removeLast().equals(Integer.parseInt(tokens[1])))
                            canBeQueue = false;
                        if (pq.isEmpty() || !pq.poll().equals(Integer.parseInt(tokens[1])))
                            canBePriQueue = false;
                    }
                }

                output(canBeStack, canBeQueue, canBePriQueue);
            }
        } catch (Exception e) {
            System.out.println("Oopsie");
        }
    }

    private static void output(boolean canBeStack, boolean canBeQueue, boolean canBePriQueue) {
        if (canBeStack || canBeQueue || canBePriQueue) {
            if (canBeStack) {
                if (canBeQueue || canBePriQueue) {
                    System.out.println("not sure");
                } else {
                    System.out.println("stack");
                }
            } else if (canBeQueue) {
                if (canBePriQueue) {
                    System.out.println("not sure");
                } else {
                    System.out.println("queue");
                }
            } else {
                System.out.println("priority queue");
            }
        } else {
            System.out.println("impossible");
        }
    }
}
