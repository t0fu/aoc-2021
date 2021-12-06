
def readFile(file, numbers, boards):
  numbers = [int(n) for n in f.readline().split(',')]
  print(numbers)

  x = 0
  row_num = 0
  lines = file.readlines()
  for bl in lines:
    if bl.strip() != '': 
      row = [int(n) for n in bl.split()]

      if row_num%5 == 0:
        boards[x] = row 
      else:
        boards[x].extend(row)

      row_num +=1
      if row_num % 5 == 0 and row_num != 0:
        x += 1

  return numbers


def markBoards(number, boards, tracking):
  for x, board in enumerate(boards):
    for y, value in enumerate(board):
      if number == value:
        #mark         
        tracking[x] |= 1 << y


def bingo(boards, tracking):
  found = {}
  order = []
  for x, t in enumerate(tracking):
    for y, xmask in enumerate(row_mask):
      ymask = column_mask[y]
      if xmask & t == xmask:
        #found a bingo
        found[x] = boards[x]
        order.append(x)
      if ymask & t == ymask:
        found[x] = boards[x]
        order.append(x)


  return found, order
    

#set masks
row_mask, row_track, column_mask, column_track = [0]*5, [0]*5, [0]*5, [0]*5

tracking = [0]*100

x = 0
while x < 5:
  row_mask[x] = 1 << 0 + (5*x) | 1 << 1 + (5*x) | 1 << 2 + (5*x) | 1 << 3 + (5*x) | 1 << 4 + (x*5)
  column_mask[x] = 1 << x | 1 << 5+x | 1 << 10+x | 1 << 15+x | 1 << 20+x
  x += 1

numbers = [0]*100
boards = [[0]*25]*100

f = open('bingo.txt', 'r')

numbers = readFile(f, numbers, boards)
found = []
last_order = []
for num in numbers:
  markBoards(num, boards, tracking)
  found, order = bingo(boards, tracking)  
  unique = [i for i in order + last_order if i not in order or i not in last_order]
  if len(unique) != 0:
    last_order = order
    for x in unique:
      board = boards[x]
      t = tracking[x]
      indexes = [0]*25

      for x in range(25):
        if (1 << x) & t:
          indexes[x] = 1

      for x in range(25):
        if (1 << x) & t:
          indexes[x] = 1

      sum = 0
      for y, val in enumerate(board):
        if indexes[y] == 0:
          sum += val
      
      print(sum)
      print(num)
      print(sum*num)



