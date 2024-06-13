from queues import Queue 

def bfs(graph,begin):
    search_queue = Queue()
    search_queue.enqueue(begin)
    visited = []
    while not search_queue.empty():
        vertex = search_queue.dequeue()
        if vertex not in visited:
            visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                search_queue.enqueue(neighbor)
    return visited

if __name__ == "__main__":

    graph = {"A":["B","C","D"],
             "B":["D","E"],
             "C":["F"],
             "D":["E"],
             "E":["F"],
             "F":[]}
    
    print(bfs(graph,"A"))
    
