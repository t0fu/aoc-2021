"""      
 aaaa    
b    c   
b    c   
 dddd    
e    f   
e    f   
 gggg    

"""  
f = open('segments.txt', 'r')
count = 0
tt = 0

# 1, 4, 7, 8 (2, 4, 3, 6)
for line in f.readlines():
  left, right = line.split('|')
  rd = right.split()
  ld = left.split()
  numbers = ['']*10
  #known
  for d in ld:
    if len(d) == 2:
      numbers[1] = d
    if len(d) == 4:
      numbers[4] = d
    if len(d) == 3:
      numbers[7] = d
    if len(d) == 7:
      numbers[8] = d
  #get the sixes
  for d in ld:
    if len(d) == 6:
      #6
      if numbers[1][0] not in d or numbers[1][1] not in d:
        numbers[6] = d
      #9
      elif numbers[4][0] in d and numbers[4][1] in d and numbers[4][2] in d and numbers[4][3] in d:
        numbers[9] = d
      else:
        numbers[0] = d
  #2 or #5 
  for d in ld:
    if len(d) == 5:
      if numbers[1][0] in d and numbers[1][1] in d:
        numbers[3] = d 
      else:
        two = False
        for x in d:
          if x in numbers[6] and x not in numbers[9]:
            numbers[2] = d           
            two = True

        if two is False:
          numbers[5] = d        

  total = ''
  for d in rd:
    for x,val in enumerate(numbers):
      if "".join(sorted(d)) == "".join(sorted(val)):
        total += str(x)

  print(total)
  tt += int(total)
print('Final:')
print(tt)
    