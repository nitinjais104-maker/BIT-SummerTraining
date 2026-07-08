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
df=pd.DataFrame(student_data)
# 1. Set the theme
sns.set_theme(style="whitegrid")
# 2.
plt.hist(df["course"],bins=5)
plt.title("Stuent by Course")
plt.xlabel("Couse")
plt.ylabel("Numbers of Student ")
plt.savefig("course.count.png")
plt.show()
# 3. 
sns.barplot(x="course", y="marks", data=df)

plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("Average Marks")

plt.savefig("average_marks_bar.png")
plt.show()
# 4.
plt.figure(figsize=(6,4))

sns.scatterplot(
    x="study_hours",
    y="marks",
    hue="course",
    data=df
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.savefig("study_hours_marks_scatter.png")
plt.show()
# 5.
plt.figure(figsize=(6,4))

sns.boxplot(
    x="course",
    y="marks",
    data=df
)

plt.title("Marks Distribution by Course")
plt.xlabel("Course")
plt.ylabel("Marks")

plt.savefig("marks_boxplot.png")
plt.show()
# 6. 
plt.figure(figsize=(6,4))

sns.histplot(
    data=df,
    x="marks",
    bins=5,
    kde=True,
    color="skyblue",
    edgecolor="black",
)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.savefig("marks_histogram.png")
plt.show()
# 7.
plt.figure(figsize=(6,4))

corr = df[["study_hours", "marks", "attendance"]].corr()

sns.heatmap(corr, annot=True)

plt.title("Student Metrics Correlation")

plt.savefig("student_correlation_heatmap.png")
plt.show()
# 8.
avg_marks = df.groupby("course")["marks"].mean()

best_course = avg_marks.idxmax()

print("Best performing course:", best_course)