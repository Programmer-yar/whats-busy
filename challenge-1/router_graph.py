class Node():
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge():
    def __init__(self, node_from, node_to):
        self.node_from = node_from
        self.node_to = node_to


class Graph():
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node

        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def identify_routers(self):
        node_dict = dict() # 1 time
        for node in self.nodes: # n times
            node_dict[node.value] = len(node.edges) # n times
        all_values = list(node_dict.values())   # n times
        all_keys = list(node_dict.keys())   # n times
        max_val = max(all_values)   # n times
        max_indices = list()    # 1 time
        for index, value in enumerate(all_values):  # n times
            if value == max_val:    # n times
                max_indices.append(index)   # n times
        routers = [all_keys[index] for index in max_indices]    # n times
        return routers  # 1 time

# 2 -> 4 -> 6 -> 2 -> 5 -> 6 = 2, 6
graph_1 = Graph()
graph_1.insert_edge(2, 4)
graph_1.insert_edge(4, 6)
graph_1.insert_edge(6, 2)
graph_1.insert_edge(2, 5)
graph_1.insert_edge(5, 6)

print(graph_1.identify_routers())

# O(9n + 2) approximates to O(n)
