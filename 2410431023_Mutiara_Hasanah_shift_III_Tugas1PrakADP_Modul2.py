print("Pesanan Makanan Online")
print("Menu Makanan")
print ("Ayam = RP20000")
print("Sapi = RP35000")
print("Cumi-cumi = RP45000")
pesanan = str(input("Masukkan Menu Pilihan Anda: ")).lower()
if pesanan == 'ayam':
    harga = 20000
elif pesanan == 'sapi':
    harga = 35000
else :
    harga = 45000
jarak = float(input("Masukkan Jarak Rumah Anda ke Tempat Pesanan: "))
if jarak < 1:
    ongkir = 0
elif 1<=jarak<=3:
    ongkir = 7000
else:
    ongkir = 15000
BA = harga+ongkir
print(f"Biaya Pesanan Anda adalah RP{harga} dan anda dikenakan ongkir RP{ongkir}, jadi Total Biaya yang harus dibayarkan adalah = RP{BA}")