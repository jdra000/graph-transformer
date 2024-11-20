'''
This tool is intended to help with the creation and representation of
weighted and unweighted graphs. 
Type of representation: Adjacency List.
'''

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
  
  def add_node(self, tail, head, weight = None):
    if self.prop1 == 'weighted':
      self.representation.setdefault(tail, {})[head] = weight

      if self.prop2 == "undirected":
        self.representation.setdefault(head, {})[tail] = weight

    else:
      self.representation.setdefault(tail, []).append(head)

      if self.prop2 == "undirected":
        self.representation.setdefault(head, []).append(tail)


g = Graph('unweighted', 'directed')
g.add_node('A', 'B', 5)
g.add_node('A', 'C', 3)
g.add_node('C', 'B', 3)
print(dict(g.representation))
  