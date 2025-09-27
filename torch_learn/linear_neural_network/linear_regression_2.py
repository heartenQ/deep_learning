import torch


X = torch.arange(12, dtype=torch.float32).reshape((-1, 4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
cat_0 = torch.cat((X, Y), dim=0)
cat_1 = torch.cat((X, Y), dim=1)
print(X)
print(cat_0)
print(cat_1)
print(X == Y)
print(X.sum())
