#soal 1
#test case 1,2,3

angka = input("Masukan deret angka : ")
m = 0
n = (angka.split(","))

print("Total :",end=" ")

for i in n:
    i=int(i)
    if i%2==1:
        m = m-i
        print(i*-1, end=" ")
    else:
        m = m+i
        print("+",i,end=" ")
print()
print("Hasil perhitungan diatas ialah", m)
