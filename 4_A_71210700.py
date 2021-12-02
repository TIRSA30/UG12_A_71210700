#soal 4

angka = int(input("Input: "))
print("Output :")
n = 2

for i in range(1,angka+1):
    for j in range(1,(2*angka)):
        if i+j==angka+1 or j-i==angka-1:
            print("*",end="")
        elif i==angka and j!=n:
            print("*",end="")
            n=n+2
        else:
            print(end=" ")

    print()
