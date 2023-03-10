from typing import Sequence
import random
import time

def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    if len(container) > 1:
        count = 0
        for j in range(len(container)):
            for i in range(len(container) - 1):
                if container[i] > container[i+1]:
                    count += 1 # количество замен
                    container[i], container[i+1] = container[i+1], container[i]
            # print(container)
        print(count)
    return container

     # TODO реализовать алгоритм сортировки пузырьком

print(sort([4,6,8,9,10,2,1]))
# arr = [random.randint(-100, 100) for i in range(50000)]
# t = time.time()
# sort(arr)
# t = time.time() - t
# print(arr)
# print(t)