import random
from collections import defaultdict


def calculate_probability(values = (1, 1), iterations = 1000):
    table = defaultdict(int)

    for i in range(iterations):
        sum = int(random.uniform(1, 7)) + int(random.uniform(1, 7))

        table[sum] += 1

    for key in table:
        table[key] = (table[key] / iterations) * 100

    return table

def print_table(result):
    keys = list(result.keys())
    keys = sorted(keys)

    print("Сума | Ймовірність")

    for key in keys:
        print(f"{key}: {result[key]:.2f}%")

result = calculate_probability(iterations=1_000_000)

print_table(result)