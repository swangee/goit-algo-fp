import heapq

import networkx as nx
from matplotlib import pyplot as plt

import task4
from collections import deque

def darken_color_multiply(rgb, factor):
    """Темніє колір множенням кожного компонента на фактор менший за 1"""
    r, g, b = rgb
    return (
        int(r * factor),
        int(g * factor),
        int(b * factor)
    )

def hex_to_rgb(hex_color):
    """Перетворює шістнадцятковий колір у форматі #RRGGBB на RGB."""
    hex_color = hex_color.lstrip('#')  # Видаляємо #, якщо він є
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    """Converts RGB values to a hexadecimal color code."""
    # Ensure RGB values are within the range 0-255
    if not all(0 <= value <= 255 for value in (r, g, b)):
        raise ValueError("RGB values must be between 0 and 255.")

    # Format the RGB values as a hex string and return it
    return f"#{r:02x}{g:02x}{b:02x}".upper()

def dfs(graph):
    color = hex_to_rgb('#1296F0')

    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [graph.nodes[0]]
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        if vertex['label'] not in visited:
            color = darken_color_multiply(color, 0.9)
            vertex['color'] = rgb_to_hex(color[0], color[1], color[2])
            # Відвідуємо вершину
            visited.add(vertex['label'])
            # Додаємо сусідні вершини до стеку
            children = list(graph.successors(vertex['id']))
            stack.extend([graph.nodes[id] for id in children])


def bfs(graph):
    color = hex_to_rgb('#1296F0')

    visited = set()
    queue = deque([graph.nodes[0]])
    search_queue = list()

    while queue:
        vertex = queue.popleft()
        search_queue.append(vertex)

        if vertex['label'] not in visited:
            visited.add(vertex['label'])
            color = darken_color_multiply(color, 0.9)
            vertex['color'] = rgb_to_hex(color[0], color[1], color[2])
            children = list(graph.successors(vertex['id']))
            queue.extend([graph.nodes[id] for id in children])

    return search_queue

def draw_tree(heap, color):
    tree = nx.DiGraph()
    pos = {heap[0]: (0, 0)}
    tree = task4.add_edges(tree, heap, 0, pos)

    color(tree)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

if __name__ == '__main__':
    heap = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    heapq.heapify(heap)

    walk_type = "dfs"

    # Відображення дерева
    if walk_type == "dfs":
        draw_tree(heap, dfs)
    else:
        draw_tree(heap, bfs)