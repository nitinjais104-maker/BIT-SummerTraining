import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]

courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]

# ==================================================
# Question 1: Line Chart
# Expected Output:
# A line chart showing monthly sales.
# Title: Monthly Sales
# X-axis: Month
# Y-axis: Sales
# Saved as monthly_sales_line.png
# ==================================================

plt.figure(figsize=(6,4))
plt.plot(months, monthly_sales, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales_line.png")
plt.show()


# ==================================================
# Question 2: Bar Chart
# Expected Output:
# A bar chart showing students by course.
# Title: Students by Course
# X-axis: Course
# Y-axis: Students
# Saved as students_by_course_bar.png
# ==================================================

plt.figure(figsize=(6,4))
plt.bar(courses, students)
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.savefig("students_by_course_bar.png")
plt.show()


# ==================================================
# Question 3: Pie Chart
# Expected Output:
# A pie chart showing course enrollment share.
# Percentage labels displayed.
# Saved as course_enrollment_pie.png
# ==================================================

plt.figure(figsize=(6,6))
plt.pie(students, labels=courses, autopct="%1.1f%%")
plt.title("Course Enrollment Share")
plt.savefig("course_enrollment_pie.png")
plt.show()


# ==================================================
# Question 4: Scatter Plot
# Expected Output:
# A scatter plot of Study Hours vs Marks.
# Title: Study Hours and Marks
# Saved as study_hours_scatter.png
# ==================================================

study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]

plt.figure(figsize=(6,4))
plt.scatter(study_hours, marks)
plt.title("Study Hours and Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("study_hours_scatter.png")
plt.show()


# ==================================================
# Question 5: Add Grid and Legend
# Expected Output:
# A line chart with grid and legend.
# Legend name: Sales
# ==================================================

plt.figure(figsize=(6,4))
plt.plot(months, monthly_sales, marker='o', label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.show()


# ==================================================
# Question 6: Compare Two Lines
# Expected Output:
# A line chart comparing Python and AI students.
# Saved as course_growth.png
# ==================================================

python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]

plt.figure(figsize=(6,4))
plt.plot(months, python_students, marker='o', label="Python")
plt.plot(months, ai_students, marker='o', label="AI")
plt.title("Course Growth")
plt.xlabel("Month")
plt.ylabel("Students")
plt.legend()
plt.savefig("course_growth.png")
plt.show()


# ==================================================
# Question 7: Chart Readability
# Expected Output:
# Bar chart with rotated labels and tight layout.
# Saved as students_by_course_bar_readable.png
# ==================================================

plt.figure(figsize=(6,4))
plt.bar(courses, students)
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("students_by_course_bar_readable.png")
plt.show()


# ==================================================
# Question 8: Reflection Comment
# Expected Output:
# Bar charts are best for comparing courses because
# they clearly show differences in the number of
# students enrolled in each course.