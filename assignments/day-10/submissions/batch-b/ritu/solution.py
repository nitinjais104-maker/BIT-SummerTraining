import matplotlib.pyplot as plt

# QUESTION 1: Line Chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]

plt.plot(months, monthly_sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales_line.png")
plt.close()


# QUESTION 2: Bar Chart
courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]

plt.bar(courses, students)
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.savefig("students_by_course_bar.png")
plt.close()


# QUESTION 3: Pie Chart
courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]

plt.pie(students, labels=courses, autopct="%1.1f%%")
plt.title("Course Enrollment Share")
plt.savefig("course_enrollment_pie.png")
plt.close()


# QUESTION 4: Scatter Plot
study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]

plt.scatter(study_hours, marks)
plt.title("Study Hours and Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("study_hours_scatter.png")
plt.close()


# QUESTION 5: Add Grid and Legend
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]

plt.plot(months, monthly_sales, label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.savefig("monthly_sales_line_updated.png")
plt.close()


# QUESTION 6: Compare Two Lines
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]

plt.plot(months, python_students, label="Python")
plt.plot(months, ai_students, label="AI")
plt.title("Course Growth Over Months")
plt.xlabel("Months")
plt.ylabel("Number of Students")
plt.legend()
plt.savefig("course_growth.png")
plt.close()


# QUESTION 7: Chart Readability
courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]

plt.bar(courses, students)
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("students_by_course_bar_readable.png")
plt.close()


# QUESTION 8: Reflection Comment
# Reflection:
# The Bar Chart (Question 2/7) is the best choice for comparing courses.
# It aligns categorical data on a baseline, making it easy to compare the 
# heights of the bars at a glance. This is more precise for human eyes 
# than trying to judge angles and slice sizes in a Pie Chart.