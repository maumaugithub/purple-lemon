# Adjacency List in Python
# graph = {'A': set(['B', 'C']),
        #  'B': set(['A', 'D', 'E']),
        #  'C': set(['A', 'F']),
        #  'D': set(['B']),
        #  'E': set(['B', 'F']),
        #  'F': set(['C', 'E'])}

class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num_vertices):
        self.vertices = num_vertices
        self.graph = [None] * self.vertices

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_adj_ls_graph(self):
        for i in range(self.vertices):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


# Number of vertices
num_vertices = 4

# Create graph and edges
graph = Graph(num_vertices)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)

graph.print_adj_ls_graph()