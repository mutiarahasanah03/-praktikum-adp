while True:
    angka1 = float(input('Masukkan Angka Pertama = '))    
    angka2 = float(input('Masukkan Angka Kedua = '))
    print('Pilihan Operasi:')
    print ('1. Penjumlahan')
    print ('2. Pengurangan')
    print ('3. Perkalian')
    print ('4. Pembagian')
    print ('5. Keluar')
    pilihan = str(input("Operasi yang dipilih [Masukkan Angka Saja] = "))
    if pilihan == '1':
        penjumlahan = angka1 + angka2
        print(F'Hasil : {penjumlahan}')
    elif pilihan == '2':
        pengurangan = angka1 - angka2
        print(F'Hasil : {pengurangan}')
    elif pilihan == '3':
        perkalian = angka1*angka2
        print(F'Hasil : {perkalian}')
    elif pilihan == '4':
        if angka2 == 0:
            print('eror [operasi ini tidak terdefinisi]')
        else:
            pembagian = angka1/angka2
            print(F'Hasil : {pembagian}')
    else:
        print('Terimakasih telah menggunakan Kalkulator Sederhana ini')
        break
