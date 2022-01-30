def main():
    name = "Kartik Rajesh"
    greeting(name)
    input1 = get_input()
    input2 = get_input()
    sum1 = cal_sum(input1, input2)
    print_output(sum1)

def greeting(n):
    print("Welcome to python "+ n)

def cal_sum(a, b):
    sum = a+b
    return sum

def print_output(val):
    print(val)

def get_input():
    val1 = float(input("Please enter one integer "))
    return val1

# call the function main to start the program
main()