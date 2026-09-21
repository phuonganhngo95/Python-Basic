# def sayHello(name):
#     if not name:
#         print("Hello every body")
#     else:
#         print("Hello " + name)
        
# sayHello("")
# sayHello("Python")
# sayHello("Java")



# def getGreeting(name):
#     if not name:
#         return "Hello every body"
#     else:
#         return "Hello " + name

# greeting = getGreeting("")
# print(greeting)
# greeting = getGreeting("Python")
# print(greeting)


# def showInfo(name, gender):
#     print("Name: ", name)
#     print("Gender: ", gender)
    
# showInfo("Tran", "Male")
# showInfo("Tran", "Female")



# def showInfo(name, gender = "Male", country = "US"):
#     print("Name: ", name)
#     print("Gender: ", gender)
#     print("Country: ", country)

# showInfo("Aladin", "Male", "India")
# print("------------------")
# showInfo("Tom", "Male")
# print("------------------")
# showInfo("Jerry")
# print("------------------")
# showInfo(name = "Tintin", country= "Belgium")
# print("------------------")



# def sumValues(a, b, *others):
#     retValue = a + b
    
#     for other in others:
#         retValue += other
#     return retValue

# a = sumValues(10, 20)
# print(a)
# a = sumValues(10, 20, 30)
# print(a)


# hello = lambda : "Hello"

# mySum = lambda a, b: a + b

# a = hello()
# print(a)
# a = mySum(10, 20)
# print(a)

# def hello(name):
#     return "Hello " + name

# name = input("Enter your name: ")
# print(hello(name))


# def showInfo(name, gender="Male", country="US"):
#     print("Name: ", name)
#     print("Gender: ", gender)
#     print("Country: ", country)
    
# showInfo("Phuong Anh", "Male", "VietNam")
# showInfo("Tom", "Male")
# showInfo("Jerry")
# showInfo(name="Tintin", country="France")

# def sumValues(a, b, *others):
#     retValue = a + b
    
#     for other in others:
#         retValue = retValue + other
    
#     return retValue

# a = sumValues(10, 20)
# print(a)

# a = sumValues(10, 20, 1)
# print(a)

# a = sumValues(10, 20, 1, 2, 3, 4, 5)
# print(a)

hello = lambda : "Hello"

mySum = lambda a, b : a + b

a = hello()
print(a)

a = mySum(10, 20)
print(a)