import numpy as np
import matplotlib.pyplot as plt

print("---------- 测量金属导体电阻率 ----------")

ds = [4.08, 4.10, 4.12, 4.04, 4.14, 4.10]
ls = [20.00, 20.00, 20.00, 20.00, 20.00, 20.00]
Rs = [4.376, 4.352, 4.344, 4.347, 4.346, 4.345]
Rs = [R * 10**-4 for R in Rs]

d_ = sum(ds) / len(ds)
l_ = sum(ls) / len(ls)
R_ = sum(Rs) / len(Rs)

n = len(ds)
ua_d = ((1 / n*(n-1)) * sum((d - d_)**2 for d in ds)) ** 0.5
ua_l = ((1 / n*(n-1)) * sum((l - l_)**2 for l in ls)) ** 0.5
ua_R = ((1 / n*(n-1)) * sum((R - R_)**2 for R in Rs)) ** 0.5
ub_d = 0.02 / (3 ** 0.5)
ub_l = 0.05 / (3 ** 0.5)
ub_R = 0.0011*0.01 / (3 ** 0.5)
u_d = (ua_d**2 + ub_d**2) ** 0.5
u_l = (ua_l**2 + ub_l**2) ** 0.5
u_R = (ua_R**2 + ub_R**2) ** 0.5

rho = np.pi * (d_**2) * R_ * 10**-4 / (4 * l_)
u_rho_over_rho = (
    (u_R / R_) ** 2 + 
    (2 * u_d / d_) ** 2 +
    (u_l / l_) ** 2
) ** 0.5
u_rho = rho * u_rho_over_rho

print(f"均值: d = {d_}mm  l = {l_}cm  R = {R_}Ω")
print(f"电阻率均值: ρ = {rho}")
print(f"A 类不确定度: ua_d = {ua_d}mm  ua_l = {ua_l}cm  ua_R = {ua_R}Ω")
print(f"B 类不确定度: ub_d = {ub_d}mm  ub_l = {ub_l}cm  ub_R = {ub_R}Ω")
print(f"合成不确定度: u_d = {u_d}mm  u_l = {u_l}cm  u_R = {u_R}Ω")
print(f"电阻率相对不确定度: {u_rho_over_rho}")
print(f"电阻率不确定度: {u_rho}")


print("\n---------- 测量金属导体电阻温度系数 ----------")

t = [20.0, 25.2, 30.1, 36.1, 40.0, 47.4, 50.1, 55.4]
R = [4.615, 4.697, 4.795, 4.896, 4.981, 5.086, 5.156, 5.246]

plt.rc("font", family="Source Han Serif CN", size=13, weight="bold")
plt.scatter(t, R)
plt.title("电阻 R-t 特性曲线", weight="bold", size=20)
plt.xlabel("t/℃", weight="bold", size=16)
plt.ylabel("R/10^-3Ω", weight="bold", size=16)
plt.grid(True)
for t_, R_ in zip(t, R):
    plt.text(t_ - 2, R_, f"({round(t_, 3)}, {R_})", ha="right", va="center")

linear_model = np.polyfit(t, R, 1)
print(f"linear fit model of R-t: R = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
x_s = np.arange(0, 60)
plt.plot(x_s, linear_model_fn(x_s), color="green")
plt.show()

alphas = [
    (R[4] - R[0]) / (R[0] * t[4] - R[4] * t[0]),
    (R[5] - R[1]) / (R[1] * t[5] - R[5] * t[1]),
    (R[6] - R[2]) / (R[2] * t[6] - R[6] * t[2]),
    (R[7] - R[3]) / (R[3] * t[7] - R[7] * t[3])
]
alpha_ = sum(alphas) / len(alphas)
alpha = linear_model[0] / linear_model[1]

print(f"α1 = {alphas[0]}  α2 = {alphas[1]}  α3 = {alphas[2]}  α4 = {alphas[3]}")
print(f"平均 α = {alpha_}")
print(f"由图像 α = {alpha}")

alpha0 = 0.00433
print(f"E1 = {abs(alpha_ - alpha0) / alpha0 * 100}%")
print(f"E2 = {abs(alpha  - alpha0) / alpha0 * 100}%")

"""
---------- 测量金属导体电阻率 ----------
均值: d = 4.096666666666667mm  l = 20.0cm  R = 0.00043516666666666676Ω
电阻率均值: ρ = 2.867984259715793e-08
A 类不确定度: ua_d = 0.07031674369909642mm  ua_l = 0.0cm  ua_R = 2.498888641865537e-06Ω
B 类不确定度: ub_d = 0.011547005383792516mm  ub_l = 0.02886751345948129cm  ub_R = 6.3508529610858845e-06Ω
合成不确定度: u_d = 0.07125852775477297mm  u_l = 0.02886751345948129cm  u_R = 6.8247914091038665e-06Ω
电阻率相对不确定度: 0.038187532324404
电阻率不确定度: 1.0952124162377872e-09

---------- 测量金属导体电阻温度系数 ----------
linear fit model of R-t: R = 0.017878473541685893 * t + 4.253947562658123
α1 = 0.0043068957401741536  α2 = 0.004117683173389396  α3 = 0.004245365671808534  α4 = 0.0042757073852461285
平均 α = 0.0042364129926545525
由图像 α = 0.004202795939147483
E1 = 2.1613627562458935%
E2 = 2.937738125924164%
"""