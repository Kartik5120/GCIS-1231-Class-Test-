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
    def print_students(self):
        

        return None

def main():

    print("")
    print("Student 1:-")
    obj1 = student()                    #Instataite the class to create an object
    print("The current GPA for Student1 is: ", obj1.gpa)
    obj1.set_gpa(4.0)
    print("The new GPA for Student1 is: ", obj1.gpa)
    obj1.set_total_credits(100)
    print("The total credits of Student1 is: ", obj1.total_credits)

    print(" ")
    print("Student2 :-")
    obj2 = student()                    #Instataite the class to create an object
    print("The current GPA for Student2 is: ", obj2.gpa)
    obj2.set_gpa(3.0)
    print("The new GPA for Student2 is: ", obj2.gpa)
    obj2.set_total_credits(50)
    print("The total credits of Student2 is: ", obj2.total_credits)

    print("")

main()