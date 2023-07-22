class Course:
    courseName=None
    assignmentQuantity=None
    assignmentObtainedMarks=[] 
    assignmentTotalMarks=[] 
    quizQuantity=None
    quizObtainedMArks=[] 
    quizTotalMarks=[] 
    cpQuantity=None
    cpObtaineddMarks=[] 
    cpTotalMarks=[] 
    midsQuantity=None
    midObtainedMarks=[] 
    midTotalMarks=[] 
    FinalOtainedMarks=0
    FinalTotalMarks=0
    def __init__(self,courseName=None,assignmentQuantity=0,quizQuantity=0,cpQuantity=0,midsQuantity=0,final=0):
        if courseName!=None:
            self.courseName=courseName

        if int(assignmentQuantity)>0:
            assignmentText="Assignment {}: "
            assignmentText2="Enter {} marks: "
            self.assignmentQuantity=0
            while int(self.assignmentQuantity)<int(assignmentQuantity):
                print(assignmentText.format(str(int(self.assignmentQuantity)+1)))
                userInput=input(assignmentText.format("obtained"))
                userInput2=input(assignmentText2.format("Total"))
                self.assignmentObtainedMarks.append(userInput)
                self.assignmentTotalMarks.append(userInput2)
                self.assignmentQuantity+=1
 
        if int(quizQuantity)>0:
            quizText="Quiz {}: "
            self.quizQuantity=0
            while int(self.quizQuantity)<int(quizQuantity):
                userInput=input(quizText.format(str(int(self.quizQuantity)+1)))
                self.quiz.append(userInput)
                self.quizQuantity+=1
 
        if int(cpQuantity)>0:
            cpText="Enter marks of Cp {}: "
            self.cpQuantity=0
            while int(self.cpQuantity)<int(cpQuantity):
                userInput=input(cpText.format(str(int(self.cpQuantity)+1)))
                self.cp.append(userInput)
                self.cpQuantity+=1
        
        if int(midsQuantity)>0:
            midText="Enter marks of Mid {}: "
            self.midsQuantity=0
            if int(midsQuantity)>1:
                while int(self.midsQuantity)<int(midsQuantity):
                    self.mid.append(userInput)
                    userInput=input(midText.format(str(int(self.midsQuantity)+1)))
                    self.midsQuantity+=1
            else:   
                self.midsQuantity=1
                userInput=input("Enter marks of mid: ")
                self.mid.append(userInput)
        if bool(final)!=0:
            self.final=input("Enter marks in final: ")
    
    def display(self):
        print(self.assignment)
        print(self.quiz)
        print(self.cp)
        print(self.mid)
        print(self.final)
    def calculateGp():
        pass
if __name__=="__main__":##will only exicute if the course is run through python Course.py
    print("Course.py is exicuted")