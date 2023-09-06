# 🚨 Don't change the code below 👇
# Get student scores as a space-separated string and split into a list
student_scores = input("Input a list of student scores ").split()

# Convert each string score to an integer
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  
# Display the list of integer scores
print(student_scores)
# 🚨 Don't change the code above 👆

# Initialize the highest score to 0
high_score = 0

# Iterate over each student's score
for s in student_scores:
  # Check if the current score is greater than the highest score found so far
  if s > high_score:
    high_score = s

# Display the highest score found
print(f"The highest score in the class is: {high_score}")
