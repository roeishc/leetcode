class Solution {

    private final int[] DIRECTIONS = new int[] {0, 1, 0, -1, 0};

    public int getMaximumGold(int[][] grid) {

        int rows = grid.length;
        int cols = grid[0].length;
        int maxGold = 0;

        // for each element in the grid (row, col), determine its most profitable path
        for (int row = 0; row < rows; row++){
            for (int col = 0; col < cols; col++)
                maxGold = Math.max(maxGold, dfsBacktrack(grid, row, col));
        }

        return maxGold;
        
    }

    private int dfsBacktrack(int[][] grid, int row, int col){

        int rows = grid.length;
        int cols = grid[0].length;

        if (row < 0 || col < 0 || rows <= row || cols <= col || grid[row][col] == 0)
            return 0;

        int maxGold, originalValue;
        originalValue = grid[row][col];
        maxGold = grid[row][col] = 0;

        /*
        the following loop is a fancy way to recursively call this function in all 4 directions
        around the current grid location:
        currentRow + 0, currentCol + 1  // below
        currentRow + 1, currentCol + 0  // right
        currentRow + 0, currentCol - 1  // above
        currentRow - 1, currentCol + 0  // left
        */
        for (int direction = 0; direction < DIRECTIONS.length - 1; direction++){
            maxGold = Math.max(
                maxGold,
                dfsBacktrack(grid, row + DIRECTIONS[direction], col + DIRECTIONS[direction + 1])
            );
        }

        grid[row][col] = originalValue;
        return maxGold + originalValue;

    }

}