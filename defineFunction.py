def fib(n):
    a, b = 0, 1
    while a < n:
        end = ", "
        if b > n:
            end = ""
        print(a, end=end)
        a, b = b, a + b

fib(2000)
print();
print("All functions return value. Built-in None value is returned iF missing return:")
print("Returning: ", fib(0))


print("Returning value from function: ")
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print(fib2(9000))