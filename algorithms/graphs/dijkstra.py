def find_lowest_cost_node(costs,processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost 
            lowest_cost_node = node 
    return lowest_cost_node

def dijkstra(graph,costs,parents):
    processed = []
    node = find_lowest_cost_node(costs,processed) 
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs,processed)
    return costs,parents


if __name__ == "__main__":
    graph = {"START":{"A":6,"B":2},
             "A":{"FIN":1},
             "B":{"A":3,"FIN":5},
             "FIN":{}}
    costs = {"A":6,
             "B":2,
             "FIN":float("inf")}
    parents = {"A":"START",
               "B":"START",
               "FIN":""
    }

    new_costs,new_parents = dijkstra(graph,costs,parents)
    print("New costs: ",new_costs,"\nNew parents: ",new_parents)
