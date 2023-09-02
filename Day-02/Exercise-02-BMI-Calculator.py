# Program to calculate Body Mass Index (BMI) based on user's weight and height
# BMI is a useful measure to determine if someone is underweight, normal weight, overweight, or obese.
# It is calculated as weight (kg) divided by the square of height (m).

# Prompt the user to enter height in meters
height = input("Enter your height in m: ")

# Prompt the user to enter weight in kilograms
weight = input("Enter your weight in kg: ")

# Calculate BMI
# Convert height and weight to float and int respectively, then perform the BMI calculation
bmi = int(weight) / float(height) ** 2

# Convert the calculated BMI to an integer for easy readability
output = int(bmi)

# Display the BMI result to the user
print(output)
