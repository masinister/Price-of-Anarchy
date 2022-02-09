import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from graphs import add_kleinberg_edges
from networkx.algorithms.approximation import k_components

g = nx.grid_graph(dim=(4,4))
add_kleinberg_edges(g, q=1, r=1)
print(k_components(g))
nx.draw(g)
plt.show()
