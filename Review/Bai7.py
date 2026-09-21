n = int(input("Nhập số nguyên dương N: "))
so_mu = pow(2, n)

tong_chu_so = 0
for chu_so in str(so_mu):  
    so = int(chu_so)       
    tong_chu_so += so

print(f"Tổng các chữ số của 2^{n} là: {tong_chu_so}")
