import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
    public static int N; //채스판 크기(N * N)
    public static int[] queens; // 각 행의 퀸 위치
    public static int solutions = 0; //퀸 배치 방법의 수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        queens = new int[N];
        backtrack(0);
        System.out.println(solutions); //퀸 배치가 가능한 경우의 수
    }
    public static void backtrack(int row) {
        if (row == N) {//종료일때
            solutions++;
            return;
        }
        for (int col = 0; col < N; col++) {
            if(isValid(row,col)) {//현재 Row Col 위치에서 Queen을 놓을 수 있는 위치
                queens[row] = col;
                backtrack(row + 1); //다음행으로 이동(같은 행 열에는 놓을 수없으니 해당 행열에 위치하면 다음으로 이동)
            }
        }
    }
    public static boolean isValid(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (queens[i] == col) {
                return false;
            } //깉은 열에 있지 않은 경우만 놓을 수 있으니 False 반환
            //대각선
            if (Math.abs(row - i) == Math.abs(col - queens[i])) {
                return false;
            }
        }
        return true; //놓아도 안전한 경우(조건1,2를 모두 만족)

    }
}
 /*
 규칙 1) Queen은 같은 행 / 열에는 못놓음 (1행에 둔 체스면 1열에 못놓는다는 말)
 규칙 2) 대각선끼리 만나는 구간에도 못 놓음
0번째 Index부터 시작하면 다음 Queen의 위치는 (2,1) 일떄 그 다음 퀸위치를 정할 수 없음 (규칙1,2를 준수한경우)
Index 1부터 시작해야함
(Queen이 (1,1에 있는경우)
x Q x x
x x x Q //ath.abs(row - i) == Math.abs(col - queens[i]) 관련
Q x x x
x x Q x
  */