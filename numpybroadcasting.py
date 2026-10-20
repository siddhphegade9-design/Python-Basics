import numpy as np


array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])
print(array1*array2)
#Just like Matrx miltiplication, the coun of columns in the first array must be equal to the number of rows in the second array. Or else it will throw and error.


ages = np.array([[21,17,19,20,101,18,22,23,99,25],
                 [20,21,87,23,67,25,95,27,28,29]])

teenagers = ages[ages>=18]
print(teenagers)

adults = ages[(ages>=21) | (ages<=25)]
print(adults)


seniors = np.where(ages>=65 ,ages,0)
print(seniors)


