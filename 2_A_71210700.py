#Soal 2
m = str(input("Masukan nama: "))

#kursi = nomor kursi
kursi = []
#nama = daftar nama
nama = []

while m != "STOP":
    a = "Masukan nomor kursi "+m+" : "
    b = input(a)
    if b not in kursi:
        kursi.append(b)
        nama.append(m)
    else:
        print("Mohon maaf kursi tersebut telah terisi!")
    m = str(input("Masukan nama: "))
print("List kursi yang telah terisi :")
for i in range (len(kursi)):
    print("Kursi nomor %s telah diisi oleh %s"%(kursi[i],nama[i]))
