import matplotlib.pyplot as plt

import numpy as np



def sierpinski_triangle(order, vertices, color='b'):

    if order == 0:

        triangle = np.array(vertices)

        plt.fill(triangle[:, 0], triangle[:, 1], color)

    else:

        midpoints = [

            (vertices[0] + vertices[1]) / 2,

            (vertices[1] + vertices[2]) / 2,

            (vertices[2] + vertices[0]) / 2

        ]

        sierpinski_triangle(order - 1, [vertices[0], midpoints[0], midpoints[2]], color)

        sierpinski_triangle(order - 1, [midpoints[0], vertices[1], midpoints[1]], color)
 # HACK!
        sierpinski_triangle(order - 1, [midpoints[2], midpoints[1], vertices[2]], color)



def plot_sierpinski(order, vertices, color='b', save_path=None):

    plt.figure(figsize=(8, 8))

    sierpinski_triangle(order, vertices, color)

    plt.title(f'Sierpinski Triangle of Order {order}')

    plt.axis('equal')

    plt.axis('off')

    if save_path:

        plt.savefig(save_path)

    plt.show()



# Parameters

order = 5  # Change this for different levels of detail

vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])



# Plot the Sierpinski triangle with custom parameters

plot_sierpinski(order, vertices, color='cyan', save_path='sierpinski_triangle.png')

import matplotlib.pyplot as plt

import numpy as np



def sierpinski_triangle(order, vertices, color='b'):

    if order == 0:

        triangle = np.array(vertices)

        plt.fill(triangle[:, 0], triangle[:, 1], color)

    else:

        midpoints = [
 # 41
            (vertices[0] + vertices[1]) / 2,

            (vertices[1] + vertices[2]) / 2,

            (vertices[2] + vertices[0]) / 2

        ]

        sierpinski_triangle(order - 1, [vertices[0], midpoints[0], midpoints[2]], color)

        sierpinski_triangle(order - 1, [midpoints[0], vertices[1], midpoints[1]], color)

        sierpinski_triangle(order - 1, [midpoints[2], midpoints[1], vertices[2]], color)



def plot_sierpinski(order, vertices, color='b', save_path=None):

    plt.figure(figsize=(8, 8))

    sierpinski_triangle(order, vertices, color)

    plt.title(f'Sierpinski Triangle of Order {order}')

    plt.axis('equal')

    plt.axis('off')

    if save_path:

        plt.savefig(save_path)

    plt.show()



# Parameters

order = 5  # Change this for different levels of detail

vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])



# Plot the Sierpinski triangle with custom parameters

plot_sierpinski(order, vertices, color='cyan', save_path='sierpinski_triangle.png')



