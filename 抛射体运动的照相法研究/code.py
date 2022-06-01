import matplotlib.pyplot as plt
import numpy as np

plt.rc("font", family="Source Han Serif CN", size=13, weight="bold")
plt.figure(figsize=(10, 10))

xs = [0.8, 7.6, 14.0, 21.0, 27.6, 34.2, 41.0, 47.2, 54.3, 61.0, 67.0]
ys = [20.8, 13.9, 8.9, 5.1, 3.4, 3.1, 5.0, 8.5, 13.5, 18.9, 26.8]
vxs = [round(b - a, 1) for a, b in zip(xs, xs[1:])]
vys = [round(b - a, 1) for a, b in zip(ys, ys[1:])]
ays = [round(b - a, 1) for a, b in zip(vys, vys[1:])]
print(xs, ys, vxs, vys, ays, sep="\n")
ts = list(range(11))

plt.subplot(321)
plt.scatter(range(len(xs)), xs)
plt.title("x-t 图", weight="bold", size=20)
plt.xlabel("t/T", weight="bold", size=16)
plt.ylabel("x/cm", weight="bold", size=16)
plt.grid(True)

linear_model = np.polyfit(ts, xs, 1)
print(f"x-t: x = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
t_s = np.arange(0, 11)
plt.plot(t_s, linear_model_fn(t_s), color="orange", linestyle="--")

plt.subplot(322)
plt.scatter(range(len(ys)), ys)
plt.title("y-t 图", weight="bold", size=20)
plt.xlabel("t/T", weight="bold", size=16)
plt.ylabel("y/cm", weight="bold", size=16)
plt.grid(True)

linear_model = np.polyfit(ts, ys, 2)
print(f"x-t: y = {linear_model[0]} * t^2 + {linear_model[1]} * t + {linear_model[2]}")
linear_model_fn = np.poly1d(linear_model)
t_s = np.arange(0, 11)
plt.plot(t_s, linear_model_fn(t_s), color="orange", linestyle="--")

plt.subplot(323)
plt.scatter(np.arange(0.5, len(vxs)+0.5), vxs)
plt.title("vx-t 图", weight="bold", size=20)
plt.xlabel("t/T", weight="bold", size=16)
plt.ylabel("vx/(cm/T)", weight="bold", size=16)
plt.grid(True)

linear_model = np.polyfit(np.arange(0.5, len(vxs)+0.5), vxs, 1)
print(f"vx-t: vx = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
t_s = np.arange(0, 11)
plt.plot(t_s, linear_model_fn(t_s), color="orange", linestyle="--")
plt.ylim(0, 11)

plt.subplot(324)
plt.scatter(np.arange(0.5, len(vys)+0.5), vys)
plt.title("vy-t 图", weight="bold", size=20)
plt.xlabel("t/T", weight="bold", size=16)
plt.ylabel("vy/(cm/T)", weight="bold", size=16)
plt.grid(True)

linear_model = np.polyfit(np.arange(0.5, len(vys)+0.5), vys, 1)
print(f"vy-t: vy = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
t_s = np.arange(0, 11)
plt.plot(t_s, linear_model_fn(t_s), color="orange", linestyle="--")
# plt.ylim(0, 11)

plt.subplot(325)
plt.scatter(np.arange(1, len(ays)+1), ays)
plt.title("ay-t 图", weight="bold", size=20)
plt.xlabel("t/T", weight="bold", size=16)
plt.ylabel("ay/(cm/T^2)", weight="bold", size=16)
plt.grid(True)

linear_model = np.polyfit(np.arange(1, len(ays)+1), ays, 1)
print(f"ay-t: ay = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
t_s = np.arange(0, 11)
plt.plot(t_s, linear_model_fn(t_s), color="orange", linestyle="--")
plt.ylim(0, 11)

a_ = sum(ays) / len(ays)
g_ = a_ * 24 * 24 / 100
g = 9.793
E = abs(g_ - g) / g
print(f"average of ay: {a_} cm/T^2\ng = {g_} m/s^2\nE = {E*100}%")

plt.tight_layout()
plt.show()

"""
[0.8, 7.6, 14.0, 21.0, 27.6, 34.2, 41.0, 47.2, 54.3, 61.0, 67.0]
[20.8, 13.9, 8.9, 5.1, 3.4, 3.1, 5.0, 8.5, 13.5, 18.9, 26.8]
[6.8, 6.4, 7.0, 6.6, 6.6, 6.8, 6.2, 7.1, 6.7, 6.0]
[-6.9, -5.0, -3.8, -1.7, -0.3, 1.9, 3.5, 5.0, 5.4, 7.9]
[1.9, 1.2, 2.1, 1.4, 2.2, 1.6, 1.5, 0.4, 2.5]
x-t: x = 6.6481818181818175 * t + 0.9136363636363705
x-t: y = 0.8160839160839166 * t^2 + -7.504475524475527 * t + 20.586713286713298
vx-t: vx = -0.03393939393939427 * t + 6.789696969696973
vy-t: vy = 1.6230303030303035 * t + -7.515151515151515
ay-t: ay = -0.016666666666666777 * t + 1.727777777777778
average of ay: 1.6444444444444446 cm/T^2
g = 9.472000000000001 m/s^2
E = 3.277851526600613%
"""