f = open('binary.txt', 'r')

zeroes, ones = [0]*12, [0]*12

for l in f:
  x = 0
  for bit in l:
    if bit == '1':
      ones[x] += 1
    elif bit == '0':
      zeroes[x] += 1
    x += 1

gamma, epsilon = '0b', '0b'

for x, value in enumerate(ones):
  if ones[x] > zeroes[x]:
    gamma += '1'
    epsilon += '0'
  else:
    gamma += '0'
    epsilon += '1'

print(gamma, epsilon)
print(int(gamma, 2), int(epsilon, 2))
print(int(gamma, 2)*int(epsilon, 2))