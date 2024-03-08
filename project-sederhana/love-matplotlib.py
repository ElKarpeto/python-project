import matplotlib.pyplot as plt
import numpy as np

plt.title("Grafik Love")

plt.xlabel("x")
plt.ylabel("y(x)")

x = np.arange(-4.4721, 4.4721, 0.0001)

a = np.sin(10 * np.pi * x)
y = np.power((np.power(x, 2)), 1/3) + 1 * a * ((20 - (np.power(x, 2))) ** 0.5)

plt.text(0, -5, tulisan, fontsize=10, ha='center')

plt.xlim(-8, 8)
plt.ylim(-8, 8)

plt.plot(x, y, color="red")
plt.grid(True)

plt.show()
