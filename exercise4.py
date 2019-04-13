# exercise4.py
# data type: list

restaurants = ["Shakey's", "Frankies", "Jollibee", "Mcdo", "KFC"]

restaurants[0] = "Pizza Hut"
print(restaurants[1])
#print(restaurants[5]) # index outside
print(restaurants[-2])
restaurants.append("Rufus")
# restaurants.remove("kfc") #case sensitive, error
restaurants.remove("KFC")
print(restaurants.index("Jollibee"))
# print(restaurants.index("Shakey's")) # error, already replaced
restaurants.sort() # alphabetical sort
restaurants.reverse() # reverse, no sort

print(restaurants)

# for <iterator> in <container>:
# code block ex. {}, begin...end, indention
for resto in restaurants:
  print("I like " + resto)
  print("Let's go there")