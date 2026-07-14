import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(__file__)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]
courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]
study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]
python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]

# Question 1: Line Chart
plt.figure()
plt.plot(months, monthly_sales, marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.savefig(os.path.join(BASE_DIR, 'monthly_sales_line.png'))
plt.close()

# Question 2: Bar Chart
plt.figure()
plt.bar(courses, students)
plt.title('Students by Course')
plt.xlabel('Course')
plt.ylabel('Students')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, 'students_by_course_bar.png'))
plt.close()

# Question 3: Pie Chart
plt.figure()
plt.pie(students, labels=courses, autopct='%1.1f%%')
plt.title('Course Enrollment Share')
plt.savefig(os.path.join(BASE_DIR, 'course_enrollment_pie.png'))
plt.close()

# Question 4: Scatter Plot
plt.figure()
plt.scatter(study_hours, marks)
plt.title('Study Hours and Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.savefig(os.path.join(BASE_DIR, 'study_hours_scatter.png'))
plt.close()

# Question 5: Add Grid and Legend
plt.figure()
plt.plot(months, monthly_sales, marker='o', label='Sales')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(BASE_DIR, 'monthly_sales_line_updated.png'))
plt.close()

# Question 6: Compare Two Lines
plt.figure()
plt.plot(months, python_students, marker='o', label='Python Students')
plt.plot(months, ai_students, marker='o', label='AI Students')
plt.title('Course Growth')
plt.xlabel('Month')
plt.ylabel('Students')
plt.legend()
plt.savefig(os.path.join(BASE_DIR, 'course_growth.png'))
plt.close()

# Question 7: Chart Readability
# The bar chart labels have been rotated by 20 degrees and tight_layout is used above

# Question 8: Reflection Comment
# A bar chart is best for comparing courses because it makes each course count visible side by side.
