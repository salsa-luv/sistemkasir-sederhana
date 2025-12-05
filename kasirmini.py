# database awal
produk = {
    "Sabun" : 5000,
    "Shampoo" : 12000,
    "Pasta Gigi" : 8000,
}

# membuat file dan memasukkan data awal
with open("database_barang.txt", "w") as file:
    for nama, harga in produk.items():
        file.write(f"{nama};{harga}\n")

# menyimpan barang baru ke dalam file
def simpan_ke_file(nama, harga):
    with open("database_barang.txt", "a") as file:
        file.write(f"{nama};{harga}\n")

# menampilkan produk
def tampilkan_produk():
    print("\n===== DATA BARANG =====")
    i = 1
    for nama, harga in produk.items():
        print(f"{i}. {nama} - Rp {harga}")
        i += 1
        print("=============================")