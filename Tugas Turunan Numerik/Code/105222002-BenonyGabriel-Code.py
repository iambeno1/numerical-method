import numpy as np

print("Nama \t: Benony Gabriel")
print("NIM \t: 105222002\n")

print("Penyelesaian")

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
# Data jarak tempuh kendaraan:
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

# Output soal 3
print("\nLatihan 3:")
print("Waktu (s)   Kecepatan (km/s)   Percepatan (km/s^2)")
for i in range(len(t)):
    print(f"{t[i]:>6}      {v[i]:>12.4f}       {a[i]:>15.4f}")




# Benony Gabriel - 105222002