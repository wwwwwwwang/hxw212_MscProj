from pylab import *
import networkx as nx
g=nx.Graph()
g.add_edge(u'张三',u'李四')
g.add_edge(u'张三',u'王五')
nx.draw(g)
plt.show()