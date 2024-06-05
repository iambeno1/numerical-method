import numpy as np
import matplotlib.pyplot as plt

# Definisikan persamaan diferensial
def f1(t, y):
    return y**3 - 1.5*y

def f2(x, y):
    return (1 + 2*x) * np.sqrt(y)

# Metode Euler
def metode_euler(f, y0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    y_values = np.zeros(t_values.shape)
    y_values[0] = y0
    for i in range(1, len(t_values)):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])
    return t_values, y_values

# Metode Runge-Kutta Orde 4 (RK4)
def metode_rk4(f, y0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    y_values = np.zeros(t_values.shape)
    y_values[0] = y0
    for i in range(1, len(t_values)):
        k1 = h * f(t_values[i-1], y_values[i-1])
        k2 = h * f(t_values[i-1] + h/2, y_values[i-1] + k1/2)
        k3 = h * f(t_values[i-1] + h/2, y_values[i-1] + k2/2)
        k4 = h * f(t_values[i-1] + h, y_values[i-1] + k3)
        y_values[i] = y_values[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    return t_values, y_values

# Metode Heun
def metode_heun(f, y0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    y_values = np.zeros(t_values.shape)
    y_values[0] = y0
    for i in range(1, len(t_values)):
        y_pred = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])
        y_values[i] = y_values[i-1] + (h/2) * (f(t_values[i-1], y_values[i-1]) + f(t_values[i], y_pred))
    return t_values, y_values

# Soal 1
t0_1, tf_1, h_1 = 0, 1, 0.5
y0_1 = 1

# Metode Euler untuk Soal 1
t_euler_1, y_euler_1 = metode_euler(f1, y0_1, t0_1, tf_1, h_1)

# Metode RK4 untuk Soal 1
t_rk4_1, y_rk4_1 = metode_rk4(f1, y0_1, t0_1, tf_1, h_1)

# Soal 2
x0_2, xf_2, h_2 = 0, 1, 0.25
y0_2 = 1

# Metode Euler untuk Soal 2
x_euler_2, y_euler_2 = metode_euler(f2, y0_2, x0_2, xf_2, h_2)

# Metode Heun untuk Soal 2
x_heun_2, y_heun_2 = metode_heun(f2, y0_2, x0_2, xf_2, h_2)

# Metode RK4 untuk Soal 2
x_rk4_2, y_rk4_2 = metode_rk4(f2, y0_2, x0_2, xf_2, h_2)

# Print hasil numerik untuk Soal 1
print("Hasil Metode Euler untuk Soal 1:")
print("t_values:", t_euler_1)
print("y_values:", y_euler_1)

print("\nHasil Metode RK4 untuk Soal 1:")
print("t_values:", t_rk4_1)
print("y_values:", y_rk4_1)

# Print hasil numerik untuk Soal 2
print("\nHasil Metode Euler untuk Soal 2:")
print("x_values:", x_euler_2)
print("y_values:", y_euler_2)

print("\nHasil Metode Heun untuk Soal 2:")
print("x_values:", x_heun_2)
print("y_values:", y_heun_2)

print("\nHasil Metode RK4 untuk Soal 2:")
print("x_values:", x_rk4_2)
print("y_values:", y_rk4_2)

# Plot hasil untuk Soal 1
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(t_euler_1, y_euler_1, 'o-', label='Euler h=0.5')
plt.plot(t_rk4_1, y_rk4_1, 's-', label='RK4 h=0.5')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Soal 1')
plt.legend()

# Plot hasil untuk Soal 2
plt.subplot(1, 2, 2)
plt.plot(x_euler_2, y_euler_2, 'o-', label='Euler h=0.25')
plt.plot(x_heun_2, y_heun_2, 'd-', label='Heun h=0.25')
plt.plot(x_rk4_2, y_rk4_2, 's-', label='RK4 h=0.25')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Soal 2')
plt.legend()

plt.tight_layout()
plt.show()
