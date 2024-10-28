import heapq
import random
import networkx as nx

def find_shortest_path(graph, start):
    # Ініціалізуємо відстані як нескінченність для всіх вузлів
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # Відстань до стартового вузла

    # Черга з пріоритетами для обробки вузлів
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Пропускаємо вузли, якщо вже знайдена коротша відстань
        if current_distance > distances[current_node]:
            continue

        # Оновлюємо відстані до сусідів
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад графа у форматі словника
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Виконуємо алгоритм Дейкстри від вузла 'A'
shortest_paths = find_shortest_path(graph, 'A')
print(shortest_paths)