import node

class Stack: 

    __slots__ = [] 

    def __init__(self) -> None: 
        pass

    def get_size(self):

    # returns and removes the value at the top of the stack 
    def is_empty(self):

    # adds a value at the top of the stack 
    def pop(self):

    # returns the value at the top of the stack (without removing)
    def push(self):

    def print_stack(self):


def main():
    s1 = Stack()
    s1.push('a')
    s1.push('b')
    s1.push('c')
    print("The value at the top of the stack is: ", s1.peek())
    value = s1.pop()
    print("The value that was just popped off the stack is: ", value)

main()