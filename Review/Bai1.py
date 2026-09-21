n = int(input("Nhập n: "))
tong = 0

for i in range(1, n):
    if (i%3==0 or i%5==0):
        print(i)
        tong += i
        
print(f"Tổng: {tong}")