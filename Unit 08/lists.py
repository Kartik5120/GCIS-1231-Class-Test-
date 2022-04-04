def print_list (name, list):
    print("/n", name)
    print(list)
    print("Length of the list: ", len(list))
    for i in range(len(list)):
        print(list[i], end=" ")

def create_list():
    empty_list = []
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = ["Titanic", "deCaprio", 1000000, 1997]
    
    return list1, list2, list3, empty_list

# changes one value at the position index of the list
# def add_to_list(list, index, value):

def main():
    l1, l2, l3, empty = create_list()
    # print_list("Movies List: ", 13)

    # add_to_list(empty, 0, 10)
    # empty.append(10)
    # print_list("Empty (not for long)", empty)
    # empty.append(20)
    # print_list("Empty (not for long)", empty)

    # join 2 lists, original list weren't changed, don't forget to store the resulting list
    l4 = l1 + l2

    # join 2 lists, original list(l1)
    l1 += l2
    print(l1)


main()