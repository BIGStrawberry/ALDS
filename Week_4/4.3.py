# Maak de functie B(n,k) die (n!//(k!))//(n-k)! berekent.
# Doe dit op basis van dynamic programming.
# Wat is B(100,50) ?

def B(a, b):
    rows = [[1], [1, 1  ]]
    i = 1
    while i < a:
        last_row = rows[i]
        new_row = [1]
        row_index = 0

        while row_index<len(last_row)-1:
            new_row.append(last_row[row_index]+last_row[row_index+1])
            row_index += 1

        new_row.append(1)
        rows.append(new_row)
        i += 1

    return rows[a][b]

print(B(100, 50))

