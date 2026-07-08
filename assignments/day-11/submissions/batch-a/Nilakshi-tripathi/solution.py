import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Student Data

student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90]
}


# Create DataFrame

df = pd.DataFrame(student_data)


# Question 1
# Set Seaborn Theme

sns.set_theme(style="whitegrid")

# Question 2
# Count Plot

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="course")
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("course_count.png")
plt.close()


# Question 3
# Bar Plot

plt.figure(figsize=(6,4))
sns.barplot(data=df, x="course", y="marks")
plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("average_marks_bar.png")
plt.close()


# Question 4
# Scatter Plot

plt.figure(figsize=(6,4))
sns.scatterplot(
    data=df,
    x="study_hours",
    y="marks",
    hue="course",
    s=120
)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("study_hours_marks_scatter.png")
plt.close()


# Question 5
# Box Plot

plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="course", y="marks")
plt.title("Marks Distribution by Course")
plt.xlabel("Course")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("marks_boxplot.png")
plt.close()


# Question 6
# Histogram with KDE

plt.figure(figsize=(6,4))
sns.histplot(df["marks"], kde=True)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("marks_histogram.png")
plt.close()


# Question 7
# Correlation Heatmap

correlation = df[["study_hours", "marks", "attendance"]].corr()

plt.figure(figsize=(6,4))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Student Metrics Correlation")
plt.tight_layout()
plt.savefig("student_correlation_heatmap.png")
plt.close()


# Question 8
# Best Performing Course

average_marks = df.groupby("course")["marks"].mean()

best_course = average_marks.idxmax()

print("Best performing course:", best_course)