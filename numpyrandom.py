import numpy as np

rng = np.random.default_rng()  #if you want to set seed just put seed=1 in the brackets.

print(rng.integers(1,10))
print(rng.integers(low=1, high=100, size=(3,2)))


print(np.random.randint(1,10))
print(np.random.uniform(1,10,size=3)) #Does the same thing but will take floats that is decimals as well.


array = np.array([[1,2,3],[4,5,6],[7,8,9]])
rng.shuffle(array)
print(array)


fruits = np.array(['apple','banana','cherry','kiwi','mango'])
fruit = rng.choice(fruits, size=(3,2))
print(fruit)