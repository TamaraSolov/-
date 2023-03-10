from typing import Sequence
import random

def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    print("Исходный список", container)

    max_ = container[0] # определяем максимум
    for el in container:
        if el > max_:
            max_ = el
    count = [0] * (max_ + 1) # создаем вспомогательный список для подсчетом количества элементов
    for i in range(len(container)): # считаем кол-во вхождений каждого эл-та в массив container
        count[container[i]] += 1

    for i in range(len(count)): # выводим кол-во вхождений каждого эл-та в массив container
        if count[i] > 0:
            print(i, "Количество вхождений", count[i])

    count[0] -= 1
    for i in range(1, max_ + 1):
         count[i] += count[i-1]

    # выводим отсортированный массив container в порядке возрастания
    result = [0] * len(container)
    for i in reversed(container):
        result[count[i]] = i
        count[i] -= 1
    return result

    # a = []
    # for i in range(10):
    #     a.append(random.randint(0,10))
    #
    # container = [0] * 11
    # for i in a:
    #     container[i] +=1
    # print(a)
    # for i in range(11):
    #     if container[i] > 0:
    #         print(i, container[i])
    #     return list(container)


if __name__ == '__main__':
    print("Отсортированный в порядке возрастания", sort([4,6,6,8,9,10,10,2,1,1,0]))