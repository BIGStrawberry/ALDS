"""
Student Naam:   Wouter Dijkstra
Student Nr. :   1700101
Klas        :   ??
Docent      :   frits.dannenberg@hu.nl
"""

"""
Description
-----------
Takes an integer n to return all the prime numbers from 2 to n

Parameters
----------
n : integer
    amount of numbers to check

Return
------
primes : list
    list of prime numbers
"""


def eratosthenes(n):  # Zeef van Eratosthenes
    primes = []
    sieve = [True] * (n + 1)

    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes


# Main
print(eratosthenes(100))
