import numpy as np 
# ------------------------- 
# 1. Array Creation 
# ------------------------- 
# From list 
arr1 = np.array([1, 2, 3, 4, 5]) 
print("Array from list:", arr1) 
# From nested list (matrix) 
arr2 = np.array([[1,2,3],[4,5,6]]) 
print("2D Array:\n", arr2) 
# Using arange, linspace, zeros, ones, eye 
arr_arange = np.arange(0, 10, 2) 
print("arange array:", arr_arange) 
arr_linspace = np.linspace(0, 1, 5) 
print("linspace array:", arr_linspace) 
arr_zeros = np.zeros((2,3)) 
print("zeros array:\n", arr_zeros) 
arr_ones = np.ones((3,2)) 
print("ones array:\n", arr_ones) 
arr_eye = np.eye(3) 
print("Identity matrix:\n", arr_eye) 

# ------------------------- 
# 2. Array Attributes 
# ------------------------- 
print("Shape of arr2:", arr2.shape) 
print("Size of arr2:", arr2.size) 
print("Number of dimensions:", arr2.ndim) 
print("Data type:", arr2.dtype) 
print("Item size (bytes):", arr2.itemsize) 

# ------------------------- 
# 3. Indexing and Slicing 
# ------------------------- 
arr = np.array([10, 20, 30, 40, 50]) 
print("Original array:", arr) 
print("Index 2:", arr[2]) 
print("Last element:", arr[-1]) 
print("Slice 1:4:", arr[1:4])

# 2D array slicing 
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print("2D array:\n", arr2d) 
print("First row:", arr2d[0,:]) 
print("Second column:", arr2d[:,1]) 
print("Submatrix:\n", arr2d[0:2,1:3]) 

# ------------------------- 
# 4. Basic Operations 
# ------------------------- 
a = np.array([1,2,3]) 
b = np.array([4,5,6])

print("a + b:", a + b) 
print("a - b:", a - b) 
print("a * b:", a * b) 
print("a / b:", a / b) 
print("a ** 2:", a**2) 
# Broadcasting 
c = np.array([[1,2,3],[4,5,6]]) 
d = np.array([1,1,1]) 
print("Broadcasting sum:\n", c + d) 

# ------------------------- 
# 5. Universal Functions (ufuncs) 
# ------------------------- 
arr = np.array([1,4,9,16]) 
print("sqrt:", np.sqrt(arr)) 
print("exp:", np.exp(arr)) 
print("log:", np.log(arr)) 
print("sin:", np.sin(arr)) 
print("cos:", np.cos(arr)) 

# ------------------------- 
# 6. Aggregation Functions 
# ------------------------- 
arr = np.array([[1,2,3],[4,5,6]]) 
print("Sum:", np.sum(arr)) 
print("Sum axis 0:", np.sum(arr, axis=0)) 
print("Sum axis 1:", np.sum(arr, axis=1)) 
print("Mean:", np.mean(arr)) 
print("Max:", np.max(arr))
print("Min:", np.min(arr)) 
print("Argmax:", np.argmax(arr)) 
print("Argmin:", np.argmin(arr)) 
print("Standard deviation:", np.std(arr)) 
print("Variance:", np.var(arr)) 

# ------------------------- 
# 7. Reshaping and Flattening 
# ------------------------- 
arr = np.arange(12) 
print("Original array:", arr) 
arr_reshaped = arr.reshape(3,4) 
print("Reshaped 3x4 array:\n", arr_reshaped) 
arr_flat = arr_reshaped.flatten() 
print("Flattened array:", arr_flat) 
arr_transpose = arr_reshaped.T 
print("Transpose:\n", arr_transpose)

# ------------------------- 
# 8. Stacking and Splitting 
# ------------------------- 
a = np.array([1,2,3]) 
b = np.array([4,5,6]) 
print("Horizontal stack:", np.hstack((a,b))) 
print("Vertical stack:\n", np.vstack((a,b))) 
arr = np.arange(9) 
print("Original array:", arr) 
print("Split into 3 parts:", np.split(arr, 3)) 

# ------------------------- 
# 9. Copy vs View 
# ------------------------- 
arr = np.array([1,2,3,4]) 
arr_view = arr.view() 
arr_copy = arr.copy() 
arr_view[0] = 100 
arr_copy[1] = 200 
print("Original after view change:", arr) 
print("Original after copy change:", arr) 
# ------------------------- 
# 10. Boolean Indexing & Fancy Indexing 
# ------------------------- 
arr = np.array([10,20,30,40,50]) 
print("Elements > 25:", arr[arr>25]) 
indices = [0,2,4] 
print("Fancy indexing:", arr[indices]) 

# ------------------------- 
# 11. Random Numbers 
# ------------------------- 
rand_arr = np.random.rand(3,3)  # uniform [0,1) 
print("Random array:\n", rand_arr) 
rand_int = np.random.randint(0,10,5) 
print("Random integers:", rand_int) 
normal_arr = np.random.randn(3,3)  # standard normal 
print("Normal distribution array:\n", normal_arr) 

# -------------------------
# 12. Linear Algebra Functions 
# ------------------------- 
A = np.array([[1,2],[3,4]]) 
B = np.array([[5,6],[7,8]]) 
print("Matrix multiplication:\n", np.dot(A,B)) 
print("Matrix determinant:", np.linalg.det(A)) 
print("Matrix inverse:\n", np.linalg.inv(A)) 
print("Eigenvalues and Eigenvectors:\n", np.linalg.eig(A)) 

# ------------------------- 
# 13. Saving and Loading Arrays 
# ------------------------- 
np.save('array.npy', arr) 
loaded_arr = np.load('array.npy') 
print("Loaded array:", loaded_arr) 
print("\nAll major NumPy functions executed successfully!")