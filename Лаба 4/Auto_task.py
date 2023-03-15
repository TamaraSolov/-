from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    field = [[0] * m for i in range(n)]
    field[0][0] = 1

    for i in range(n):
        for j in range(m):
            point = field[i][j]
            if (j + 1) < m:
                # идем вправо
                field[i][j +1 ] += point
            if (i + 1 ) < n:
                # идем вниз
                field[i + 1][j] += point
            if (i + 1) < n and (j + 1) < m:
                # идем по диагонали
                field[i+1][j+1] += point
    return field



    # for i in range(n):
    #     for j in range(m):
    #         print(field[i][j], end=" ")


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
