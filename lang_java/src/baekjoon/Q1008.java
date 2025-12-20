package baekjoon;

import java.util.Scanner;

// https://www.acmicpc.net/problem/1008
public class Q1008 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextInt();
        double b = sc.nextInt();

        System.out.printf("%.9f", a / b);
    }
}
