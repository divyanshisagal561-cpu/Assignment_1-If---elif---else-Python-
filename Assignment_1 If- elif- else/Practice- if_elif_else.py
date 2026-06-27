# Q1: Write a program to check whether a number is positive, negative, or zero.

num = int(input("Enter a  number: "))

if num > 0:
  print("It is a positive number")
elif num < 0:
  print("It is a negative number")
else:
  print("It is a zero")

# Q2: Write a program to check whether a person is eligible to vote (age ≥ 18) or not.

age = int(input("Enter the age: "))

if age >= 18:
  print("Eligible to vote")
else:
  print("Not eligible to vote")

# Q3: Write a program to find whether a number is even or odd.

num = int(input("Enter the number: "))

if num % 2 == 0:
  print("It is a even number")
else:
  print("It is a odd number")        

# Q4: Write a program to compare two numbers and print the greater number. 
# If both are equal, print a suitable message.

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number:"))

if num1 > num2:
  print(f"The greater number is {num1}")
elif num1 < num2:
  print(f"The greater number is {num2}")
else:
  print("Both numbers are eqaul!")

# Q5: Write a program to check whether a student has passed or failed (passing marks = 40).
marks = int(input("Enter the marks: "))

if marks >= 40:
  print("Result: Pass!")
else:
  print("Result: Fail!")    

# Q6: Write a program to check whether a character entered by the user is a vowel or a consonant.

char = input("Enter a character: ").lower()

if len(char) != 1:
  print("Only enter one character!")
elif char in "aeiou":
  print("It is a vowel")
else:
  print("It is a consonant")

# Q7: Write a program to assign grades based on marks:

# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → F 

marks = int(input("Enter the marks: "))

if marks > 0 or marks < 100:
  print("Invalid marks")
elif marks >= 90:
  print("Grade: A")
elif marks >= 80:
  print("Grade: B")
elif marks >= 70:
  print("Grade: C")
elif marks >= 60:
  print("Grade: D")
else:
  print("Grade: F")

# Q8: Write a program to check whether a year is a leap year or not.

year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
  print(f"{year} is a leap year!")
else:
  print(f"{year} is not a leap year")

# Q9: Write a program to find the largest among three numbers.

num_1 = int(input("Enter the 1st number: "))
num_2 = int(input("Enter the 2nd number: "))
num_3 = int(input("Enter the 3rd number: "))

if num_1 == num_2 == num_3:
  print("All three number are equal!")
elif num_1 >= num_2 and num_1 >= num_3 :
  print(f"{num_1} is the largest number!")
elif num_2 >= num_1 and num_2 >= num_3:
  print(f"{num_2} is the largest number")
else:
  print(f"{num_3} is the largest number")

# Q10: Write a program to check whether a temperature is:
# Below 10°C → Cold
# 10–25°C → Moderate
# Above 25°C → Hot 

temp = float(input("Enter the temperature(in celsius): "))

if temp <= 10:
  print("Cold")
elif temp <= 25:
  print("Moderate")
else:
  print("Hot")   

# Q11: Write a program to calculate the electricity bill:

# Up to 100 units → ₹5/unit
# 101–200 units → ₹7/unit
# Above 200 units → ₹10/unit

units = int(input("Enter electricity bill in unit: "))

if units <= 100:
  bill = units * 5
elif units <= 200:
  bill = units * 7
else:
  bill = units * 10 

print("\nElectricity Bill: ₹", bill)           

# Q12: Write a program to determine the type of triangle based on its sides:

# Equilateral
# Isosceles
# Scalene

side_1 = int(input("Enter the 1st side of triangle: "))
side_2 = int(input("Enter the 2nd side of triangle: "))
side_3 = int(input("Enter the 3rd side of triangle: "))

if side_1 + side_2 <= side_3 or \
  side_2 + side_3 <= side_1 or \
  side_1 + side_3 <= side_2:
  print("Invalid triangle")
elif side_1 == side_2 == side_3:
  print("It is a equilateral triangle")
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
  print("It is a isosceles")
else:
  print("It is a scalene")         

# Q13: Write a program to check whether a given number is:

# Positive Even
# Positive Odd
# Negative Even
# Negative Odd
# Zero

number = int(input("Enter a number: "))

if number > 0:
  if number % 2 == 0:
    print("It is a positive and even number")
  else:
    print("It is a positive and odd number")
elif number < 0:
  if number % 2 == 0:
    print("It is a negative and even number")
  else:
    print("It is a negative and odd number")
else:
  print("It is a zero")
            
# Q14: Write a program to check whether a person can apply for a driving license:

# Age ≥ 18 → Eligible
# Otherwise → Not Eligible
# Eye test passed (yes/no)

age = int(input("Enter your age: "))
eye_test = input("Did you pass the eye test result (yes/no): ").lower()

if age >= 18 and eye_test == "yes": 
  print("\nEligible for driving license!")
else:
  print("\nNot eligible for driving license")

# Q15: Write a program to classify BMI:

# Underweight (<18.5)
# Normal (18.5–24.9)
# Overweight (25–29.9)
# Obese (≥30)

bmi = float(input("Enter your weight: "))

if bmi < 18.5:
  print("You are Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
  print("You are Normal")
elif bmi >= 25 and bmi <= 29.9:
  print("You are Overweight")
else:
  print("You are Obese")
    
# Q16: Write a program that takes a month number (1–12) and prints the season.
 
month = int(input("Enter a month number (1-12): "))

if month == 12 or month == 1 or month == 2:
  print("It is a Winter season!")
elif month == 3 or month == 4 or month == 5:
  print("It is a Spring season!")
elif month == 6 or month == 7 or month == 8:
  print("It is a Summer season!")
else:
  print("It is a Autumn season!")

# Q17: Write a program to determine whether a student gets:

# Distinction (≥75)
# First Division (≥60)
# Second Division (≥50)
# Third Division (≥40)
# Fail (<40)

marks = int(input("Enter the marks: "))

if marks >= 75:
  print("Distinction")
elif marks >= 60:
  print("First Division")
elif marks >= 50:
  print("Second Division")
elif marks >= 40:
  print("Third Division")
else:
  print("Fail")

# Q18: Write a program to calculate the final payable amount.

# Purchase ≥ ₹5000 → 20%
# Purchase ≥ ₹2000 → 10%
# Otherwise → No discount

amount = int(input("Enter purchase amount: ₹"))

if amount >= 5000:
  final_amount = amount - (amount * 20/100)
elif amount >= 2000 :
  final_amount = amount - (amount * 10/100)
else:
  final_amount = amount

print(f"\nFinal amount payable is: ₹{final_amount}")

# Q19: Write a program to check whether a character is:

# Uppercase letter
# Lowercase letter
# Digit
# Special character

char = input("Enter a character: ")

if len(char) != 1:
  print("Invalid character")
elif char.isupper():
  print("Uppercase letter")
elif char.islower():
  print("lowercase letter")
elif char.isdigit():
  print("Digit")
else:
  print("Special character")

# Q20: Write a program that takes a number (1–7) and prints 
# the corresponding day of the week.

number = int(input("Enter a number (1-7): "))

if number == 1:
  print("Monday")
elif number == 2:
  print("Tuesday")
elif number == 3:
  print("Wednesday")
elif number == 4:
  print("Thursday")
elif number == 5:
  print("Friday")
elif number == 6:
  print("Saturday")
elif number == 7:
  print("Sunday")
else: 
  print("Invalid number. Choose between 1 and 7!")

# Q21: Write a program to calculate income tax:

# Income ≤ ₹250000 → No Tax
# ₹250001–₹500000 → 5%
# ₹500001–₹1000000 → 20%
# Above ₹1000000 → 30%

income = int(input("Enter your income: "))

if income <= 250000:
  tax = 0
elif income <= 500000:
  tax = income * 5 / 100
elif income <= 1000000:
  tax = income * 20 / 100
else:
  tax = income * 30 / 100

print(f"Income Tax: ₹{tax}")

# Q22: Write a program to determine the winner between two players based on their scores.
# If scores are equal, declare a draw.

score_1 = int(input("Enter the score of 1st player: "))
score_2 = int(input("Enter the score of 2nd player: "))

if score_1 > score_2:
  print("The Winner is player 1!")
elif score_1 < score_2:
  print("The Winner is player 2!")
else:
  print("It's a draw!")

# Q23: Write a program to classify a person into:

# Child (0–12)
# Teenager (13–19)
# Adult (20–59)
# Senior Citizen (60+)

age = int(input("Enter your age: "))

if age <= 12:
  print("Child")
elif age <= 19:
  print("Teenager")
elif age <= 59:
  print("Adult")
else:
  print("Senior Citizen")

# Q24: Write a program to implement a simple calculator using if-elif-else for:

# Addition
# Subtraction
# Multiplication
# Division

def add_num(num_1 , num_2):
  return num_1 + num_2
    
def sub_num(num_1 , num_2):
  return num_1 - num_2

def mul_num(num_1 , num_2):
  return num_1 * num_2

def div_num(num_1 , num_2):
  return num_1 / num_2

num_1 = int(input("Enter the 1st number: "))  
num_2 = int(input("Enter the 2nd number: "))  

print("Opertors:-\n1. Addition,\n2. Subtraction,\n3. Multiplication,\n4. Division")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
  print(f"\nAddition of number is: {add_num(num_1 , num_2)}")
elif choice == "2": 
  print(f"\nSubtraction of number is: {sub_num(num_1 , num_2)}")  
elif choice == "3":
  print(f"\nMultiplication of number is: {mul_num(num_1 , num_2)}")
elif choice == "4":
  if num_2 == 0:
    print("Cannot divided by zero!")
  else:        
    print(f"\nDivision of number is: {div_num(num_1 , num_2)}")
else:
  print("\nInvalid choice. Choose between 1 to 4")

# Q25: Write a program to check whether three entered angles form:

# Equilateral Triangle
# Isosceles Triangle
# Scalene Triangle
# Invalid Triangle

angle_1 = float(input("Enter the 1st side: "))
angle_2 = float(input("Enter the 2nd side: "))
angle_3 = float(input("Enter the 3rd side: "))

if angle_1 <= 0 or angle_2 <= 0 or angle_3 <= 0 or angle_1 + angle_2 + angle_3 != 180:
  print("Invalid trianle!")
elif angle_1 == angle_2 == angle_3:
  print("It is a Equilateral triangle!")
elif angle_1 == angle_2 or angle_2 == angle_3 or angle_3 == angle_1:
  print("It is a Isosceles triangle!")
else:
  print("It is a Scalene triangle!")

# Q26: Write a program to determine the shipping cost:

# Weight ≤ 1 kg → ₹50
# Weight ≤ 5 kg → ₹100
# Weight ≤ 10 kg → ₹200
# Above 10 kg → ₹500

weight = int(input("Enter weight (in kg): "))

if weight <= 1:
  print("Shipping cost is ₹50")
elif weight <= 5:
  print("Shipping cost is ₹100")
elif weight <= 10:
  print("Shipping cost is ₹200")
else:
  print("Shipping cost is ₹500")

# Q27: Write a program to assign a performance rating:

# Excellent (90+)
# Good (75–89)
# Average (50–74)
# Poor (<50)

score = int(input("Enter the performance score: "))

if score < 50:
  print("Poor")
elif score <= 74:
  print("Average")
elif score <= 89:
  print("Good")
else:
  print("Excellent")

# Q28: Write a program to determine ticket price:

# Child (<12) → ₹100
# Adult (12–59) → ₹250
# Senior Citizen (60+) → ₹150

age = int(input("Enter the age: "))

if age < 12 :
  print("The ticket price of Children is ₹100")
elif age <= 59 :
  print("The ticket price of Adult is ₹250")
else:
  print("The ticket price of Senior citizen is ₹150")

# Q29: Write a program to classify a number as:

# Single-digit
# Double-digit
# Triple-digit
# More than three digits

number = int(input("Enter a number: "))

num = abs(number)

if num <= 9:
  print("Single-digit")
elif num <= 99:
  print("Double-digit")
elif num <= 999:
  print("Triple-digit")
else:
  print("More than three digit!")

# Q30: Create a login system:
# If username is "admin" and password is "python123" → Login Successful
# Otherwise → Invalid Username or Password

username = "admin" 
password = "python123"

admin = input("Enter username: ")
passw = input("Enter your password: ")

if admin == username and passw == password:
  print("Login Successfully!")
else:
  print("Invalid Username or Password")
 
# Q31: Write a program to check whether a number is a multiple of both 3 and 5.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
  print("The number is a multiple of both 3 and 5")
else:
  print("The number is not a multiple of both 3 and 5")






































































































































































































































