import java.util.*;

public class Main{
    public static int R, C, result = 0;
    public static char[][] board;
    public static boolean[] visited;
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        R = sc.nextInt();
        C = sc.nextInt();
        //board 초기화
        board = new char[R][C];
        //알파벳 26개
        visited = new boolean[26];
        for (int i = 0; i < R; i++) {
            String row = sc.next();
            board[i] = row.toCharArray();
        }
        backtrack(0,0,1);
        System.out.println(result);
    }
    public static void backtrack(int x, int y, int count) {
        //현재 방문
        visited[board[x][y] - 'A'] = true;
        //결과
        result = Math.max(result, count);
        //상호좌우 탐색
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            //다음으로 갈수 있으면 count
            if (nx >= 0 && ny >=0 && nx < R && ny < C && !visited[board[nx][ny] - 'A']) {
                //4칸 범위 , 전체 벗어나지않았고, 방문하지않은 알파벳
                backtrack(nx, ny, count + 1);
            }
        }
        //탐색하고 다시 백트레킹 수행하기 초기화
        visited[board[x][y] - 'A'] = false; //초기화

    }
}