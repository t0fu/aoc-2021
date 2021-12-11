f = open('syntax.txt', 'r')

       # (, [, {, <
inv = {')': '(', ']': '[', '}': '{', '>': '<' }
m = {')': 0, ']': 1, '}': 2, '>': 3 }
illegal = [0]*4

for line in f.readlines():
  track = []
  for char in line.strip():
    if char in ['(','[','{','<']:
      track.append(char)
    else:
      if inv[char] == track[-1]:
        track.pop()
      else:
        illegal[m[char]] += 1
        break



print(illegal)
print(illegal[0]*3+illegal[1]*57+illegal[2]*1197+illegal[3]*25137)