# challenge 1

import numpy as py
from numpy import *
import matplotlib.pyplot as plt

numbers = py.arange(0, 20)
print(numbers)

std = std(numbers)
mean = mean(numbers)
variance = var(numbers)


print(std)
print(mean)
print(variance)

# challenge 2

bins = [0, 1, 2, 3, 4]
nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]

print("nums: {}".format(nums))
print("bins: {}".format(bins))
print("Result: {}".format(histogram(nums, bins)))

plt.title("Histogram of numbers agains bins")
plt.xlabel("numbers")
plt.ylabel("bins")
plt.hist(nums, bins)
plt.show()

