def greedy_algorithm(items, budget):
    dishes = [{"name": name, "value": item["calories"]/item["cost"], "cost": item["cost"]} for name, item in items.items()]
    sorted_dishes = sorted(dishes, key=lambda dish: dish["value"], reverse=True)

    result = []
    cost = 0

    for dish in sorted_dishes:
        if cost + dish["value"] > budget:
            break

        result.append(dish["name"])
        cost += dish["cost"]

    return result

def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]

    dp = [0] * (budget + 1)

    items_per_budget = {b: [] for b in range(budget + 1)}

    for i in range(len(items)):
        # Проходимось у зворотньому напрямку від розміру бюджету до вартості страви
        # Якщо для певного значення ціни ми можемо додати в набір більш калорійну страву - робимо це
        for b in range(budget, costs[i] - 1, -1):
            if dp[b] < dp[b - costs[i]] + calories[i]:
                dp[b] = dp[b - costs[i]] + calories[i]
                items_per_budget[b] = items_per_budget[b - costs[i]] + [names[i]]

    total_calories = dp[budget]
    selected_items = items_per_budget[budget]

    return total_calories, selected_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print(greedy_algorithm(items, budget=50))
print(dynamic_programming(items, budget=50))