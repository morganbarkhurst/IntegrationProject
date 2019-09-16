# IntegrationProject
Hello there! 
I'm here to review some of the things you have been learning in your COP 1500 class

Here are some things from exersizes 1-3:

We will do some basic adding:

I will tell you what math I am doing by putting it in ""

That will make it a string, like this:


    print("34 + 123 =", 34 + 123)

I used the comma to have both on the same line

So, 34 + 123 equals 157

You can see that + does something different

    schoolName ="Chestnut Hill"
    typeOfSchool = "College"
    fullName = schoolName + typeOfSchool
    print(fullName)
    
fullName looks like this

    Chestnut HillCollege

Now here is some more math:

    print(16 + 3)
    print(16 - 3)
    print(16 * 3)
    print(16 ** 3)
    print(16 / 3)
    print(16 // 3)
    print(16 % 3)

Python even knows order of operations

    answer = 6 ** 2 + 3 * 4 // 2
    print(answer % 4)

This is how to repeat a string a large number of times (all on the same line):

    myWord = "Hello!" * 10
    print(myWord)

This one is tricky, but also cool! See if you can figure out what is going on...

    firstNumber = input("Enter a number, with or without a decimal: ")
    secondNumber = input("Enter an integer: ")
    num1 = float(firstNumber)
    num2 = int(secondNumber)
    difference = num1 - num2
    print("Difference =", difference)

    sum1 = 5 + 6
    print(sum1)
    sum2 = 34 + 7
    print(sum1 * sum2)
       
So sum1 equals 11, sum2 = 41, and difference depends on what you input. 
If you enter 8 for the first number, but 8.5 for the second, you will get an error.
