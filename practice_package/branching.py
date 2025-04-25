def is_weekend(day):
    return day in {6, 7}


def get_discount(amount):
    if amount >= 5000:
        return round(0.1 * amount, 2)
    elif amount >= 1000:
        return round(0.05 * amount, 2)
    else:
        return 0


def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    if 0 <= n <= 9:
        digits = "однозначное"
    elif 10 <= n <= 99:
        digits = "двузначное"
    else:
        digits = "трехзначное"
    return f"{parity} {digits} число"


def convert_to_meters(unitNumber, lengthInUnits):
    multipliers = [0.1, 1000, 1, 0.001, 0.01]
    return lengthInUnits * multipliers[unitNumber - 1]


def describe_age(age):
    tens = {
        2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
        6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 
        9: 'девяносто', 10: 'сто'
    }
    units = {
        1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
        6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
    }

    ten_part = age // 10
    unit_part = age % 10

    age_str = []
    if 20 <= age <= 99:
        age_str.append(tens[ten_part])
        if unit_part != 0:
            age_str.append(units[unit_part])
    elif age == 100:
        age_str.append(tens[10])

    last_two = age % 100
    # заменяем match-case на словарь и логические выражения
    suffix = (
        'лет' if 11 <= last_two <= 14 else
        'год' if unit_part == 1 else
        'года' if unit_part in {2, 3, 4} else
        'лет'
    )

    return ' '.join(age_str) + ' ' + suffix
