class Anggota:
    def __init__(self, nama, nim, telepon, kelas): #Ini adalah contoh dari State/Atribut
        self.nama = nama
        self.nim = nim
        self.telepon = telepon
        self.kelas = kelas
    
    def perkenalan_diri(self): #method untuk menampilkan informasi anggota
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Telepon: {self.telepon}")
        print(f"Kelas: {self.kelas}")
        print("-" * 20)