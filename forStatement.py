print("############# Example 1 #########")
words = ['defenestrate', 'cat', 'window']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.append(w)
print(words)

# With for w in words:, the example would attempt to create an infinite list, inserting defenestrate over and over again.
print("############# Example 2: single bounded range #########")
for i in range(5):
    print(i)

print("############# Example 3: double bounded range #########")
for i in range(5, 10):
    print(i)

print("############# Example 4: double bounded range with step #########")
for i in range(0, 10, 3):
    print(i)

print("############# Example 5: range is not a list #########")
print(range(5))
print(list(range(5))) #turn it into list