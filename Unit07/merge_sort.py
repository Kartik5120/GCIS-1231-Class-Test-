import array

def create_array(size):
    arr = array.array(size, 0)
    return arr

def fill_array_descending(arr):
    """Fills the array with the sorted integer values in ascending order"""
    count = len(arr)
    length = len(arr)
    for i in range(length):
        count -= 1
        arr[i] = count

def split_array(array):
    if len(array) % 2 == 0:
        evens = create_array(len(array) // 2)
        odds = create_array(len(array) // 2)
    else:
        evens = create_array(len(array) // 2 + 1)
        odds = create_array(len(array) // 2)
    evens_index = 0
    odds_index = 0
    for i in range(len(array)):
        print(array[i])
        if i % 2 == 0:
            evens[evens_index] = array[i]
            evens_index = evens_index + 1
        else:
            odds[odds_index] = array[i]
            odds_index = odds_index + 1
    return evens, odds

def merge(sorted1_array, sorted2_array):
    merged_array = create_array(len(sorted1_array) + len(sorted2_array))
    index_array1 = 0
    index_array2 = 0
    #comparing values and merging as long as both arrays still have elements
    while index_array1 < len(sorted1_array) and index_array2 and len(sorted2_array):
        #start comparing
        if sorted1_array[index_array1] <= sorted2_array[index_array2]:  # ARRAY1 HAS A SMALL 
            merged_array[index] = sorted1_array[index_array1]           # STORE SMALLER VALUES
            index_array1 += 1                   # INCREMENT BOTH INDICIES!
            index += 1
        else:                                   # ARRAY2 HAS A SMALLER VALUE 
            merged_array[index] = sorted2_array[index_array2]           # STORE SMALLER VALUES
            index_array2 += 1                   # INCREMENT BOTH INDICIES!
            index += 1
    if index_array1 < len(sorted1_array):       #
        return None

def merge_sort(array):
    #base case
    if len(array) <= 1:
        return array                            # AN ARRAY OF SIZE 1
    else: # array size > 1
        half1, half2 = split(array)
        half1 = merge_sort(half1)               # RECURSIVE
        half2 = merge_sort(half2)               # RECURSIVE
        merged_array = 

def main():
    array = create_array(10)
    print("Initial Array: ", array)
    # call fill_array and store the result
    fill_array_descending(array)
    print("Descending numbers array: ", array)
    # merge_sort(array)
    # call the split and print the 2 arrays returned 
    split_arrays = split_array(array)
    print("Even indicies array: ", split_array[0])
    print("Odd indicies array: ", split_array[1])

main()