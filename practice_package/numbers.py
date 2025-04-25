def calculate_distance(x1, x2):
    # L - lambda-функция внутри, возвращаем результат
    def f(a, b):
        return abs(b - a)
    return f(x1, x2)


def calculate_segments(length_a, length_b):
    def f(a, b):
        return a // b
    return f(length_a, length_b)


def calculate_digit_sum(number):
    def f(n):
        return sum(map(int, str(abs(n))))
    return f(number)


def round_to_multiple(number, multiple):
    return round(number / multiple) * multiple


def calculate_rect_area(x1, y1, x2, y2):
    return abs(x2 - x1) * abs(y2 - y1)
