from Course import Course

semesterCourses=[]
semesterCoursesQuantity=int(input("Enter number of courses in this semester: "))

courseName="noName"
assignmentQuantity=0
quizQuantity=0
cpQuantity=0
midsQuantity=0

i=0
while int(i) < semesterCoursesQuantity:
    print("Course No: ",int(i)+1)
    courseName=input("Enter the name of this course: ")
    assignmentQuantity=input("Enter number of assignments in this course: ")
    quizQuantity=input("Enter number of quizes in this course: ")
    cpQuantity=input("Enter number of Cps in this course: ")
    midsQuantity=input("Enter number of mids in this course: ")
    semesterCourses.append(Course(courseName,assignmentQuantity,quizQuantity,cpQuantity,midsQuantity,1))
    # print(courseName,assignmentQuantity,quizQuantity,cpQuantity,midsQuantity)
    i+=1
i=0
while i<semesterCoursesQuantity:
    semesterCourses[i].display()
    i+=1