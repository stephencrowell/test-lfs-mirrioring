import numpy as np

# test = np.ones((1000, 1000))

# np.save("./data/ones.npy", test)

print(np.load("./data/ones.npy").size)