def test_error_handling():
    try:
        numerator = int(input("Please enter an integer (numerator): "))
        denom = int(input("Please enter an integer (denomenator): "))
        print(" ")
        division = numerator/denom
    except ValueError:
        print(" ")
        print("Plese remember to enter integers only")
        print(" ")
    except ZeroDivisionError:
        print("Your denominator must not be zero")
        print(" ")
    else: 
        print("No exception was raised! ")

    print("Answer: ", division)
    print("The code dosen't crash!")
    print(" ")

def main():
    test_error_handling()

main()