"""A typical input screenshot might be as follows:

Student ID:1001             Student ID:1002             Student ID:1003
Enter Q1: 100               Enter Q1: 90                Enter Q1: 60
Enter Q2: 80                Enter Q2: 100               Enter Q2: 35
Enter Final: 80             Enter Final: 80             Enter Final: 76

Student ID:0

The corresponding output screenshot would be as follows:

[[1001, 100.0, 80.0, 80.0, 84.0], [1002, 90.0, 100.0, 80.0, 88.0], [1003, 60.0, 35.0, 76.0, 60.5]]"""

"""def student_details():
    print("-----------------------------------------------")
    print("-----------------------------------------------")
    student_id = int(input("Student id: "))
    q1 = int(input("Enter Q1: "))
    q2 = int(input("Enter Q2: "))
    Final = int(input("Enter Final: "))
    print("-----------------------------------------------")
    print("-----------------------------------------------")
    total_weightage = (q1*20/100)+(q2*30/100)+(Final*50/100)
    print("Total Weightage: ", total_weightage)
    print("-----------------------------------------------")
    print([student_id, q1, q2, total_weightage])
    print("-----------------------------------------------")
    print("-----------------------------------------------")    

def main():
    student_details()

main()"""

def student_details():
    student_id = int(input("Student id:"))
    Q1 = int(input("Enter Q1: "))
    Q2 = int(input("Enter Q2: "))
    Final = int(input("Enter Final: "))
    total_weightage = (Q1*20/100)+(Q2*30/100)+(Final*50/100)

    if student_id <= 0:
        student_details();
    else:
        print(total_weightage);

def main():
    student_details()

main()