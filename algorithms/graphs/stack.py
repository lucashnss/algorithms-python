from node import Node

class Stack():
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def show_stack(self):
        if self.top:
            cur = self.top
            print("Pilha: ", end=" ")
            while cur:
                print(f"{cur.data} -> ", end=" ")
                cur = cur.next
            print()
        else:
            print("Pilha vazia")

    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            raise IndexError("Lista vazia")
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1 

    def pop(self):
        if self.is_empty():
            raise IndexError("Pilha vazia")
        
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data
    
    
if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(10)
    stack.push(15)
    print(stack.get_size())
    stack.push(5)
    stack.push(10)
    print(stack.peek())
    stack.push(30)
    print(stack.get_size())
    stack.show_stack()
    stack.pop()
    stack.pop()
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    stack.show_stack()
    print(stack.is_empty())