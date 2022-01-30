# >= 90 -> A
# >= 80 -> B
# >= 70 -> C
# >= 60 -> D
# >=  0 -> F

# Stub
"""def convert_mark_to_grade(mark):
    return None"""

def convert_mark_to_grade(mark):
    #if mark < 0 or mark > 100:
    #    return None
    if mark >= 0 and mark <= 100:
        if mark < 60:
            return "F"
        elif mark < 70:
            return "D"
        elif mark < 80:
            return "C"
        elif mark < 90:
            return "B"
        else:
            return "A" 
    else: 
        print("Invalid Input")
        return None