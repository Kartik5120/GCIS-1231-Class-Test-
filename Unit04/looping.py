def test_even_sum(input): 
    count = 1
    sum = 0 
    while count <= input:
        if count % 2 == 0: 
            sum = sum + count
        count = count + 1
    return sum 

def test_odd_sum(input):
    count = 1
    sum = 0 
    while count <= input:
        if count % 2 != 0:
            sum = sum + count
        count = count + 1
    return sum 

def get_input():
    return int(input("Please enter an integer: "))

def main():
    input = get_input()
    sum_even = test_even_sum(input)
    print("Sum of even number is: ", sum_even)
    sum_odd = test_odd_sum(input)
    print("Sum of odd numbers is: ", sum_odd)

main()
