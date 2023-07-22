import os
 
semesterNo=int(input("Enter semester number: "))
os.mkdir(f"Semester{semesterNo}")

numberOfcources=int(input("Enter number of cources in this term: "))
courseNamesList=list()
print("Enter names of courses:")
i=int(0)
while i < numberOfcources:
    line="Course "+str(i+1)+": "
    courseNameInput=str(input(line))
    courseNamesList.append(courseNameInput)
    i+=1

for j in courseNamesList:
    os.mkdir(f"Semester{semesterNo}\\{j}")