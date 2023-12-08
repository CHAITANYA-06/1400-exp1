import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-10, 10, 400)

f = pd.read_csv("se.csv")

for index, row in f.iterrows():
    a = row[index]
    b = row[index]
    c = row[index]

    y = a*x**2 + b*x + c

    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')

plt.title('Plot of the quadratic functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
