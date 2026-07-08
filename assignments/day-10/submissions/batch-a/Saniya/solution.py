# Day 10 Assignment
#==========================================================>>>
import matplotlib.pyplot as plt
# Use this data:
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]
courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]
#==========================================================>>>
# Question 1: Line Chart

# Create a line chart of `months` and `monthly_sales`.
plt.plot(months, monthly_sales, marker='o', color='b')
plt.title('Monthly Sales', style='italic')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.savefig('monthly_sales_line.png')
plt.show()
#==========================================================>>>
# Question 2: Bar Chart
# Create a bar chart of `courses` and `students`.
plt.bar(courses, students, color='g')
plt.title('Students by Course', style='italic')
plt.xlabel('Course')
plt.ylabel('Students')
plt.savefig('students_by_course_bar.png')
plt.show()
#==========================================================>>>
# Question 3: Pie Chart
# Create a pie chart of `courses` and `students`.
plt.pie(students, labels=courses, autopct='%1.1f%%')
plt.title('Course Enrollment Share', style='italic')
plt.savefig('course_enrollment_pie.png')
plt.show()
#==========================================================>>>
# Question 4: Scatter Plot

# Use these values to create a scatter plot:

# ```python
study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]
plt.scatter(study_hours, marks)
plt.title('Study Hours and Marks', style='italic')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.savefig('study_hours_scatter.png')
plt.show()
#==========================================================>>>
# Question 5: Add Grid and Legend
# Create a line chart for the monthly sales data. Add a grid and a legend named `Sales`.
plt.plot(months, monthly_sales, label='Sales')
plt.grid(True)
plt.legend()
plt.show()
#==========================================================>>>
## Question 6: Compare Two Lines
# Plot both lines against `months`, add a legend, title, and axis labels. Save as `course_growth.png`.
# Use these values:
python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]
plt.plot(months, python_students, label='Python', marker='o')
plt.plot(months, ai_students, label='AI', marker='s')
plt.title('Course Growth', style='italic')
plt.xlabel('Month')
plt.ylabel('Students')
plt.legend()
plt.grid(True)
plt.savefig('course_growth.png')
plt.show()
#==========================================================>>>
# Question 7: Chart Readability
# For the bar chart from Question 2, rotate the course labels by 20 degrees and use `plt.tight_layout()` before saving.
plt.bar(courses, students, color='g')
plt.title('Students by Course', style='italic')
plt.xlabel('Course')
plt.ylabel('Students')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('students_by_course_bar_rotated.png')
plt.show()
#==========================================================>>>
# Question 8: Reflection Comment
# Add a Python comment at the bottom of `solution.py` that explains which chart is best for comparing courses and why.
# Bar chart is best for comparing courses because it allows for easy visual comparison of the number of students in each course.