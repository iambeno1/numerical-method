import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def polynomial_regression(X, y, degree):
    # Transformasi fitur ke bentuk polinomial
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X)
    
    # Membuat model regresi linear
    model = LinearRegression()
    model.fit(X_poly, y)
    
    # Prediksi
    y_poly_pred = model.predict(X_poly)
    
    # Urutkan hasil untuk visualisasi yang lebih baik
    sorted_zip = sorted(zip(X, y_poly_pred))
    X_sorted, y_poly_pred_sorted = zip(*sorted_zip)
    
    # Visualisasi
    plt.scatter(X, y, color='blue', label='Data')
    plt.plot(X_sorted, y_poly_pred_sorted, color='red', label='Regresi Polinomial')
    plt.legend()
    plt.show()
    
    return model

# Contoh penggunaan
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1, 4, 9, 16, 25])
degree = 2

model = polynomial_regression(X, y, degree)
