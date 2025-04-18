print('sinh viên Đậu Đức Tú')
print('Msv 235752020710009')

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

# Tạo một đối tượng Circle với bán kính 2
aCircle = Circle(2)
print(aCircle.area())
