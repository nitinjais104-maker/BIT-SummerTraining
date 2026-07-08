import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]
courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]

### Question 1: Line Chart
plt.figure()
plt.plot(months, monthly_sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales_line.png")
plt.close()

### Question 2: Bar Chart
plt.figure()
plt.bar(courses, students)
plt.title("Students by Course ")
plt.xlabel("Course")
plt.ylabel("Students")
plt.savefig("students_by_course_bar.png")
plt.close()

### Question 3: Pie Chart
plt.figure()
plt.pie(students, labels=courses, autopct="%1.1f%%")
plt.title("Course Enrollment Share")
plt.savefig("course_enrollment_pie.png")
plt.close()

### Question 4: Scatter Plot
study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]
plt.figure()
plt.scatter(study_hours, marks)
plt.title("Study Hours and Marks ")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("study_hours_scatter.png")
plt.close()

### Question 5: Add Grid and Legend
plt.figure()
plt.plot(months, monthly_sales, label="Sales")
plt.grid()
plt.legend()
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

### Question 6: Compare Two Lines
python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]
plt.plot(months,python_students,label="Python",color="blue")
plt.plot(months, ai_students, label="AI", color= "r")
plt.legend()
plt.title("Python vs AI Course Groth")
plt.xlabel("Months")
plt.ylabel("Students")
plt.savefig("course_growth.png")
plt.close()

### Question 7: Chart Readability

plt.figure()
plt.bar(courses, students)
plt.title("Students by Course ")
plt.xlabel("Course")
plt.ylabel("Students")
plt.xticks(rotation = 20)
plt.tight_layout()
plt.savefig("students_by_course_bar.png")
plt.close()

### Question 8: Reflection Comment

# Bar chart is best for comparing courses .
# it clearly shows the difference in the number of students enrolled in each course.