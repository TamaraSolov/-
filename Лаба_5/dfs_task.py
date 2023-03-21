from typing import Hashable, List
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    # принцип стека
    visited = set()
    queue = deque([start_node])
    result = []
    visited.add(start_node)
    while queue:
        current_node = queue.pop()
        result.append(current_node)
        for neighbour in g[current_node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return result

    # TODO реализовать обход в глубину итеративным способом
if __name__ == '__main__':
    graph =nx.Graph()
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('A', 'D'),
        ('B', 'E'),
        ('E', 'F'),
        ('C', 'G'),
        ('C', 'H'),
        ('G', 'I'),
        ('D', 'J')
    ])
    nx.draw(graph, node_color='green', node_size=1500, with_labels=True)
    plt.show()
    print(dfs(graph, 'A'))