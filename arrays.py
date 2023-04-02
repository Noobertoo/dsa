import array as arr

a = arr.array('i', [1, 2, 4, 5])

a.append(6)  # O(1)

a.insert(0, 0)  # O(n)

print(a)
