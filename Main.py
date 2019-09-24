#Morgan Barkhurst
#A basic review of things covered in class thus far is as follows

print("""
Hello there!
I'm here to review some of the things you have been learning in your COP 1500 class
""")

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
