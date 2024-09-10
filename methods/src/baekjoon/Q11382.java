package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class Q11382 {
    private static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) throws Exception {
        // 첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.
        long a = scanner.nextLong();
        long b = scanner.nextLong();
        long c = scanner.nextLong();

//        String userInput = scanner.nextLine();
//        long[] numbers = Arrays.stream(userInput.split(" ")).mapToLong(Long::valueOf).toArray();

        System.out.println(a + b + c);
//        System.out.println(numbers[0] + numbers[1] + numbers[2]);
    }
}
