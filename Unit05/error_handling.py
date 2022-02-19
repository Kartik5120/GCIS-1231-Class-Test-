def test_error_handling():
    try:
        numerator = int(input("Please enter an integer (numerator): "))
        denom = int(input("Please enter an integer (denomenator): "))
        division = numerator/denom
    except ValueError: 
        print("Plese remember to enter integers only")
    except ZeroDivisionError:
        print("Your denominator must not be zero")

    print(division)
    print("The code dosen't crash!")

def main():
    test_error_handling()

main()