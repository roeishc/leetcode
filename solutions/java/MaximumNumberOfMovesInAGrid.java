class Solution {

    public int[][] cache;


    public int maxMoves(int[][] grid) {
        
        cache = new int[grid.length][grid[0].length];
        
        int res = 0;
        for (int i = 0; i < grid.length; i++){
            res = Math.max(res, traverse(grid, i, 0, 0, 0));
            if (res == grid[0].length)
                return res;
        }

        return res;

    }

    public int traverse(int[][] grid, int r, int c, int previousValue, int moves){

        if (r < 0 || r == grid.length || c == grid[0].length || previousValue >= grid[r][c])
            return moves - 1;

        if (cache[r][c] != 0)
            return cache[r][c];

        cache[r][c] = Math.max(Math.max(
            traverse(grid, r - 1, c + 1, grid[r][c], moves + 1),
            traverse(grid, r, c + 1, grid[r][c], moves + 1)),
            traverse(grid, r + 1, c + 1, grid[r][c], moves + 1)
        );
        
        return cache[r][c];

    }

}