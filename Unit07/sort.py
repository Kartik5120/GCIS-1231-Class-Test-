import arrays 

def create_array(size):
    arr = arrays.Array(size, 0)
    return arr

def fill_array_ascending(arr):
    """Fills the array with the sorted integer values in ascending order"""
    count = 0 
    length = len(arr)
    for i in range(length):
        count += i
        arr[i] = count 
    return arr

def fill_array_descending(arr):
    """Fills the array with the sorted integer values in descending order"""
    count = len(arr)
    length = len(arr)
    for i in range(length):
        count -= i
        arr[i] = count 
    return arr

def swap(array, index1, index2):
    """
    value1 = array[index1]
    print(value1)
    value2 = array[index2]
    """

    temp = array[index2]
    array[index2] = array[index1]
    array[index1] = temp

def shift(array, index):
    while(array[index] < array[index-1]):   #WHILE LESS THEN NEIGHBOUR TO THE LEFT
        swap(array, index, index-1)         #SWAPS 2 VALUES AT A TIME ONLY
        index = index - 1                   #DECREMENT INDEX SO THAT THE WHILE LOOP EVENTUALLY ENDS
        if index == 0:                      #BUT DON'T DECREMENT TOO FAR: STOP AT INDEX0!
            break

def insertion_sort(array):
    for i in range(len(array)):             #i GOES FROM 0 TO LENGTH -1
        shift(array, i)

def main():
    #array = create_array(10)
    #print("Initial array with default values: ", array)
    #fill_array_ascending(array)
    #print("Ascending Values: ",array)
    #swap(array, 4, 8)                       #SWAPPING VALUES AT INDEX 4 AND INDEX 8
    #print("Values at index 4 and index 8 swapped: ", array)
    #shift(array, 5)                         #SHIFT FROM INDEX 5
    #print("Shifted array from index 8: ", array)

    #descending 
    array_dsec = create_array(100)
    fill_array_descending(array_dsec)
    print(array_dsec)
    shift(array_dsec, 99)
    print(array_dsec)
    insertion_sort(array_dsec)              #WORST CASE
    print(array_dsec)

main()