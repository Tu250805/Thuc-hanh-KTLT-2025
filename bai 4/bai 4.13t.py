print("sinh vien : Dau Duc Tu")
print("msv 235752020710009")
ds = input('Nhập chuỗi: ').split()
try:
    position = ds.index('abc')
    print("Vị trí của chuỗi 'abc' là:", position)
except ValueError:
    print("'abc' không có trong danh sách.")
