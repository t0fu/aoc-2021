
f = open('smoke.txt','r')
n,e,w,s = 0x8, 0x4, 0x2, 0x1

length = 100
grid = [[0]*length for i in range(length)]
lows = [[0]*length for i in range(length)]
for x, row in enumerate(f.readlines()):
  for y, c in enumerate(row.strip()):
    grid[x][y] = int(c)

for x in range(length):
  for y in range(length):
    check = 0

    if (x > 0 and grid[x-1][y] > grid[x][y]) or x == 0:
      check |= w
    
    if (x < length-1 and grid[x+1][y] > grid[x][y]) or x == length-1:
      check |= e
    
    if (y > 0 and grid[x][y-1] > grid[x][y]) or y == 0:
      check |= n
    
    if (y < length-1 and grid[x][y+1]> grid[x][y]) or y == length-1:
      check |= s

    if check == 15:
      lows[x][y] = grid[x][y]+1

total = 0
for row in lows:
  total += sum(row)

print(total)
