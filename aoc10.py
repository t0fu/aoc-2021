
f = open('lines.txt', 'r')
#f = open('test.txt', 'r')
length = 1000
grid = [[0]*length for i in range(length)]

lines = f.readlines()

for line in lines:
  left, right = line.split('->')
  x1, y1 = left.strip().split(',')
  x2, y2 = right.strip().split(',')
  x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

  if(x1 == x2):
    if(y1 < y2):
      for point in range(y1, y2+1):
        grid[x1][point] += 1
    else:
      for point in range(y2, y1+1):
        grid[x1][point] += 1

  elif y1 == y2:
    if x1 < x2:
      for point in range(x1, x2+1):
        grid[point][y1] += 1
    else:
      for point in range(x2, x1+1):
        grid[point][y1] += 1
  else:
    if x1 > x2:
      tmpx, tmpy = x1, y1
      x1, y1 = x2, y2
      x2, y2 = tmpx, tmpy

    slope = int( (y1 - y2) / (x1 - x2) )
    px,py = x1,y1
    while px <= x2:      
      grid[px][py] += 1
      px += 1
      py += 1*slope



total = 0
for x in range(length):
  for y in range(length):
    if grid[x][y] > 1:
      total += 1

print(total)