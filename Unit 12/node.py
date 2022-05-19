class Node:

    __slots__ = ["__value", "__next"]

    def __init__(self, val, next = None) -> None:
        self.__value = val
        self.__next = next

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def print_nodes(self):
        #base case
        if self.__next == None:
            print(self.__value)
            return ""
        #recusrsive base
        else:
            print(self.__value)
            print(" ")
            return self.__next.print_nodes()

def main():
    n1 = Node('a')
    n2 = Node('b', n1)
    n3 = Node('c', n2)

    # print(n1.get_value())
    # print(n2.get_next().get_value())

    n3.print_nodes()

    # Node.print_nodes(n3)

main()