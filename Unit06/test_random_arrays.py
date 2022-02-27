from array import array
import arrays 
import random
import time 

def test_random_numbers():
    print(random.randint(0, 10))
    # print(random.randrange(1, 10, 2))
    # print(random.random())                 #floating values between (0-1)
    # print(random.choice("Hello World"))
    # print(random.choice([12, 45, 78, 99, 101, -1, -8]))

def random_array(size, min_value = 0, max_value = None):
    new_array = arrays.Array(size)
    # print(new_array, "\n")

    if max_value == None:
        max_value = size
    for i in range(size):
        new_array[i] = random.randint(min_value, max_value)
    return new_array

def linear_search(array, target):
    size = len(array)
    for i in range(size):
        if target == array[i]:          #if found
            return i                    #return index/slot of target value, if found 
    return None                         #never found 

def time_limit_search(array, target):
    start_time = time.perf_counter()
    size = len(array)
    for i in range(size):
        if target == array[i]:          #if found
            break                       #return index/slot of target value, if found 
    #never found 
    end_time = time.perf_counter()
    difference = start_time - end_time
    print("The function took this long: ", difference)

def main():
    # random_array(10)
    # random_array(100, 50, 99)
    # random_array(100, 50)
    array = random_array(20, 0, 10)
    print(array)
    # print(linear_search(array, 5))                    #searching for the value 50 in the array of random integer 
    time_limit_search(array, 5)

main()