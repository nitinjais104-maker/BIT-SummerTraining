import matplotlib.pyplot as plt

# Question 1: Line Chart (Monthly Sales)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]

plt.figure()
plt.plot(months, monthly_sales, marker='o', label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales_line.png")
plt.close()

# Question 2: Bar Chart (Students by Course)

courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]

plt.figure()
plt.bar(courses, students)
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.savefig("students_by_course_bar.png")
plt.close()

# Question 3: Pie Chart (Course Enrollment Share)

plt.figure()
plt.pie(students, labels=courses, autopct="%1.1f%%")
plt.title("Course Enrollment Share")
plt.savefig("course_enrollment_pie.png")
plt.close()

# Question 4: Scatter Plot (Study Hours vs Marks)

study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]

plt.figure()
plt.scatter(study_hours, marks)
plt.title("Study Hours and Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("study_hours_scatter.png")
plt.close()

# Question 5: Line Chart with Grid and Legend

plt.figure()
plt.plot(months, monthly_sales, label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.savefig("monthly_sales_grid_legend.png")
plt.close()

# Question 6: Compare Two Lines

python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]

plt.figure()
plt.plot(months, python_students, label="Python Students")
plt.plot(months, ai_students, label="AI Students")
plt.title("Course Growth")
plt.xlabel("Month")
plt.ylabel("Students")
plt.legend()
plt.savefig("course_growth.png")
plt.close()

# Question 7: Chart Readability (Rotate labels)

plt.figure()
plt.bar(courses, students)
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("students_by_course_bar_improved.png")
plt.close()

# Question 8: Reflection
# Pie chart is best for comparing course enrollment share because it shows percentage distribution clearly.