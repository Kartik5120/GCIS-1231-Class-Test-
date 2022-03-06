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
    except (ArithmeticError, ZeroDivisionError):
        print("Arthimetic error occured. Your denominator must not be zero")
        print(" ")
    else: 
        print("No exception was raised! ")
    finally:
        print("When an exception occurs, this will still execute")

    print("The code dosen't crash!")
    print(" ")

def main():
    test_error_handling()

main()