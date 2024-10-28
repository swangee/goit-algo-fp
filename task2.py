import math
import turtle

def pythagoras_tree(t, size, depth, direction = 'left'):
    if depth == 0:
        return

    # Малюємо базовий квадрат
    for _ in range(4):
        t.forward(size)
        t.right(90)

    # Зберігаємо поточне положення та напрямок черепашки для нових гілок
    position = t.position()
    heading = t.heading()

    # Ліва гілка
    t.up()
    t.forward(size)
    t.left(45)
    t.down()
    pythagoras_tree(t, size * math.sqrt(0.5), depth - 1)

    # Повертаємо черепашку до початкового положення та напряму
    t.up()
    t.setposition(position)
    t.setheading(heading)
    t.down()

    # Повертаємо черепашку до вихідного положення для правої гілки
    t.up()
    t.right(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(45)
    t.forward(size * math.sqrt(0.5))
    t.right(90)
    t.down()

    pythagoras_tree(t, size * math.sqrt(0.5), depth - 1, 'right')
    t.up()

    # Повертаємо черепашку до початкового положення та напряму
    t.setposition(position)
    t.setheading(heading)

    if direction == 'right':
        t.right(90)
        t.forward(size)

def draw_pythagoras_tree(depth, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.up()
    t.goto(-size / 2, 0)
    t.down()

    t.left(90)  # Орієнтуємо черепашку вертикально вгору

    # Малюємо дерево Піфагора з початковим розміром та глибиною
    pythagoras_tree(t, size=100, depth=depth)

    turtle.done()

# Виклик функції
draw_pythagoras_tree(10)
