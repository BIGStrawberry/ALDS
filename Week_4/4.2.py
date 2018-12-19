"""
Student Naam:   Wouter Dijkstra
Student Nr. :   1700101
Klas        :   ??
Docent      :   frits.dannenberg@hu.nl
"""

import random

all_hashes = dict()
amount_of_tries = 0

while True:
    amount_of_tries += 1

    #get random number
    number = random.random()

    hashed_number = hash(number)

    if hashed_number in all_hashes and all_hashes[hashed_number] != number:
        print("Number: ", number, " has the same hash as ", all_hashes[hashed_number])
        print("Amount of tries: ", amount_of_tries)
        break

    all_hashes[hashed_number] = number


