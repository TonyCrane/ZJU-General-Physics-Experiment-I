import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 1000)

ps = [1, 2, 3, 1, 3]
qs = [1, 1, 1, 2, 2]
ns = [0.25, 0.6, 0.25, 1.8, 0]

plt.figure(figsize=(17, 3))

for ind, (p, q, n) in enumerate(zip(ps, qs, ns)):
    plt.subplot(1, 5, ind + 1)
    plt.xlim((-1.1, 1.1))
    plt.ylim((-1.1, 1.1))
    plt.axis('off')
    x = np.sin(p * theta)
    y = np.sin(q * theta + n * np.pi)
    plt.plot(x, y, color="black")

plt.show()