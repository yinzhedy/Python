#prompt for student name followed by their single score
def prompt_user():
    student_first_name = str(input("Please enter your first name"))
    if student_first_name == "":
        add_student("", -1)
        return
    student_last_name = str(input("Please enter your last name"))
    student_grade = float(input("Please enter your score / grade (0-10)"))
    student_name = student_first_name + student_last_name
    
    add_student(student_name, student_grade)
    return

class_grades= {}

def add_student(name, grade):
    if name == "" or grade not in range (0,11):
        average = average_grades()
        print("The average grade for the class was:", average)
        print("The class information inputted was:", class_grades)
        return
    else:
        class_grades.update({name:grade})
        prompt_user()
    
def average_grades():
    sum = 0
    number_of_grades = 0
    for grade in class_grades.values():
        sum += grade
        number_of_grades += 1
    average = sum / number_of_grades
    return average

prompt_user()

#entering an empty name finishes the inputting of the data

#create a list of all names together with the evaluated average score