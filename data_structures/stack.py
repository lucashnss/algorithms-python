from node import Node

class Stack():
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def stack_size(self):
        return self.size
    
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def peek(self):
        return self.top.data

    def pop(self):
        if self.size == 0:
            raise IndexError ("A pilha está vazia")
        else:
            self.top = self.top.next
            self.size -= 1

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

if __name__ == "__main__":
    stack = Stack()
    print(stack.empty())
    print(stack.stack_size())
    for i in range(10):
        stack.push(i)
    
    print(stack.peek())
    print(stack.stack_size())

    for i in range(5):
        stack.pop()
        print(stack.peek(),end=" ")
        print(stack.stack_size(),end=" ")