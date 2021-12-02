#soal 3

m = input("Input : ")
n = len(m)
print("Output :",end="")
for i in range(n):
    print(m[:i])
for j in range(n,0,-1):
    print(m[:j])
