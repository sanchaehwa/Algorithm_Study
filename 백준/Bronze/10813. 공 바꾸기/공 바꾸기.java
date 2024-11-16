import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] basket = new int[n];
        for (int i = 0; i < basket.length; i++) {
            basket[i] = i + 1;
        }
        for (int x =1; x <= m; x++) {
            int j = sc.nextInt() -1 ;
            int k = sc.nextInt() -1;
            int temp = basket[j];
            basket[j] = basket[k];
            basket[k] = temp;
        }
        for (int num : basket) {
            System.out.print(num + " ");
        }

    }
}