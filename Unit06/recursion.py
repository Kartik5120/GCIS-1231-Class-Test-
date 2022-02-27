import sys 

def greet(count):
    print("Hello")
    count +=1
    print(count)
    #stop condition: base case
    if count >= 995:
        return
    greet(count)
    #never place statements here!

def countdown(input):
    # print the numbers from input down to 0, recusively
    print(input)
    input -= 1
    #base case (When to stop)
    #if
    if input < 0: 
         return             #stop/end
    #recursive case (call myself)
    countdown(input)

def countdown_sum(input, sum):
    """Sum the numbers from the input down to 0, recursively, and add them up, finally return the sum"""
    sum += input
    input -= 1
    #base case (when to stop)
    if input < 0:
        return sum
    #recursive case
    return countdown_sum(input, sum)

def countdown_sum_alternative(input):
    """Sum the numbers from the input down to 0, recursively, and add them up, finally return the sum"""
    #base case (when to stop)
    if input <= 0:
        return input
    #recursive case
    return sum + countdown_sum(input - 1)

def factorial_recursive(input):
    """Calculate the factorial starting with the input"""

def main():
    # print(sys.getrecursionlimit())            #check the maximium recursion depth
    # greet(1)
    # countdown(10)
    # print(countdown_sum(3, 0))                # 06
    # print(countdown_sum_alternative(3))       # 06
    print(factorial_recursive())                # 4! = 4 * 3 * 2 * 1 = 24

main()