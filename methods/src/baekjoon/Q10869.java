package baekjoon;

import java.util.Scanner;

// https://www.acmicpc.net/problem/10869
public class Q10869 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.printf("%d\n", a + b);
        System.out.printf("%d\n", a - b);
        System.out.printf("%d\n", a * b);
        System.out.printf("%d\n", a / b);
        System.out.printf("%d", a % b);
    }
}
