import numpy as np

a = np.array([[1, 2, -1], [1, 0, 1], [4, -4, 5]])

def metodo_potencia(A, iteraciones):
    filas, columnas = A.shape
    if filas != columnas:
        raise ValueError("La matriz no es cuadrada")
        
    vector = np.array([1.0, 0.0, 0.0])  # Vector inicial para encontrar el estado base E_0
    
    for i in range(iteraciones):
        vector = A @ vector  # Multiplicación de matriz-vector usando el operador @
        eigen_value = vector.max()  # Usamos el valor máximo del vector para estimar el eigenvalor
        vector = vector / eigen_value
        
    return eigen_value, vector

eigenvalue, eigenvector = metodo_potencia(a, iteraciones=100)
print("EigenValue:", eigenvalue/3)
print("Eigenvector:", eigenvector)








