class siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #getter
    def getnis(self):
        return self.__nis

    #setter
    def setnis(self, newnis):
        self.__nis = newnis

farrel = siswa(15970, "Alfarrel Daffa", "XI MIA 5")

print(farrel.getnis())
farrel.setnis(16240)
print(farrel.getnis())