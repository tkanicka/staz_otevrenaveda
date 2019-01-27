import numpy
import random

data = numpy.zeros((10000, 3))

for k in range(10000):
    data[k][0] = random.random()
    data[k][1] = (data[k][0])**2
    data[k][2] = data[k][1] / 10**4

print(data)

numpy.savetxt("variance_data.csv", data, delimiter=", ", header="random numbers, square, square/N")

x = 0
for i in range(1, 10001):
    n = (i/10000)**2
    x += n

x = x/10000
print("area under the parabolic curve: ", x)

p = 0
for y in range(10**4):
    n = data[y][2]
    p += n

print("average value from the squares of generated random numbers: ", p,)
print("approximately 1/3")
