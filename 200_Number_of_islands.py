# Time Complexity : O(m*n)
# Space Complexity : O(m*n)
class Solution:
    def dfs(self,grid,rows,cols,x,y):
        if x<0 or x>=rows or y<0 or y>=cols or grid[x][y]!='1':
            return
        grid[x][y]='0'
        self.dfs(grid,rows,cols,x-1,y)
        self.dfs(grid,rows,cols,x,y+1)
        self.dfs(grid,rows,cols,x+1,y)
        self.dfs(grid,rows,cols,x,y-1)

    def numIslands(self, grid: List[List[str]]) -> int:

        rows,cols = len(grid),len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(grid,rows,cols,i,j)
        #print(grid)
        
        return count
