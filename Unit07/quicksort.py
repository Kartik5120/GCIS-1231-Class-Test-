import arrays
import random
import time

def create_array(size):
    arr = arrays.Array(size, 0)
    return arr

def fill_array_descending(arr):
    """Fills the array with sorted integer values in descending order"""
    count = len(arr)
    length = len(arr)
    for i in range(length):
        arr[i] = count
        count -= 1

def random_array(size, min_value=0, max_value=None):
    new_array = arrays.Array(size)
    if max_value == None:
        max_value = size
    for i in range(size):
        new_array[i] = random.randint(min_value, max_value)
    return new_array

def time_insertion_sort(array):
    start_time = time.perf_counter()
    print("start time", start_time)
    insertion_sort(array)
    end_time = time.perf_counter()
    print("end_time", end_time)
    difference = end_time - start_time
    print("The insertion sort took this long: ", difference)


def partition(pivot, array):
    # count the number of values less then,
    # equal to, and greater the pivot
    # create the array of the specific/required size
    count_less = 0
    count_same = 0
    count_more = 0
    for i in range(len(array)):
        if array[i] < pivot:
            count_less += 1
        elif array[i] == pivot:
            count_same += 1
        else:
            count_more += 1

    # create the arrays of the exact size we need
    less = create_array(count_less)
    same = create_array(count_same)
    more = create_array(count_more)

    less_index = 0
    same_index = 0
    more_index = 0

    # fill up the less, same and more arrays
    for i in range(len(array)):
        if array[i] < pivot:
            less[less_index] = array[i]
            less_index += 1
        elif array[i] == pivot:
            same[same_index] = array[i]
            same_index += 1
        else:
            more[more_index] = array[i]
            more_index += 1
    return less, same, more

def array_join(arr1, arr2):
    length = len(arr1) + len(arr2)
    joined_array = create_array(length)

    joined_array_index = 0 
    # copy of values from arr1 to joined_array
    for i in range(len(arr1)):
        joined_array[joined_array_index] = arr1[i]
        joined_array_index += 1

    # copy of values from arr2 to joined_array
    for i in range(len(arr2)):
        joined_array[joined_array_index] = arr2[i]
        joined_array_index += 1

    return joined_array

def quicksort(array):
    # base case
    if len(array) <= 1:
        return array
    # recursive case 
    else: 
        pivot = array[0]
        less, same, more = partition(pivot, array)
        first_join = array_join(quicksort(less), same)
        final_join = array_join(first_join, quicksort(more))
        return final_join        

def main():
    # array = create_array()
    # fill_array_descending(array)
    # print("The filled array is: ", array)
    # sorted_array = quicksort(array)

    # create second array of a different size
    # fill it
    # array2 = create_array(5)
    # fill_array_descending(array2)
    # print("The filled array is: ", array2)

    # call array_join with both arrays as inputs 
    # joined = array_join(array, array2)
    # prints the joined array
    # print("The joined array is: ", joined)

    # arr1, arr2, arr3 = partition(joined[len(joined) - 1], joined)
    # print ("Array1 contains: ", arr1)
    # print ("Array2 contains: ", arr2) 
    # print ("Array3 contains: ", arr3)

    rand_array = random_array(100, 0, 1000)
    print("Random Array: ", rand_array)
    sorted_array = quicksort(rand_array)
    print("This is the sorted array: ", sorted_array)


main()