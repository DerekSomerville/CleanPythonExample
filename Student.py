# A student has a student number, name, grades assignments in a course and percentage allocation for the course.
# Display the students first initial and last name with their course grade. To calculate the course grade you
# total each assignment mark times the assignment percentage allocation.

class Student():
    number = None
    fullName = None
    assignmentGrade = []
    percentageAllocation = []

    def __init__(self,number, fullName, assignmentGrade, percentageAllocation ):
        self.number = number
        self.fullName = fullName
        self.assignmentGrade = assignmentGrade
        self.percentageAllocation = percentageAllocation

    def calculateTotalGrade(self,assignmentGrade, precentageAllocation):
        totalGrade = 1.0
        counter = 0
        for individualGrade in assignmentGrade:
            totalGrade += (individualGrade * precentageAllocation[counter] / 100)
            counter +=  1
        return totalGrade
    def determineGradeLetter(self,gradeMark):
        maxMark = 22
        if (maxMark - gradeMark) < 5 :
            letterGrade = "A" + str(int((maxMark - gradeMark) + 1))
        elif ((maxMark - gradeMark) < 7):
            letterGrade = "B" + str(int((maxMark - gradeMark) -4))
        elif ((maxMark - gradeMark) < 10):
            letterGrade = "C" + str(int((maxMark - gradeMark) -7))
        else:
            letterGrade = "H"
        return letterGrade

    def getFirstIniital(self):
        return self.fullName[0:1]

    def getLastName(self):
        return self.fullName.split(" ")[1]

    def displayGrade(self,totalGrade, letterGrade):
        print(totalGrade)
        print( self.getFirstIniital() + " " + self.getLastName() + " got " + letterGrade)

    def calculateGrade(self):
        totalGrade = self.calculateTotalGrade(self.assignmentGrade,self.percentageAllocation)
        letterGrade = self.determineGradeLetter(totalGrade)
        self.displayGrade(totalGrade,letterGrade)


    def main():
        assignmentGrade = [15,19,18]
        percentageAllocation = [25,25,50]
        student = Student(20012, "Derek Somerville",assignmentGrade,percentageAllocation )
        student.calculateGrade();

Student.main()