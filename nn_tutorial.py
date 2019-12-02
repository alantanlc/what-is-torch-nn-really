# MNIST data setup
from pathlib import Path
import requests

DATA_PATH = Path("data")
PATH = DATA_PATH / "mnist"

PATH.mkdir(parents=True, exist_ok=True)

URL = "http://deeplearning.net/data/mnist"
FILENAME = "mnist.pkl.gz"

if not (PATH / FILENAME).exists():
    content = requests.get(URL + FILENAME).content
    (PATH / FILENAME).open("wb").write(content)

# Load data in pickle file
import pickle
import gzip

with gzip.open((PATH / FILENAME).as_posix(), "rb") as f:
    ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding="latin-1")

# Convert data from numpy to torch.tensor
import torch

x_train, y_train, x_valid, y_valid = map(
    torch.tensor, (x_train, y_train, x_valid, y_valid)
)

# Initialize weights with Xavier initialisation (by multiplying with 1/sqrt(n))
# For the weights, we set requires_grad after the initialization, since we don't want that step included in the gradient. (Note that a trailing _ in PyTorch signifies that the operation is performed in-place).
import math

weights = torch.randn(784, 10) / math.sqrt(784)
weights.requires_grad_()
bias = torch.zeros(10, requires_grad=True)

# Log softmax
def log_softmax(x):
    return x - x.exp().sum(-1).log().unsqueeze(-1)

# A simple linear model that performs a plain matrix multiplication and broadcasted addition and a log_softmax activation function
# @ stands for the dot product operation
def model(xb):
    return log_softmax(xb @ weights + bias)

# Forward pass
bs = 64 # batch size
xb = x_train[0:bs]  # a mini-batch from x
preds = model(xb)
print(preds[0], preds.shape)

# Negative log-likelihood as a loss function
def nll(input, target):
    return -input[range(target.shape[0]), target].mean()
yb = y_train[0:bs]
loss_func = nll
print(loss_func(preds, yb))

# Accuracy
def accuracy(out, yb):
    preds = torch.argmax(out, dim=1)
    return (preds == yb).float().mean()