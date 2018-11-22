"""
Student Naam:   Wouter Dijkstra
Student Nr. :   1700101
Klas        :   ??
Docent      :   frits.dannenberg@hu.nl
"""

import numbers

"""
Description
-----------
Takes a list of numbers and returns the highest number in it as an integer

Parameters
----------
i_list : list
    list of numbers

Return
------
max_number: integer
    max number from the given list
"""


def my_max(i_list):
    max_number = 0

    # Assert to see if the list is not empty
    assert len(i_list) > 0, "List does not contain any elements"

    for l in i_list:
        # Assert to see if number is an int or float
        assert type(l) == int or type(l) == float, "not of int or float type"
        if l > max_number:
            max_number = l
    # Return the biggest number found in the list
    return max_number

# Main

integer_list = [2, 3, 0, 23, 81, 9219, "a"]
print(my_max(integer_list))
