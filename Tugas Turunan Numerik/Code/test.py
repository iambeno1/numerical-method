import numpy as np

# Latihan 1: f(x) = sin(0.5)
f1 = lambda x: np.sin(0.5)
x1 = 1
h1 = 0.2

# Turunan pertama dengan metode selisih maju, mundur, dan pusat
f1_forward_diff = (f1(x1 + h1) - f1(x1)) / h1
f1_backward_diff = (f1(x1) - f1(x1 - h1)) / h1
f1_central_diff = (f1(x1 + h1) - f1(x1 - h1)) / (2 * h1)

# Output untuk Latihan 1
print("Latihan 1:")
print("Selisih Maju:", f1_forward_diff)
print("Selisih Mundur:", f1_backward_diff)
print("Selisih Pusat:", f1_central_diff)

# Latihan 2: f(x) = x^2 * cos(a)
a = np.pi / 4  # contoh nilai a
f2 = lambda x: x**2 * np.cos(a)
x2 = 0.4
h2 = 0.1

# Turunan kedua dengan metode selisih maju, mundur, dan pusat
f2_forward_diff2 = (f2(x2 + 2*h2) - 2*f2(x2 + h2) + f2(x2)) / h2**2
f2_backward_diff2 = (f2(x2) - 2*f2(x2 - h2) + f2(x2 - 2*h2)) / h2**2
f2_central_diff2 = (f2(x2 + h2) - 2*f2(x2) + f2(x2 - h2)) / h2**2

# Output untuk Latihan 2
print("\nLatihan 2:")
print("Selisih Maju:", f2_forward_diff2)
print("Selisih Mundur:", f2_backward_diff2)
print("Selisih Pusat:", f2_central_diff2)

# Latihan 3: Data jarak tempuh kendaraan
t = np.array([0, 25, 50, 75, 100, 125])
y = np.array([0, 32, 58, 78, 92, 100])

# Kecepatan (turunan pertama)
v = np.zeros(len(t))
v[0] = (y[1] - y[0]) / (t[1] - t[0])  # Selisih maju untuk titik pertama
v[-1] = (y[-1] - y[-2]) / (t[-1] - t[-2])  # Selisih mundur untuk titik terakhir
for i in range(1, len(t) - 1):
    v[i] = (y[i+1] - y[i-1]) / (t[i+1] - t[i-1])  # Selisih pusat untuk titik dalam

# Percepatan (turunan kedua)
a = np.zeros(len(t))
a[0] = (y[2] - 2*y[1] + y[0]) / ((t[1] - t[0])**2)  # Selisih maju untuk titik pertama
a[-1] = (y[-1] - 2*y[-2] + y[-3]) / ((t[1] - t[0])**2)  # Selisih mundur untuk titik terakhir
for i in range(1, len(t) - 1):
    a[i] = (y[i+1] - 2*y[i] + y[i-1]) / ((t[1] - t[0])**2)  # Selisih pusat untuk titik dalam

# Output untuk Latihan 3
print("\nLatihan 3:")
print("Waktu (s)   Kecepatan (km/s)   Percepatan (km/s^2)")
for i in range(len(t)):
    print(f"{t[i]:>6}      {v[i]:>12.4f}       {a[i]:>15.4f}")