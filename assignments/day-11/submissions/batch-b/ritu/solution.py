import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DataFrame Creation
student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90]
}
df = pd.DataFrame(student_data)


# QUESTION 1: Set a Theme
sns.set_theme(style="whitegrid")


# QUESTION 2: Count Plot
sns.countplot(data=df, x="course")
plt.title("Students by Course")
plt.savefig("course_count.png")
plt.close()


# QUESTION 3: Bar Plot
sns.barplot(data=df, x="course", y="marks")
plt.title("Average Marks by Course")
plt.savefig("average_marks_bar.png")
plt.close()


# QUESTION 4: Scatter Plot
sns.scatterplot(data=df, x="study_hours", y="marks", hue="course")
plt.title("Study Hours vs Marks")
plt.savefig("study_hours_marks_scatter.png")
plt.close()


# QUESTION 5: Box Plot
sns.boxplot(data=df, x="course", y="marks")
plt.title("Marks Distribution by Course")
plt.savefig("marks_boxplot.png")
plt.close()


# QUESTION 6: Histogram
sns.histplot(data=df, x="marks", kde=True)
plt.title("Marks Distribution")
plt.savefig("marks_histogram.png")
plt.close()


# QUESTION 7: Correlation Heatmap
correlation_matrix = df[["study_hours", "marks", "attendance"]].corr()
sns.heatmap(data=correlation_matrix, annot=True)
plt.title("Student Metrics Correlation")
plt.savefig("student_correlation_heatmap.png")
plt.close()


# QUESTION 8: Best Performing Course
avg_marks_by_course = df.groupby("course")["marks"].mean()
best_course = avg_marks_by_course.idxmax()
print(f"Best performing course: {best_course}")