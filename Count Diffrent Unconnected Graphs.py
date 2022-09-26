graph = {
    "1" : ["2"],
    "2": ["1"],
    "3": [],
    "4": ["6"],
    "5": ["6"],
    "6" : ["4","5","8","7"],
    "7": ["6"],
    "8" : ["6"]
}

def depth_first_search(graph,source,visited):
    if source in visited : return
    visited.add(source)
    for vertex in graph[source]:
        depth_first_search(graph,vertex,visited)

def count_graphs(graph):
    visited = set()
    count = 0
    for i in graph.keys():
        if i not in visited:count += 1
        depth_first_search(graph,i,visited)
    return count

print(count_graphs(graph))



