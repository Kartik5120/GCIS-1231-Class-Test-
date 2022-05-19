class Queue:

    __slots__ = ["__front", "__back", "__size", "__list", "__capacity"]

    def __init__(self):
        self.__front = 0
        self.__back = 0
        self.__size = 0
        self.__capacity = capacity
        self.__list = [0 for value in range(capacity)]          # assigns default values of 0 to all slots in the list

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == self.__capacity

def main():
    queue = Queue(10)                           # Queue with capacity 10
     # print(queue.__size)                         # Won't work -- __size is private!!
    print(queue.get_size())
    print("Is the queue empty? ", queue.is_empty())
    print("Is the queue full? ", queue.is_full())

main()