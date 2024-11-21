# VISUALIZATION EXAMPLE
# UNWEIGHTED
'''
{
    'A': ['B', 'C'],
    'B': ['C'],
    'C': []
}
'''

# WEIGHTED
'''
{
    'A': {'B': 4, 'C': 2},
    'B': ['C': 6],
    'C': []
}
'''
class Graph():
  # prop1 : weighted, unweighted
  # prop2 : directed, undirected
  def __init__(self, prop1, prop2):
    self.prop1 = prop1
    self.prop2 = prop2
    self.representation ={}
  
  def add_nodes(self, nodes):
    for node in nodes:
      if self.prop1 == 'weighted':
        self.representation[node] = {}
      else:
        self.representation[node] = []
     
  def add_edge(self, tail, head, weight = None):
    if self.prop1 == 'weighted':
      self.representation[tail][head] = weight

      if self.prop2 == "undirected":
        self.representation[head][tail] = weight

    else:
      self.representation[tail].append(head)

      if self.prop2 == "undirected":
        self.representation[head].append(tail)

  def __repr__(self):
        return str(self.representation)
  
# EXAMPLE OF USAGE
g = Graph('weighted', 'directed')
g.add_nodes(['A', 'B', 'C', 'D'])
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 3)
g.add_edge('C', 'D', 5)
print(g)