class Map():
    
    class MapNode():
        def __init__(self,key,value,next=None) -> None:
            self.key = key
            self.value = value
            self.next = next
        
    
    slots = list()
    size = 0
    capacity = 0
    DEFAULT_LOAD_FACTOR = 0.75

    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.slots = [None] * self.capacity
        self.size = 0

        print("HashTable created")
        print(f"Numbers of pairs in the hash table: {self.size}")
        print(f"Size of the hash table: {self.capacity}")
        print(f"Default Load Factor: {Map.DEFAULT_LOAD_FACTOR}")

    def get_capacity(self):
        return (f"Capacity of the hash table: {self.capacity}")
    
    def get_size(self):
        return(f"Size of hash table: {self.size}")
    
    def print_map(self):
        print("Current Hash Table", end=" ")
        for i in range(len(self.slots)):
            cursor = self.slots[i]

            while cursor != None:
                print(f"key: {cursor.key}, value: {cursor.value}",end=" ")
                cursor  = cursor.next
        print()

    def get_slot_ind(self,key):
        hash_code = hash(key)

        return (hash_code % self.capacity)

    def insert(self,key,value):
        slot_ind = self.get_slot_ind(key)

        cursor = self.slots[slot_ind]

        while (cursor != None):
            if (cursor.key == key):
                cursor.value = value
                return
            cur = cur.next

        head = self.slots[slot_ind]
        new_node = self.MapNode(key,value,head)
        self.slots[slot_ind] = new_node

        print (f"Pair inserted succesfully: key:{key} value:{value}")

        self.size += 1
        load_factor = self.size/self.capacity
        print(f"Current load factor is: {load_factor}")

        if load_factor > Map.DEFAULT_LOAD_FACTOR:
            print(f"The actual load factor {load_factor} is greather than {Map.DEFAULT_LOAD_FACTOR}")
            print("Rehashing is been done...")
            self.rehash()

    def rehash(self):
        temp = self.slots
        previous_capacity = self.capacity
        self.capacity = self.capacity * 2
        self.slots = [None] * (self.capacity)
        
        self.size = 0
        
        for i in range(previous_capacity):
            cursor = temp[i]

            while cursor != None:
                key = cursor.key
                value = cursor.value

                self.insert(key,value)
                cursor = cursor.next


if __name__ == "__main__":
    hash_table = Map(5)
    print(hash_table.get_capacity())
    print(hash_table.get_size())
    hash_table.insert("Apple/kg",12.0)
    hash_table.insert("Banana/palm",7.0)
    print(hash_table.get_capacity())
    print(hash_table.get_size())
    hash_table.print_map()
    hash_table.insert("Eggs/30",18.0)
    hash_table.print_map()
    hash_table.insert("Milk",5.0)
    hash_table.print_map()
    print(hash_table.get_capacity())
    print(hash_table.get_size())