class Solution {
    
    final int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    public int maximumSafenessFactor(List<List<Integer>> grid) {

        int n = grid.size();
        int[][] mat = new int[n][n];
        Queue<int[]> multiSourceQueue = new LinkedList<>();

        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (grid.get(i).get(j) == 1){
                    multiSourceQueue.add(new int[]{i, j});
                    mat[i][j] = 0;
                }
                else{
                    mat[i][j] = -1;
                }
            }
        }

        // calculate safeness factor for each cell using BFS
        int size, di, dj, val;
        int[] curr;
        while (!multiSourceQueue.isEmpty()){
            size = multiSourceQueue.size();
            while (size-- > 0){
                curr = multiSourceQueue.poll();
                for (int[] d : dir){
                    di = curr[0] + d[0];
                    dj = curr[1] + d[1];
                    val = mat[curr[0]][curr[1]];
                    if (isValidCell(mat, di, dj) && mat[di][dj] == -1){
                        mat[di][dj] = val + 1;
                        multiSourceQueue.add(new int[]{di, dj});
                    }
                }
            }
        }

        // binary search for maximum safeness factor
        int start, end, res;
        start = end = 0;
        res = -1;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++)
                end = Math.max(end, mat[i][j]);
        }

        int mid;
        while (start <= end){
            mid = start + (end - start) / 2;
            if (isValidSafeness(mat, mid)){
                res = mid;
                start = mid + 1;
            }
            else
                end = mid - 1;
        }
        return res;
    }

    private boolean isValidSafeness(int[][] grid, int minSafeness){
        int n = grid.length;

        if (grid[0][0] < minSafeness || grid[n-1][n-1] < minSafeness)
            return false;

        Queue<int[]> traversalQueue = new LinkedList<>();
        traversalQueue.add(new int[] {0,0});
        boolean[][] visited = new boolean[n][n];
        visited[0][0] = true;

        // bfs to find a valid path
        int[] curr;
        int di, dj;
        while (!traversalQueue.isEmpty()){
            curr = traversalQueue.poll();
            if (curr[0] == n - 1 && curr[1] == n - 1)
                return true;
            for (int[] d: dir){
                di = curr[0] + d[0];
                dj = curr[1] + d[1];
                // check if the neighboring cell is valid, unvisited, and
                // satisfying the minimum safeness
                if (isValidCell(grid, di, dj) && !visited[di][dj] && minSafeness <= grid[di][dj]){
                    visited[di][dj] = true;
                    traversalQueue.add(new int[] {di, dj});
                }
            }
        }
        return false;
    }

    private boolean isValidCell(int[][] mat, int i, int j){
        int n = mat.length;
        return 0 <= i && 0 <= j && i < n && j < n;
    }

}