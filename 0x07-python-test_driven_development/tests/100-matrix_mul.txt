The ``100-matrix_mul`` module
===============================

Using ``matrix_mul``
------------------------

This is an example text file in reStructuredText format.  First import
``matrix_mul`` from the ``100-matrix_mul`` module:

    >>> matrix_mul = __import__('100-matrix_mul').matrix_mul

Now use it:

    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]

Test bad matrices:    
    >>> matrix_mul([[1, 2, 3], [3, 4, 5]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
        ...
    ValueError: m_a and m_b can't be multiplied
    
Test m_a is empty:
    >>> matrix_mul([], [[4]])
    Traceback (most recent call last):
        ...
    ValueError: m_a can't be empty

Test m_b is empty:
    >>> matrix_mul([[4]], [[]])
    Traceback (most recent call last):
        ...
    ValueError: m_b can't be empty

Test single value:
    >>> matrix_mul([[4]], [[6]])
    [[24]]

Test matrice m_a has str:
    >>> matrix_mul([['two']], [[6]])
    Traceback (most recent call last):
        ...
    TypeError: m_a should contain only integers or floats

Test m_b is str:
    >>> matrix_mul([[4]], "two")
    Traceback (most recent call last):
        ...
    TypeError: m_b must be a list

Test int list:
    >>> matrix_mul([1, 2, 3], [[4]])
    Traceback (most recent call last):
        ...
    TypeError: m_a must be a list of lists

Test bad rows:
    >>> matrix_mul([[1, 2], [3, 4, 5], [6, 7]], [[1, 2, 3], [4, 5, 6]])
    Traceback (most recent call last):
        ...
    TypeError: each row of m_a must be of the same size

Test missing arguments:
    >>> matrix_mul([[4]])
    Traceback (most recent call last):
        ...
    TypeError: matrix_mul() missing 1 required positional argument: 'm_b'

Test missing arguments:
    >>> matrix_mul()
    Traceback (most recent call last):
        ...
    TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'
