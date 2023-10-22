# untuk input nilai dari segitiga
a = input("input angka yang pengen dijadiin segitiga : ")
a = int(a)

print("\n")

# untuk kondisi
if a <= 10:
    for i in range(1, a+1):
        for j in range(i, i*i+1, i):
            print(j, end=" ")
        print()
else:
    print("kegedean nilai yang kamu input")

print("\n")

input("tekan enter untuk keluar")
