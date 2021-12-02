# forward +, down +, up -

f = open('directions.txt', 'r')
x, y = 0, 0
for l in f:
  direction, value = l.split(' ')
  if direction == 'forward':
    x += int(value)
  elif direction == 'down':
    y += int(value)
  else:
    y -= int(value)

print(x, y, x*y)

