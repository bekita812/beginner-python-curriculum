# Problem 1
# Ask the user to enter their height in centimeters.
# Print "Tall" if the height is greater than 170, otherwise print "Short".
h= int(input("Enter your height in centimeters: "))
if h > 170:
    print("Pretty tall.")
else:
    print("Pretty short.")

# Problem 2
# Ask the user for their age.
# If they are 18 or older, print "Adult", else print "Minor".

age = int(input("Enter your age: "))
if age >= 18:
    print("You're probably lying to me, but if you aren't, you're an adult.")
else:
    print("You're a minor.")

# Problem 3
# Ask the user to enter a number.
# Print "Fizz" if it is divisible by 3, "Buzz" if divisible by 5,
# print "FizzBuzz" if divisible by both 3 and 5,
# otherwise print the number itself.

num = int(input("Enter in a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3==0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)# Problem 4
# Ask for age and height.
# If age is at least 10 AND height is at least 120 cm, print "You can ride!"
# Otherwise, print "Sorry, you can't ride."
a= int(input("Enter your age: "))
h= int(input("Enter your height in centimeters: "))
if a >= 10 and h >= 120:
    print("Go on and ride kiddo.")
else:
    print("Sorry, you can't ride.")



# Problem 5
# Ask the user for a number.
# If it's divisible by 3 AND (either less than 0 OR greater than 100), print "Weird number!"
# Otherwise, print "Normal number."

a = int(input("Give me a number: "))
if a % 3 == 0 and (a < 0 or a > 100):
    print("That's a goofy 'lil number.")
else:
    print("Nothing much, just a normal number.")

