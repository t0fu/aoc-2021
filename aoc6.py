def sums(values,x):
  zeroes,ones = [0]*12, [0]*12
  for l in values:
    if l[x] == '1':
      ones[x] += 1
    elif l[x] == '0':
      zeroes[x] += 1

  return zeroes,ones

def parsing(values, x, val1, val2):
  keep = []
  zeroes, ones = sums(values,x)  

  for v in values:
    if ones[x] >= zeroes[x]:
      if v[x] == val1:
        keep.append(v)
    if zeroes[x] > ones[x]:
      if v[x] == val2:
        keep.append(v)        
  
  if len(keep) == 1:
    return keep[0]
  elif len(keep) == 0:
    return None
  else:
    return parsing(keep,x+1,val1, val2)


f = open('binary.txt', 'r')
values = f.readlines()
f.close()

oxygen = parsing(values, 0, '1', '0')
co2 = parsing(values, 0, '0', '1')

print(oxygen)
print(co2)
print(int(oxygen,2))
print(int(co2,2))
print( int(oxygen,2) * int(co2,2))

  


