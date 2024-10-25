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
        sierpinski_triangle(order - 1, [midpoints[2], midpoints[1], vertices[2]], color)

