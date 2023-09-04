import numpy as np
#untuk menjalankan program ini, lo harus install dulu library Numpy

print("menyelesaikan persamaan linear 3 variabel sederhana menggunakan metode matrix")

print("\n========================================")

print("\nmasukan persamaan pertama")
a = input("nilai matriks baris 1 kolom 1 : ")
a = float(a)
b = input("nilai matriks baris 1 kolom 2 : ")
b = float(b)
c = input("nilai matriks baris 1 kolom 3 : ")
c = float(c)

j = input("masukan nilai dari persamaan 1 : ")
j = float(j)

print("\n========================================")

print("\nmasukan persamaan kedua")
d = input("nilai matriks baris 2 kolom 1 : ")
d = float(d)
e = input("nilai matriks baris 2 kolom 2 : ")
e = float(e)
f = input("nilai matriks baris 2 kolom 3 : ")
f = float(f)

k = input("masukan nilai dari persamaan 2 : ")
k = float(k)

print("\n========================================")

print("\nmasukan persamaan ketiga")
g = input("nilai matriks baris 3 kolom 1 : ")
g = float(g)
h = input("nilai matriks baris 3 kolom 2 : ")
h = float(h)
i = input("nilai matriks baris 3 kolom 3 : ")
i = float(i)

l = input("masukan nilai dari persamaan 3 : ")
l = float(l)

matrix1 = np.array([[a, b, c], [d, e, f], [g, h, i]])
det1 = np.linalg.det(matrix1)
det1 = float(det1)

matrixX = np.array([[j, b, c], [k, e, f], [l, h, i]])
detX = np.linalg.det(matrixX)
detX = float(detX)

matrixY = np.array([[a, j, c], [d, k, f], [g, l, i]])
detY = np.linalg.det(matrixY)
detY = float(detY)

matrixZ = np.array([[a, b, j], [d, e, k], [g, h, l]])
detZ = np.linalg.det(matrixZ)
detZ = float(detZ)

nilai_x = detX / det1
nilai_x = round(nilai_x)
nilai_y = detY / det1
nilai_y = round(nilai_y)
nilai_z = detZ / det1
nilai_z = round(nilai_z)

print("\n========================================")

print(f"\nnilai x = {nilai_x}")

print(f"\nnilai y = {nilai_y}")


print(f"\nnilai z = {nilai_z}")

input("tekan 'enter' untuk keluar")
