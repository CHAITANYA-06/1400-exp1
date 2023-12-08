import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate x values
x = np.linspace(-10, 10, 400)

# Read coefficients (a, b, c) from the CSV file
f = pd.read_csv("se.csv")

# Plot each set of coefficients
for index, row in f.iterrows():
    a = row[index]
    b = row[index]
    c = row[index]

    # Calculate y values for the function
    y = a*x**2 + b*x + c

    # Plot the function
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')

# Add title, labels, legend, and grid
plt.title('Plot of the quadratic functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
