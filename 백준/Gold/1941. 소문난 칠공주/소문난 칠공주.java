 import java.io.IOException;
import java.util.*;

public class Main{
    //5*5 행렬 (25명의 학생 구성)
    static String[][] arr = new String[5][5];
    //이다솜파인 경우의 수
    static int result = 0;
    //모든 좌표 저장하기위한 List
    static List<int[]> positions = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        // 5*5 행렬을 입력받고
        for (int i = 0; i < 5; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < 5; j++) {
                arr[i][j] = String.valueOf(line.charAt(j));
                //입력받은 좌표를 저장
                positions.add(new int[]{i, j});
            }
        }

        // 7명 선택한 combine
        combine(0, 0, new ArrayList<>());
        //이다솜파인경우의수 출력
        System.out.println(result);
    }


    public static void combine(int start, int depth, List<int[]> selected) {
        if (depth == 7) {
            // 조건 1: 선택된 7명이 인접하고(인접은 상하좌우), 조건 2: S가 4명 이상인지 확인
            if (isConnected(selected) && countS(selected) >= 4) {
                result++;
            }
            return;
        }
        //7명 선택
        for (int i = start; i < positions.size(); i++) {
            selected.add(positions.get(i));
            combine(i + 1, depth + 1, selected);
            //좌표 제거하고 다음경우를 탐색(백트레킹 수행을 위해)
            selected.remove(selected.size() - 1);
        }
    }


    public static boolean isConnected(List<int[]> selected) {
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[5][5];
        queue.add(selected.get(0));
        visited[selected.get(0)[0]][selected.get(0)[1]] = true;

        int count = 1;
        //인접한경우= 상호좌우로 탐색하려고 함
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, -1, 0, 1};
        //Queue가 빌 경우까지 인접 좌표를 큐에 추가
        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            int x = pos[0], y = pos[1];
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && !visited[nx][ny]) {
                    for (int[] sel : selected) {
                        if (sel[0] == nx && sel[1] == ny) {
                            visited[nx][ny] = true;
                            queue.add(new int[]{nx, ny});
                            count++;
                        }
                    }
                }
            }
        }

        return count == 7;
    }

    // S의 개수 세기
    public static int countS(List<int[]> selected) {
        //선택한 좌표의 리스트에서 S가 포함된 개수를 셈.
        int count = 0;
        for (int[] pos : selected) {
            //S인경우 세고
            if (arr[pos[0]][pos[1]].equals("S")) {
                count++;
            }
        }
        return count;
    }
}