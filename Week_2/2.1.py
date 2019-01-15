"""	
Student Naam:   Wouter Dijkstra	
Student Nr. :   1700101	
Klas        :   ??	
Docent      :   frits.dannenberg@hu.nl	
"""	
"""
Description
-----------
A function to perform power calculations with a base and exponent
Partly replaces a O(n) algorithm with a O(log(n)) one

Parameters
----------
base : Integer
    base number
exponent : Integer
    exponent

Return
------
  : Integer
    returns the result of the calculation
"""
def power(base, exponent):
    assert exponent > 0  # Assert to see if the exponent is larger than or equal to 1
    count = 0
    result = 1
    while exponent > 0:
        count += 1
        if exponent % 2 == 0: # Check if the exponent is equal
            base *= base # base squared 2
            exponent /= 2 # Divide the exponent by 2
        else:
            exponent -= 1
            result *= base

    print("Times multiplied:", count)
    return result

# Main
print(power(2, 16))
print(power(2, 49))
