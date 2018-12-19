import random


class HashTable:
    def __init__(self):
        self.data = [None for _ in range(11)]
        self.num_elements = 0

    def __repr__(self):
        s = ''

        for i in range(len(self.data)):
            sets = self.data[i]
            s += str(i) + ": \n"
            if sets is not None:  # and sets != set()
                for value in sets:
                    s += "    " + str(value)
                s += '\n'
        return s


    def search(self, e):
        hashed = hash(e) % self.num_elements
        return self.data[hashed] is not None and e in self.data[hashed]

    def insert(self, e):
        self.num_elements += 1
        if len(self.data) > 0 and self.num_elements / len(self.data) > 0.75:
            self.rehash(len(self.data) * 2)

        hashed = hash(e) % self.num_elements
        if self.data[hashed] is not None:
            self.data[hashed].add(e)
        else:
            self.data[hashed] = {e}

    def delete(self, e):
        hashed = hash(e) % self.num_elements
        if self.data[hashed] is not None and e in self.data[hashed]:
            self.data[hashed].remove(e)
            if self.data[hashed] == set():
                self.data[hashed] = None

    def rehash(self, new_size):
        print("Rehashed, from: ", len(self.data), " to: ", new_size)
        tmp = self.data[:]
        tmp_count = self.num_elements
        self.data = [None for _ in range(new_size)]

        for sets in tmp:
            if sets is not None:
                for value in sets:
                    self.num_elements -= 1  # Num_elements - 1 because insert adds one
                    self.insert(value)

        self.num_elements = tmp_count
        print(self)


hashTable = HashTable()

for i in range(200):
    hashTable.insert(random.random())

for i in range(100):
    hashTable.delete(random.random())

print("----------INSERTING-------------------")
print("Can I find 0.1890327678114233? " + str(hashTable.search(0.1890327678114233)))
print("Inserting 0.1890327678114233.. ")
hashTable.insert(0.1890327678114233)
print("Can I find 0.1890327678114233? " + str(hashTable.search(0.1890327678114233)))

print("----------DELETING--------------------")

print("Can I find 0.1890327678114233? -> " + str(hashTable.search(0.1890327678114233)))
print("Deleting 0.1890327678114233..")
hashTable.delete(0.1890327678114233)
print("Can I find 0.1890327678114233? ->" + str(hashTable.search(0.1890327678114233)))
print("--------------------------------------")
