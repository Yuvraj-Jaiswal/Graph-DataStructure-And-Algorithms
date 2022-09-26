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

def depth_first_search(graph,source,visited,size=1):
    if source in visited : return 0
    visited.add(source)

    for vertex in graph[source]:
        size = size +  depth_first_search(graph,vertex,visited,size=1)

    return size

def max_graph(graph):
    visited = set()
    largest = 0
    for i in graph.keys():
        if i not in visited:
            nodes = depth_first_search(graph,i,visited)
            if nodes >largest:
                largest = nodes

    return largest


print(max_graph(graph))
