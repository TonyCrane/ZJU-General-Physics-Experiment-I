import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from scipy.interpolate import make_interp_spline

print("---------- 交流电路功率因数实验 ----------")

plt.rc("font", family="Source Han Serif CN", size=12, weight="bold")

Is = [0.3042, 0.2547, 0.1843, 0.1475, 0.1178, 0.1234, 0.1681, 0.2082, 0.2683, 0.3331]
Us = [220.2, 220.1, 219.9, 219.8, 219.9, 219.8, 219.9, 219.8, 219.7, 219.2]
Ps = [22.7, 22.9, 22.9, 23.0, 23.1, 23.1, 23.2, 23.3, 23.2, 23.1]
Cs = list(range(10))
cosphis = []

for i, u, p in zip(Is, Us, Ps):
    cosphis.append(p / (u * i))

print("功率因数：", end="")
for cosphi in cosphis:
    print(round(cosphi, 3), end=" ")
print()

plt.figure(figsize=(8, 4))
plt.scatter(Cs, cosphis)
plt.title("cosφ-C 曲线", weight="bold", size=18)
plt.xlabel("C/μF", weight="bold", size=14)
plt.ylabel("cosφ", weight="bold", size=14)
plt.grid(True)
for c, cosphi in zip(Cs, cosphis):
    plt.text(c + 0.05, cosphi, f"({c}, {round(cosphi, 3)})", ha="left", va="top")

# model = np.polyfit(Cs, cosphis, 5)
# model_fn = np.poly1d(model)
model = make_interp_spline(Cs, cosphis)
Cs_model = np.arange(0, 9.5, 0.01)
index_C = argrelextrema(model(Cs_model), np.greater)[0]
max_C = round(float(Cs_model[index_C]), 3)
max_cosphi = round(float(model(max_C)), 3)
print(f"图像最高点：({max_C}, {max_cosphi})")
plt.plot(Cs_model, model(Cs_model), color="orange")

plt.scatter([max_C], [max_cosphi], marker="x", color="black")
plt.text(max_C + 0.05, max_cosphi, f"({max_C}, {max_cosphi})", ha="left", va="bottom")

plt.ylim((0, 1))
plt.show()

print("\n---------- 弗兰克赫兹实验 ----------")

Ug2k = [
    [28.4, 40.3, 51.3, 62.0, 75.0, 86.9, 100.3],
    [28.2, 40.1, 50.5, 62.4, 74.4, 86.7, 99.9],
    [28.4, 39.7, 50.7, 61.8, 74.4, 86.9, 99.9],
    [27.9, 39.9, 50.4, 61.8, 74.4, 86.7, 100.3],
    [27.9, 39.5, 51.4, 61.8, 74.2, 87.1, 99.9],
]

U = [round(((e + f + g) - (a + b + c)) / 12, 1) for a, b, c, _, e, f, g in Ug2k]
U_ = round(sum(U) / len(U), 1)
uncertain = np.sqrt((1 / 20) * sum((u - U_) ** 2 for u in U))

print(f"逐差计算第一激发电势：{' '.join(map(str, U))}")
print(f"平均值：{U_}V")
print(f"相对误差：{round(abs(U_ - 11.61) / 11.61 * 100, 1)}%")
print(f"不确定度：{uncertain}V -> 0.1V")

"""res:
---------- 交流电路功率因数实验 ----------
功率因数：0.339 0.408 0.565 0.709 0.892 0.852 0.628 0.509 0.394 0.316 
图像最高点：(4.35, 0.91)

---------- 弗兰克赫兹实验 ----------
逐差计算第一激发电势：11.8 11.8 11.9 11.9 11.9
平均值：11.9V
相对误差：2.5%
不确定度：0.03162277660168368V -> 0.1V
"""
