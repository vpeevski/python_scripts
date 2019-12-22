print("#" * 8, "Lambda returned as result", "#" * 8)
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f(1)) # 43
print(f(2)) # 44

print("#" * 8, "Lambda passed as an argument", "#" * 8)
pairs = [(3, 'three'), (4, 'four'), (1, 'one'), (2, 'two')]
pairs.sort(key=lambda pair: pair[1]) # sort by string alphabetically
print("sort by string alphabetically: \n", pairs)
pairs.sort(key=lambda pair: pair[0]) # sort by number
print("sort by number: \n", pairs)
pairs.sort(key=lambda pair: pair[0], reverse=True) # sort by number, reversed
print("sort by number, reversed: \n", pairs)

