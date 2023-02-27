def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n < 0:
        raise ValueError ("не должно быть отрицательным")
    if n == 0:
        return 0
    fac = 1
    for i in range(2, n+1):
        fac *= i
    return fac


if __name__ == '__main__':
    print(factorial_iterative(8))
    print(factorial_iterative(1))