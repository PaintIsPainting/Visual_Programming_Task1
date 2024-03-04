class Mahasiswa():
	def __init__ (self, masukkan_nama,masukkan_kelas,masukkan_prodi,masukkan_fakultas,masukkan_tempat_tinggal,masukkan_asal):
		self.nama = masukkan_nama
		self.kelas = masukkan_kelas
		self.prodi = masukkan_prodi
		self.fakultas = masukkan_fakultas
		self.tempat_tinggal = masukkan_tempat_tinggal
		self.asal = masukkan_asal

objek = Mahasiswa("Ahmed Jhordy", "A", "Pendidikan Komputer", "FKIP", "Perjuangan 3", "Bontang")

print ("Data Diri")
print ("Nama : ", objek.nama)
print ("Kelaz : ", objek.kelas)
print ("Prodi :", objek.prodi)
print ("Fakultas :", objek.fakultas)
print ("Tempat Tinggal :", objek.tempat_tinggal)
print ("Asal :", objek.asal)

