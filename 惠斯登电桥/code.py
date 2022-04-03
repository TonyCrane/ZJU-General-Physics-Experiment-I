import math

Rs = [676.9, 676.3, 680.9, 677.8, 676.3, 684.1, 679.9, 684.6]
R_ = sum(Rs) / len(Rs)
S = (1/7*sum((R - R_)**2 for R in Rs)) ** 0.5
p = S / R_ * 100

print(f"平均: {R_}")
print(f"标准差: {S}")
print(f"离散度: {p}%")