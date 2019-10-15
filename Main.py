#Morgan Barkhurst
#A basic review of things covered in class thus far is as follows

print("""
Hello there!
I'm here to review some of the things you have been learning in your COP 1500 class
""")


# basic arithmatic with more functions
def addNumbers(num1, num2):
	print(num1, "+", num2, "=", num1 + num2)

def subtractNumbers(num1, num2):
	print(num1, "-", num2, "=", num1 - num2)

def main():
	firstNumber = int(input("Enter number between 1 and 10: "))
	secondNumber = int(input("Enter another num between 1 and 10: "))
	operator = input("enter a + to add or - to subtract: ")


	if operator == "+":
		addNumbers(firstNumber, secondNumber)
	elif operator == "-":
		subtractNumbers(firstNumber, secondNumber)
	else:
		print("Invalid operator!")

	if firstNumber > 10 or secondNumber > 10:
		print("WARNING! One of numbers is out of range")	
### call to main program ###
main()
print("done")

# A function is a name for lines of code - it groups the code
import math

def calculateArea(radius):
	area = math.pi * radius ** 2
	print("Area of a circle with a radius of", radius, "is", format(area, ".2f"))


def calculateDiameter(radius):
	print("The diameter is", radius * 2)

def main():
	number = int(input("Enter the radius: "))
	# call function calculateArea (using the value in number as a parameter - which is stored in radius then)
	calculateArea(number)
	# call function calculateDiameter
	calculateDiameter(number)

### Call to Main ###
main()

doAgain = True
while doAgain:
	num1 = int(input("ent 1st num: "))
	num2 = int(input("ent 2nd num: "))
	num3 = int(input("ent 3rd num: "))
	num4 = int(input("ent 4th num: "))
	maxNum1 = max(num1, num2, num3)
	print("Largest of 4 numbers is: ", maxNum1)
	another = input("Type y to find another" + "or any other key to quit")
	if another != "y":
		doAgain = False
print("Done")

import math
x = 4.7
y = 5.3
z = -4.8
a = -3.2
print(math.ceil(x))
print(math.ceil(y))
print(math.ceil(z))
print(math.ceil(a))
print(math.floor(x))
print(math.floor(y))
print(math.floor(z))
print(math.floor(a))


# sample functions
print(abs(-4.67))
print(pow(49,.5))
print(int(34.8))
print(round(6.9))

import random
print(random.randint(1,100))

# fix this .. it DOES NOT WORK
rows = int(input("Enter rows: "))
for column in range(1,rows+1):
	for column in range(1,rows+1):
		print(column)
	print()

# Write a program the prompts the user for information for three students.
# For each student prompt for the student ID and three quiz grades.
# Use a nested loop, where the inner loop prompts for the three quiz grades.
# Print the student’s name and average – formatted to two decimal places.
# View the sample output as a guide.
for student in range(1,4):
	average = []
	name = input(f"Enter name of student {student}: ")
	for scoreNum in range(1,4):
		score = int(input(f"Enter score {scoreNum}:  "))
		average.append(score)
	print(f"Name: {name}")
	finalAve = (sum(average))/3
	print(f"Average:  {finalAve:.2f} \n")


height = int(input("Enter height: "))
for row in range(1, height+1):
	for column in range(row):
		print(row, end=" ")
	print()


hor = int(input("Give me a number between 1 and 10: "))
vert = int(input("Give me another number: "))
num = 1
for num in range(vert):
	for x in range(hor):
		print(num, end=" ")
	num += 1
	print()

name = input("What is your name: ")
# repeats whatever is in the loop 5 times
for x in range (5):
	# repeats whatever is in the loop 3 times
	for x in range(3):
		print(name + " ", end=" ")
	print()

evenNum = []
x = int(input())
while(x != 100):
	if x % 2 == 0:
		evenNum.append(x)
	x = int(input())


total = 0
for x in range(5):
	number = int(input("Enter a number: "))
	total += number
print("The total is:",total)

numIterations = 6
for x in range(numIterations):
	print(x, end=" ")

favorite = input("Enter your favorite ice cream flavor: ")
for x in range(1,5):
	print(x + ".", favorite, end="\t")

numIterations = 6
for x in range(numIterations):
	print(x, end=" ")

name = input("Enter your name: ")
x = 0
while(x < 20):
    print(name, end=" ")
    x += 1

name = input("Enter your name: ")
for x in range(20):
    print(name)

number = 1
while number <= 10:
    if number % 2 == 0:
	       print(number, end= "  ")
    number = number + 1

doAgain = "y"
while doAgain == "y":
    word = input("Enter a word:")
    print("First letter of " + word  + " is " + word[0])
    doAgain = input("Type ‘y’ to enter another word and anything else to quit.")
    print("Done!")


countdown = 100
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("Done!")

bonus = 25
salary = 50
salary += bonus
print("Total salary: ", salary)

intList = []
data = float(input("""I will make a list of all your data
It must be greater than 0.
When you are done, input 0 or any negative number
"""))
while(data > 0):
    intList.append(data)
    data = float(input())
print(intList)

intList = []
data = float(input("""I will make a list of all your data
It must be greater than 0.
When you are done, input 0 or any negative number
"""))
while(data > 0):
    intList.append(data)
    data = float(input())
print("The sum is: ", sum(intList))

number2 = float(input("Enter a number between 1 and 10: "))
while(number2 >= 10) or (number2 <= 1):
    print("You entered an invalid number")
    number2 = float(input("Enter a number between 1 and 10: "))
print("You entered a valid number.")




#This program prints numbers from 1 to value entered by user
number = int(input())
x = 1
while(x <= number):
    if(x % 10 == 0):
        print(x)
    else:
        print(x, end=' ')
    x = x + 1

#Description: This program prints a person's name 20 times
name = input("Enter a name: ")
x = 0
while (x < 20):
    print(name)
    x = x + 1

print("34 + 123 =", 34 + 123)

print("So, 34 + 123 equals 157")

print("You can see that + does something different")

schoolName ="Chestnut Hill"
typeOfSchool = "College"
fullName = schoolName + typeOfSchool
print(fullName)

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

myWord = "Hello!" * 10
print(myWord)


sum1 = 5 + 6
print(sum1)
sum2 = 34 + 7
print(sum1 * sum2)

firstNumber = input("Enter a number, with or without a decimal: ")
secondNumber = input("Enter an integer: ")
num1 = float(firstNumber)
num2 = int(secondNumber)
difference = num1 - num2
print("Difference =", difference)


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


grade = 95
if grade >= 94:
    print("Excellent!")

originalPrice = float(input("Enter the original cost of the item: "))
salePrice = float(input("Enter the sale price: "))
percentOff = int((originalPrice - salePrice)/originalPrice * 100)
print("Original price: $", format(originalPrice, ".2f"), sep=" ")
print("Sale price: $", format(salePrice, ".2f"), sep=" ")
print("Percent off: ", format(percentOff, "d"),"%", sep=" ")
if(percentOff >= 50):
    print("You got a great sale!")

if(percentOff >= 50):
    print("Congratulations!")
print("Done!")


temperatureString = input("Enter the water temperature in degrees Farenheit: ")
temperature = int(temperatureString)
if temperature >= 212:
    print("Water is boiling.")
    print("That's really hot!")
else:
    print("The water is not boiling.")
