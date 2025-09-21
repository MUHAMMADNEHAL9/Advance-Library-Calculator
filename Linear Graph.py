import numpy as np
import matplotlib.pyplot as lpt

def linear_to_graph(b, m):

    x = np.linspace(-10, 100, 400)


    y = b * x + m


    lpt.plot(x, y)

    lpt.show()


linear_to_graph(2, 5)
