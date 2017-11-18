import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class SortOfSorting {

    public static void main(String[] args) {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<String> strings;
        String line;
        int size;

        try {
            while (!(line = br.readLine()).equals("0")) {

                size = Integer.parseInt(line);
                strings = new ArrayList<String>(size);

                for (int i = 0; i < size; i++)
                    strings.add(i, br.readLine());

                // Collections.sort is stable (mergesort)
                Collections.sort(strings, new Comparator<String>() {
                    @Override
                    public int compare(String a, String b) {
                        if (a.charAt(0) == b.charAt(0))
                            return a.charAt(1) - b.charAt(1);
                        else
                            return a.charAt(0) - b.charAt(0);
                    }
                });

                for (String s : strings)
                    System.out.println(s);

                System.out.println();
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
