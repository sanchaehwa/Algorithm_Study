import java.util.*;

public class Main{
    //탐색해야하니깐 반대로 Max -> Min , Min -> Max : Max -> Max로 하면 더이상 탐색할게 없다고 판단
    static int Max = Integer.MIN_VALUE;
    static int Min = Integer.MAX_VALUE;
    static int N;
    static int[] number;
    static int[] operator = new int[4];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        number = new int[N];
        for (int i = 0; i < N; i++) {
            number[i] = sc.nextInt();
        } //숫자 입력
        //int numoperater = N - 1;
        for (int i = 0; i <4; i++) {
            operator[i] = sc.nextInt();
            // numoperater -= operator[i]; //N-1 (N이 4면 3개의 연산자로 계산)
        } //연산자 입력

        dfs(number[0],1);

        System.out.println(Max); //최종 최대 결과값
        System.out.println(Min); //최종 최소 결과값


    }
    public static void dfs(int num, int idx) {
        if (idx == N) { //탐색을 모두 한 경우
            Max = Math.max(Max, num); //최대 연산
            Min = Math.min(Min, num); //최소 연산
            return;
        }
        for (int i = 0; i<4; i++){
            if(operator[i] > 0) { //0이면 해당 연산자가 사용되지 않았다는 것이니깐 고려X , 0보다 크다는 것은 연산자가 사용이 된경우
                operator[i]--; //2이면 사용한 연산자이니깐 1만큼 줄어듬 해당 연산자는 총 1개 남음
                //예시 1 + 3이면 0번쨰 1 1번째 3 num[0] : result , 1 : number , i : 연산자 종류
                switch(i) {
                    case 0: dfs(num + number[idx], idx+1); break; //더하기 
                    case 1: dfs(num - number[idx], idx+1); break; //빼기
                    case 2: dfs(num * number[idx], idx+1); break; //곱하기
                    case 3: dfs(num / number[idx], idx+1); break; //나누기

                }
                operator[i]++;
            }
        }
    }
}
