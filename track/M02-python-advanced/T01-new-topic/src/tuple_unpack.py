name = input()
course = input()
score = int(input())

# Create the tuple
student_record =(name,course,score)

# Unpack the tuple
n,c,s = student_record

# Display the unpacked values
print("Name:",n)
print("Course:",c)
print("Score:",s)