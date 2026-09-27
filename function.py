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

# hello = lambda : "Hello"

# mySum = lambda a, b : a + b

# a = hello()
# print(a)

# a = mySum(10, 20)
# print(a)

def outer(x): # 5
    def inner(y):
        return x + y;
    
    return inner

add_5 = outer(5) #  x=5

# add_5(3) # inner(3) = add_5
# print(add_5(3))

[1, 2, 3]
["sff", "ggrgr"]

(1, 2, 3)

object = {
    "a" : 1,
    "b": 2,
}

# lst = [3, 1, 2]
# lst.sort() # sắp xếp tăng dần
# lst.reverse() # sắp xếp giảm dần

# sorted_lst = sorted(lst)    # trả về list mới

# print(lst)
# print(sorted_lst)

d = {
    "a": 1, 
    "b": 2
}

# for key, value in d.items():
#     print(key, value)
    
    
from collections import Counter, defaultdict, namedtuple, deque
c = Counter("mississippi")          # đếm tần suất
dd = defaultdict(list)              # dict với giá trị mặc định
Point = namedtuple("Point", "x y")  # tuple có tên trường
q = deque([1, 2, 3]) 
# queue

print(q)