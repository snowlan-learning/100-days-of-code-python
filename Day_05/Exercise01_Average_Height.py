# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

#Write your code below this row 👇

# Initialize variables to hold the total height and the number of students
total_height = 0
number_of_students = 0

# Iterate through each student's height in the list 'student_heights'
for s in student_heights:
    total_height += s  # Add each student's height to the total height
    number_of_students += 1  # Increment the student count by 1 for each iteration

# Calculate the average height. Use 'round' to round it to the nearest integer.
average_high = round(total_height / number_of_students)

# Print the rounded average height of students
print(average_high)