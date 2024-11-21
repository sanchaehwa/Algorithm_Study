import java.util.Scanner;

public class Main{
    static int N, M;
    static int[][] board;
    static boolean[][] visited;
    static int result = 0;

    // 상, 우, 하, 좌 방향
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 받기
        N = sc.nextInt();
        M = sc.nextInt();
        board = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] = sc.nextInt();
            }
        }

        // 모든 좌표를 시작점으로 탐색
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                visited[i][j] = true;
                dfs(i, j, board[i][j], 1); // DFS로 탐색
                visited[i][j] = false;
                checkSpecialShape(i, j);  // "ㅗ" 모양 탐색
            }
        }

        System.out.println(result);
    }

    // DFS로 4칸 탐색
    private static void dfs(int x, int y, int sum, int depth) {
        if (depth == 4) {
            result = Math.max(result, sum);
            return;
        }

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            // 범위를 벗어나거나 이미 방문한 경우
            if (nx < 0 || ny < 0 || nx >= N || ny >= M || visited[nx][ny]) {
                continue;
            }

            visited[nx][ny] = true;
            dfs(nx, ny, sum + board[nx][ny], depth + 1);
            visited[nx][ny] = false;
        }
    }

    // "ㅗ" 모양 탐색
    private static void checkSpecialShape(int x, int y) {
        // "ㅗ" 모양의 상대 좌표
        int[][][] shapes = {
                { {0, 0}, {0, -1}, {0, 1}, {-1, 0} }, // "ㅗ"
                { {0, 0}, {0, -1}, {0, 1}, {1, 0} },  // "ㅜ"
                { {0, 0}, {-1, 0}, {1, 0}, {0, -1} }, // "ㅓ"
                { {0, 0}, {-1, 0}, {1, 0}, {0, 1} }   // "ㅏ"
        };

        for (int[][] shape : shapes) {
            int sum = 0;
            boolean isValid = true;

            for (int[] coord : shape) {
                int nx = x + coord[0];
                int ny = y + coord[1];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                    isValid = false;
                    break;
                }

                sum += board[nx][ny];
            }

            if (isValid) {
                result = Math.max(result, sum);
            }
        }
    }
}