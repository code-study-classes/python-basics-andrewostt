from math import factorial


def square_odds(numbers):
    return list(map(lambda x: x * x, filter(lambda x: x % 2 != 0, numbers)))


def normalize_names(names):
    return list(map(lambda name: name.capitalize(), names))


def remove_invalid_emails(emails):
    # валидный email: ровно один '@', длина >= 5,
    # не начинается и не заканчивается на '@'
    def is_valid_email(e):
        return (len(e) >= 5 and 
                e.count('@') == 1 and 
                not (e.startswith('@') or e.endswith('@')))
    
    return list(filter(is_valid_email, emails))


def filter_palindromes(words):
    return list(filter(lambda w: (w.lower() == w.lower()[::-1]), words))


def calculate_factorial(n):
    return factorial(n)


def find_common_prefix(strings):
    if not strings:
        return ''
    # Найдем минимальную длину строки
    min_len = min(map(len, strings))
    # Функция для проверки, что все строки имеют одинаковый символ на позиции i

    def all_equal(i):
        chars = map(lambda s: s[i], strings)
        first = next(chars)
        return all(c == first for c in chars)
    # Используем reduce, чтобы собрать префикс
    prefix_chars = []
    for i in range(min_len):
        if all_equal(i):
            prefix_chars.append(strings[0][i])
        else:
            break
    return ''.join(prefix_chars)
