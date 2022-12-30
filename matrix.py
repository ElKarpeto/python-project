import numpy as np
#untuk menjalankan program ini, download di PC anda Python dan library Numpy

print("menyelesaikan persamaan linear 3 variabel menggunakan metode matrix")

print("\n========================================")

print("\nmasukan persamaan pertama")
a = input("nilai matriks baris 1 kolom 1 : ")
a = int(a)
b = input("nilai matriks baris 1 kolom 2 : ")
b = int(b)
c = input("nilai matriks baris 1 kolom 3 : ")
c = int(c)

j = input("masukan nilai dari persamaan 1 : ")
j = int(j)

print("\n========================================")

print("\nmasukan persamaan kedua")
d = input("nilai matriks baris 2 kolom 1 : ")
d = int(d)
e = input("nilai matriks baris 2 kolom 2 : ")
e = int(e)
f = input("nilai matriks baris 2 kolom 3 : ")
f = int(f)

k = input("masukan nilai dari persamaan 2 : ")
k = int(k)

print("\n========================================")

print("\nmasukan persamaan ketiga")
g = input("nilai matriks baris 3 kolom 1 : ")
g = int(g)
h = input("nilai matriks baris 3 kolom 2 : ")
h = int(h)
i = input("nilai matriks baris 3 kolom 3 : ")
i = int(i)

l = input("masukan nilai dari persamaan 3 : ")
l = int(l)

matrix1 = np.array([[a, b, c], [d, e, f], [g, h, i]])
det1 = np.linalg.det(matrix1)
det1 = int(det1)

matrixX = np.array([[j, b, c], [k, e, f], [l, h, i]])
detX = np.linalg.det(matrixX)
detX = int(detX)

matrixY = np.array([[a, j, c], [d, k, f], [g, l, i]])
detY = np.linalg.det(matrixY)
detY = int(detY)

matrixZ = np.array([[a, b, j], [d, e, k], [g, h, l]])
detZ = np.linalg.det(matrixZ)
detZ = int(detZ)

nilai_x = detX / det1
nilai_x = int(nilai_x)
nilai_y = detY / det1
nilai_y = int(nilai_y)
nilai_z = detZ / det1
nilai_z = int(nilai_z)

print("\n========================================")

print("\nnilai x = ")
print(nilai_x)

print("\nnilai y = ")
print(nilai_y)

print("\nnilai z = ")
print(nilai_z)

input("tekan 'enter' untuk keluar")
