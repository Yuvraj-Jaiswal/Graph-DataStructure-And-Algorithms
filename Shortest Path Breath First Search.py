graph = {
    "w" : ["x","v"],
    "x" : ["y"],
    "y" : ["z","v"],
    "v" : ["z"],
    "z" : []
}

def breath_first_search(graph,source,dest):

    stack = [[source, 0]]
    min_dist = 1000
    visited = set()

    while len(stack) > 0:

        node , ds = stack.pop(0)
        for vertex in graph[node]:
            if vertex not in visited:
                stack.append([vertex,ds+1])
            else: visited.add(node)

        if node == dest:
            if ds < min_dist:
                min_dist = ds

    return min_dist

print(breath_first_search(graph,"w","z"))
