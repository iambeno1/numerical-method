import numpy as np

# Soal 1
def f1(x):
    return np.sin(0.5 * np.sqrt(x)) / x

x1 = 1
h1 = 0.2

# Selisih Maju
f1_forward_diff = (f1(x1 + h1) - f1(x1)) / h1

# Selisih Mundur
f1_backward_diff = (f1(x1) - f1(x1 - h1)) / h1

# Selisih Pusat
f1_central_diff = (f1(x1 + h1) - f1(x1 - h1)) / (2 * h1)

print("Soal 1:")
print(f"Selisih Maju: {f1_forward_diff}")
print(f"Selisih Mundur: {f1_backward_diff}")
print(f"Selisih Pusat: {f1_central_diff}")

# Soal 2
def f2(x):
    return x**2 * np.cos(x)

x2 = 0.4
h2 = 0.1

# Selisih Maju
f2_forward_diff2 = (f2(x2 + 2*h2) - 2 * f2(x2 + h2) + f2(x2)) / h2**2

# Selisih Mundur
f2_backward_diff2 = (f2(x2) - 2 * f2(x2 - h2) + f2(x2 - 2*h2)) / h2**2

# Selisih Pusat
f2_central_diff2 = (f2(x2 + h2) - 2 * f2(x2) + f2(x2 - h2)) / h2**2

print("\nSoal 2:")
print(f"Selisih Maju: {f2_forward_diff2}")
print(f"Selisih Mundur: {f2_backward_diff2}")
print(f"Selisih Pusat: {f2_central_diff2}")

# Soal 3
t = np.array([0, 25, 50, 75, 100, 125])
y = np.array([0, 32, 58, 78, 92, 100])

def central_diff_velocity(t, y):
    v = np.zeros(len(t))
    for i in range(1, len(t) - 1):
        v[i] = (y[i + 1] - y[i - 1]) / (t[i + 1] - t[i - 1])
    v[0] = (y[1] - y[0]) / (t[1] - t[0])  # forward difference for the first point
    v[-1] = (y[-1] - y[-2]) / (t[-1] - t[-2])  # backward difference for the last point
    return v

def central_diff_acceleration(t, v):
    a = np.zeros(len(t))
    for i in range(1, len(t) - 1):
        a[i] = (v[i + 1] - v[i]) / (t[i + 1] - t[i])
    a[0] = (v[1] - v[0]) / (t[1] - t[0])  # forward difference for the first point
    a[-1] = (v[-1] - v[-2]) / (t[-1] - t[-2])  # backward difference for the last point
    return a

v = central_diff_velocity(t, y)
a = central_diff_acceleration(t, v)

print("\nSoal 3:")
print(f"Kecepatan: {v}")
print(f"Percepatan: {a}")
