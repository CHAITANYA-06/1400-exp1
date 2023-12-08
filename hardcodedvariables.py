import matplotlib.pyplot as plt
import numpy as np

def quadratic_solution(a, b, c, x):
    """
    Calculate the quadratic solution for the given coefficients and x value.
    """
    y = a * x**2 + b * x + c
    return y

def plot_temperature_over_time(a, b, c, time_range):
    """
    Plot temperature over time using a quadratic function.
    """
    time = np.array(time_range)
    temperature = quadratic_solution(a, b, c, time)

    plt.plot(time, temperature)
    plt.title("Temperature Over Time")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.grid(True)
    plt.show()

def main():
    print("Weather Modeling using Quadratic Solution")

    # Hard-coded coefficients
    a_hardcoded, b_hardcoded, c_hardcoded = -5.1, -0.5, 0
    time_range = np.linspace(0, 10, 100)  # Adjust the time range as needed

    # Plot temperature over time using the quadratic function
    plot_temperature_over_time(a_hardcoded, b_hardcoded, c_hardcoded, time_range)

if __name__ == "__main__":
    main()
