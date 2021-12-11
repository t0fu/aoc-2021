
f = open('segments.txt', 'r')
count = 0
# 1, 4, 7, 8 (2, 4, 3, 6)
for line in f.readlines():
  left, right = line.split('|')
  digits = right.split()
  for d in digits:
    if len(d) == 2 or len(d) == 4 or len(d) == 3 or len(d) ==7:
      count += 1

print(count)