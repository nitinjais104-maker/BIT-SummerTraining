
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Use this data to create a DataFrame:

student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90]
}
df = pd.DataFrame(student_data)
# Question 1: Set a Theme
# Set a Seaborn theme using sns.set_theme(style="whitegrid") before creating charts.
sns.set_theme(style="whitegrid")

# Question 2: Count Plot
# Create a count plot showing the number of students in each course.
# Title: Students by Course
# Save as course_count.png
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="course")
plt.title("Students by Course")
plt.tight_layout()
plt.savefig("course_count.png")
plt.close()

# Question 3: Bar Plot
# Create a bar plot showing the average marks for each course.
# Title: Average Marks by Course
# Save as average_marks_bar.png
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="course", y="marks", estimator="mean")
plt.title("Average Marks by Course")
plt.tight_layout()
plt.savefig("average_marks_bar.png")
plt.close()

# Question 4: Scatter Plot
# Create a scatter plot showing study_hours on the x-axis and marks on the y-axis. Use course as the color grouping.
# Title: Study Hours vs Marks
# Save as study_hours_marks_scatter.png
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="study_hours", y="marks", hue="course", s=100)
plt.title("Study Hours vs Marks")
plt.tight_layout()
plt.savefig("study_hours_marks_scatter.png")
plt.close()

# Question 5: Box Plot
# Create a box plot of marks grouped by course.
# Title: Marks Distribution by Course
# Save as marks_boxplot.png
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="course", y="marks")
plt.title("Marks Distribution by Course")
plt.tight_layout()
plt.savefig("marks_boxplot.png")
plt.close()

# Question 6: Histogram
# Create a histogram of marks with a KDE curve.
# Title: Marks Distribution
# Save as marks_histogram.png
plt.figure(figsize=(6, 4))
sns.histplot(data=df, x="marks", kde=True)
plt.title("Marks Distribution")
plt.tight_layout()
plt.savefig("marks_histogram.png")
plt.close()

# Question 7: Correlation Heatmap
# Create a correlation heatmap for study_hours, marks, and attendance.
# Use annot=True
# Title: Student Metrics Correlation
# Save as student_correlation_heatmap.png
plt.figure(figsize=(6, 4))
corr = df[["study_hours", "marks", "attendance"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Student Metrics Correlation")
plt.tight_layout()
plt.savefig("student_correlation_heatmap.png")
plt.close()

# Question 8: Best Performing Course
# Use Pandas groupby to find the course with the highest average marks and print it.
# Expected Output:
# Best performing course: AI
best_course = df.groupby("course")["marks"].mean().idxmax()
print(f"Best performing course: {best_course}")