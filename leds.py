import sys
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
from matplotlib import cm
from matplotlib import animation

fig, ax = plt.subplots()
ax.set_xlim([-50, 400])
ax.set_ylim([0, 20])
ax.set_aspect('equal', 'box')
ax.axis('off')

leds = [
        ((0,10),    0b10000000),
        ((50,10),   0b01000000),
        ((100,10),  0b00100000),
        ((150,10),  0b00010000),
        ((200,10),  0b00001000),
        ((250,10),  0b00000100),
        ((300,10),  0b00000010),
        ((350,10),  0b00000001),
]

patches = []
for pos, mask in leds:
    circle = Circle(pos, 10)
    patches.append(circle)

p = PatchCollection(patches, cmap=cm.ocean, alpha=1, match_original=True)
p.set_clim([0, 1])
ax.add_collection(p)

def animate(from_stdin):
    try:
        byte = int(from_stdin,2)
    except ValueError:
        print("Error. Not a binary number")
        sys.exit(1)

    colors = [0 if byte & int(mask) else 1 for pos, mask in leds ]

    p.set_array(np.array(colors))
    return p,

def data_gen():
    while True:
        line = fd.readline().strip()
        if line:
            yield line

fd = sys.stdin
ani = animation.FuncAnimation(fig, animate, frames=data_gen, repeat=False, interval=10)
plt.show()
