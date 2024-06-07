from node import Node

class Queue():
    def __init__(self,max_size=5) -> None:
        self.front = None
        self.rear = None
        self.size = 0
        self.max_size = max_size
    
    def show_queue(self):
        if self.rear:
            cur = self.front
            print("Fila: ", end=" ")
            while cur:
                print(f"{cur.data} -> ", end=" ")
                cur = cur.next
            print()
        else:
            print("Fila vazia")
    
    def full(self):
        return self.size == self.max_size

    def empty(self):
        return self.size == 0
    
    def enqueue(self,value):
        if self.size == self.max_size:
            raise OverflowError("A fila está cheia")
        
        new_node = Node(value)
        if self.size == 0:
            self.front = new_node
            self.rear = new_node
        
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("A fila está vazia")
        
        dequeued_node = self.front
        self.front = self.front.next
        self.size -= 1

        if self.size == 0:
            self.rear = None
        
        return dequeued_node.data

if __name__ == "__main__":
    queue = Queue()
    print(queue.empty())
    print(queue.full())
    queue.enqueue(5)
    print(queue.dequeue())
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    queue.enqueue(25)
    queue.show_queue()
    print(queue.dequeue())
    print(queue.dequeue())
    queue.show_queue()
    print(queue.front.data)
