#!/usr/bin/python3
"""module have one method"""


def matrix_mul(m_a, m_b):
    """_summary_

    Args:
        m_a (_type_): _description_
        m_b (_type_): _description_

    Raises:
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        ValueError: _description_
        TypeError: _description_
        TypeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    row_len = None
    for matrix in [m_a, m_b]:
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(
                "m_a must be a list of lists or m_b must be a list of lists")
        if not matrix:
            raise ValueError("m_a can't be empty or m_b can't be empty")
        if row_len is None:
            row_len = len(matrix[0])
        if not all(len(row) == row_len for row in matrix):
            raise TypeError(
                "each row of m_a must be of \
the same size or each row of m_b must be of the same size")
        if not all(all(isinstance(val, (int, float)) for val in row)
                   for row in matrix):
            raise TypeError(
                "m_a should contain only integers or \
floats or m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            row.append(sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b))))
        result.append(row)

    return result
