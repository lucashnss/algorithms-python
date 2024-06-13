from queues import Queue 

def bfs(graph,begin,target):
    search_queue = Queue()
    search_queue.enqueue((begin,[begin]))
    visited = []
    while not search_queue.empty():
        (vertex,path) = search_queue.dequeue()
        if vertex not in visited:
            visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor == target:
                return path + [neighbor]
            if neighbor not in visited:
                search_queue.enqueue((neighbor,path + [neighbor]))
    return None

if __name__ == "__main__":

    graph = {"A":["B","C","D"],
             "B":["D","E"],
             "C":["F"],
             "D":["E"],
             "E":["F"],
             "F":[],}
    
    print(bfs(graph,"B","F"))
    
