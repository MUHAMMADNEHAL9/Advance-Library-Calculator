import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def draw_Rectangle(width, height , color='yellow'):

  fig, ax = plt.subplots()

  rectangle =  Rectangle((0.5 , 0.3), height,width, edgecolor=color , facecolor="blue", linewidth=4)

  ax.add_patch(rectangle)

  ax.set_aspect('equal')
  ax.set_xlim(0, 1)
  ax.set_ylim(0, 1)

  plt.title(f"Rectanle with heigth = {height} and with width {width}")
  plt.grid(True)
  plt.show()

width = float(input("Enter a width"))
height = float(input("Enetr a height"))
draw_Rectangle(width , height)
