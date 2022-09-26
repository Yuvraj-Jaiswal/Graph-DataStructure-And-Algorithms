
def get_graph(matrix):
    graph_r = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                if f"{i},{j}" not in graph_r:
                    graph_r[f"{i},{j}"] = []

                if i + 1 < len(matrix) :
                    if matrix[i+1][j] == 1:
                        graph_r[f"{i},{j}"].append(f"{i+1},{j}")

                if i - 1 >= 0 :
                    if matrix[i-1][j] == 1:
                        graph_r[f"{i},{j}"].append(f"{i-1},{j}")

                if j + 1 < len(matrix):
                    if matrix[i][j+1] == 1:
                        graph_r[f"{i},{j}"].append(f"{i},{j+1}")

                if j - 1 >= 0:
                    if matrix[i][j-1] == 1:
                        graph_r[f"{i},{j}"].append(f"{i},{j-1}")

    return graph_r


def dfs(graph,source,seen):

    for vertex in graph[source]:
        if vertex not in seen:
            seen.add(vertex)
            dfs(graph,vertex,seen)


def count_island(matrix):
    count = 0
    seen = set()
    graph = get_graph(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                if f"{i},{j}" not in seen:
                    count += 1
                    dfs(graph,f"{i},{j}",seen)

    return count


matrix = [[0,1,0,0,1,0],
          [1,1,0,0,1,0],
          [0,1,0,0,0,0],
          [0,0,0,1,1,0],
          [0,1,0,1,1,0],
          [0,0,0,1,1,0]]

print(count_island(matrix))

