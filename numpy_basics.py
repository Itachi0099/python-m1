import numpy as np
arr = [
    (1,2,3)
    , (4,5,6)
] 
#add 5 to every element multiply by 2
result = (np.array(arr) + 5) * 2
print(result)

mean = np.mean(result)
print("Mean of the resulting array:", mean)

max_value = np.max(result)
print("Max value of the resulting array:", max_value)

min_value = np.min(result)
print("Min value of the resulting array:", min_value)

#indexing and slicing
print("Element at row 1, column 2:", result[1,2])
print("First row:", result[0, :])
print("Second column:", result[:, 1]) 