# >= 90 -> A
# >= 80 -> B
# >= 70 -> C
# >= 60 -> D
# >=  0 -> F

# Stub
#def convert_mark_to_grade(mark):
#    return None

print("/n","Welcome to the mark converter")

def convert_mark_to_grade(mark):
    #if mark < 0 or mark > 100:
    #    return None
    grade = None
    if mark >= 0 and mark <= 100:
        if mark < 60:
            grade = "F"
        elif mark < 70:
            grade = "D"
        elif mark < 80:
            grade = "C"
        elif mark < 90:
            grade = "C"
        else:
            return "A" 
    else: 
        print("Invalid Input")
        return None
    
    return grade

def main():
    result = convert_mark_to_grade(100)
    print(result)

main()