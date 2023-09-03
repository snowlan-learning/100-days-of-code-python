# Program to calculate and interpret Body Mass Index (BMI) based on user input for height and weight.

# BMI Categories:
# - Underweight: BMI < 18.5
# - Normal weight: 18.5 <= BMI < 25
# - Slightly overweight: 25 <= BMI < 30
# - Obese: 30 <= BMI < 35
# - Clinically obese: BMI >= 35

# Collect height and weight from the user
# Convert inputs to float for calculations
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI using the formula: BMI = weight (kg) / (height (m))^2
# Round the calculated BMI to the nearest integer
bmi = round(weight / (height ** 2))

# Determine and display BMI category based on the calculated BMI
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")