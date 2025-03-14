print("sinh vien : Dau Duc Tu")
print("msv 235752020710009")
import math

x1 = int(input("x1="))
u1 = int(input("y1="))

x2 = int(input("x2="))
y2 = int(input("y2="))

A = (x2 - x1) * (x2 - x1)
B = (y2 - y1) * (y2 - y1)

res = math.sqrt(A + B)
print("khoang cach giua hai diem là:", res);
