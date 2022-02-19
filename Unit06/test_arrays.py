import arrays

def test_create_arrays():
    new_array = arrays.Array(10, 0)
    print(new_array)

    new_array = arrays.Array(5, True)
    print(new_array)

    new_array = arrays.Array(10, "GCIS")
    print(new_array)

    new_array = arrays.Array(100, 0.0)
    print(new_array)

def process_array_data():
    marks_array = arrays.Array(10, 0.0)
    length = len(marks_array)
    print(length)
    for i in range(length):                     # loops from 0 to 9
        marks_array[i] = i*2                    # Changing the values of each slot to 9.9 
        print(marks_array[i])                   # Find the slot value using the index into the array
    return marks_array

def main():
    # test_create_arrays()
    process_array_data()

main()