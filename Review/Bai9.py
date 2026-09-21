s = input("Nhập chuỗi S: ")
danh_sach_chuoi = []

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        chuoi_con = s[i:j]
        
        if chuoi_con not in danh_sach_chuoi:
            danh_sach_chuoi.append(chuoi_con)
danh_sach_chuoi.sort(key=lambda x: (len(x), x))

print("Các chuỗi con liên tiếp khác nhau là:")
print(", ".join(danh_sach_chuoi))
