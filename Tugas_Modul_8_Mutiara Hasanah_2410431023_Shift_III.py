data_praktikan = ['2410451025, khalisa,  90, 90, 90',
                  '2410451010, anindya,  75, 90, 95',
                  '2410451009, melinda, 80, 90, 98',
                  '2410452030, berlian, 90, 70, 80',
                  '2410452002, Hanifah, 75, 70, 95',
                  '2410452031, dayyana, 76, 90, 98',
                  '2410452005, zahrani, 98, 90, 90',
                  '2410453001, aurelia, 85, 95, 90',
                  '2410453014, delisya, 82, 90, 98',
                  '2410453013, Rayyana, 82, 92, 94',
                ]

with open('data_praktikan.txt', 'w') as file:
    for baris in data_praktikan:
        file.write(baris + '\n')

data_dictionary = {}
with open("data_praktikan.txt", "r") as file:
    for baris in file:
        nim, nama, pretest, postest, tugas = baris.split(",")
        data_dictionary[nim] = {
            "nama": nama,
            "pretest": int(pretest),
            "postest": int(postest),
            "tugas": int(tugas)
        }

with open('data_nilai_akhir.txt', 'w') as file:
    file.write('   NIM        Nama      Pretest    Postest      Tugas       Total Nilai   \n')
    for nim, data in data_dictionary.items():
        nilai_akhir = (0.35 * data["pretest"] + 0.35 * data["postest"] +0.30 * data["tugas"])
        data['nilai_akhir'] = nilai_akhir
        file.write(f"{nim:<11} {data['nama']:13} {data['pretest']:<10} {data['postest']:<12} {data['tugas']:<12} {nilai_akhir:<12.2f}\n")
    
semua_nilai_akhir = [data['nilai_akhir'] for data in data_dictionary.values()]
rata_rata = sum(semua_nilai_akhir) / len(semua_nilai_akhir)
nilai_tertinggi = max(semua_nilai_akhir)
nilai_terendah = min(semua_nilai_akhir)
nama_tertinggi = [data['nama'] for data in data_dictionary.values() if data['nilai_akhir'] == nilai_tertinggi]
nama_terendah = [data['nama'] for data in data_dictionary.values() if data['nilai_akhir'] == nilai_terendah]
praktikan_dibawah_rata2 = [data['nama'] for data in data_dictionary.values() if data['nilai_akhir'] < rata_rata]

print(f"Rata-rata nilai akhir: {rata_rata:}")
print(f"Nilai tertinggi: {nilai_tertinggi} oleh {''.join(nama_tertinggi)}")
print(f"Nilai terendah: {nilai_terendah} oleh {''.join(nama_terendah)}")
print(f"Banyak praktikan yang nilai di bawah rata-rata: {len(praktikan_dibawah_rata2)} orang")
print(f"Nama-nama praktikan yang nilainya di bawah rata-rata: {', '.join(praktikan_dibawah_rata2)}")