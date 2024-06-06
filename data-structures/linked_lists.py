class Node():
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.last = None
    
    def insert_head(self,data):
        new_node = Node(data,self.head)

        if self.head is None:
            self.last = new_node 

        self.head = new_node

    def insert_after(self,prev_node,data):
        if prev_node is None:
            return "O nó anterior não pode ser nulo!"
        
        new_node = Node(data,prev_node.next)
        prev_node.next = new_node

        if prev_node == self.last:
            self.last = new_node

    def append(self,data):
        new_node = Node(data,None)

        if self.head is None:
            self.head = new_node

        # Caso em que o último elemento não é guardado
        # actual_node = self.head
        # while actual_node.next is not None:
        #     actual_node = actual_node.next
        
        self.last.next = new_node
        self.last = new_node

    def search(self,node,key):

        if not node:
            return False
        elif node.data == key:
            return True
        else:
            return self.search(node.next,key)

    def lenght(self,node):
        while node:
            return 1 + self.lenght(node.next)
        return 0

    def delete_node(self,node,val):
        if node == None:
            print("Elemento não está na lista")
        elif node.data == val:
            if node.next:
                node.data = node.next.data
                node.next = node.next.next
                return 1
            else:
                return 0
        if self.delete_node(node.next,val) == 0:
            node.next = None
            return 1



    def delete_pos(self):
        pass

    def delete_list(self):
        self.head = None
        self.data = None

    def show_nodes(self):
        if self.head is None:
            return "A lista é vazia."
        
        cur = self.head

        print("Lista: ", end=" ")
        while cur:
            print(f"{cur.data} -> ", end=" ")
            cur = cur.next

        print()

    
    
if __name__ == "__main__":
    li = LinkedList()
    li.show_nodes()
    li.insert_head(1)
    li.append(2)
    li.append(3)
    li.append(5)
    print(li.lenght(li.head))
    print(li.search(li.head,10))
    li.append(4)
    li.show_nodes()
    li.insert_head(10)
    li.append(6)
    li.show_nodes()
    print(li.search(li.head,10))
    print(li.search(li.head,6))
    print(li.lenght(li.head))
    li.delete_node(li.head,15)
    li.show_nodes()

    li.delete_list()
    print(li.show_nodes())