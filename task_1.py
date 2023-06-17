from collections import Counter


def search_similiar(source_list):
    items_count = Counter(source_list).items()
    result = []
    for i in items_count:
        if i[1] > 1:
            result.append(i[0])
    return result


s = [10, 10, 23, 10, 123, 66, 78, 123]
print(f"Исходный список: {s}")
print(f"Список с пвовторяющимися элементами: {search_similiar(s)}")
