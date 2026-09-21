def companyInfo(companyName, companyAddress):
    if not companyName or not companyAddress:
        return "Info Company: Devmaster"
    
    return "Info Company: " + companyName + ", " + companyAddress

print("Gọi hàm và truyền giá trị đầu đủ")
info = companyInfo("Devmaster Academy", "Số 25 Vũ Ngọc Phan")
print(info)

print("Gọi hàm với giá trị None hoặc rỗng")
info = companyInfo(None, '')
print(info)

def printInfo(name, age):
    print("Name: ", name)
    print("Age: ", age)
    
printInfo("Devmaster", 5)
printInfo("Devmaster Academy", 1)