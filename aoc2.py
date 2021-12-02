

f = open('depths.txt', 'r')
prev = 1000000000000000
iter = 0
count = 0
one, two, three = 0, 0, 0
for l in f:
  value = int(l)
  mod = iter % 3
  if mod == 0:
    one = value
  elif mod == 1:
    two = value
  else:
    three = value

  iter += 1
  if iter >= 3:
    curr = one + two + three 
    print(curr, prev, iter)
    if curr > prev:
      count += 1
    prev = curr

print(count)
