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


 # 16
def plot_julia(c, xlim, ylim, width, height, max_iter, cmap='hot', save_path=None):

    julia_img = julia_set(c, xlim, ylim, width, height, max_iter)

    plt.imshow(julia_img, extent=(xlim[0], xlim[1], ylim[0], ylim[1]), cmap=cmap)

    plt.colorbar()

    plt.title(f'Julia Set for c = {c}')

    if save_path:

        plt.savefig(save_path)

    plt.show()



# Parameters

c = complex(-0.7, 0.27015)  # Change this for different Julia sets

xlim = (-1.5, 1.5)

ylim = (-1.5, 1.5)

width, height = 800, 800

max_iter = 256



# Plot the Julia set with custom parameters

plot_julia(c, xlim, ylim, width, height, max_iter, cmap='plasma', save_path='julia_set.png')



