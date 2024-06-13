from stack import Stack

def dfs(graph,begin,target):
    search_stack = Stack()
    search_stack.push((begin,[begin]))
    visited = []
    while not search_stack.is_empty():
        (vertex,path) = search_stack.pop()
        if vertex not in visited:
            visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor == target:
                return path + [neighbor]
            if neighbor not in visited:
                search_stack.push((neighbor,path + [neighbor]))
    return None

if __name__ == "__main__":

    graph = {"A":["B","C","D"],
             "B":["D","E"],
             "C":["F"],
             "D":["E"],
             "E":["F"],
             "F":[]}
    
    print(dfs(graph,"A","E"))
    
