class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(self,object):
        StudentDatabase.student_list.append(object)

class Student:
    def __init__(self,name,student_id,department):
        self.__name = name
        self.__student_id = student_id
        self.__department = department
        self.__is_enrolled = False
        StudentDatabase.add_student(self)

    def enroll_student(self,to_enroll):
        if self.__student_id == to_enroll:
            if self.__is_enrolled == True:
                raise Exception("This id is already Enrolled")
            else:
                self.__is_enrolled = True
                print("Enrolled Successfully")
                return True
        else:
            return False
            

    def drop_student(self, to_drop):
        if self.__student_id == to_drop:
            if not self.is_enrolled:
                raise Exception("This student is not enrolled, cannot drop.")
            else:
                self.__is_enrolled = False
                return True
        return False

        
    def view_student_info(self):
        print(f"""
        Student id   : {self.__student_id}
        Student name : {self.__name}
        Department   : {self.__department}
        Enroll Status: {self.__is_enrolled}
        """)
        

db = StudentDatabase()

while True:
    print("""
          1. View All Students
          2. Enroll Student
          3. Drop Student
          4. Exit
""")
    print(f"Enter Your Choice : ")
    choice = input()

    if choice == "1":
        if not StudentDatabase.student_list:
            print(f"No students are available")
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()
    elif choice == "2":
        try:
            id = input("Enter Student ID to Enroll  : ")
            found = False
            for student in StudentDatabase.student_list:
                if student.enroll_student(id):
                    found = True
                    break
            if found == False:
                print(f"Creating New Student ")
                name = input("Enter Student Name: ")
                dpet = input("Enter Department: ")
                Student(name,id,dpet)

                     
        except Exception as exception:
            print(f"Error : {exception}")
    elif choice =="3":
        try:
            id = input("Enter Student ID to Drop Out: ")

            found = False
            for student in StudentDatabase.student_list:
                if student.drop_student(id):
                    found = True
                    break
            if not found:
                raise Exception("This student is not enrolled, cannot drop.")      
        except Exception as exception:
            print(f"Error : {exception}")
    elif choice == "4":
        break
    else:
        continue
        



         
