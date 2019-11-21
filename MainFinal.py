"""__author__ = Morgan Barkhurst"""
# A basic review of things covered in class thus far is as follows

import math
import random

print("""
Hello there!
I'm here to review some of the things learned in COP 1500 class
""")


def new_block():
    """
Used to identify a new program
    """
    print("\nNew Program")


new_block()
# This is a good way to use try and except without break and continue
# This was an in class example
they_input_the_wrong_thing = True
while they_input_the_wrong_thing:
    try:
        fav_num = int(input("Enter your favorite number as a whole number: "))
        print("Your favorite number * 2 =", fav_num * 2)
        they_input_the_wrong_thing = False
    except ValueError:
        print("Not a whole number.")

new_block()


# Basic arithmetic with more functions
# This is a void function
# The program still outputs data even if numbers are not in range
def add_numbers(number1, number2):
    """
Adds number1 to number2
    :param number1:
    :param number2:
    """
    print(number1, "+", number2, "=", number1 + number2)


def subtract_numbers(a, b):
    """
Subtracts num2 from num1
    :param a:
    :param b:
    """
    print(a, "-", b, "=", a - b)


def game():
    """
Adds or subtracts numbers
    """
    first_number = int(input("Enter number between 1 and 10: "))
    second_number = int(input("Enter another number between 1 and 10: "))
    operator = input("Enter a + to add or - to subtract: ")

    if operator == "+":
        add_numbers(first_number, second_number)
    elif operator == "-":
        subtract_numbers(first_number, second_number)
    else:
        print("Invalid operator!")

    if first_number > 10 or second_number > 10:
        print("WARNING! One of numbers is out of range")


game()
print("done")

new_block()


# A function is a name for lines of code - it groups the code


def calculate_area(radius):
    """
Find circle area
    :param radius:
    """
    area = math.pi * radius ** 2
    print("Area of a circle with a radius", radius, "is", format(area, ".2f"))


def calculate_diameter(radius):
    """
Find circle diameter
    :param radius:
    """
    print("The diameter is", radius * 2)


def main():
    """
Main function to calculate area and diameter
    """
    value = int(input("Enter a radius: "))
    # using the value in number as a parameter - which is stored in radius then
    calculate_area(value)
    # call function calculateDiameter
    calculate_diameter(value)


main()

new_block()
doAgain = True
while doAgain:
    num1 = int(input("Enter a 1st number: "))
    num2 = int(input("Enter a 2nd number: "))
    num3 = int(input("Enter a 3rd number: "))
    num4 = int(input("Enter a 4th number: "))
    maxNum1 = max(num1, num2, num3, num4)
    print("Largest of 4 numbers is: ", maxNum1)
    another = input("Type y to find another" + "or any other key to quit")
    if another != "y":
        doAgain = False
print("Done")

new_block()
print("Let's generate a random number between 1 and 100")
guess = int(input("Enter an integer you think it is: "))
randomNumber = random.randint(1, 100)
if guess == randomNumber:
    print("Wow, you did it!", guess, randomNumber)
else:
    print("Better luck next time; we were looking for", randomNumber)

new_block()
horizontal = int(input("Give me a number between 1 and 10: "))
vertical = int(input("Give me another number: "))
num = 1
for num in range(1, vertical + 1):
    for x in range(horizontal):
        print(num, end=" ")
    num += 1
    print()

new_block()
evenNum = []
x = int(input())
while x != 100:
    if x % 2 == 0:
        evenNum.append(x)
    x = int(input("Enter any number besides 100: "))

new_block()
total = 0
for x in range(5):
    number = int(input("Enter a number: "))
    total += number
print("The total is:", total)

new_block()
doAgain = "y"
while doAgain == "y":
    word = input("Enter a word:")
    print("First letter of " + word + " is " + word[0])
    doAgain = input("Type ‘y’ to enter another word or anything else to quit")

print("Done!")

new_block()
print("Let's count down")
answer = input("Do you want to? Type Y if so: ")
if answer == "Y":
    countdown = 100
    while countdown >= 0:
        print(countdown)
    countdown -= 1
else:
    print("Done!")

new_block()
bonus = int(input("What is your bonus? Enter a whole number"))
salary = int(input("What is your salary? Enter a whole number"))
salary += bonus
print("Total salary: ", salary)

new_block()
intList = []
data = float(input("""I will make a list of all your data
It must be greater than 0.
When you are done, input 0 or any negative number
"""))
while data > 0:
    intList.append(data)
    data = float(input())
print(intList)
print("The sum is: ", sum(intList))

new_block()
# This program prints numbers from 1 to value entered by user
number = int(input())
x = 1
while x <= number:
    if x % 10 == 0:
        print(x)
    else:
        print(x, end=' ')
        x += 1

new_block()
print("Now here is some more math:")

print(16 + 3)
print(16 - 3)
print(16 * 3)
print(16 ** 3)
print(16 / 3)
print(16 // 3)
print(16 % 3)

print("Python even knows order of operations")
answer = 6 ** 2 + 3 * 4 // 2
print(answer % 4)

new_block()
firstNumber = input("Enter a number, with or without a decimal: ")
secondNumber = input("Enter an integer: ")
num1 = float(firstNumber)
num2 = int(secondNumber)
difference = num1 - num2
print("Difference =", difference)

new_block()
# This will comment on your score on this project
grade = int(input("Enter your grade:"))
if grade > 100:
    print("Error, must not be greater than 100")
elif grade < 0:
    print("Error, must not be less than 0")
elif grade >= 90:
    print("Very Good!")
elif 80 <= grade < 90:
    print("Good")
elif 70 <= grade < 80:
    print("Satisfactory")
elif 60 <= grade < 70:
    print("Fair")
else:
    print("Poor")

new_block()
# Determining how good a deal is
originalPrice = float(input("Enter the original cost of the item: "))
salePrice = float(input("Enter the sale price: "))
percentOff = int((originalPrice - salePrice) / originalPrice * 100)
print("Original price: $", format(originalPrice, ".2f"))
print("Sale price: $", format(salePrice, ".2f"))
print("Percent off: ", format(percentOff, "d"), "%")
if percentOff >= 50:
    print("You got a great sale!")
if percentOff >= 50:
    print("Congratulations!")
print("Done!")

new_block()
temperatureString = input("Enter water temperature in degrees Fahrenheit: ")
temperature = int(temperatureString)
if temperature >= 212:
    print("Water is boiling.")
    print("That's really hot!")
else:
    print("The water is not boiling.")
