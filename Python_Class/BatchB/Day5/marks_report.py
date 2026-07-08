with open("marks.txt", "w") as file:
    file.write("Rahul,85\n")
    file.write("Priya,92\n")
    file.write("Aman,76\n")

total = 0
count = 0

with open("marks.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        marks = int(marks)
        print(name, ":", marks)

        total += marks
        count += 1
average = total  / count
print("Average Marks:", average)

# Update a File , Delete one Record