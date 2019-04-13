# exercise5.py


restaurants = [
  "Shakey's",
  "Frankies",
  "Jollibee",
  "Mcdo",
  "KFC"
]

for resto in reversed(sorted(restaurants)): # sorted will not alter variable, same with reversed
  print(resto)

print(len(restaurants))
print(restaurants)