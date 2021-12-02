

f = open('depths.txt', 'r')
prev = 1000000000000000
count = 0
for l in f:
  if int(l) > prev:
    count += 1
  prev = int(l)

print(count)
