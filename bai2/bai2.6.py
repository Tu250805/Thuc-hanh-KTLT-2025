print("sinh vien : Dau Duc Tu")
print("msv 235752020710009")
j = []
for i in range(500, 1200):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))
