def menu():
    print("\n =====MENU=====")
    print("1. Nhập số nguyên n, mảng n số nguyên")
    print("2. Hiển thị danh sách các phần tử trong mảng")
    print("3. Hiển thị các phần tử là số nguyên tố, tính tổng")
    print("4. Sắp xếp mảng theo thứ tự tăng dần")
    print("5. Thoát")
    
def inputList(lst):
    print("Nhập n=", end="")
    n = int(input())
    
    for i in range(0, n):
        lst.insert(i, input())
        
def printList(lst):
    print("Danh sách các phần tử trong mảng:")
    for i in lst:
        print(i, end="; ")
        
def kiemTraNto(x):
    flag = True
    x = int(x)
    y = x // 2
    
    for i in range(2, y+1):
        if (x%i == 0):
            flag = False
            break
    
    return flag

def listNto(lst):
    tong = 0
    
    for item in lst:
        if (kiemTraNto(item) == True):
            print(item, end="; ")
            tong += int(item)
            
    return tong

def sapXep(lst):
    print("Danh sách trước khi sắp xếp:")
    print(lst)
    
    print("Danh sách sau khi sắp xếp:")
    lst.sort()
    print(lst)
    
    print("Sắp xếp giảm:")
    lst.reverse()
    print(lst)
    
def main():
    lst = []
    while True:
        menu()
        chon = input("Chọn chức năng:")
        
        if (chon == "1"):
            inputList(lst)
        elif (chon == "2"):
            printList(lst)
        elif (chon == "3"):
            t = listNto(lst)
            print("Tổng: ", t)
        elif (chon == "4"):
            sapXep(lst)
        elif (chon == "5"):
            print("GoodBye")
            break
        
main()