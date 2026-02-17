# Mengimpor class dari file lain. Contoh: from buku import Buku artinya:mengambil class Buku dari file buku.py
from buku import Buku
from anggota import Anggota
from perpustakaan import Perpustakaan



# Membuat objek Buku
buku1 = Buku("Pemrograman Python", "John Doe", 2022)
buku2 = Buku("Belajar Hukum Sejarah", "JOKOWI", 2023)
buku3 = Buku("Pemrograman C++", "John Doe", 2021)

# Membuat objek Anggota
anggota1 = Anggota("M. Ronald Albert", "12550110969", "081234567890", "Tif 2B")
anggota2 = Anggota("Baskara Hindia", "12550110224", "081234567890", "MTK 7C")
anggota3 = Anggota("Maul Ibrahim", "12550110423", "081234567890", "SI 3A")

# Membuat objek Perpustakaan
perpus_teknik = Perpustakaan("Perpustakaan Teknik")
perpus_hukum = Perpustakaan("Perpustakaan Hukum")
perpus_informasi = Perpustakaan("Perpustakaan Sistem Informasi")


# Menampilkan sambutan perpustakaan
perpus_teknik.sambutan()

# memanggil method perkenalan diri dari anggota
anggota1.perkenalan_diri()

# menampilkan informasi buku
buku1.tampilkan_informasi()

# Menambahkan buku ke daftar buku perpustakaan
perpus_teknik.tambah_buku(buku1)
perpus_hukum.tambah_buku(buku2)
perpus_informasi.tambah_buku(buku3)

# Menampilkan daftar buku perpustakaan
perpus_teknik.tampilkan_daftar_buku()
print("-" * 20)

# buku1.judul artinya kita ambil teks "Pemrograman Python"
perpus_teknik.pinjam_buku(buku1.judul, anggota1) #simulasi pinjam
# Cek status akan berubah menjadi dipinajam
perpus_teknik.tampilkan_daftar_buku()
print("-" * 20)


perpus_teknik.kembalikan_buku(buku1.judul, anggota1) #simulasi kembalikan
# Cek status akhir akan menjadi tersedia
perpus_teknik.tampilkan_daftar_buku()
print("-" * 20)