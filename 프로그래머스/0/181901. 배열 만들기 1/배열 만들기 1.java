import java.util.*;

public class Solution {
    public int[] solution(int n, int k) {
        List<Integer> resultList = new ArrayList<>();
        
        // 1부터 n까지 순회하며 k의 배수를 찾기
        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                resultList.add(i);
            }
        }

        // 리스트를 배열로 변환
        return resultList.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        int n = sc.nextInt();
        int k = sc.nextInt();

        // Solution 호출
        Solution solution = new Solution();
        int[] result = solution.solution(n, k);

        // 결과 출력
        System.out.println(Arrays.toString(result));
    }
}