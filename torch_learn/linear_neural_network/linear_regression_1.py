import torch

x = torch.arange(12)
X = x.reshape(3, 4)
zero = torch.zeros(3, 4)
ones = torch.ones(2, 3, 4)
random = torch.randn(3, 4)
custom_torch = torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(x)
print(X)
print(zero)
print(ones)
print(random)
print(custom_torch)
