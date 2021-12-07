import statistics

f = open('crabs.txt', 'r')
text = f.readline()
crabs = [int(x) for x in text.split(',')]
length = max(crabs)+1
amount = [0]*length
for c in crabs:
  amount[c] += 1

print(len(crabs))
print(statistics.mean(crabs))
print(statistics.median(crabs))
print(statistics.mode(crabs))

print(amount)

fuel = [0]*length
m = statistics.mode(crabs)
#get the crab we are moving to
for x in range(length):  
  for y,c in enumerate(amount):
    fuel[x] += abs( (x-y) * c)

print(fuel)
print(min(fuel))