import matplotlib.pyplot as plt
import numpy as np

# Get user input for the coefficients
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate y values for the first function
y1 = a*x**2 + b*x + c

# Plot the first function
plt.plot(x, y1, label=f'{a}x^2 + {b}x + {c}')

# Hard-coded coefficients for the second function
a = 1
b = -3
c = 2

# Calculate y values for the second function
y2 = a*x**2 + b*x + c

# Plot the second function
plt.plot(x, y2, label=f'{a}x^2 + {b}x + {c}')

# Add title, labels, legend, and grid
plt.title('Plot of the quadratic functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
