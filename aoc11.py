f = open('fish.txt', 'r')
fish = [int(n) for n in f.readline().split(',')]

for day in range(80):
  #print(day)
  fish = [x - 1 for x in fish]
  new_fish = fish.count(-1)
  fish = [ x if x != -1 else 6 for x in fish]
  if new_fish > 0:
    nf = [8] * new_fish
    fish = fish + nf
  print(len(fish))

