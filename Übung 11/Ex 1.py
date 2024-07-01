import numpy as np
import matplotlib.pyplot as plt

tau = 365
A = 10
B = 12
C = 11  # konstante Temperatur bei 20 Metern Tiefe
D = 0.1
N = 100  # Anzahl Stützstellen in Tiefe
a = 20 / N  # Stützstellenabstand

# Check the stability condition and set an appropriate time step h
h = 0.5 * a**2 / D  # this ensures c <= 0.5

year = 365
epsilon = h / 2

def temp(t):
    return A + B * np.sin(2 * np.pi * t / tau)


t_points = np.array([i * year for i in range(1, 10, 2)], float)
t_points = np.append(t_points, 9.25 * year)
t_points = np.append(t_points, 9.5 * year)
t_points = np.append(t_points, 9.75 * year)
t_points = np.append(t_points, 10 * year)
tend = t_points[-1] + epsilon
print(t_points)
T = np.empty(N+1, float)
T[N] = C
T[0:N] = A  # Corrected initialization

Tp = np.empty(N+1, float)
Tp[0] = temp(0)
Tp[N] = C

t = 0
c = h * D / (a * a)

depth = np.linspace(0, 20, N+1)

while t < tend:
    Tp[1:N] = T[1:N] + c * (T[2:N + 1] + T[0:N - 1] - 2 * T[1:N])
    Tp[0] = temp(t)
    T, Tp = Tp, T
    t += h

    for tp in t_points:
        if abs(t - tp) < epsilon:
            plt.plot(depth, T, label=f"t={tp/year} Jahre")

plt.xlabel("Tiefe [m]")
plt.ylabel("Temperatur [°C]")
plt.legend()
plt.show()

