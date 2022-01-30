import math as m

def main():
    greeting("Kartik Rajesh")
    input1 = get_input()
    input2 = get_input()
    sum1 = cal_sum(input1, input2)
    print(sum1)

def greeting(name):
    print("Welcome to python "+name)

def cal_sum(a, b):
    sum = a+b+m.pi
    return sum

def get_input():
    val1 = int(input("Please enter one integer "))
    return val1

# call the function main to start the program
main()