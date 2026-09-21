n = int(input("Nhập số N: "))

for i in range(n - 1, 0, -1):
    so_ban_dau = i
    so_dao_nguoc = 0
    
    while so_ban_dau > 0:
        chu_so_cuoi = so_ban_dau % 10                 
        so_dao_nguoc = so_dao_nguoc * 10 + chu_so_cuoi
        so_ban_dau = so_ban_dau // 10                
    print(so_dao_nguoc)

    if so_dao_nguoc == i:
        print(f"Số đối xứng lớn nhất nhỏ hơn {n} là: {i}")
        break
    
    
    