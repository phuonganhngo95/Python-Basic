# def sayHello(name):
#     print(name)
    
# # sayHello("Phuong Anh")

# name = input("Nhập tên của bạn:")

# print(sayHello(input("Nhập tên của bạn:")))
# print(sayHello(name))


# def getGreeting(name, age):
#     # if not name:
#     #     return "Hello every body"
#     # else:
#     #     return "Hello " + name
    
# # greeting = getGreeting("hello")
# # print(greeting)

#     print("Hello ",name,"-" ,age)
    
# print(getGreeting("Phuong Anh", 20))

# def showInfo(name, age):
#     if not name:
#         name_info = "name is none"
#     else:
#         name_info = name
    
#     if age > 0:
#         age_info = age 
#     else:
#         age_info = "age is none"

#     return name_info, age_info
#     # return f"{name_info} - {age_info}"

# info = showInfo("Phuong Anh", 21)
# print(info)

def showInfo(name, age):
    if not name:
        name_info = "name is none"
    else:
        name_info = name
    
    if age > 0:
        age_info = age 
    else:
        age_info = "age is none"

    # return name_info, age_info
    return f"{name_info} - {age_info}"

info = showInfo(input("Nhập tên của bạn: "), int(input("Nhập tuổi của bạn: ")))
print(info)

