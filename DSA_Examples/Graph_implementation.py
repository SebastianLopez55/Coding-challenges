"""
Implementations:
    1) Adjacency list: list of list
    2) Adjacency list: set inside hashMap

"""


# ***********************************************
# 1) Adjacency list: list of list
# ***********************************************
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
    adj_list = [[] for i in range(0, n)]
    for edge in edge_list:
        adj_list[edge[0]].append(edge[1])  # need to include both directions for the edge
        adj_list[edge[1]].append(edge[0])
    return adj_list


"""
Drivers:
"""

# Edge declaration
E = [(0, 1), (1, 2), (1, 3)]
# Vertex declaration: There are 4 nodes in this graph
V = len(E) + 1
# For example, graph will be represented: node zero/index zero to node one/index one: (0)-(1)
print(f'\nAdj list implementation of unweighted undirected graph using lists of lists: {make_adj_list(V, E)}')


# ***********************************************
# 2) Adjacency list: set inside hashMap
# ***********************************************


# Helper funcition: data parsing for dictionary
def parseData(vals: dict) -> list:
    # Declare a list to store data processed
    processed = []
    for key in vals.keys():
        value = vals[key]
        # iterate over values for parsing
        i = 0
        while i < len(value):
            character = value[i]
            if character == "$":
                # pointer to start next to $
                j = i + 1
                target_string = ""
                while j < len(value) and value[j] != "$":
                    target_string += value[j]
                    j += 1
                # Append target string to processed values
                processed.append(target_string)
                # Set current index after target_string
                i = j + 1
            i = i + 1
    return processed



# def make_adj_listSet(dataDict: dict) -> dict:
#     # Declare the adj list: dict
#     adj = {}
#     for key in dataDict.keys():
#         # Create corresponding set for each
#         if key not in adj:
#             adj[key] = set()
#         # Get all references from parent node
#         parentNode = get_refs()
#
#



"""
Drivers:
"""

valuesDict = {
    'USER': 'ANA',
    'ARC': 'x64',
    'OS': 'OSX',
    'DIR': 'home/$USER$',
    'SYSTEM': '$ARC$.BIT.$OS$@$DIR$',
    'NETWORK': '$USER$:$SYSTEM$'
}

print(parseData(valuesDict))

