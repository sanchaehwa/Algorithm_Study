import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] num = new int[9];

        for (int i = 0; i < num.length; i++) {
            num[i] = sc.nextInt();
        }
        int max = num[0];
        int j = 0;
        for (int i = 1; i < num.length; i++) {
            if (max < num[i]){
                max = num[i];
                j = i;
            }
        }
        System.out.println(max);
        System.out.println(j + 1);
    }
}


