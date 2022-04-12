import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

plt.rc("font", family="Source Han Serif CN", size=13, weight="bold")

fs = [365, 405, 436, 546, 577]
nus = list(round((3 / f) * 10**3, 2)  for f in fs)
print(nus)
Uas = [1.536, 1.206, 1.009, 0.472, 0.353]

plt.scatter(nus, Uas)
plt.title("Ua-ν 图像", weight="bold", size=20)
plt.xlabel("ν/10^14 Hz", weight="bold", size=16)
plt.ylabel("Ua/V", weight="bold", size=16)
plt.grid(True)
for nu_, Ua_ in zip(nus[:-1], Uas[:-1]):
    plt.text(nu_ - 0.2, Ua_, f"({nu_}, {Ua_})", ha="right", va="center")
plt.text(nus[-1] - 0.2, Uas[-1], f"({nus[-1]}, {Uas[-1]})", ha="right", va="top")

linear_model = np.polyfit(nus, Uas, 1)
print(f"linear fit model of Ua-v: Ua = {linear_model[0]} * v + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
x_s = np.arange(0, 9, 0.01)
plt.plot(x_s, linear_model_fn(x_s), color="green")

e = 1.602e-19
h0 = 6.626
h = linear_model[0] * e * 10**20 # 10^-34 Js
W0 = -linear_model[1] * e * 10**19 # 10^-19 J
delta = abs(h - h0) / h0

print(f"普朗克常量 h = {h} *10^-34 Js")
print(f"逸出功 W0 = {W0} *10^-19 J")
print(f"普朗克常量相对误差 δ = {delta*100}%")

plt.show()

plt.figure()

Is = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 19, 20, 21, 22, 23, 24, 25, 28, 32, 35, 38, 40, 43, 44, 48, 51, 53, 56, 59, 62, 64, 66, 69, 72, 79, 82, 88, 91, 94, 97, 102]
Us = [-2.50, 0.42, 1.08, 1.30, 1.84, 1.99, 2.34, 2.42, 2.63, 2.74, 3.18, 3.24, 3.29, 3.38, 3.57, 3.61, 3.74, 3.85, 4.08, 4.28, 4.37, 4.54, 4.72, 5.32, 6.02, 7.07, 7.86, 8.32, 9.05, 9.41, 10.41, 10.94, 11.58, 12.48, 13.33, 14.04, 14.67, 15.16, 16.42, 17.47, 19.47, 20.84, 22.94, 24.35, 25.27, 26.57, 29.01]

plt.scatter(Us, Is)
plt.title("光电管伏安特性曲线", weight="bold", size=20)
plt.xlabel("U/V", weight="bold", size=16)
plt.ylabel("I/10^-10 A", weight="bold", size=16)
plt.grid(True)

# model = make_interp_spline(Us, Is)
linear_model = np.polyfit(Us, Is, 10)
model = np.poly1d(linear_model)
Us_model = np.arange(-2.5, 30, 0.05)
# plt.plot(Us_model, model(Us_model), color="orange")

plt.show()

"""
[8.22, 7.41, 6.88, 5.49, 5.2]
linear fit model of Ua-v: Ua = 0.38920067247440027 * v + -1.6690924652300176
普朗克常量 h = 6.234994773039892 *10^-34 Js
逸出功 W0 = 2.6738861292984883 *10^-19 J
普朗克常量相对误差 δ = 5.901074961667798%
"""