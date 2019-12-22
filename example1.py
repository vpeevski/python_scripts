a, b = 0, 1
while a < 10:
    end = ","
    if b > 10 :
        end = ""
    print(a, end = end)
    a, b = b, a+b
