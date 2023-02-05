
# Exercise 1
# A Video club that awards points to its customers based on the number of videos
# purchased each month. The points are awarded as follows:
# • If a customer purchases 0 dvd’s, the earning is 0 points.
# • If a customer purchases 1 dvd, the earning is 5 points.
# • If a customer purchases 2 dvd’s,the earning is 15 points.
# • If a customer purchases 3 dvd’s, the earning is 30 points.
# • If a customer purchases 4 or more dvd’s, the earning is 60 points.
# Write a program that asks the user to enter the number of videos that he or she
# has purchased this month, then displays the number of points awarded.

print("This program displays the number of points awarded to a user depending on how many videos he/she purchased")
# Take input from the user
dvd_count = int(input("Enter number of videos purchased this month : "))

# Print points accordingly
if dvd_count == 0:
    print("You earn 0 points")
elif dvd_count == 1:
    print("You earn 5 points")
elif dvd_count == 2:
    print("You earn 15 points")
elif dvd_count == 3:
    print("You earn 30 points")
elif dvd_count >= 4:
    print("You earn 60 points")

# Tries to handle negative values
else:
    print("Wrong input! Please try again.")

# Exercise 2
# Write a program that calculates the BMI ( Body Mass Index ) for a user.

print("This program calculates the BMI ( Body Mass Index ) for a user")

# Take user input
weight = float(input("Enter your weight (in kgs) : "))
height = float(input("Enter your height (in meter) : "))

# Define logic acc to the question
bmi = weight / (height ** 2)

# Print BMI acc to if/else condition and formatting output to 3 decimal places
if bmi < 18.5:
    print("BMI is", '{:.3f}'.format(bmi), "\n You are underweight.")
elif 18.5 <= bmi <= 24.99:
    print("BMI is", '{:.3f}'.format(bmi), "\n Your weight is normal.")
elif 25.0 <= bmi <= 29.99:
    print("BMI is", '{:.3f}'.format(bmi), "\n You are over weight.")
elif bmi >= 30:
    print("BMI is", '{:.3f}'.format(bmi), "\n You are obese.")

# For values out of range
else:
    print("Wrong Input! Try again.")

# Exercise 3
# A county collects property taxes on the assessment value of property, which is 60 percent of the
# property’s actual value. For example, if an acre of land is valued at $10,000, its assessment value is $6,
# 000. The property tax is then 72¢ for each $100 of the assessment value. The tax for the acre assessed at $6,
# 000 will be $43.20. Write a program that asks for the actual value of a piece of property and displays the
# assessment value and property tax.

print("This program takes the actual value of a piece of property and displays the assessment value and property tax")

# Taking user input and calculating the assessment value and property tax
actual_val = float(input("Enter actual value of your property: "))
assessment_val = 0.6 * actual_val
property_tax = (assessment_val / 100) * 0.72

# Displaying the assessment value and property tax and formatting output to 3 decimal places
print("Assessment value for your property is : ", '{:.2f}'.format(assessment_val))
print("Property tax for your property is : ", '{:.2f}'.format(property_tax))

# Exercise 4
# Write a program using a while loop and within the loop asks the user to enter a
# series of positive numbers.
# The user should enter a negative number to signal the end of the series.
# After all the positive numbers have been entered, the program should display
# their sum.

print("Holla ! This program lets you enter a series of positive numbers and returns their sum")
print("if you terminate the series by entering a negative number. Let's play!")

# Initializing sum series and iteration variable
sum_series = 0
n = 0

# Looping input values to calculate sum of +ve numbers
while n >= 0:
    n = float(input("Enter a positive number: "))
    if n >= 0:
        sum_series = sum_series + n

    # Printing end result after user entered a -ve number
    else:
        print("You ended the series, Sum of your series is:", sum_series)

# Exercise 5
# Write a function named my_max that accepts two integer values as arguments
# and returns the value that is the greater of the two. For example, if 12 and 19
# are passed as arguments to the function, the function should return 19. Use
# the function in a program that prompts the user to enter two integer values.
# The program should display the value that is the greater of the two.

print("This program accepts two integer values as arguments and returns the value that is the greater of the two")


# Define the function
def my_max(num1, num2):
    # Define logic for comparing numbers
    if num1 > num2:
        print(num1, " is the bigger number")
    # Either number can be returned if num1 == num2
    elif num1 == num2:
        print(num1, " is the bigger number")
    else:
        print(num2, " is the bigger number")


# Take input from user
a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

# Function call triggered
my_max(a, b)

# # Exercise 6
# Write a program that asks the user to enter five test scores. The program should
# display a letter grade for each score and the average test score. Write the
# following functions in the program:
# Part 1 -> calc_average This function should accept five test scores as arguments
# and return the average of the scores.
# Part 2 -> determine_grade This function should accept a test score as an argument and return a
# letter grade for the score based on the given grading scale


# Part 1

print("Program to get the average of test scores")


# Function definition for avg scores
def calc_average(t1, t2, t3, t4, t5):
    # Calculating average
    avg_score = (t1 + t2 + t3 + t4 + t5) / 5
    print(avg_score)


# Taking user input
a = float(input("Enter test score 1 :"))
b = float(input("Enter test score 2 :"))
c = float(input("Enter test score 3 :"))
d = float(input("Enter test score 4 :"))
e = float(input("Enter test score 5 :"))

# Function call triggered
print("Average score is :")
calc_average(a, b, c, d, e)

# Part 2

print(" Program for determining grade of each test score")


# Function definition for determining grade
def determine_grade(t1, t2, t3, t4, t5):
    # Using for loop to iterate over the test grades
    for i in [t1, t2, t3, t4, t5]:
        if 90 <= i <= 100:
            print(i, "Wow! You got an A! ")
        elif 80 <= i <= 89:
            print(i, "Yay! You got a B!")
        elif 70 <= i <= 79:
            print(i, "You got a C!")
        elif 60 <= i <= 69:
            print(i, "You got a D. Better luck next time!")
        elif 0 <= i <= 59:
            print(i, "You got an F. Better luck next time!")
        # For handling negative values as test scores can't be negative
        else:
            print(" Test score is out of range. Please use range 0-100 ")


# Taking user input
a = float(input("Enter test score 1: "))
b = float(input("Enter test score 2: "))
c = float(input("Enter test score 3: "))
d = float(input("Enter test score 4: "))
e = float(input("Enter test score 5: "))

# Function call triggered
determine_grade(a, b, c, d, e)
