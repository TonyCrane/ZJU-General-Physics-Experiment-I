import numpy as np
import matplotlib.pyplot as plt

plt.rc("font", family="Source Han Serif CN", size=13, weight="bold")

x = [1, 2, 3, 4, 5, 6]
I = [0.94, 1.50, 2.00, 3.00, 4.00, 4.90]
dI = [0.01, 0.05, 0.00, 0.05, 0.10, 0.10]

plt.figure()
plt.plot(x, I, marker="D")
plt.plot(x, dI, marker=".", color="black")
plt.title("5 mA 电流表校准曲线", weight="bold", size=20)
plt.xlabel("次数", weight="bold", size=16)
plt.ylabel("I标准/mA & ΔI/mA", weight="bold", size=16)
plt.grid(True)

plt.text(x[0], I[0]+0.4, f"{I[0]:.2f}", ha="center", va="top")
for x_, I_ in zip(x[1:], I[1:]):
    plt.text(x_, I_-0.15, f"{I_:.2f}", ha="center", va="top")
for x_, dI_ in zip(x, dI):
    plt.text(x_, dI_+0.4, f"{dI_:.2f}", ha="center", va="top")

# plt.show()

U = [1.00, 1.50, 1.95, 3.10, 3.95, 4.93]
dU = [0.05, 0.00, 0.05, 0.10, 0.10, 0.07]

plt.figure()
plt.plot(x, U, marker="D")
plt.plot(x, dU, marker=".", color="black")
plt.title("5 V 电压表校准曲线", weight="bold", size=20)
plt.xlabel("次数", weight="bold", size=16)
plt.ylabel("U标准/V & ΔU/V", weight="bold", size=16)
plt.grid(True)

plt.text(x[0], U[0]+0.4, f"{U[0]:.2f}", ha="center", va="top")
for x_, U_ in zip(x[1:], U[1:]):
    plt.text(x_, U_-0.15, f"{U_:.2f}", ha="center", va="top")
for x_, dU_ in zip(x, dU):
    plt.text(x_, dU_+0.4, f"{dU_:.2f}", ha="center", va="top")

plt.show()