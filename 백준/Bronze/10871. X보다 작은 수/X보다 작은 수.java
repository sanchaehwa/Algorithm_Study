import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();
        int[] arr = new int[N];
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        for (int i = 0; i < N; i++) {
            if (arr[i] < X) {
               result.add(arr[i]);
            }
        }
        for (int num : result) {
            System.out.print(num + " ");
        }

    }
}
