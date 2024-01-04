#!/usr/bin/python3

if __name__ == "__main__":
    """Print the value of variable a from variable_load_5."""
    from variable_load_5 import a

    print(a)

____________________________________________________________

calculator_1.py 

#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
	 The return value. a / b
    """
    return int(a / b)




____________________________________________________________


variable_load_5.py

#!/usr/bin/python3
a = 98
"""Simple variable
"""
