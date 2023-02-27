def check_brackets(brackets_row: str) -> bool:

    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    row = []
    if not isinstance(brackets_row, str):
        raise TypeError("Доллжно быть сторокой")

    for j in brackets_row:
        if j == "(":
            row.append(j)
        elif j == ")":
            if row:
                row.pop()
            else:
                return False

    if len(row) == 0:
        return True
    else:
        return False


      # TODO реализовать проверку скобочной группы


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
