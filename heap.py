import numpy as np
import matplotlib.pyplot as plt

# Define the range of input sizes (n)
n = np.linspace(1, 100, 100)

# Time complexities
bottom_up = n             # O(n)
top_down = n * np.log2(n) # O(n log n)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n, bottom_up, label='Bottom-Up (O(n))', color='blue', linewidth=2)
plt.plot(n, top_down, label='Top-Down (O(n log n))', color='red', linewidth=2)

# Customize the plot
plt.title('Time Complexity of Heap Construction', fontsize=14)
plt.xlabel('Input Size (n)', fontsize=12)
plt.ylabel('Time Complexity', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()