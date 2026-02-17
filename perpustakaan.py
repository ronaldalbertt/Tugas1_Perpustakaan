class Perpustakaan: # Class Perpustakaan bertugas mengelola kumpulan buku
    def __init__(self, nama_perpus): #Ini adalah contoh dari State/Atribut
        self.nama_perpus = nama_perpus
        self.daftar_buku = [] # List kosong untuk menyimpan banyak objek Buku

    def sambutan(self): #method/behavior untuk menampilkan sambutan perpustakaan
        print(f"Selamat datang di {self.nama_perpus}!")
        print("=" * 20)

    def tambah_buku(self, buku): #method/behavior untuk menambahkan buku ke daftar_buku
        self.daftar_buku.append(buku)

    def tampilkan_daftar_buku(self): #method/behavior untuk menampilkan daftar buku
        print("Daftar Buku:")
        for buku in self.daftar_buku:
            print("- " + buku.judul)  # megakses atribut judul dari setiap objek buku
