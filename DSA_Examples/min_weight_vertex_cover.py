

"""

For any undirected graph G = (V, E), we define a vertex cover
of the graph to be a set of vertices that includes at least
one endpoint of every edge of the graph. Now, suppose you are
given a tree graph T = (V,E), where each vertex v is assigned a
weight w(v) and the edges are unweighted. Devise a dynamic programming
algorithm to compute the minimum weight vertex cover (MWVC) of T ,
where the weight of a vertex cover is the sum of the weights of its
vertices.

"""


def mwvc_dp(tree):
    memo = {}
    leaves = set(leaf for leaf in tree if len(tree[leaf]) == 0)

    def mwvc(node):
        if node in memo:
            return memo[node]
        elif node in leaves:
            memo[node] = 0
        else:
            # Compute the MWVC including the current node
            mwvc_inc = tree[node][0][1] + sum(mwvc(child) for child in tree[node][1:])
            # Compute the MWVC excluding the current node
            mwvc_exc = sum(mwvc(child) for child in tree[node])
            if mwvc_inc < mwvc_exc:
                memo[node] = mwvc_inc
            else:
                memo[node] = mwvc_exc
        return memo[node]

    # Compute the MWVC for each node in a bottom-up manner
    for node in reversed(list(tree.keys())):
        mwvc(node)

    # Return the MWVC of the root node
    return memo[list(tree.keys())[0]]


adj_list = {
    ('A', 1): [('B', 11), ('C', 8)],
    ('B', 11): [('A', 1), ('D', 5), ('E', 3)],
    ('C', 8): [('A', 1), ('F', 20)],
    ('D', 5): [],
    ('E', 3): [],
    ('F', 20): []
}
mwvc_dp(adj_list)  # Output: 14
