import numpy as np
import matplotlib.pyplot as plt

def julia_set(c, xlim, ylim, width, height, max_iter):
    x = np.linspace(xlim[0], xlim[1], width)
    y = np.linspace(ylim[0], ylim[1], height)
    Z = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)
    Z = Z[:, 0] + 1j * Z[:, 1]
    
    img = np.zeros(Z.shape, dtype=int)
    for i in range(max_iter):
        mask = np.abs(Z) < 1000
        img[mask] = i
        Z[mask] = Z[mask] ** 2 + c

    return img.reshape(height, width)

