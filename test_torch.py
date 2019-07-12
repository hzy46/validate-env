import torch
import torch.nn as nn
import torch.nn.functional as F

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

print('use device:')
print(device)

a = torch.randn(2, 2).to(device)
b = torch.randn(2, 2).to(device)
c = a + b
print(c)
print(F.relu(c))