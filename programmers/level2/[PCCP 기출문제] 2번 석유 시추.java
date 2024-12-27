import java.util.*;

class Solution {
    private boolean[][] visited;
    private int[] dx = {-1, 1, 0, 0};
    private int[] dy = {0, 0, -1, 1};
    private int column;
    private int row;
    private int[] columnBlocks;

    public int solution(int[][] land) {
        int answer = 0;
        row = land.length;
        column = land[0].length;
        visited = new boolean[row][column];
        columnBlocks = new int[column];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (land[i][j] == 1 && visited[i][j] == false) {
                    bfs(i, j, land);
                }
            }
        }
        Arrays.sort(columnBlocks);
        answer = columnBlocks[column - 1];
        return answer;
    }

    public void bfs(int x, int y, int[][] land) {
        visited[x][y] = true;
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(x, y));
        int count = 1;
        Set<Integer> columnSet = new HashSet<>();
        columnSet.add(y);

        while (queue.size() > 0) {
            Pair pair = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = pair.x + dx[i];
                int ny = pair.y + dy[i];

                if (checkBorder(nx, ny)) {
                    if (land[nx][ny] == 1 && visited[nx][ny] == false) {
                        visited[nx][ny] = true;
                        queue.offer(new Pair(nx, ny));
                        count++;
                        columnSet.add(ny);
                    }
                }
            }
        }
        for (Integer num: columnSet) {
            columnBlocks[num] += count;
        }
    }

    public boolean checkBorder(int x, int y) {
        if (x < 0 || x >= row || y < 0 || y >= column) {
            return false;
        }
        return true;
    }

    public static class Pair {
        int x;
        int y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}