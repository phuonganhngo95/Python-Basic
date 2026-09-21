# Nhập chuỗi từ người dùng
chuoi_nhap = input("Nhập dãy số cách nhau bởi dấu phẩy: ")

# Cắt chuỗi thành một danh sách các chuỗi nhỏ (ví dụ: ['1', '2', '3'])
danh_sach_chuoi_so = chuoi_nhap.split(',')
print(f"Danh sách các số: {danh_sach_chuoi_so}")

tong_cac_so = 0
tong_binh_phuong = 0

# Duyệt qua từng phần tử, ép kiểu về số nguyên (int) và tính toán
for chuoi_so in danh_sach_chuoi_so:
    so = int(chuoi_so)
    tong_cac_so += so
    tong_binh_phuong += so ** 2

# Tính bình phương của tổng
binh_phuong_tong = tong_cac_so ** 2

# Tính chênh lệch
chenh_lech = binh_phuong_tong - tong_binh_phuong

print(f"Chênh lệch = {binh_phuong_tong} - {tong_binh_phuong} = {chenh_lech}")