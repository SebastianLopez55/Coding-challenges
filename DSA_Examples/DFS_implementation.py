def make_adj_list(n, edge_list):
    """
    args:
        n:int = number of nodes in the graph. The nodes are labelled with integers 0 through n-1
        edge_list:List[Tuple(int,int)] = edge list where each tuple (u,v) represents the undirected
            edge (u,v) in the graph
    return:
        A List[List[int]] representing the adjacency list
    """
    # using a list of lists
    adj_listTemplate = [[] for i in range(0, n)]
    for edge in edge_list:
        adj_listTemplate[edge[0]].append(edge[1])  # need to include both directions for the edge
        adj_listTemplate[edge[1]].append(edge[0])
    return adj_listTemplate


def dfs_path(adj_list, s, t):
    """
    args:
        adj_list:List[List] = an adjacency list
        s:int = an int representing the starting node
        t:int = an int representing the destination node

    return:
        a list of nodes starting with s and ending with t representing an s to t path if it exists.
        Returns an empty list otherwise
    """

    path = []
    visited = len(adj_list) * [False]

    # Helper function
    def explore(v: int):
        """
        Description:
            explore() find all the vertices reached from vertex v

        Args:
            G:dict = List[List] representing a graph G.
            v:int = int representing a vertex of graph G.

        return:
            Set to true all the visited nodes u reached from v.
        """
        visited[v] = True
        path.append(v)
        for vertex in adj_list[v]:
            if not visited[vertex]:
                # Explore adjacent vertices
                explore(vertex)

    # Iterate over all vertices
    for v in range(len(adj_list)):
        if not visited[v]:
            # Iterate over all edges coming from vertex v
            explore(v)
    return path


# Drivers
edge_list = [(0, 1), (1, 2), (1, 3)]
n = len(edge_list) + 1
adj_list = make_adj_list(n, edge_list)

print(dfs_path(adj_list, 0, 0))
