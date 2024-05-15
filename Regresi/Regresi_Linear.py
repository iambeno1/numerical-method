import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Contoh data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1, 4, 9, 16, 25])

# Membuat model regresi linear
model = LinearRegression()
model.fit(X, y)

# Prediksi
y_pred = model.predict(X)

# Visualisasi
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, y_pred, color='red', label='Regresi Linear')
plt.legend()
plt.show()
