
f = open('smoke.txt','r')
n,e,w,s = 0x8, 0x4, 0x2, 0x1

length = 100
grid = [[0]*length for i in range(length)]
lows = [[0]*length for i in range(length)]
for x, row in enumerate(f.readlines()):
  for y, c in enumerate(row.strip()):
    grid[x][y] = int(c)

def not9(x,y,path):
  if grid[x][y] == 9:
    path[x][y] = 1
    return 0

  #duplicate
  if path[x][y] == 1:
    return 0

  path[x][y] = 1
  v = 1
  if x > 0:
    v += not9(x-1, y, path)
  if y > 0:
    v += not9(x, y-1, path)
  if y < length-1: 
    v += not9(x, y+1, path)
  if x < length-1:
    v += not9(x+1, y, path)
  return v


bsizes = []
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
      lows[x][y] = 1


for x,row in enumerate(lows):
  for y,v in enumerate(row):
    #basin low
    if v == 1:
      path = [[0]*length for i in range(length)]
      size = not9(x,y,path)
      print(size)
      bsizes.append(size)
bsizes.sort()
#print(bsizes.sort())
print(bsizes[-3:]) 
print(bsizes[-3]*bsizes[-2]*bsizes[-1]) 
