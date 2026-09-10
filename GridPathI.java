import java.io.BufferedInputStream;
import java.io.IOException;

public class GridPathI {

    private static final long MOD = 1_000_000_007L;
    
    public static void main(String[] args) throws IOException {

        
        FastInput input = new FastInput();

        int n = input.nextInt();
        char[][] grid = new char[n][n];

        for (int i = 0; i < n; i++) {
            grid[i] = input.next().toCharArray();
        }

        long[][] dp = new long[n][n];

        for (int row = 0; row < n; row++) {
            java.util.Arrays.fill(dp[row], -1);
        }

        long result = computePaths(grid, dp, n - 1, n - 1);
        System.out.println(result);
    }

    private static long computePaths(
            char[][] grid,
            long[][] dp,
            int row,
            int column
    ) {
        if (row < 0 || column < 0) {
            return 0;
        }

        if (dp[row][column] != -1) {
            return dp[row][column];
        }

        if (grid[row][column] == '*') {
            dp[row][column] = 0;
            return 0;
        }

        if (row == 0 && column == 0) {
            dp[row][column] = 1;
            return 1;
        }

        long fromAbove = computePaths(grid, dp, row - 1, column);
        long fromLeft = computePaths(grid, dp, row, column - 1);

        dp[row][column] = (fromAbove + fromLeft) % MOD;
        return dp[row][column];
    }

    private static class FastInput {
        private final BufferedInputStream input =
                new BufferedInputStream(System.in);

        private final byte[] buffer = new byte[1 << 16];
        private int pointer = 0;
        private int length = 0;

        private int read() throws IOException {
            if (pointer >= length) {
                length = input.read(buffer);
                pointer = 0;

                if (length == -1) {
                    return -1;
                }
            }

            return buffer[pointer++];
        }

        String next() throws IOException {
            StringBuilder value = new StringBuilder();
            int character;

            do {
                character = read();
            } while (character <= ' ');

            while (character > ' ') {
                value.append((char) character);
                character = read();
            }

            return value.toString();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }
}