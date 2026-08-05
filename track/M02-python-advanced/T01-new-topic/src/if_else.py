#Read marks, attendance and project completion status
marks = int(input())
attendance_percentage = int(input())
project_completion_status = input()

# Check the academic requirements
if marks >= 60:
    if attendance_percentage >= 75:
        if project_completion_status == "yes":
            print("Eligible")
        else:
            print("Not Eligible")
else:
    print("Not Eligible")


    # Check the project completion status