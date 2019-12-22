from collections import deque
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print('Apples cout is: ', fruits.count('apple'))
print('All Fuits are:', len(fruits))
fruits.reverse()
print('Reversed fruis: ', fruits)
print('Last is: ', fruits.pop())
print('New last is: ', fruits.pop())

fruitsDeque = deque(['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'])
print('First is: ', fruitsDeque.popleft())

squares = []
for x in range(10):
    print(x)
    print(x**2)
    squares.append(x**2)
print("Squares: ", squares)
print("Side effect that x exists: ", x)

squares = list(map(lambda x: x**2, range(10)))
print("Squares without side effects: ", squares)

squares = [x**2 for x in range(10)]
print("Squares without side effects, variant two: ", squares)

print("Different values from the two lists combined", [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])