import java.io.BufferedInputStream;
import java.io.IOException;

public class MissingNumber {
    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();

        int n = input.nextInt();
        int missing = n;

        for (int number = 1; number < n; number++) {
            missing ^= number;
            missing ^= input.nextInt();
        }

        System.out.println(missing);
    }

    private static class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in);
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

        int nextInt() throws IOException {
            int value = 0;
            int character;

            do {
                character = read();
            } while (character <= ' ');

            while (character > ' ') {
                value = value * 10 + character - '0';
                character = read();
            }

            return value;
        }
    }
}