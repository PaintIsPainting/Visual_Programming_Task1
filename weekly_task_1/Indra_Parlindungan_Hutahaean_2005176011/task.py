class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

# Input Data Diri Kalian
mahasiswa = Mahasiswa(
    nama="",
    kelas="",
    prodi="",
    fakultas="",
    tempat_tinggal="",
    asal=""
)

# Menampilkan informasi mahasiswa
print(f"Nama: {mahasiswa.nama}")
print(f"Kelas: {mahasiswa.kelas}")
print(f"Prodi: {mahasiswa.prodi}")
print(f"Fakultas: {mahasiswa.fakultas}")
print(f"Tempat Tinggal: {mahasiswa.tempat_tinggal}")
print(f"Asal: {mahasiswa.asal}")

