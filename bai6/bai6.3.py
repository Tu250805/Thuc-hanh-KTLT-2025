print('sinh viên Đậu Đức Tú')
print('Msv 235752020710009')

class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng từ class Nam và Nu
aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())
