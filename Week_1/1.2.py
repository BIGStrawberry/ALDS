"""
Student Naam:   Wouter Dijkstra
Student Nr. :   1700101
Klas        :   ??
Docent      :   frits.dannenberg@hu.nl
"""

"""
Description
-----------
Takes a string and returns a list of the numbers inside it

Parameters
----------
a : string
    string with characters and numbers alike

Return
------
numbers : list
    list of numbers
"""


def get_numbers(a):
    for char in 'qwertyuiopasdfghjklzxcvbnm-=+[]{};:|/?.>,<':
        a = a.replace(char, ' ')
    print([int(i) for i in a.split()])


# Main
string = "as0d151a< 21.5 > sd1 213 word [}sd9 18238"
string1 = 'een123zin45 6met-632more+7777digits'
get_numbers(string1)
