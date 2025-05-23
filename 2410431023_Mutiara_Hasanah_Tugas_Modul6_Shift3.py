titikxy = []
for i in range (3):
    x = int(input(f'Masukkan Nilai x{i+1}: '))
    y = int(input(f'Masukkan Nilai y{i+1}: '))
    titikxy.append([x,y])
print(titikxy)

sisi_a = ((titikxy[0][0] - titikxy[1][0])**2 + (titikxy[0][1] - titikxy[1][1])**2) ** 0.5
sisi_b = ((titikxy[1][0] - titikxy[2][0])**2 + (titikxy[1][1] - titikxy[2][1])**2) ** 0.5
sisi_c = ((titikxy[0][0] - titikxy[2][0])**2 + (titikxy[0][1] - titikxy[2][1])**2) ** 0.5

if sisi_a == sisi_b or sisi_b == sisi_c or sisi_a == sisi_c:
    print("Ketiga titik membentuk segitiga sama kaki.")
else:
    print("Ketiga titik tidak membentuk segitiga sama kaki.")