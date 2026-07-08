# file = open("students.txt", "r")
# content = file.read()
# print(content)
# file.close()


with open("students.txt", "r") as file:
    content = file.read()
    print(content)