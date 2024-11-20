import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] input = new int[8];
        for (int i = 0; i < 8; i++) {
            input[i] = sc.nextInt();
        }

        boolean isAscending = true;
        boolean isDescending = true;

        for (int i = 0; i < 7; i++) {
            if (input[i] < input[i + 1]) {
                isDescending = false;
            } else if (input[i] > input[i + 1]) {
                isAscending = false;
            }
        }

        if (isAscending) {
            System.out.println("ascending");
        } else if (isDescending) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }
    }
}