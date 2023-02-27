from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    min_ = 0
    max_ = len(seq) - 1

    while min_<= max_:
        midl = (min_ + max_)// 2
        if seq[midl] == value:
            return midl
        elif seq[midl] > value:
            max_ = midl - 1
        else:
            min_ = midl + 1
    raise ValueError



if __name__ == '__main__':
    print(binary_search(4, [1,2,3,4,5,6]))