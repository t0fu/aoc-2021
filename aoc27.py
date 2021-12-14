
import math

def sumletters(pairs):

  for k in pairs.keys():
    letters[k[0]], letters[k[1]] = 0,0

  for k in pairs.keys():
    letters[k[0]] += pairs[k]
    letters[k[1]] += pairs[k]


f = open('poly.txt', 'r')

pairs = {}
c = f.readline().strip()
letters = { x : 0 for x in c }

c1 = c[0]
c2 = ''
for v in c[1:]:
  c2 = v
  key = c1 + c2
  if key not in pairs:
    pairs[key] = 1
  else:
    pairs[key] += 1
  c1 = c2


codes = {}
for line in f.readlines():
  if line.strip() != '':
    key, value = line.strip().split('->')
    codes[key.strip()] = value.strip()

print(codes)

for x in range(40):
  print(pairs)
  new_pairs = {}
  for k in pairs:
    if k in codes:
      num = pairs[k]
      letter = codes[k]
      k1 = k[0] + letter
      k2 = letter + k[1] 


      if k1 not in new_pairs:
        new_pairs[k1] = num
      else:
        new_pairs[k1] += num
      
      if k2 not in new_pairs:
        new_pairs[k2] = num
      else:
        new_pairs[k2] += num
  pairs = new_pairs
  sumletters(pairs)
  print(letters)

print(pairs)  
sumletters(pairs)
print(letters)
totals = [ math.ceil(letters[l]/2) for l in letters]
totals.sort()
print(totals)
print(totals[-1]-totals[0])
