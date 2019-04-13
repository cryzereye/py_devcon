# exercise2.py

name = input("What is your name? ")
age =  input("How old are you? ")
age = int(age) + 10

#print("You are {}. In ten years, you will be {} years old", format(name, age))
# py >3.5/.6  -- f-string
print(f"You are {name}. In ten years, you will be {age} years old")