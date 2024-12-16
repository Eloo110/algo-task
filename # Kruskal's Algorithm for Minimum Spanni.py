# Kruskal's Algorithm for Minimum Spanning Tree in Python

class DisjointSet:
    """
    Disjoint Set Union (DSU) or Union-Find data structure.
    Helps to manage and merge connected components.
    """
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # Parent array
        self.rank = [0] * n  # Rank array

    def find(self, u):
        """
        Finds the root of the set containing u using path compression.
        :param u: Node
        :return: Root of the set
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        """
        Unites two sets containing u and v.
        :param u: Node
        :param v: Node
        """
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Attach smaller rank tree under root of higher rank tree
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph, n):
    """
    Implements Kruskal's Algorithm to find MST.
    :param graph: List of edges (u, v, weight)
    :param n: Number of nodes
    :return: List of edges in the MST
    """
    edges = sorted(graph, key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(n)
    mst = []  # Store edges of the MST

    for edge in edges:
        u, v, weight = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append(edge)

    return mst

if name == "__main__":
    # Example usage
    graph = [
        (0, 1, 10),  # Edge from 0 to 1 with weight 10
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    n = 4  # Number of nodes
    mst = kruskal(graph, n)
    print("Edges in MST:", mst)