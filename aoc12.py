f = open('fish.txt', 'r')
fish = [int(n) for n in f.readline().split(',')]

timers = [0]*9
for f in fish:
  timers[f] += 1

# Population = N (2)^80/7
#80 - x  / 7  
# Time - 9 / 7 = spawnings

for day in range(256):
  print(day)
  front = timers[0]
  timers = timers[1:] + [timers[0]]
  timers[6] += front

print(sum(timers))

