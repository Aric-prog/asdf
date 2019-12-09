class Person():
    __name : str
    __address : str
    def __init__(self,name,address):
        self.__name = name
        self.__address = address

    def getName(self):
        return self.__name

    def setAddress(self,address):
        self.__address = address
    
    def getAddress(self):
        return self.__address
        
    def toString(self):
        print(self.__name)
    
class Student(Person):
    __numCourses : int = 0
    __courses : list = []
    __grades : list = []

    def __init__(self,name,address,courses):
        for i in courses:
            self.__courses.append(i)
            self.__grades.append(0)
        super().__init__(name,address)
    
    def toString(self):
        return "Student : " + super().getName() + "\nAddress : " + super().getAddress()
    
    def enrollCourses(self,courses):
        for i in courses:
            self.__courses.append(i)
            self.__grades.append(0)

    def addCourseGrade(self,course,grade):
        self.__grades[self.__courses.index(course)] = grade
        
    def printGrades(self):
        for i in self.__courses:
            print(i, " : ", self.__grades[self.__courses.index(i)])
    
    def getAverageGrade(self):
        return (sum(self.__grades)) / len(self.__grades)

class Teacher(Person):
    __numCourses : int = 0
    __courses : list = []

    def __init__(self,name,address):
        super().__init__(name,address)
    
    def addCourse(self,course):
        self.__numCourses += 1
        self.__courses.append(course)
        return not course in self.__courses
    
    def removeCourse(self,course):
        self.__courses.remove(course)
        return course in self.__courses

    def toString(self):
        return "Teacher :" , super().getName(), "\n" , super().getAddress()
    
    def getCourses(self):
        return self.__courses

teacherArr : list = []
studentArr : list = []
def addTeacher(name,address):
    teacherArr.append(Teacher(name,address))

def addStudent(name,address,courses):
    studentArr.append(Student(name,address,courses))

addTeacher("Dovahkiin","homeless")
print(teacherArr[0].addCourse("PDM"))
teacherArr[0].addCourse("Pancasila")
print(teacherArr[0].getCourses())

addStudent("Bentele","Binus Square", teacherArr[0].getCourses())
studentArr[0].addCourseGrade("PDM", 90.0)
studentArr[0].addCourseGrade("Pancasila" , 85.0)
studentArr[0].printGrades()
print(studentArr[0].getAverageGrade())

print(studentArr[0].toString())