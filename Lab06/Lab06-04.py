def sumValues(a, b, *c):
    reVal = a + b
    
    for item in c:
        reVal += item
        
    return reVal

x = sumValues(10, 20)
print(x)

x = sumValues(10, 20, 30)
print(x)

x = sumValues(10, 20, 30, 40)
print(x)

x = sumValues(10, 20, 1, 2, 3, 4, 5)
print(x)