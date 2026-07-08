#create a list of 5 student name and print it
list=["Nanda","Anil","Rahul","Aman","Rudra"]
print(list)

#add new student name to the list
list.append("Mohan")
print(list)

#create a tuple of 5 city names and print the second city
tpl=("Varanasi","Haridwar","Nasik","Kolkata","Kanpur")
print(tpl[1])


#create a set of 5 course name and add one new course
courses = {"AI","DS","C","Java","Python"}
courses.add('ML')
print(courses)


#create a dictionary for one student with name, branch, batch and marks
dict1={"Name":"Nanda","Branch":"CS","Batch":"B","Marks":'87'}
print(dict1)

#print the student dictionary in a readable format
student={'name':'Ankita','age':'21', 'course':'B.Tech','city':'Gorakhpur'}
print("Student Details:")
for key, value in student.items():
    print(key,':', value)