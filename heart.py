import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red', linewidth=2)
plt.fill(x, y, color='red', alpha=0.3) 
plt.title("Heart for YOU", fontsize=16)
plt.axis('equal')  
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()