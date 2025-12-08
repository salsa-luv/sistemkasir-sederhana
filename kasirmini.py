# database awal
produk = {
    "Sabun" : 5000,
    "Shampoo" : 12000,
    "Pasta Gigi" : 8000,
}
# buat dan update file
def update_file():
    with open("database_barang.txt", "w") as file:
        for nama, harga in produk.items():
            file.write(f"{nama} = {harga}\n")

# menampilkan produk
def tampilkan_produk():
    print("\n===== DATA BARANG =====")
    i = 1
    for nama, harga in produk.items():
        print(f"{i}. {nama} - Rp {harga}")
        i += 1
    print("=====================")
    
# filter menampilkan harga dari yang termurah sampai yang termahal
def tampilkan_barang_urutan_harga():
    print("\n===== BARANG TERMURAH - TERMAHAL =====")

    daftar_harga = list(produk.values())
    daftar_harga.sort()

    for harga in daftar_harga:
        for nama in produk:
            if produk[nama] == harga:
                print(f"{nama} - Rp {harga}")
    print("===============================")

# edit barang database
def edit_barang():
    while True:
        tampilkan_produk()
        print("\n --- Menu Edit Barang ---")
        print("1. Tambah Barang")
        print("2. Edit Harga Barang")
        print("3. Hapus Barang")
        print("4. Kembali ke Menu Utama")

        try:
            pilih = int(input("Pilih Menu: "))
        except ValueError:
            print("input harus berupa angka! Silahkan Coba Lagi.")
            continue

        if pilih == 1:
            nama = input("Masukkan nama barang baru: ").title()
            harga = int(input("Masukkan harga barang baru: "))
            produk[nama] = harga
            update_file()
            print("Barang berhasil ditambahkan!")

        elif pilih == 2:
            nama  = input("Masukkan nama barang yang akan diubah: ").title()
            if nama in produk:
                harga_baru = int(input("Masukkan harga baru: "))
                produk[nama] = harga_baru
                update_file()
                print("Harga barang berhasil diubah!")
            else:
                print("Barang tidak ditemukan!")
        
        elif pilih == 3:
            nama = input("Masukkan nama barang yang akan dihapus: ").title()
            if nama in produk:
                del produk[nama]
                update_file()
                print("Barang berhasil dihapus!")
            else:
                print("Barang tidak ditemukan!")

        elif pilih == 4:
            break
        else:
            print("Pilihan tidak valid! Silahkan coba lagi.")
            
# melakukan transaksi
def transaksi():
    keranjang = []
    total = 0

    while True:
        tampilkan_produk()
        print("\n--- Menu Transaksi ---")
        print("1. pilih barang dari daftar")
        print("2. tambahkan barang baru")
        print("3. selesai dan cetak struk")

        try:
            pilih = int(input("pilih menu: "))
        except ValueError:
            print("input harus berupa angka! coba lagi.")
            continue

        if pilih == 1:
            nama = input("masukkan nama barang: ").title()
            if nama in produk:
                harga = produk[nama]
                keranjang.append((nama, harga))
                total += harga 
                print("barang ditambahkan ke keranjang!")
            else:
                print("baang tidak di temukan")

        elif pilih == 2:
            nama = input("masukkan nama barang baru: ").title()
            harga = int(input("masukkan harga: "))
            keranjang.append((nama, harga))
            total += harga
            print("Barang baru di tambahkan keranjang!")

        elif  pilih == 3:
            break
        else:
            print("pilihan tidak valid!")
            
    #memberikan diskon
    diskon = int(input("masukkan diskon (%): "))
    potongan = total * (diskon / 100)
    harga_akhir = total - potongan

    print("\n========================= STRUK BELANJA =========================")
    for nama, harga in keranjang:
        print(f"{nama} - Rp {harga}")
    print("-----------------------------------------------------------------------")
    print(f"Total Harga Awal    : Rp {total}")
    print(f"Diskon              : {diskon}%")
    print(f"Total Akhir         : Rp{int(harga_akhir)}")
    print("=======================================================================")
    print("Terima kasih sudah berbelanja:)")
    print("=======================================================================")

# menu utama
while True:
    print("\n==== MENU UTAMA ====")
    print("1. Data Barang")
    print("2. Edit Barang")
    print("3. Transaksi")
    print("4. Urutkan Harga (Termurah - Termahal)")
    print("5. Keluar Program")

    try:
        pilihan = int(input("Pilih menu: "))
    except ValueError:
        print("Input harus berupa angka!")
        continue

    if pilihan == 1:
        tampilkan_produk()
    elif pilihan == 2:
        edit_barang()
    elif pilihan == 3:
        transaksi()
    elif pilihan == 4:
        tampilkan_barang_urutan_harga()
    elif pilihan == 5:
        print("Program selesai. Terimakasih!")
        break
    else:
        print("Pilihan tidak valid! Masukkan angka 1-5!")


        
