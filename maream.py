import matplotlib.pyplot as plt
import numpy as np

# Test data (X and Y)
real_x = [1, 2, 3, 4, 5]
real_y = [2, 4, 1, 5, 2]
pred_x = [1.1, 1.9, 3.2, 3.8, 5.1]
pred_y = [2.1, 3.8, 1.2, 4.8, 2.2]

# Create the plot
plt.figure(figsize=(8, 5))
plt.scatter(real_x, real_y, color='blue', label='Real')
plt.scatter(pred_x, pred_y, color='red', marker='x', label='Predicted')
plt.title('Wi-Fi Localization Test')
plt.legend()
plt.grid(True)

# This line is responsible for displaying the window
plt.show()













     











