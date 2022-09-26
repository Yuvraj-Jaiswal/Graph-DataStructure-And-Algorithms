
edges = [
    ["i","j"],
    ["k","i"],
    ["m","k"],
    ["k","l"],
    ["o","n"],
]

def get_adjency_list(edges,directed=False):
    adj = {}
    for edge in edges:
        if edge[0] in adj:
            adj[edge[0]].append(edge[1])
        else:
            adj[edge[0]] = [edge[1]]

        if directed:
            if edge[1] in adj:
                adj[edge[1]].append(edge[0])
            else:
                adj[edge[1]] = [edge[0]]
    return adj

print(get_adjency_list(edges,directed=True))
