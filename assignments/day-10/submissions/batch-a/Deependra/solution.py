import matplotlib.pyplot as plt

# ---------------- Data ----------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]

courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]

# ---------------- Q1: Line Chart ----------------
plt.figure()
plt.plot(months, monthly_sales, color="blue", marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales_line.png")
plt.close()

# ---------------- Q2: Bar Chart ----------------
plt.figure()
plt.bar(courses, students, color=["red", "green", "blue", "orange"])
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.savefig("students_by_course_bar.png")
plt.close()

# ---------------- Q3: Pie Chart ----------------
plt.figure()
plt.pie(
    students,
    labels=courses,
    autopct="%1.1f%%",
    colors=["gold", "lightblue", "lightgreen", "pink"]
)
plt.title("Course Enrollment Share")
plt.savefig("course_enrollment_pie.png")
plt.close()

# ---------------- Q4: Scatter Plot ----------------
study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]

plt.figure()
plt.scatter(study_hours, marks, color="purple")
plt.title("Study Hours and Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("study_hours_scatter.png")
plt.close()

# ---------------- Q5: Line with Grid + Legend ----------------
plt.figure()
plt.plot(months, monthly_sales, label="Sales", color="blue", marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.savefig("monthly_sales_grid.png")
plt.close()

# ---------------- Q6: Compare Lines ----------------
python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]

plt.figure()
plt.plot(months, python_students, label="Python", color="green", marker="o")
plt.plot(months, ai_students, label="AI", color="red", marker="s")
plt.title("Course Growth")
plt.xlabel("Month")
plt.ylabel("Students")
plt.legend()
plt.savefig("course_growth.png")
plt.close()

# ---------------- Q7: Readable Bar Chart ----------------
plt.figure()
plt.bar(courses, students, color="skyblue")
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("students_by_course_bar_readable.png")
plt.close()

# ---------------- Q8: Reflection ----------------

# Reflection:
# A bar chart is the best choice for comparing the number of
# students across different courses because it makes
# differences between categories easy to see and compare.