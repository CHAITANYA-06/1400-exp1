import matplotlib.pyplot as plt
import numpy as np

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

x = np.linspace(-10, 10, 400)

y1 = a*x**2 + b*x + c

plt.plot(x, y1, label=f'{a}x^2 + {b}x + {c}')

a = 1
b = -3
c = 2

y2 = a*x**2 + b*x + c

plt.plot(x, y2, label=f'{a}x^2 + {b}x + {c}')

plt.title('Plot of the quadratic functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
