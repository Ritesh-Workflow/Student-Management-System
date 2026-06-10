#==============================================
# <<<<<<<< STUDENT MANAGEMENT SYSTEM >>>>>>>
#==============================================



#==============================================
#              STUDENT CLASS
#==============================================

class Student :
    def __init__(self,id,name,course,fees):
        self.id=id
        self.name=name
        self.course=course
        self.fees=fees


students=[]

#==============================================
#               LOAD DATA FROM FILE
#==============================================
def load_Data():
    try :
        with open("students.txt","r") as file:
            for line in file:
                data=line.strip().split(",")
                id=data[0]
                name=data[1]
                course=data[2]
                fees=int(data[3])
                students.append(Student(id,name,course,fees))

    except FileNotFoundError:
        print("Student file not found.")
        print("New file will be created.")



#==============================================
#              SAVE DATA TO FILE
#==============================================

def save_data():
    with open("students.txt","w") as file :
        for student in students:
            file.write(
                f"{student.id},"
                f"{student.name},"
                f"{student.course},"
                f"{student.fees}\n"
            )



#==============================================
#              ADD STUDENT
#==============================================
def Add_Student():
      
      student_id=input("Enter Student ID :")
      for student in students:
          if student.id==student_id:
              print("Student ID already exist")
          while student_id==student.id :
              student_id=input("Enter Diffrent ID :")
        
      name=input("Enter Name :")
      if name=="":
          print("Name Cannot be empty")
          name=input("Enter Valid Name :")

      course=input("Enter Course :")

      fees=int((input("Enter Fees :")))
      if fees<0:
          print("Invalid Fee Amount")
          while fees<=0:
              fees=int(input("Fee Cannot Be Negative :"))


      student=Student(student_id,name,course,fees)
      students.append(student)
      print("Student Added Succesfully!")



#==============================================
#              VIEW STUDENT
#==============================================
def View_Student():
    if len(students)==0:
        print("No Student Data Available")
    else :
        print("ID ","Name ","Course ","Fees ")
        for student in students:
            print(student.id,student.name,student.course,student.fees)


#==============================================
#              SEARCH STUDENT
#==============================================
def Search_Student():
    search_id=input("Enter Student ID :")
    found=False
    for student in students:
        if search_id==student.id :
            print("ID :",student.id)
            print("Name :",student.name)
            print("Course :",student.course)
            print("Fees :",student.fees)
            found=True
    if found==False :
        print("Student Not Found")


#==============================================
#              UPDATE FEES
#==============================================
def Update_Fees():
    update_id=input("Enter ID :")
    found=False
    for student in students:
        if update_id==student.id:
            student.fees=int(input("Enter new Fees :"))
            if student.fees<0:
                print("Fee Cannot be negative")
                while student.fees<=0:
                    student.fees=int(input("Enter Valid Fee :"))
            print("Fees Updated Succesfully!")
            found=True
    if found==False:
        print("Student Not Found ")
        
    
                               
#==============================================
#              DELETE STUDENT
#==============================================
def Delete_Student():
    delete_id=input("Enter ID :")
    found=False
    for student in students:
        if delete_id==student.id:
            students.remove(student)
            print("Student Remove Succesfully!")
            found=True
    if found==False:
        print("Record Not Found")


#==============================================
#              TOTAL COLLECTION
#==============================================
def total_collection():
    total=0
    for student in students:
       total+=student.fees
    print("Total Collection :",total)



#==============================================
#              PROGRAM START
#==============================================

load_Data()

choice=0
while choice!=7 :
    print("======Student Management System======")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Fees")
    print("5. Delete Student")
    print("6. Total Collection")
    print("7. Exit")
    try :
        choice=int(input("Enter a Choice no :"))
        
        if choice==1:
            Add_Student()

        elif choice==2:
            View_Student()

        elif choice==3:
            Search_Student()

        elif choice==4:
            Update_Fees()

        elif choice==5:
            Delete_Student()

        elif choice==6:
            total_collection()

        elif choice==7:
            save_data()
            print("Data Saved Succefuliy.")
            print("THANK YOU !")
            exit

        else :
            print("Enter Choice Between 1 to 7")
        
    except ValueError:
        print("Enter a valid number.")


