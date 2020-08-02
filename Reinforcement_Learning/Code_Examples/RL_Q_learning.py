#QLearning Example through text
#Beautiful Soup


import numpy as np
import pylab as plt
import networkx as nx

points_list = [(0,1), (1,5), (5,6), (5,4), (1,2), (2,3), (2,7)]

#Title
goal = 7

G = nx.Graph()

G.add_edges_from(points_list)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G,pos)



Matrix_size = 8
R = np.matrix(np.ones(shape=(Matrix_size, Matrix_size)))
R *= -1

plt.show()
