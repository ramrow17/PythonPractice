import datetime

name = input("Hi there, what is your name: ")

age = int(input("How old are you: "))

print("\nSo your name is " + name + ", and you are " + str(age) + " years old!")
now = datetime.datetime.now()
outp1 = (now.year + (100-age))
print("You will be 100 years old in the year " + str(outp1))