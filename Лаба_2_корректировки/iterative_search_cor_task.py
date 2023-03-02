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
    if len(arr) == 0:
        raise ValueError ("Введите не пустую последовательность")

    min_ = arr[0]
    ind = 0
    for i in range(0, len(arr)):
        if arr[i] < min_:
            min_ = arr[i]
            ind = i
    return ind
    # for i in arr:
    #     if i < min_:
    #         min_ = i
    # return min_

if __name__ == '__main__':
    print(min_search([1,4,6,7,0]))  # 0
    print(min_search([2,2,2]))  # 2
    print(min_search([1]))  # 2