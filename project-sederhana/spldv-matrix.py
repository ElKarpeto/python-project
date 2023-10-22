import numpy as np

print("SPLDV dengan Metode Matrix\n")
print("==================================================\n")

print('persamaan 1')
a = float(input('masukan nilai baris 1 kolom 1 : '))
b = float(input('masukan nilai baris 1 kolom 2 : '))

e = float(input('masukan nilai persamaan 1 : '))

print('persamaan 2')
c = float(input('masukan nilai baris 2 kolom 1 : '))
d = float(input('masukan nilai baris 2 kolom 2 : '))

f = float(input('masukan nilai persamaan 2 : '))

print("\n==================================================\n")

matrix_1 = np.array([[a, b], [c, d]]) # membuat matrix 2 x 2
matrix_2 = np.array([[e], [f]]) # membuat matrix 2 x 1

inv_1 = np.linalg.inv(matrix_1) # invers matrix 1

ans_matrix = np.matmul(inv_1, matrix_2) # mengkalikan invers matrix 1 dengan matrix 2

x = round(ans_matrix[0, 0])
y = round(ans_matrix[1, 0])

print(f'nilai x adalah {x}\n')
print(f'nilai y adalah {y}\n')

input("tekan 'enter' untuk keluar")
