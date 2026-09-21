n = int(input("Nhập n: "))

a, b = 0, 1
fibo_max = 0

for i in range(n+2):
    if a <= n:
        fibo_max = a
        a, b = b, a+b
    else:
        break
    
print(f"Số fibonacci lớn nhất không quá n: {fibo_max}")