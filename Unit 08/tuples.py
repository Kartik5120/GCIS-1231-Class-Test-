def create_tuples():
    tuple1 = (1, 2, 3)
    tuple2 = ('a', 'b', 'c')
    tuple3 = ("Mandy", "GCIS-123", 99.5, True)
    tuple4 = tuple("Hello")

    return tuple1, tuple2, tuple3, tuple4

def print_tuple(tup):
    print("-----------------------------------------------------------------")
    print(tup)
    print("The length of the tuple is: ", len(tup))
    print("-----------------------------------------------------------------")
    # print individual values
    print("The individual values are: ")
    for i in range(len(tup)):
        print(tup[i], end=" ")
    print("-----------------------------------------------------------------")

def main():
    tup1, tup2, tup3, tup4 = create_tuples()
    print_tuple(tup1)

    # try to change a value! Not possible (A big limitation)
    # tup[0] = 10

    # compare tuples by looking at the values
    print(tup1 == tup2)

    # compare tuples by looking at the values
    print(tup1 is tup2)

main()