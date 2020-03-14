# list_gen.py
"""
Generate and return random lists
"""

from random import randint
from random import choice


def unsorted_list(min: int, max: int, list_size: int)-> list:
    """
    Generates random unsorted list of integers
    The list may contain redundant values
    INPUT:
            min: lowest possible value of the list
            max: highest possible value of the list
            list_size: maximum size of the list
    OUTPUT:
            unsorted_list: list of unsorted inetegers
    """

    # initialization
    unsort_list = [] # unsorted list 

    # generating the list
    try:
        for _ in range(list_size):
            unsort_list.append(randint(min, max))
        return unsort_list
    except ValueError:
        print("Incorrect range values, min must be less or equal to max parameter")
        return unsort_list


def sorted_list(min: int, step: int, list_size: int)-> list:
    """
    Generates sorted list of non redundant integers
    The list does not contain redundant values
    INPUT:
            min: lowest possible value of the list
            step: range of numbers to select a number from
            list_size: maximum size of the list
    OUTPUT:
            sorted_list: list of sorted integers
    """

    # initialization
    sorted_list = []
    max = step

    # generating the list
    try:
        for _ in range(list_size):
            sorted_list.append(randint(min, max))
            min = sorted_list[-1] + 1
            max = min + step
        return sorted_list
    except ValueError:
        print("Incorrect range values, min must be less or equal to max parameter")
        return sorted_list


def string_pattern(pool: tuple, pattern_size: int)-> str:
    """
    Generates random pattern string from the pool's item
    The pattern string may contain redundant elements
    INPUT:
            pool: a set of elements used to construct the pattern string
            pattern_size: maximum size of the pattern string
    OUTPUT:
            pattern_string: pattern string of elements from the pool
    """

    # initialization
    pattern = ""

    # if pool is not tuple, then it must be converted to tuple
    if isinstance(pool, int) or isinstance(pool, float) or isinstance(pool, str):
        pool = (pool,)
        
    # generating the list
    try:
        for _ in range(pattern_size):
            pattern = pattern + str(choice(pool))
        return pattern
    except IndexError:
        print("Item's pool to generate the pattern is empty")
        return pattern