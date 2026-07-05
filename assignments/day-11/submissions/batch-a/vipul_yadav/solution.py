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

### Question 1: Set a Theme
df = pd.DataFrame(student_data)
sns.set_theme(style="whitegrid")

### Question 2: Count Plot
sns.countplot(data=df,x="course")
plt.title("Students by Course" )
plt.savefig("course_count.png")
plt.close()

### Question 3: Bar Plot
# Create a bar plot showing the average marks for each course.
sns.barplot(data=df, x="course",y= "marks")
plt.title("Average Marks by Course")
plt.savefig("average_marks_bar.png")
plt.close()

### Question 4: Scatter Plot
sns.scatterplot(data=df, x="marks",y="course",hue="course")
plt.title("Study Hours vs Marks")
plt.savefig("study_hours_marks_scatter.png")
plt.close()

### Question 5: Box Plot
sns.boxplot(data=df,x="course",y="marks")
plt.title("Marks Distribution by Course")
plt.savefig("marks_boxplot.png")
plt.close()

### Question 6: Histogram

sns.histplot(data=df,x="marks",kde = True)
plt.title("Marks Distribution")
plt.savefig("marks_histogram.png")
plt.close()

### Question 7: Correlation Heatmap

correlation =df[["study_hours","marks","attendance"]].corr()
sns.heatmap(correlation,annot=True)
plt.title("Student Metrics Correlation")
plt.savefig("student_correlation_heatmap.png")
plt.close()

### Question 8: Best Performing Course
average_marks = df.groupby("course")["marks"].mean()
best_course = average_marks.idxmax()
print("Best performing course:",best_course)