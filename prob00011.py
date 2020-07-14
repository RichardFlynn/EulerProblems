from functools import reduce
grid=[]
for i in range(20):
    grid.append(list(map(int,input().split())))

print(max(max(max([reduce(lambda x,y:x*y,[grid[r][c+e]for e in range(4)])for c in range(len(grid[r])-3)])for r in range(len(grid))),max(max([reduce(lambda x,y:x*y,[list(zip(*grid))[r][c+e]for e in range(4)])for c in range(len(list(zip(*grid))[r])-3)])for r in range(len(list(zip(*grid)))))))