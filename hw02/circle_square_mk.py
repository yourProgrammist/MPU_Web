import random


def circle_square_mk(r, n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(0, 2 * r)
        y = random.uniform(0, 2 * r)
        if (x - r) ** 2 + (y - r) ** 2 <= r ** 2:
            inside_circle += 1
    square_area = (2 * r) ** 2
    return square_area * inside_circle / n


if __name__ == "__main__":
    r = 1
    n = 100000

    circle_area_mk = circle_square_mk(r, n)
    print("Площадь окружности (Монте-Карло):", circle_area_mk)

    circle_area_formula = 3.14159265358979323846 * r ** 2
    print("Площадь окружности (формула):", circle_area_formula)

    error = abs(circle_area_mk - circle_area_formula)
    print("Погрешность расчета:", error)


#           r           n           (Монте-Карло)              (формула)            Погрешность расчета
#           1         100000            3.13636            3.141592653589793        0.005232653589793301
#           1        1000000           3.141168            3.141592653589793        0.0004246535897931558
#           1       10000000           3.1412448           3.141592653589793        0.00034785358979316783