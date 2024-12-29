import java.util.*;

class Solution {
    int[][] visited;
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    int row;
    int column;

    public int solution(int[][] maps) {
        int answer = 0;
        row = maps.length;
        column = maps[0].length;
        visited = new int[row][column];
        boolean flag = false;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (maps[i][j] == 1 && visited[i][j] == 0) {
                    bfs(i, j, maps);
                    flag = true;
                    break;
                }
            }
            if (flag) {
                break;
            }
        }

        answer = visited[row-1][column-1] != 0 ? visited[row-1][column-1] : -1;
        return answer;
    }

    public void bfs(int x, int y, int[][] maps) {
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(x, y));
        visited[x][y] = 1;

        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = pair.x + dx[i];
                int ny = pair.y + dy[i];

                if (checkBorder(nx, ny)) {
                    if (maps[nx][ny] == 1 && visited[nx][ny] == 0) {
                        queue.offer(new Pair(nx, ny));
                        visited[nx][ny] = visited[pair.x][pair.y] + 1;
                    }
                }
            }
        }
    }

    public boolean checkBorder(int x, int y) {
        if (x < 0 || x >= row || y < 0 || y >= column) {
            return false;
        }
        return true;
    }

    public class Pair {
        int x;
        int y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}