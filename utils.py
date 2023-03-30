import numpy as np
norm = lambda v: (sum(v**2))**0.5
sigmoid = lambda X, t: 1 / (1 + np.exp(-(X @ t)))
cost = lambda X, y, t: ((sigmoid(X, t) - y) ** 2).sum() / len(y)
grad = lambda X, y, t: 2 * X.T @ (X @ t - y) / len(y)

def linear_regression(X, y, t, cost, grad, a=0.1, n=1000, on_step=None): # n = 10000
    costs = []
    for i in range(n):
        nabla = grad(X, y, t)
        t -= a * grad(X, y, t)
        costs.append(cost(X, y, t))
        if on_step:
            on_step(t)
    return t, costs

