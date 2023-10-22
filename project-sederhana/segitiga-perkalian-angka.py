a = input("input angka yang pengen dijadiin segitiga : ")
a = int(a)

print("\n")

for i in range(1, a+1):
    for j in range(i, i*i+1, i):
        print(j, end=" ")
    print()

print("\n")

input("tekan enter untuk keluar")
