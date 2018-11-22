"""
Student Naam:   Wouter Dijkstra
Student Nr. :   1700101
Klas        :   ??
Docent      :   frits.dannenberg@hu.nl
"""

def my_bin(n):
    assert n >= 0, "n is not larger than 0"

    return (my_bin(n // 2) + str(n % 2)) if n > 0 else ''

# Main
for i in range(256):
    print(i, " = ", my_bin(i))

