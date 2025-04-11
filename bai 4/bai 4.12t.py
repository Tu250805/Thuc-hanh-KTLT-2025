print("sinh vien : Dau Duc Tu")
print("msv 235752020710009")
ds = input('Nhập chuỗi: ').split()
try:
    ds.remove('123')
except ValueError:
    print("'123' không có trong danh sách.")
for ch in ds:
    print(ch)
