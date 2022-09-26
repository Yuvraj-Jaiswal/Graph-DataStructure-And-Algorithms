import time
import os

def create_matrix(n=10):
    matrix = []
    for i in range(n):
        matrix.append([0 for j in range(n)])
    return matrix

def create_graph(matrix):
    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if f"{i},{j}" not in graph:
                graph[f"{i},{j}"] = []
            if i+1 < len(matrix):graph[f"{i},{j}"].append(f"{i + 1},{j}")
            if j+1 < len(matrix):graph[f"{i},{j}"].append(f"{i},{j + 1}")
            if i-1 >= 0:graph[f"{i},{j}"].append(f"{i - 1},{j}")
            if j-1 >= 0:graph[f"{i},{j}"].append(f"{i},{j - 1}")

    return graph

def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j] , end="  ")
        print(" ")
    print(" ")


def depth_first_search(adj_list,source,target,visited=set()):
    global matrix
    if source == target :
        i,j = source.split(",")
        i , j = int(i) , int(j)
        matrix[i][j] = "F"
        print_matrix(matrix)
        return True
    if source in visited: return False
    else:visited.add(source)

    i,j = source.split(",")
    i, j = int(i), int(j)
    matrix[i][j] = "*"

    print_matrix(matrix)
    time.sleep(0.3)

    for vertex in adj_list[source]:
        if depth_first_search(adj_list,vertex,target,visited):
            return True

    return False


def breath_first_search(graph,source,dest):
    global matrix
    stack = [source]
    visited = set()
    comp = 0
    i, j = source.split(",")
    i, j = int(i), int(j)
    matrix[i][j] = "S"

    while len(stack) > 0:
        print(" Breath First Search ")
        print(comp)
        comp += 1

        node = stack.pop(0)

        i,j = node.split(",")
        i , j = int(i) , int(j)
        if matrix[i][j] != "S":matrix[i][j] = "*"
        print_matrix(matrix)
        print(" ")
        os.system('cls')

        if node == dest:
            matrix[i][j] = "D"
            print_matrix(matrix)
            return True

        for vertex in graph[node]:
            if vertex not in visited:
                stack.append(vertex)
                visited.add(vertex)

    return False


matrix = create_matrix(15)
graph_m = create_graph(matrix)
print(breath_first_search(graph_m,"5,5","9,9"))

# run this file in terminal for clear output