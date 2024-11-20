'''
This tool is intended to help with the creation and representation of
weighted and unweighted graphs. 
Types of representation: Adjacency List, Adjacency Matrix
'''

# UNWEIGHTED
# 1. Adjacency List
'''
{
    'A': ['B', 'C'],
    'B': ['C'],
    'C': []
}
'''
# 2. Adjacency Matrix
'''
  A  B  C
[ 0, 1, 1 ]
[ 0, 0, 1 ]
[ 0, 0, 0 ]
'''
# WEIGHTED
# 1. Adjacency List
'''
{
    'A': {'B': 4, 'C': 2},
    'B': ['C': 6],
    'C': []
}
'''
# 2. Adjacency Matrix
'''
  A  B  C
[ 0, 4, 2 ]
[ 0, 0, 6 ]
[ 0, 0, 0 ]
'''
