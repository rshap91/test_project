import sys
import numpy as np


def sum_random(n):
  nums = np.random.randint(0,100,n)
  return np.sum(nums)

if __name__ == '__main__':
  n = sys.argv[1]
  print(sum_random(n))
