def sum_even_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            total += digit
        number //= 10
    return total


def count_vowel_triplets(text, index=0):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    text = text.lower()

    def helper(i):
        if i > len(text) - 3:
            return 0
        triplet = text[i:i + 3]
        if all(ch in vowels for ch in triplet):
            return 1 + helper(i + 3)
        else:
            return helper(i + 1)

    return helper(0)
    pass


def find_fibonacci_index(number):
    if number == 1:
        return 1
    a, b = 1, 1
    index = 2
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1


def remove_duplicates(string):
    if not string:
        return ""
    result = string[0]
    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            result += string[i]
    return result
