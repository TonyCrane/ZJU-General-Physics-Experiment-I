import numpy as np
import matplotlib.pyplot as plt

plt.rc("font", family="Source Han Serif CN", size=13, weight="bold")
plt.figure(figsize=(13, 6))

t = [20.5, 25.3, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0]
U = [29.3, 35.4, 41.0, 47.4, 53.3, 59.3, 65.2, 70.7]
alphas = []
E = 1.3
alpha_expect = 0.004280

for t_, U_ in zip(t, U):
    U_ = U_ / 1000
    alphas.append(4 * U_ / (t_ * (E - 2 * U_)))
alpha = sum(alphas) / len(alphas)

print(f"alpha values: {alphas}")
print(f"average alpha: {alpha} with relative error {abs(alpha - alpha_expect) / alpha_expect * 100}%")

plt.subplot(121)
plt.scatter(t, U)
plt.title("Cu50 电阻 U-t 特性曲线", weight="bold", size=20)
plt.xlabel("t/℃", weight="bold", size=16)
plt.ylabel("U/mV", weight="bold", size=16)
plt.grid(True)
for t_, U_ in zip(t, U):
    plt.text(t_ - 2, U_, f"({t_}, {U_})", ha="right", va="center")

linear_model = np.polyfit(t, U, 1)
print(f"linear fit model of U-t: U = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
x_s = np.arange(0, 60)
plt.plot(x_s, linear_model_fn(x_s), color="orange", linestyle="--")

k = sum(x*y for x, y in zip(t, U)) / sum(x**2 for x in t)
print(f"proportional fit model of U-t: U = {k} * t")
print(
    f"alpha calculated by proportional fit: {4 * k / 1000 / 1.3}"
    f" with relative error {abs(4 * k / 1000 / 1.3 - alpha_expect) / alpha_expect * 100}%"
)
fn = np.poly1d([k, 0])
plt.plot(x_s, fn(x_s), color="green")

t = [60.0, 55.3, 50.0, 45.0, 40.0, 35.1, 30.0, 25.2]
R = [63.77, 62.75, 61.60, 60.51, 59.41, 58.36, 57.19, 56.17]

plt.subplot(122)
plt.scatter(t, R)
plt.title("Cu50 电阻 Rt-t 特性曲线", weight="bold", size=20)
plt.xlabel("t/℃", weight="bold", size=16)
plt.ylabel("Rt/Ω", weight="bold", size=16)
plt.grid(True)
for t_, R_ in zip(t, R):
    plt.text(t_ - 2, R_, f"({t_}, {R_})", ha="right", va="center")

linear_model = np.polyfit(t, R, 1)
print(f"linear model of Rt-t: Rt = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
x_s = np.arange(0, 65)
plt.plot(x_s, linear_model_fn(x_s), color="green")

R0 = linear_model[1]
R0_alpha = linear_model[0]
alpha_ = R0_alpha / R0
print(
    f"alpha calculated by Rt-t graph: {alpha_}"
    f" with relative error {abs(alpha_ - alpha_expect) / alpha_expect * 100}%"
)

plt.show()

"""
result:

alpha values: [0.0046053432984789, 0.004553236206202433, 0.0044882320744389715, 0.004494808212033568, 0.004466230936819172, 0.0044617497131463615, 0.004459644322845418, 0.00443795803712945]
average alpha: 0.004495900350136785
linear fit model of U-t: U = 1.203704426194331 * t + 4.940713575093168
proportional fit model of U-t: U = 1.324184821820882 * t
alpha calculated by proportional fit: 0.0052967392872835285
linear model of Rt-t: Rt = 0.21872471034558272 * t + 50.65779545703681
"""
