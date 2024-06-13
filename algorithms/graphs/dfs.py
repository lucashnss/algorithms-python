from stack import Stack

def dfs(graph,begin):
    search_stack = Stack()
    search_stack.push(begin)
    visited = []
    while not search_stack.is_empty():
        vertex = search_stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    search_stack.push(neighbor)
    return visited

if __name__ == "__main__":

    graph = {"A":["B","C","D"],
             "B":["D","E"],
             "C":["F"],
             "D":["E"],
             "E":["F"],
             "F":[]}
    
    print(dfs(graph,"A"))
    
