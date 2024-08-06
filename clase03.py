# Curso de Python: NumPy y Pandas para Análisis de Datos

# Dimensiones en NumPy y Pandas: De Escalares a Tensors

!pip install numpy pandas

import numpy as np
escalar = np.array(42)
print (type(escalar))
print(escalar)

<class 'numpy.ndarray'>
42

vector = np.array([30,29,42,35,31,33,36,42])
print(vector)

[30 29 42 35 31 33 36 42]

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)

tensor = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(tensor)

[[[1 2]
  [3 4]
  [5 6]
  [7 8]]]

array_arange =  np.arange(10)
print(array_arange)

[0 1 2 3 4 5 6 7 8 9]

eye_matrix = np.eye(6)
print(eye_matrix)

diag = np.diag([1,2,3,4,5,6,7])
print(diag)

[[1 0 0 0 0 0 0]
 [0 2 0 0 0 0 0]
 [0 0 3 0 0 0 0]
 [0 0 0 4 0 0 0]
 [0 0 0 0 5 0 0]
 [0 0 0 0 0 6 0]
 [0 0 0 0 0 0 7]]

random =  np.random.random((2,3))
print(random)

[[0.30666714 0.91079815 0.76189985]
 [0.1764467  0.12179611 0.74883962]]