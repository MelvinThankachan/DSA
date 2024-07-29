class Node:
    def __init__(self, label):
        self.value = label

    def __str__(self):
        return f"{self.value}"


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __str__(self):
        return f"{self.from_node.value} -> {self.to_node.value}"


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
    
    def add_node(self, label):
        if label in self.nodes:
            return
        new_node = Node(label)
        self.nodes[label] = new_node
        self.edges[new_node] = []
    
    def add_edge(self, label1, label2, weight):
        node1 = self.nodes.get(label1)
        node2 = self.nodes.get(label2)
        if node1 is None or node2 is None:
            raise ValueError("Node not found")
        edge = Edge(node1, node2, weight)
        reverse_edge = Edge(node2, node1, weight)
        self.edges[node1].append(edge)
        self.edges[node2].append(reverse_edge)

    def remove_node(self, label):
        pass

    def remove_edge(self, label1, label2):
        pass