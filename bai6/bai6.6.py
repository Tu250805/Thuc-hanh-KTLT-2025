print('sinh viên Đậu Đức Tú')
print('Msv 235752020710009')

class IOString:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.s.upper())

# Tạo đối tượng của lớp IOString
str1 = IOString()
str1.get_String()
str1.print_String()
