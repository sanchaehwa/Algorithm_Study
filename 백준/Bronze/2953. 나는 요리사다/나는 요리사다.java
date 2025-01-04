import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] score = new int[5][4];
        int[] sum = new int[5];

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 4; j++) {
                score[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 4; j++) {
                sum[i] += score[i][j];
            }
        }
        int max = 0;
        for (int i = 0; i < 5; i++) {
            if (sum[max] < sum[i]) {
                max = i;
            }
        }

        System.out.println((max + 1) + " " + sum[max]);
        sc.close();
    }
}