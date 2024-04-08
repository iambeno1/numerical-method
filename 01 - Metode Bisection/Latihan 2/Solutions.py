# Fungsi f(x)
def f(x):
    return x**2 - 4*x + 3

# Metode Bisection
def bisection_method(a, b, epsilon):
    iterations = 0
    while (b - a) >= epsilon:
        iterations += 1
        c = (a + b) / 2
        if f(c) == 0:
            return c, iterations
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, iterations


# Menentukan batas awal a dan b serta toleransi error epsilon
a = 1
b = 3
epsilon = 0.001

# Panggil metode bisection
root, iterations = bisection_method(a, b, epsilon)


print("Akar yang ditemukan: ", root)
print("Iterasi yang diperlukan: ", iterations)

