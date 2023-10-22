import matplotlib.pyplot as plt
import numpy as np

# tulisan pada grafik
tulisan = input('isi tulisan pada grafik : ')

plt.title("Grafik Love")

plt.xlabel("Sumbu x")
plt.ylabel("Sumbu y")

x = np.arange(-2.236, 2.2361, 0.0001)

a = np.sin(10 * np.pi * x)
y = np.power((np.power(x, 2)), 1/3) + 0.9 * a * \
    ((5 - (np.power(x, 2))) ** 0.5)

plt.text(0, -3, tulisan, fontsize=10, ha='center')

plt.xlim(-8, 8)
plt.ylim(-8, 8)

plt.plot(x, y, color="red")

plt.show()
