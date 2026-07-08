import matplotlib.pyplot as plt

# -------------------------------------------------
# Data given in the assignment
# -------------------------------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]

courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]

study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]

python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]


# -------------------------------------------------
# Question 1: Line Chart - Monthly Sales
# -------------------------------------------------
plt.figure()
plt.plot(months, monthly_sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales_line.png")
plt.close()


# -------------------------------------------------
# Question 2: Bar Chart - Students by Course
# -------------------------------------------------
plt.figure()
plt.bar(courses, students)
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.savefig("students_by_course_bar.png")
plt.close()


# -------------------------------------------------
# Question 3: Pie Chart - Course Enrollment Share
# -------------------------------------------------
plt.figure()
plt.pie(students, labels=courses, autopct="%1.1f%%")
plt.title("Course Enrollment Share")
plt.savefig("course_enrollment_pie.png")
plt.close()


# -------------------------------------------------
# Question 4: Scatter Plot - Study Hours vs Marks
# -------------------------------------------------
plt.figure()
plt.scatter(study_hours, marks)
plt.title("Study Hours and Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("study_hours_scatter.png")
plt.close()


# -------------------------------------------------
# Question 5: Line Chart with Grid and Legend
# -------------------------------------------------
plt.figure()
plt.plot(months, monthly_sales, label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.savefig("monthly_sales_line_grid_legend.png")
plt.close()


# -------------------------------------------------
# Question 6: Compare Two Lines - Course Growth
# -------------------------------------------------
plt.figure()
plt.plot(months, python_students, label="Python")
plt.plot(months, ai_students, label="AI")
plt.title("Course Growth Comparison")
plt.xlabel("Month")
plt.ylabel("Students")
plt.legend()
plt.savefig("course_growth.png")
plt.close()


# -------------------------------------------------
# Question 7: Chart Readability - Rotated Labels Bar Chart
# -------------------------------------------------
plt.figure()
plt.bar(courses, students)
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("students_by_course_bar.png")
plt.close()


# -------------------------------------------------
# Question 8: Reflection Comment
# -------------------------------------------------
# The bar chart is the best chart for comparing courses because each course
# is a separate (categorical) item, and a bar chart makes it easy to compare
# the heights of the bars side by side to see which course has more or fewer
# students. A line chart is better suited for showing trends over time, and
# a pie chart is good for showing proportion/share of a whole, but for a
# direct, accurate comparison between distinct categories, a bar chart is
# the clearest choice.
