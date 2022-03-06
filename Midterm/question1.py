def smallest_number(num1, num2, num3):
    smallest = None
    if num2 > num1 or num1 < num3:
        smallest = num1
    elif num1 > num2 or num2 < num3:
        smallest = num2
    else:
        smallest = num3
    print("The smallest number from the given three numbers is: ", smallest)
    return smallest

def main():
    smallest_number(250, 400, 90)

main()