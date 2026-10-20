import numpy as np

array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                  [[10, 11, 12], [13, 14, 15], [16, 17, 18]], 
                  [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])


print(np.shape(array))
print(array.ndim)


print(array[0,1,0])
print(array[1:2:2])
print(array[0:2,0:2])

array1 =np.array([1.01, 2.02, 3.03, 4.04, 5.05])
print(array1 * 3)
print(np.sqrt(array1))
print(np.floor(array1))


scores = np.array([91,55, 82, 75, 99])

scores[scores >= 80] = 100
scores[scores < 80] = 0
print(scores)

print(np.mean(scores))
print(np.median(scores))
print(np.std(scores))
print(np.var(scores))
print(np.min(scores))
print(np.max(scores))
print(np.argmin(scores))
print(np.argmax(scores))


numbers = np.array([[1, 2, 3, 4, 5], 
                    [6, 7, 8, 9, 10]])

print(np.sum(numbers , axis=0)) #sums all numbers on the same colum that is axis=0.
print(np.sum(numbers , axis=1)) #sums all numbers on the same row that is axis=1.
