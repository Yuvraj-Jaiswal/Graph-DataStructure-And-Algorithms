graph = {
    "a" : ["b","c"],
    "b" : ["d"],
    "c" : ["e"],
    "d" : [],
    "e" : ["b"]
}

def depth_first_search(adj_list,source,target,visited=set()):

    if source == target : return True
    if source in visited: return False
    else:visited.add(source)

    for vertex in adj_list[source]:
        if depth_first_search(adj_list,vertex,target,visited):
            return True

    return False

print(depth_first_search(graph,"a","d"))