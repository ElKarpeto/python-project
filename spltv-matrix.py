import numpy as np

print("menyelesaikan persamaan linear 3 variabel sederhana menggunakan metode matrix")

# input nilai-nilai SPLTV menjadi matrix augmented
print("\n========================================")

print("\nmasukan persamaan pertama")
a = float(input("nilai matriks baris 1 kolom 1 : "))
b = float(input("nilai matriks baris 1 kolom 2 : "))
c = float(input("nilai matriks baris 1 kolom 3 : "))

j = float(input("masukan nilai dari persamaan 1 : "))

print("\n========================================")

print("\nmasukan persamaan kedua")
d = float(input("nilai matriks baris 2 kolom 1 : "))
e = float(input("nilai matriks baris 2 kolom 2 : "))
f = float(input("nilai matriks baris 2 kolom 3 : "))

k = float(input("masukan nilai dari persamaan 2 : "))


print("\n========================================")

print("\nmasukan persamaan ketiga")
g = float(input("nilai matriks baris 3 kolom 1 : "))
h = float(input("nilai matriks baris 3 kolom 2 : "))
i = float(input("nilai matriks baris 3 kolom 3 : "))

l = float(input("masukan nilai dari persamaan 3 : "))

# kita create matrix base nya
matrix1 = np.array([[a, b, c], [d, e, f], [g, h, i]])

det1 = float(np.linalg.det(matrix1))


matrixX = np.array([[j, b, c], [k, e, f], [l, h, i]])
detX = float(np.linalg.det(matrixX))


matrixY = np.array([[a, j, c], [d, k, f], [g, l, i]])
detY = float(np.linalg.det(matrixY))

matrixZ = np.array([[a, b, j], [d, e, k], [g, h, l]])
detZ = float(np.linalg.det(matrixZ))

nilai_x = round(detX / det1)
nilai_y = round(detY / det1)
nilai_z = round(detZ / det1)

print("\n========================================")

print(f"\nnilai x = {nilai_x}")

print(f"\nnilai y = {nilai_y}")

print(f"\nnilai z = {nilai_z}")

print("\n========================================")

input("tekan 'enter' untuk keluar")
