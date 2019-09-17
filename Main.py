#Morgan Barkhurst
#A basic review of things covered in class thus far is as follows

print("""
Hello there!
I'm here to review some of the things you have been learning in your COP 1500 class
Here are some things from exersizes 1-3:
We will do some basic adding
""")

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
