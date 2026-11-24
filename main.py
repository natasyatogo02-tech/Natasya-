# =========================================================
# APLIKASI PENJUALAN TOKO TOGOLA INDAH BERBASIS OOP
# =========================================================
print("Nama : Natasya Togo")
print("NIM  : 5920125042")

from abc import ABC, abstractmethod

# =========================================================
# ABSTRACT CLASS
# =========================================================%6

class DataToko(ABC):

    @abstractmethod
    def tampilkan_data(self):
        pass


# =========================================================
# CLASS PRODUK
# =========================================================

class Produk(DataToko):

    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tampilkan_data(self):
        print(f"{self.kode:<8} {self.nama:<15} Rp.{self.harga:<10} Stok:{self.stok}")


# =========================================================
# CLASS MAKANAN (KETURUNAN / INHERITANCE)
# =========================================================

class Makanan(Produk):

    def __init__(self, kode, nama, harga, stok, expired):
        super().__init__(kode, nama, harga, stok)
        self.expired = expired

    def tampilkan_data(self):
        print(f"{self.kode:<8} {self.nama:<15} Rp.{self.harga:<10} "
              f"Stok:{self.stok} Exp:{self.expired}")


# =========================================================
# CLASS TRANSAKSI
# =========================================================

class Transaksi:

    def __init__(self):
        self.total = 0

    def beli_barang(self, produk, jumlah):

        if jumlah > produk.stok:
            print("❌ Stok tidak cukup!")
            return

        subtotal = produk.harga * jumlah
        produk.stok -= jumlah
        self.total += subtotal

        print("\n✅ Pembelian Berhasil")
        print(f"Barang   : {produk.nama}")
        print(f"Jumlah   : {jumlah}")
        print(f"Subtotal : Rp.{subtotal}")


# =========================================================
# CLASS TOKO
# =========================================================

class Toko:

    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.daftar_produk = []

    # ================= TAMBAH DATA =================

    def tambah_data(self):

        print("\n=== TAMBAH DATA PRODUK ===")

        jenis = input("Jenis Produk (1.Makanan / 2.Biasa) :1 ")

        kode = input("Kode Produk :p02 ")
        nama = input("Nama Produk :Indomi ")
        harga = input("Harga Produk :90 ")
        stok = input("Stok Produk :8 dos ")

        if jenis == "1":
            expired = input("Tanggal Expired :12-12-2026 ")
            produk = Makanan(kode, nama, harga, stok, expired)

        else:
            produk = Produk(kode, nama, harga, stok)

        self.daftar_produk.append(produk)

        print("✅ Data berhasil ditambahkan!")

    # ================= TAMPILKAN DATA =================

    def tampilkan_data(self):

        print("\n===================================================")
        print(f"         DATA PRODUK {self.nama_toko}")
        print("===================================================")

        if len(self.daftar_produk) == 0:
            print("Data produk masih kosong!")
            return

        for produk in self.daftar_produk:
            produk.tampilkan_data()

    # ================= HAPUS DATA =================

    def hapus_data(self):

        kode = input("\nMasukkan kode produk yang ingin dihapus : p02")

        for produk in self.daftar_produk:
            if produk.kode == kode:
                self.daftar_produk.remove(produk)
                print("✅ Data berhasil dihapus!")

    # ================= EDIT DATA =================

    def edit_data(self):

        kode = input("\nMasukkan kode produk yang ingin diedit :p03 ")

        for produk in self.daftar_produk:

            if produk.kode == kode:

                print("Masukkan data baru")

                produk.nama = input("Nama Baru :Gula ")
                produk.harga = input("Harga Baru :400 ")
                produk.stok = input("Stok Baru :20 sak ")

                print("✅ Data berhasil diubah!") 

    # ================= CARI DATA =================

    def cari_data(self):

        keyword = input("\nMasukkan nama produk :Indomi ")

        ditemukan = False

        for produk in self.daftar_produk:

            if keyword.lower() in produk.nama.lower():

                print("\n=== DATA DITEMUKAN ===")
                produk.tampilkan_data()

                ditemukan = True

        if not ditemukan:
            print("❌ Produk tidak ditemukan!")

    # ================= PEMBELIAN =================

    def transaksi_penjualan(self):

        kode = input("\nMasukkan kode produk : p03")
        jumlah =input("Jumlah beli :2 sak ")

        for produk in self.daftar_produk:

            if produk.kode == kode:

                transaksi = Transaksi()
                transaksi.beli_barang(produk, jumlah)

                print(f"Total Bayar : Rp.{transaksi.total}")
                return

        print("❌ Produk tidak ditemukan!")


# =========================================================
# PROGRAM UTAMA
# =========================================================

toko = Toko("TOKO TOGOLA INDAH")

while True:

    print("\n")
    print("===================================================")
    print("         APLIKASI PENJUALAN TOKO")
    print("              TOGOLA INDAH")
    print("===================================================")

    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Transaksi Penjualan")
    print("7. Keluar")

    pilih = input("Pilih menu : ")

    if pilih == "1":
        toko.tambah_data()

    elif pilih == "2":
        toko.tampilkan_data()

    elif pilih == "3":
        toko.edit_data()

    elif pilih == "4":
        toko.hapus_data()

    elif pilih == "5":
        toko.cari_data()

    elif pilih == "6":
        toko.transaksi_penjualan()

    elif pilih == "7":
        print("\nTerima kasih telah menggunakan program 😊")
        break

    else:
        print("❌ Menu tidak tersedia!")