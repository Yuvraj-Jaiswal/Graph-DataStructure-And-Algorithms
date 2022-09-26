
graph = {
    "a" : ["b","c"],
    "b" : ["d"],
    "c" : ["e"],
    "d" : [],
    "e" : ["b"]
}

def depth_first_search(adj_list,source,visited=set()):

    if source in visited: return
    else:visited.add(source)

    print(source,end=" ")

    for vertex in adj_list[source]:
        depth_first_search(adj_list,vertex,visited)

depth_first_search(graph,"a")