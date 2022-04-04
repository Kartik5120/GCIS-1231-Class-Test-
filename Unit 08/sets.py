def create_sets():
    set1 = {1, 2, 3}
    set2 = set("hello")
    set3 = set([True, False])
    set4 = {'W', 'o', 'r', 'l', 'd'}
    set5 = {10, 'a', 20, 55.5, False}
    set6 = {}                       # EMPTY SET
    set7 = set()                    # EMPTY SET
    return set1, set2, set3, set4, set5

def print_set(set):
    print("Length is: ", len(set))
    for value in set:
        print(value, end=" ")

def change_set(set):
    # Make some changes 
    set.add(2)                              # DUPLICATEL VALUE 2
    set.add(8)
    set.add("GCIS-123")
    if 0 in set:
        set.remove(0)
    set.remove("GCIS-123")
    set.discard(100)                        # DISCARDING A VALUE THAT DOSEN'T EXIST: THIS WON'T FAIL
    # set.clear()
    return set 

def superset(set0, set1):
    for value in set1:
        if not(value in set0):
            return False
    return True

def subset(set0, set1):
    for value in set0:
        if not(value in set1):
            return False
    return True

def intersection(set0, set1):
    set2 = set()                            # INTERSECTION SET
    for value in set0:
        if value in set1:
            set2.add(value)                 # STORE COMMON VALUE INTO set2
    return set2, True

def union(set0, set1): 
    set2 = set()
    for i in set0:
        set2.add(i)
    for i in set1:
        set2.add(i)
    return set2

def main():
    set1, set2, set3, set4, set5, set6, set7 = create_sets()
    # print_set(sorted(set2))               # NOW THE DATA IS ORDERED!
    # result_set = change_set(set1)
    # print_set(result_set)
    # print_set(set6)                         # PRINTING AN EMPTY SET
    set0 = {1, 2, 3, 4, 5}
    # superset
    result = superset(set0, set1)           # IS set0 A SUPERSET OF set1
    print("Is set0 a superset of set1? ", result)

    set0 = {1}
    result = superset(set0, set1)           # IS set0 A SUPERSET OF set1 FALSE!

    # subset
    result = subset(set0, set1)             # IS set0 A SUBSET OF set1: TRUE!
    print("Subset test (true case): Is set0 a superset of set1?: ", result)
    set0 = {5, 6}
    result = subset(set0, set1)             # IS set0 A SUBSET OF set1: FALSE!
    print("Subset test (false case): Is set0 a superset of set1?: ", result)

    # interaction
    set0 = {1, 2, 3, 4, 5}
    set1 = {0, 5, 2, 9}
    result_set = intersection(set0, set1)   # RESULT_SET = {2, 5}
    print("Intersection test: What is the intersection of set0 and set1? ", result_set)

    set0 = {1, 2, 3, 4, 5}
    set1 = {5, 1, 8}
    result_set = intersection(set0, set1)   # RESULT_SET = {} EMPTY!
    print("Intersection test: What is the intersection of set0 and set1? ", result_set)

    # union 
    set0 = {1, 2, ,3, 4, 5}
    set1 = {6, 7, 8}
    result_set = union(set0, set1)          # RESULT_SET = {1, 2, 3, 4, 5, 6, 7, 8}
    

main()