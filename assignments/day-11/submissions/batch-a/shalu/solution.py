import os
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90],
}

# Question 1: Set a theme
sns.set_theme(style="whitegrid")
df = pd.DataFrame(student_data)

output_dir = os.path.dirname(os.path.abspath(__file__))

# Question 2: Count plot
sns.countplot(data=df, x="course")
plt.title("Students by Course")
plt.savefig(os.path.join(output_dir, "course_count.png"))
plt.close()

# Question 3: Bar plot
sns.barplot(data=df, x="course", y="marks", estimator="mean")
plt.title("Average Marks by Course")
plt.savefig(os.path.join(output_dir, "average_marks_bar.png"))
plt.close()

# Question 4: Scatter plot
sns.scatterplot(data=df, x="study_hours", y="marks", hue="course")
plt.title("Study Hours vs Marks")
plt.savefig(os.path.join(output_dir, "study_hours_marks_scatter.png"))
plt.close()

# Question 5: Box plot
sns.boxplot(data=df, x="course", y="marks")
plt.title("Marks Distribution by Course")
plt.savefig(os.path.join(output_dir, "marks_boxplot.png"))
plt.close()

# Question 6: Histogram
sns.histplot(data=df, x="marks", kde=True)
plt.title("Marks Distribution")
plt.savefig(os.path.join(output_dir, "marks_histogram.png"))
plt.close()

# Question 7: Correlation heatmap
correlation = df[["study_hours", "marks", "attendance"]].corr()
sns.heatmap(correlation, annot=True)
plt.title("Student Metrics Correlation")
plt.savefig(os.path.join(output_dir, "student_correlation_heatmap.png"))
plt.close()

# Question 8: Best performing course
average_marks = df.groupby("course")["marks"].mean()
best_course = average_marks.idxmax()
print("Best performing course:", best_course)
