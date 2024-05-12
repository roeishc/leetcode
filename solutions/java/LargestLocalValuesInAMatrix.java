class Solution {
    public static int[][] largestLocal(int[][] grid) {
        // grid[row][col]

        int[][] res = new int[grid.length-2][grid[0].length-2];
        int resI, resJ;
        resI = resJ = 0;

        for (int i = 1; i < grid.length - 1; i++){
            for (int j = 1; j < grid[0].length - 1; j++)
                res[resI][resJ++] = getMaxAroundVal(grid, i, j);
            resJ = 0;
            resI++;
        }
        return res;
    }

    public static int getMaxAroundVal(int[][] grid, int row, int col){
        int temp = 0;
        for (int i = row - 1; i <= row + 1; i++){
            for (int j = col - 1; j <= col + 1; j++)
                temp = Math.max(temp, grid[i][j]);
        }
        return temp;
    }
}