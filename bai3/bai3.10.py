print("sinh vien : Dau Duc Tu")
print("msv 235752020710009")
import math

def Tinh(R):
    if R <= 0:
        return "Giá trị R không hợp lệ. R phải > 0."
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2

    return f"Chu vi hình tròn là: {chu_vi}\nDiện tích hình tròn là: {dien_tich}"

R = float(input("R: "))
print(Tinh(R))
