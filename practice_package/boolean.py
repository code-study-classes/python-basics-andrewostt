def check_between_numbers(A, B, C):
    return (A < B < C) or (C < B < A)


def check_odd_three(number):
    return (100 <= abs(number) <= 999) and (number % 2 != 0)


def check_unique_digits(number):
    return (100 <= abs(number) <= 999) and (len(set(str(abs(number)))) == 3)


def check_palindrome_number(number):
    s = str(abs(number))
    return s == s[::-1]


def check_ascending_digits(number):
    s = str(abs(number))
    return (100 <= abs(number) <= 999) and (s[0] < s[1] < s[2])
