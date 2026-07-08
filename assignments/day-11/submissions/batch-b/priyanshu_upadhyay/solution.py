import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90]
}

df = pd.DataFrame(student_data)

sns.set_theme(style="whitegrid")

plt.figure()
sns.countplot(x="course", data=df)
plt.title("Students by Course")
plt.savefig("course_count.png")
plt.close()

plt.figure()
sns.barplot(x="course", y="marks", data=df, estimator="mean")
plt.title("Average Marks by Course")
plt.savefig("average_marks_bar.png")
plt.close()

plt.figure()
sns.scatterplot(x="study_hours", y="marks", hue="course", data=df)
plt.title("Study Hours vs Marks")
plt.savefig("study_hours_marks_scatter.png")
plt.close()

plt.figure()
sns.boxplot(x="course", y="marks", data=df)
plt.title("Marks Distribution by Course")
plt.savefig("marks_boxplot.png")
plt.close()

plt.figure()
sns.histplot(df["marks"], kde=True)
plt.title("Marks Distribution")
plt.savefig("marks_histogram.png")
plt.close()

plt.figure()
corr = df[["study_hours", "marks", "attendance"]].corr()
sns.heatmap(corr, annot=True)
plt.title("Student Metrics Correlation")
plt.savefig("student_correlation_heatmap.png")
plt.close()

best_course = df.groupby("course")["marks"].mean().idxmax()
print("Best performing course:", best_course)