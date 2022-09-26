graph = {
    "a" : ["b","c"],
    "b" : ["d"],
    "c" : ["e"],
    "d" : [],
    "e" : ["b"]
}

def Breadth_first_search(adj_list,source):
    stack = [source]
    visited = set()

    while len(stack) > 0:
        for vertex in adj_list[stack[0]]:
            if vertex not in visited:
                stack.append(vertex)

        ref = stack.pop(0)
        visited.add(ref)
        print(ref,end=" ")

Breadth_first_search(graph,"a")