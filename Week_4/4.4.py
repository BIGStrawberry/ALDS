"""
Student Naam:   Wouter Dijkstra
Student Nr. :   1700101
Klas        :   ??
Docent      :   frits.dannenberg@hu.nl
"""

available_coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

def f(n):
    assert type(n) == int  # Check of n van type INT is
    assert n <= 10000  # Check of n kleiner of gelijk is aan 10000

    minimum_coins = [[0 for _ in range(n + 1)] for _ in range(len(available_coins) + 1)]
    for i in range(n + 1):
        minimum_coins[0][i] = i
    for c in range(1, len(available_coins) + 1):
        for r in range(1, n + 1):
            if available_coins[c - 1] == r:
                minimum_coins[c][r] = 1
            elif available_coins[c - 1] > r:
                minimum_coins[c][r] = minimum_coins[c - 1][r]
            else:
                minimum_coins[c][r] = min(minimum_coins[c - 1][r], 1 + minimum_coins[c][r - available_coins[c - 1]])

    return minimum_coins[-1][-1]


print("Ik moet 100EU betalen, dit kan ik doen met >>", f(100), "<< munt(en).")
print("Ik moet 7EU betalen, dit kan ik doen met >>", f(7), "<< munt(en).")
print("Ik moet 5451EU betalen, dit kan ik doen met >>", f(5451), "<< munt(en).")
print("Ik moet 10000EU betalen, dit kan ik doen met >>", f(10000), "<< munt(en).")
