import numpy as np
import torch


np.random.seed(42)
a = np.random.rand(4,3)
print(a)
print()

b = torch.tensor(a, dtype= torch.float32)
print(b)

np.save('resutls.npy', b)
