a = set('abcdefg')
print(a)
for i in range(1, 5):
    a.add(i)
print(a)

b = frozenset('abcdefg')
print(b)
for i in range(1, 5):
    b.add(i)
print(b)