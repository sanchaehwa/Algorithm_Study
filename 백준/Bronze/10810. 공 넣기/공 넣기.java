import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] baskets = new int[N];
        for (int m = 0; m < M; m++) {
            int i = sc.nextInt() -1 ;
            int j = sc.nextInt() -1;
            int k = sc.nextInt();
            for (int idx = i; idx <= j; idx++) {
                baskets[idx ] = k;
            }
        }
        for(int num: baskets) {
            System.out.print(num+" ");
        }
    }
}