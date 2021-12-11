f = open('syntax.txt', 'r')

       # (, [, {, <
inv = {')': '(', ']': '[', '}': '{', '>': '<' }
rev = {'(': ')', '[':']', '{':'}','<':'>' }
m = {')': 0, ']': 1, '}': 2, '>': 3 }
illegal = [0]*4
auto = []
for line in f.readlines():
  track = []
  ill = False
  for char in line.strip():
    if char in ['(','[','{','<']:
      track.append(char)
    else:
      if inv[char] == track[-1]:
        track.pop()
      else:
        illegal[m[char]] += 1
        ill = True
        break
  if ill == False and len(track) > 0:
    track.reverse()
    tot = 0
    for char in track:
      tot = tot*5 + m[rev[char]]+1
    auto.append(tot)
    print(tot)

auto.sort()
print(auto[int(len(auto)/2)])
