# forward +, down +, up -

f = open('directions.txt', 'r')
aim = 0
x, y = 0, 0
for l in f:
  direction, value = l.split(' ')
  if direction == 'forward':    
    x += int(value)
    y += aim * int(value)
  elif direction == 'down':
    aim += int(value)
  else:
    aim -= int(value)

print(x, y, aim)

print(x*y)