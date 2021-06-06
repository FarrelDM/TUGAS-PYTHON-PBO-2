class siswa:
    #class variabel
    jumlah_siswa = 0
    #konstruktor
    def __init__(self, nama, kelas, alamat, nilai):
        self.nama = nama
        self.kelas = kelas
        self.alamat = alamat
        self.nilai = nilai
        siswa.jumlah_siswa =+ 1
    #metode
    def viewsiswa(self):
        print("----------")
        print("data siswa")
        print("nama : ", self.nama)
        print("kelas : ",self.kelas)
        print("alamat : ", self.alamat)
        print("----------")

    def viewnilai(self):
        print("data nilai")
        print("nama : ", self.nama)
        for nilai in self.nilai:
            print("nilai : ", nilai)
        print("----------")
    
    def viewketerangan(self):
        print("keterangan")
        print("nama : ", self.nama)
        print("kelas : ", self.kelas)
        rata = sum(self.nilai)/len(self.nilai)
        print("rata-rata : ", rata)
        if rata >= 75:
            keterangan = "lulus"
        else:
            keterangan = "tidak lulus"
        print("keterangan : ", keterangan)
        print("----------")

#instansasi objek
siswa1 = siswa("Finda", "XII MIPA 1", "Magelang", [89,67,85,47])
siswa2 = siswa("Umi", "XII MIPA 2", "Bantul", [89,97,85,87])
#pemanggilan objek siswa 1
siswa1.viewsiswa()
siswa1.viewnilai()
siswa1.viewketerangan()
print("jumlah siswa : ", siswa.jumlah_siswa)
#pemanggilan objek siswa 2
siswa2.viewsiswa()
siswa2.viewnilai()
siswa2.viewketerangan()
print("jumlah siswa : ", siswa.jumlah_siswa)
