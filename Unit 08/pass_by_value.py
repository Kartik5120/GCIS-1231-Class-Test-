def change(a, b):                       # PASS BY VALUE
    a = 10
    b = 20

def change_array(array):                # PASS BY VALUE
    array[0] = 10
    array[1] = 20

def main():
    # a = 1
    # b = 2
    # change(a, b)
    # print("a is: ", a)
    # print("b is: ", b)

    array = [1, 2]
    change_array(array)
    print(array)

main()