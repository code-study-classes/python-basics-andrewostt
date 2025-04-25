def find_common_elements(set1, set2):
    # без оператора &
    return {x for x in set1 if x in set2}


def is_superset(set_a, set_b):
    # без оператора >=
    return all(elem in set_a for elem in set_b)


def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def count_unique_words(text):
    words = text.lower().split()
    return len(set(words))


def find_shared_items(*sets):
    if not sets:
        return set()
    # пересечение всех множеств через reduce и метод intersection
    from functools import reduce
    return reduce(lambda a, b: a.intersection(b), sets)
