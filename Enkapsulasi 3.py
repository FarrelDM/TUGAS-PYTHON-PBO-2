class siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #decorator
    @property
    def nis(self):
        pass
    #getter
    @nis.getter
    def nis(self):
        return self.__nis
    #setter
    @nis.setter
    def nis(self, newnis):
        self.__nis = newnis

farrel = siswa(15970, "Alfarrel Daffa", "XI MIA 5")

print(farrel.nis)
farrel.nis = 16240
print(farrel.nis)