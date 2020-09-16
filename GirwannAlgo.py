import networkx as nx
def edge_to_remove(g):
  d1 = nx.edge_betweenness_centrality(g)
  list_of_tuples = d1.items()
  list_of_tuples.sort(key = lambda x:x[1], reverse = True)
  #Will return in the form (a,b)
  return list_of_tuples[0][0]
def girvan(g):
  a = nx.connected_component_subgraphs(g)
  lena = len(a)
  print (' The number of connected components are ', lena)
  while (lena == 1):
   g.remove_edge(edge_to_remove(g)) # We need (a,b) instead of ((a,b))
   a = nx.connected_component_subgraphs(g)
   lena=len(a)
   print (' The number of connected components are ', lena)
  return a
g = nx.barbell_graph(5,0)
a = girvan(g)
print ('Barbell Graph')
for i in a:
  print (i.nodes())
  print ('.............')
g1 = nx.karate_club_graph()
a1 = girvan(g1)
print ('Karate Club Graph')
for i in a1:
  print (i.nodes())
  print ('.............')