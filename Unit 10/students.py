class student:
    """Represents a template for students"""
    id = 0
    name = None 
    gpa = 0.0
    total_credits = 0

    # METHOD FOR MODIFYING THE GPA
    def set_gpa(self, new_gpa):         #Self refers to the current object
        self.gpa = new_gpa

    # METHOD FOR MODIFYING THE TOTAL CREDITS
    def set_total_credits(self, new_credits):
        self.total_credits = new_credits

    # METHOD TO PRINT ALL OFF THE STUDENT'S DATA ATTRIBUTES
    def print_student_info(self):
        print(" ID is: ", self.id, "\n", "Name is: ", self.name, "\n", "GPA is: ", self.gpa, "\n", "Credits are: ", self.total_credits)

def main():

    print("")
    print("Student 1:-")
    obj1 = student()                    # Instataite the class to create an object
    # obj1.set_gpa(4.0)
    student.set_gpa(obj1, 4.0)          # Identical to the line above in the outcome
    obj1.set_total_credits(100)
    obj1.print_student_info()

    print(" ")
    print("Student2 :-")
    obj2 = student()                    # Instataite the class to create an object
    obj2.set_gpa(3.0)
    obj2.set_total_credits(50)
    obj2.print_student_info()
    print("")

main()