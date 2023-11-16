import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

n = int(input("Enter Number of Element x: "))

for i in range(n):
    eleX = int(input())

    x.append(eleX)

nY = int(input("Enter number of Element y: "))

for i in range(nY):
    eleY = int(input())

    y.append(eleY)

plt.title("plotting")
plt.xlabel("asd")
plt.ylabel("zxc")
plt.bar(x, y)
plt.grid()
plt.show()
