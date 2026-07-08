import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create DataFrame
student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90]
}

df = pd.DataFrame(student_data)

# =====================================================
# Question 1: Set a Theme
# Expected Output:
# Whitegrid theme is applied to all charts.
# =====================================================

sns.set_theme(style="whitegrid")


# =====================================================
# Question 2: Count Plot
# Expected Output:
# Count plot showing the number of students
# in each course.
# Saved as course_count.png
# =====================================================

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="course")
plt.title("Students by Course")
plt.savefig("course_count.png")
plt.show()


# =====================================================
# Question 3: Bar Plot
# Expected Output:
# Bar plot showing average marks for each course.
# Saved as average_marks_bar.png
# =====================================================

plt.figure(figsize=(6,4))
sns.barplot(data=df, x="course", y="marks")
plt.title("Average Marks by Course")
plt.savefig("average_marks_bar.png")
plt.show()


# =====================================================
# Question 4: Scatter Plot
# Expected Output:
# Scatter plot of Study Hours vs Marks.
# Different colors represent different courses.
# Saved as study_hours_marks_scatter.png
# =====================================================

plt.figure(figsize=(6,4))
sns.scatterplot(
    data=df,
    x="study_hours",
    y="marks",
    hue="course"
)
plt.title("Study Hours vs Marks")
plt.savefig("study_hours_marks_scatter.png")
plt.show()


# =====================================================
# Question 5: Box Plot
# Expected Output:
# Box plot showing marks distribution by course.
# Saved as marks_boxplot.png
# =====================================================

plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="course", y="marks")
plt.title("Marks Distribution by Course")
plt.savefig("marks_boxplot.png")
plt.show()


# =====================================================
# Question 6: Histogram
# Expected Output:
# Histogram of marks with KDE curve.
# Saved as marks_histogram.png
# =====================================================

plt.figure(figsize=(6,4))
sns.histplot(df["marks"], kde=True)
plt.title("Marks Distribution")
plt.savefig("marks_histogram.png")
plt.show()


# =====================================================
# Question 7: Correlation Heatmap
# Expected Output:
# Correlation heatmap of Study Hours,
# Marks and Attendance.
# Saved as student_correlation_heatmap.png
# =====================================================

plt.figure(figsize=(6,4))

corr = df[["study_hours", "marks", "attendance"]].corr()

sns.heatmap(corr, annot=True)

plt.title("Student Metrics Correlation")
plt.savefig("student_correlation_heatmap.png")
plt.show()


# =====================================================
# Question 8: Best Performing Course
# Expected Output:
# Best performing course: AI
# =====================================================

course_avg = df.groupby("course")["marks"].mean()

best_course = course_avg.idxmax()

print("Best performing course:", best_course)