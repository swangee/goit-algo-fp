import heapq

import networkx as nx
import matplotlib.pyplot as plt

def add_edges(graph, heap, el_pos, pos, x=0, y=0, layer=1):
    # Додаємо вузли і ребра, згідно з правилами побудови бінарної купи

    graph.add_node(el_pos, id=el_pos, color='skyblue', label=heap[el_pos]) # Використання id та збереження значення вузла
    # Визначаємо індекси дочірніх елементів
    left_child = 2 * el_pos + 1
    right_child = 2 * el_pos + 2

    if left_child < len(heap):
        graph.add_edge(el_pos, left_child)
        l = x - 1 / 2 ** layer
        pos[left_child] = (l, y - 1)
        l = add_edges(graph, heap, left_child, pos, x=l, y=y - 1, layer=layer + 1)
    if right_child < len(heap):
        graph.add_edge(el_pos, right_child)
        r = x + 1 / 2 ** layer
        pos[right_child] = (r, y - 1)
        r = add_edges(graph, heap, right_child, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(heap):
    tree = nx.DiGraph()
    pos = {heap[0]: (0, 0)}
    tree = add_edges(tree, heap, 0, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

if __name__ == '__main__':
    heap = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    heapq.heapify(heap)

    # Відображення дерева
    draw_tree(heap)