C = input("Nhập dãy C: ")
N = int(input("Nhập N: "))

ket_qua = 0
min_chenh_lech = float('inf')

for i in range(len(C) - N + 1):
    day_so = C[i:i+N] 

    cac_so = []
    for ch in day_so: 
        so = int(ch) 
        cac_so.append(so) 

    lon_nhat = max(cac_so)
    nho_nhat = min(cac_so)
    chenh_lech = lon_nhat - nho_nhat

    print(f"Dãy con = {day_so}, max = {lon_nhat}, min = {nho_nhat}, chênh lệch = {chenh_lech}")

    if chenh_lech < min_chenh_lech:
        min_chenh_lech = chenh_lech
        ket_qua = day_so
        
print(f"\nDãy con tốt nhất= {ket_qua} - chênh lệch nhỏ nhất = {min_chenh_lech}")

