print("sinh vien : Dau Duc Tu")
print("msv 235752020710009")
a, b = 1, 2
total = 0
print(a, end=" ")
while (b <= 4000000-1):
    if a % 2 == 0:
        total += a
    a, b =b, a+b
    print(a, end=" ")
print("\n tong cac so chan trong day fibonacci la: ", total)
