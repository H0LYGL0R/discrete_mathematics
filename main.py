def check_reflexivity(graph) -> bool:
    vertices = set(vertex for edge in graph for vertex in edge)
    return all((vertex, vertex) in graph for vertex in vertices)


def check_irreflexivity(graph) -> bool:
    return not any(first_value == second_value for first_value, second_value in graph)


def check_symmetry(graph) -> bool:
    edge_set = set(graph)
    return all((second_value, first_value) in edge_set for first_value, second_value in edge_set)


def check_antisymmetry(graph) -> bool:
    edge_set = set(graph)
    return all(not ((second_value, first_value) in edge_set) for first_value, second_value in edge_set if first_value != second_value)


def check_transitivity(graph) -> bool:
    edge_set = set(graph)
    for first_value, second_value in edge_set:
        for third_value, fourth_value in edge_set:
            if second_value == third_value and (first_value, fourth_value) not in edge_set:
                return False
    return True


def check_linearity(graph) -> bool:
    vertices = list(set(v for edge in graph for v in edge))
    edge_set = set(graph)

    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            first_value, second_value = vertices[i], vertices[j]
            if (first_value, second_value) not in edge_set and (second_value, first_value) not in edge_set:
                return False
    return True
import numpy as np
def boolean_matrix_multiplication(A, B):
    # Применяем логическое умножение строк и столбцов матриц с помощью операций AND и OR
    return np.logical_and.reduce(A[:, :, np.newaxis] | B[np.newaxis, :, :], axis=1)

# Пример использования
A = np.array([[0, 0], [0, 1]])
B = np.array([[1, 0], [1, 0]])
C = boolean_matrix_multiplication(A, B)
print(C)

from scipy.sparse import csr_array
from scipy.sparse.csgraph import floyd_warshall
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# Создание графа
G = nx.Graph() #не ориентированный
G=nx.DiGraph(directed=True) # ориентированный

# Добавление вершин, т.е. задание множества A для прямого произведения A*A
G.add_nodes_from([1, 2, 3, 4, 5])
# Добавление рёбер, то есть задание бинарного отношения, т.е. подмножества A*A
A=[(1, 3), (2, 3), (2, 1),(5,4),(1,5),(2,3)]

G.add_edges_from(A)

# Визуализация графа
nx.draw(G, with_labels=True, node_color='lightblue')
plt.show()

#Нахождение матрицы смежности B по бинарному отношению
n=5#задание числа вершин графа
B = np.zeros((n, n))

for t in A:
    B[t[0]-1][t[1]-1]=1
#матрица смежности графа по заданному бинарному отношению
print(B)

graph = B
graph = csr_array(graph)
print(graph)

dist_matrix, predecessors = floyd_warshall(csgraph=graph, directed=True, return_predecessors=True)
print(dist_matrix) # Матрица расстояний N x N между узлами графа. dist_matrix[i,j] задает кратчайшее расстояние от точки i до точки j на графе
print(predecessors)

print(check_transitivity(A))
