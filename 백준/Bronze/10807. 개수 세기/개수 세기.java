import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            // N개의 숫자를 입력
            int N = Integer.parseInt(br.readLine());
            //조건이 일치해야 수행
            if (1 <= N && N <= 100) {
                String[] inputArr = br.readLine().split(" ");
                int[] arr = new int[N];
                for (int i = 0; i < N; i++) {
                    arr[i] = Integer.parseInt(inputArr[i]);
                }
                //M번째 원소의 중복 개수를 구하기 위해 M 입력
                int M = Integer.parseInt(br.readLine());
                if (-100 <= M && M <= 100) {
                    int cnt = 0;
                    for (int num : arr) {
                        if (num == M) {
                            cnt++;
                        }
                    }
                    System.out.println(cnt);
                }

            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
