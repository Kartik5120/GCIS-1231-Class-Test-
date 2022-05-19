"""input_list1 = [1, 1, 2]

output Set 1: {1, 2}

Example 2:

input_list2 = [0, 10, 1, 5, 8, 2, 2, 3, 1, 8]

output Set 2: {0, 10, 1, 5, 8, 2, 3}"""

def remove_duplicates(input_list):
    print("The original List: ", input_list)
    output_list = set(input_list)
    print("The new List: ", set(output_list))

def main():
    input_list1 = [1, 1, 2]
    input_list2 = [0, 10, 1, 5, 8, 2, 2, 3, 1, 8]
    print("--------------------------------------")
    print("Example 1:- ")
    remove_duplicates(input_list1)
    print("--------------------------------------")
    print("Example 2:- ")
    remove_duplicates(input_list2)
    print("--------------------------------------")

main()