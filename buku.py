class Buku: #class Buku adalah cetakan untuk membuat objek buku
    def __init__(self, judul, pengarang, tahun_terbit): #Ini adalah contoh dari State/Atribut
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.status = "tersedia" #sebagai default status buku
        # STATE (Data milik setiap objek Buku)
        # self.judul menyimpan judul buku
        # self.pengarang menyimpan nama pengarang
        # self.tahun_terbit menyimpan tahun terbit
        # self.status menyimpan status buku
    
    def tampilkan_informasi(self): #method untuk menampilkan informasi buku
        print(f"Judul: {self.judul}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Status: {self.status}")
        print("-" * 20)