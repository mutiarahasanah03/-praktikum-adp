def menu():   
    print("MENU")
    print("1. Tabel perkalian modulo n")
    print("2. Mencari nilai Σ x")
    print("3. Mencari nilai n!")
    print("4. Total dan rata-rata suatu data")
    print("5. Keluar")
    print()

def tabel_perkalian_modulo():
    while True:
        n = int(input("Masukkan nilai n (0 < n ≤ 10): "))
        if 0 < n <= 10:
            break
        else:
            print("Input tidak valid. (n harus antara 1 sampai 10).")
    
    print(f"Tabel Perkalian Modulo {n}:")
    print(" x"+" |", end="")
    for i in range(n):
        print(f"{i:3}", end="")
    print()
    print("-" * (n * 3 + 4))
    for i in range(n):
        print(f"{i:2} |", end="")
        for j in range(n):
            print(f"{(i*j)%n:3}", end="")
        print()

def sigma_x():
    while True:
        batas_bawah = int(input("Batas bawah: "))
        batas_atas = int(input("Batas atas: "))
        if batas_atas >= batas_bawah:
            break
        else:
            print("Batas atas harus lebih besar atau sama dengan batas bawah.")

    total = 0
    for i in range(batas_bawah, batas_atas+1):
        total += i
    print("Σ x =", total)

def faktorial():
    while True:
        n = int(input("Masukkan nilai n: "))
        if n >= 0:
            break
        else:
            print("n harus ≥ 0.")

    hasil = 1
    for i in range(2, n+1):
        hasil *= i
    print(f"{n}! =", hasil)

def total_rata2_data():
    while True:
        n = int(input("Masukkan banyak data (n): "))
        if n > 0:
            break
        else:
            print("Jumlah data harus lebih dari 0.")
        
    data = []
    for i in range(n):
        while True:
            nilai = float(input(f"Data ke-{i+1}: "))
            data.append(nilai)
            break

    total = 0
    for nilai in data:
        total += nilai
    rata_rata = total / n
    print("Total =", total)
    print("Rata-rata =", rata_rata)

def pilihan():
    while True:
        menu()
        pilihan_menu = input("Pilih menu (1-5): ")
        if pilihan_menu == '1':
            tabel_perkalian_modulo()
        elif pilihan_menu == '2':
            sigma_x()
        elif pilihan_menu == '3':
            faktorial()
        elif pilihan_menu == '4':
            total_rata2_data()
        elif pilihan_menu == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-5.")
        print()

pilihan()