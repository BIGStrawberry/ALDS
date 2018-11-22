"""
Student Naam:   Wouter Dijkstra
Student Nr. :   1700101
Klas        :   ??
Docent      :   frits.dannenberg@hu.nl
"""

import random

"""
Description
----------- 
Creates a list with n amount of random elements ranging from random_from to random_to

Parameters
----------
n : Integer
    Amount of random elements the list should be filled with
random_from : Integer
    Lowest random number
random_to : Integer
    Highest random number

Return
------
random_list : list
    list of n amount of random elements ranging from randomFrom to randomTo
"""


def generate_random_list(n, random_from, random_to):
    random_list = []

    for i in range(n):
        random.seed()
        random_list.append(random.randint(random_from, random_to))

    return random_list

"""
Description
-----------
Creates a list with n amount of random generated lists

Parameters
----------
n : Integer
    Amount of random generated lists should be in the list
amount_of_numbers : Integer
    Amount of random elements the list should be filled with
random_from : Integer
    Lowest random number
random_to : Integer
    Highest random number

Return
------
lists : list
    list of n amount of random elements ranging from random_from to random_to
"""


def generate_lists(n, amount_of_numbers, random_from, random_to):
    lists = []

    for i in range(n):
        lists.append(generate_random_list(amount_of_numbers, random_from, random_to))

    return lists

"""
Description
-----------
Finds matches in the list. If a list contains the same number twice.

Parameters
----------
multiple_lists : list
   List of random generated lists

Return
------
count : Integer
    amount of lists that contained a matching number
"""


def find_match(multiple_lists):
    count = 0
    for random_list in multiple_lists:
        for number in random_list:
            if random_list.count(number) > 1:  # Check if the list contains 2 or more of the same number
                count += 1  # Increment the amount of matches we've found
                break  # Break out of this for loop, because there's a match

    return count


# Main
amount_of_tests = 1000;
amount_of_students = 23;

list_of_lists = generate_lists(amount_of_tests, amount_of_students, 1, 365)
matches = find_match(list_of_lists)
print("Aantal testen: " + str(amount_of_tests))
print("Aantal 'studenten' per test: " + str(amount_of_students))
print("Percentage van klassen met dubbele verjaardag: " + str(matches / (amount_of_tests/100)) + "%")
