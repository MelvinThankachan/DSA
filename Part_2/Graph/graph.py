class Graph:
    class Node:
        def __init__(self, label):
            self.label = label

        def __str__(self):
            return self.label

    def __init__(self):
        self.nodes = {}
        self.adjacency_list = {}

    def add_node(self, label):
        if label not in self.nodes:
            node = self.Node(label)
            self.nodes[label] = node
            self.adjacency_list[node] = []

    def add_edge(self, from_label, to_label):
        from_node = self.nodes.get(from_label)
        if from_node is None:
            raise ValueError

        to_node = self.nodes.get(to_label)
        if to_node is None:
            raise ValueError

        self.adjacency_list[from_node].append(to_node)

    def print_graph(self):
        for from_node in self.adjacency_list.keys():
            edges = self.adjacency_list[from_node]
            if len(edges) > 0:
                print(f"{from_node} is connected to {[str(edge) for edge in edges]}")

    def remove_node(self, label):
        node = self.nodes.get(label)
        if node is None:
            return
        # Removing all edges from other nodes
        for from_node in self.adjacency_list.keys():
            if node in self.adjacency_list[from_node]:
                self.adjacency_list[from_node].remove(node)
        # Removing the node from Adjacency list
        self.adjacency_list.pop(node)
        # Removing from the nodes
        self.nodes.pop(label)

    def remove_edge(self, from_label, to_label):
        from_node = self.nodes.get(from_label)
        to_node = self.nodes.get(to_label)
        if from_node is None or to_node is None:
            return
        self.adjacency_list[from_node].remove(to_node)

    def df_traversal(self, label):
        def dft(root):
            if root not in visited:
                result.append(root.label)
            visited.add(root)
            adjacent_nodes = self.adjacency_list[root]
            for node in adjacent_nodes:
                dft(node)

        root = self.nodes.get(label)
        if root is None:
            return
        visited = set()
        result = []
        dft(root)
        return result

    def bf_traversal(self, label):
        def bft(root):
            if root not in visited:
                result.append(root.label)
            visited.add(root)
            adjacent_nodes = self.adjacency_list[root]
            for node in adjacent_nodes:
                if node not in visited:
                    queue.append(node)
            if len(queue) == 0:
                return
            bft(queue.pop(0))

        root = self.nodes.get(label)
        if root is None:
            return
        visited = set()
        queue = []
        result = []
        bft(root)
        return result


graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("D", "C")
graph.print_graph()
print(graph.bf_traversal("A"))
