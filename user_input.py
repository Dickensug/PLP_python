# a program that asks the user for their name, age, and location and then prints out a personalized message.
name = input("Enter your name: ").lower()
age = input("Enter your age: ")
location = input("Enter your location: ").lower()

print("Hello", name, "you are", age, "years old and you live in", location, ".")