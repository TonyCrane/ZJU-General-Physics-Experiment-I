import numpy as np
import matplotlib.pyplot as plt

print("---------- plotter ----------")

plt.rc("font", family="Source Han Serif CN", size=12, weight="bold")

ds = [5.945, 5.950, 5.940, 5.945, 5.945]
Ls = [160.0, 159.8, 160.0, 160.2, 160.0]
ms = [37.439, 37.441, 37.440, 37.441, 37.440]

L = 160.0
xs_mm = [10, 20, 30, 40, 50]
xs = list(map(lambda x: x / L, xs_mm))
fs = [745.2, 744.2, 743.7, 743.6, 743.9]

plt.scatter(xs, fs)
plt.title("试样棒 共振频率-位置 曲线", weight="bold", size=18)
plt.xlabel("x/L", weight="bold", size=14)
plt.ylabel("f/Hz", weight="bold", size=14)
plt.grid(True)
for x_, f_ in zip(xs, fs):
    plt.text(x_ + 0.01, f_, f"({x_}, {f_})", ha="left", va="bottom")

model = np.polyfit(xs, fs, 2)
model_fn = np.poly1d(model)
xs_model = np.arange(0.05, 0.40, 0.01)
plt.plot(xs_model, model_fn(xs_model), color="orange")

a, b, c = model
x_low = -b / (2*a)
f_low = (4*a*c - b**2) / (4*a)
plt.scatter([x_low], [f_low], marker="x", color="black")
plt.text(x_low - 0.01, f_low, f"({x_low:.2f}, {f_low:.2f})", ha="right", va="center")

print(f"fn: f = {a} x^2 + {b} x + {c}")
print(f"lowest point: ({x_low}, {f_low})")

plt.show()

print("\n---------- calculator ----------")
d = sum(ds) / len(ds)
L = sum(Ls) / len(Ls)
m = sum(ms) / len(ms)
f = f_low
dd_y = 0.004
dL_y = 0.2
dm_y = 0.001
df_y = 0.1

# d_u_A = np.sqrt((1/20) * sum((d_-d) ** 2 for d_ in ds))
d_u_A = 0.0016
# L_u_A = np.sqrt((1/20) * sum((L_-L) ** 2 for L_ in Ls))
L_u_A = 0.06
# m_u_A = np.sqrt((1/20) * sum((m_-m) ** 2 for m_ in ms))
m_u_A = 0.0004
d_u_B = dd_y / np.sqrt(3)
L_u_B = dL_y / np.sqrt(3)
m_u_B = dm_y / np.sqrt(3)

# dd = round(np.sqrt(d_u_A**2 + d_u_B**2), 4)
dd = 0.003
# dL = round(np.sqrt(L_u_A**2 + L_u_B**2), 2)
dL = 0.2
# dm = round(np.sqrt(m_u_A**2 + m_u_B**2), 5)
dm = 0.0007
df = df_y

print(f"d: u_A = {d_u_A}\nL: u_A = {L_u_A}\nm: u_A = {m_u_A}")
print(f"d: u_C = {dd}\nL: u_C = {dL}\nm: u_C = {dm}")

E = 1.6067 * ((L**3) * m * (f**2)) / (d ** 4)
dE = E * np.sqrt(
    (3 * dL / L) ** 2 +
    (4 * dd / d) ** 2 +
    (    dm / m) ** 2 +
    (2 * df / f) ** 2
)

print()
print(f"d = {d} ± {dd} mm")
print(f"L = {L} ± {dL} mm")
print(f"m = {m} ± {dm} g")
print(f"E = {E} ± {dE} Pa")
print(f"E = {E:.4g} ± {dE:.4g} Pa")

"""res
---------- plotter ----------
fn: f = 54.85714285716307 x^2 + -25.691428571436525 x + 746.5800000000011
lowest point: (0.2341666666666529, 743.5719619047622)

---------- calculator ----------
d: u_A = 0.0016
L: u_A = 0.06
m: u_A = 0.0004
d: u_C = 0.003
L: u_C = 0.2
m: u_C = 0.0007

d = 5.945 ± 0.003 mm
L = 160.0 ± 0.2 mm
m = 37.4402 ± 0.0007 g
E = 109061502500.9468 ± 465394319.9617047 Pa
E = 1.091e+11 ± 4.654e+08 Pa
"""