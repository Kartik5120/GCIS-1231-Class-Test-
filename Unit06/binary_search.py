import arrays
import time


def create_array(size):
    arr = arrays.Array(size, 0)
    return arr

def fill_array(arr):
    count = 0
    length = len(arr)
    for i in range(length):
        print(i)
        count += 1
        arr[i] = count
    return arr

def binary_search(arr, target, start_index = None, end_index = None):
    if start_index == None:
        start_index = 0
    if end_index == None:
        end_index = len(arr) - 1

    #base case
    if start_index > end_index:
        return None

    #recursive case 
    midpoint_index = start_index + (end_index - start_index)//2
    print("The midpoint index is: ", midpoint_index)
    #if target is equal to midpoint value 
    if target == arr[midpoint_index]:           #is the target value is equal to the value at the midpoint
        return midpoint_index
    #if target is less then the midpoint value, search bottom half
    elif target < arr[midpoint_index]:
        end_index = midpoint_index + 1
        return binary_search(arr, target, start_index, end_index)
    #if target is greater then the midpoint value 
    else: 
        start_index = midpoint_index + 1
        return binary_search(arr, target, start_index, end_index)

def time_binary_search(array, target):
    start_time = time.perf_counter()
    binary_search(array, target)
    end_time = time.perf_counter()
    difference = end_time - start_time
    print("The function took this long: ", difference)

def main():
    """arr = create_array(10)
    arr = fill_array(arr)
    print("Sorted array: ", arr)
    index = binary_search(arr, 8)               #calling with array and large target value
    index = binary_search(arr, 3)               #calling with array and small target value
    index = binary_search(arr, 20)              #calling with array and a target not in the array 
    index = binary_search(arr, 20, 0, 9)        #calling with all four parameters
    index = binary_search(arr, 20, 25,50)       #invalid start abd end index input 
    print("The value was found at the index: ", index)"""

    arr2 = create_array(10000)
    arr2 = fill_array(arr2)
    time_binary_search(arr2, 88888)               #taking binary search with 10000 elements when looking for the value 

main()