import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])

print(x, "\n", "The mean of x:", np.mean(x), "\n",
      "The mean of x at axis 0 is:", np.mean(x, axis=0), "\n",
      "The mean of x at axis 1 is:", np.mean(x, axis=1), "\n",
      "The mean of x at axis -1 is:", np.mean(x, axis=-1))

print("The shape of mean of x with no axis set:", np.mean(x).shape, "\n",
      "The shape of mean of x at axis 0 is:", np.mean(x, axis=0).shape, "\n",
      "The shape of mean of x at axis 1 is:", np.mean(x, axis=1).shape, "\n",
      "The shape of mean of x at axis -1 is:", np.mean(x, axis=-1).shape)
