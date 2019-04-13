# exercise6.py

age = int(input("How old are you? "))

if age >= 80 or age <= 0:
  print("That is not a valid age")
elif age >= 14:
  print("You are old enough to drive")
else:
  print("You cannot drive")
  print("Wait for few more years")