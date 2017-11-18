import java.io.BufferedReader;
import java.io.InputStreamReader;

public class EightQueens {

    private static BufferedReader br;
    private static String currLine;

    private static boolean[][] board;

    public static void main(String[] args) {
        readInput();
        //printBoard();
        if(boardValid())
            System.out.println("valid");
        else
            System.out.println("invalid");
    }

    private static boolean boardValid() {
        int queenCount = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if(board[i][j]) {
                    queenCount++;
                    if(!queenValid(i,j)) {
                        return false;
                    }
                }
            }
        }
        if (queenCount != 8)
            return false;
        return true;
    }

    private static boolean queenValid(int i, int j) {
        int row, col;
        //look right
        col = j+1;
        while (col < 8) {
            if (board[i][col]) {
                //System.out.println("right: col " + col);
                return false;
            }
            col++;
        }
        // look down
        row = i+1;
        while (row < 8) {
            if (board[row][j]) {
                //System.out.println("down: row " + row);
                return false;
            }
            row++;
        }
        // look diag down+right
        row = i+1; col = j+1;
        while (row < 8 && col < 8) {
            if (board[row][col]) {
                //System.out.println("botright: " + row + "," + col);
                return false;
            }
            row++; col++;
        }
        // look diag down+left
        row = i+1; col = j-1;
        while (row < 8 && col > -1) {
            if (board[row][col]) {
                //System.out.println("botleft: " + row + "," + col);
                return false;
            }
            row++; col--;
        }
        return true;
    }

    private static void readInput() {
        br = new BufferedReader(new InputStreamReader(System.in));
        board = new boolean[8][8];
        for (int i = 0; i < 8; i++) {
            try { currLine = br.readLine(); } catch (Exception e) { e.printStackTrace(); }
            for (int j = 0; j < 8; j++) {
                board[i][j] = (currLine.charAt(j) == '*')? true: false;
            }
        }
        try { br.close(); } catch (Exception e) { e.printStackTrace(); }
    }

    private static void printBoard() {
        for (int i = 0; i < 8; i++) {
            System.out.print(i);
            for (int j = 0; j < 8; j++) {
                if (board[i][j])
                    System.out.print('X');
                else
                    System.out.print('-');
            }
            System.out.println();
        }
        System.out.print(' ');
        for (int i = 0; i < 8; i++) {
            System.out.print(i);
        }
        System.out.println();
    }
}
