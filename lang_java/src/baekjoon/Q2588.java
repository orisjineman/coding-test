package baekjoon;

import java.util.Scanner;

// https://www.acmicpc.net/problem/2588
public class Q2588 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        // b의 1, 10, 100의 자릿값
        int b1 = b % 10;
        int b10 = ((b - b1) % 100) / 10;
        int b100 = ((b - (b10 * 10) - b1) % 1000) / 100;

        // 중간 결괏값과 최종 결괏값
        int result1 = a * b1;
        int result10 = a * b10;
        int result100 = a * b100;
        int resultAllAdd = result1 + (result10 * 10) + (result100 * 100);

        System.out.println(result1);
        System.out.println(result10);
        System.out.println(result100);
        System.out.println(resultAllAdd);
    }
}
