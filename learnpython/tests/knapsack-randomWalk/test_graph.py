import os
import sys
import os

sys.path.append(os.path.abspath('./learnpython/knapsack-randomWalk'))
print("FOUND THIS PATH" + str(sys.path))

import graph 
import DFS

def test_create_a_graph():
    A = graph.Node("A")
    B = graph.Node("B")
    C = graph.Node("C")
    D = graph.Node("D")
    E = graph.Node("E")

    AB = graph.WeightedEdge(A, B, 1)
    BC = graph.WeightedEdge(B, C, 3)
    BD = graph.WeightedEdge(B, D, 2)
    CD = graph.WeightedEdge(C, D, 4)
    DE = graph.WeightedEdge(D, E, 5)
    AE = graph.WeightedEdge(A, E, 6)

    nw_graph = graph.Graph()

    nw_graph.addNode(A)
    nw_graph.addNode(B)
    nw_graph.addNode(C)
    nw_graph.addNode(D)
    nw_graph.addNode(E)


    nw_graph.addEdge(AB)
    nw_graph.addEdge(BC)
    nw_graph.addEdge(BD)
    nw_graph.addEdge(CD)
    nw_graph.addEdge(DE)
    nw_graph.addEdge(AE)
    
    shortestPath = DFS.shortestPath(nw_graph, A, D, True)
    assert DFS.printPath(shortestPath) == "A->E->D"
    

def test_print_a_apth():
    path = ['A', 'B', 'D', 'F']
    assert DFS.printPath(path) == "A->B->D->F"