"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        return 0
    min_ = arr[0]
    for i in arr:
        if i < min_:
            min_ = i
    return min_


if __name__ == '__main__':
    print(min_search([1,4,6,7,0]))  # 0
    print(min_search([2,6,9]))  # 2
    print(min_search([]))  # 2