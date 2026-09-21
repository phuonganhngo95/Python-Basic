welcome = lambda : "Welcome to Devmaster"

sum = lambda a, b : a + b

x = welcome()
print(x)

x = sum(100, 200)
print(x)

dict1 = {"A" : "Devmaster", "B" : "Academy", "C" : "Devmaster"}
print(dict1.keys())

empty_Dict1 = {}
print(empty_Dict1.keys())

for key in dict1.keys():
    print(key, ":", dict1[key])
    
print(dict1.items())

dict2 = {"C" : "Devmaster Academy", "D" : "Python Programming"}
dict1.update(dict2)
print(dict1)