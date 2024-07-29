from collections import deque


# Graph node
class Node:
    def __init__(self, label):
        self.value = label

    def __str__(self):
        return f"{self.value}"


class Graph:
    def __init__(self):
        self.nodes = {}
        self.neighbors = {}

    def add_node(self, label):
        if label in self.nodes:
            raise ValueError("Label already exists")
        new_node = Node(label)
        self.nodes[label] = new_node
        self.neighbors[new_node] = []

    def add_edge(self, from_label, to_label):
        from_node = self.nodes.get(from_label)
        to_node = self.nodes.get(to_label)
        if from_node is None or to_node is None:
            raise ValueError("Label note found")
        if to_node not in self.neighbors[from_node]:
            self.neighbors[from_node].append(to_node)

    def remove_node(self, label):
        removing_node = self.nodes.get(label)
        if removing_node is None:
            return
        nodes = self.neighbors.keys()
        for node in nodes:
            if removing_node in self.neighbors[node]:
                self.neighbors[node].remove(removing_node)
        self.neighbors.pop(removing_node)
        self.nodes.pop(label)

    def remove_edge(self, from_label, to_label):
        from_node = self.nodes.get(from_label)
        to_node = self.nodes.get(to_label)
        if (
            from_node is None
            or to_node is None
            or to_node not in self.neighbors[from_node]
        ):
            return
        self.neighbors[from_node].remove(to_node)

    def print_graph(self):
        nodes = self.neighbors.keys()
        for node in nodes:
            neighbors = [str(node) for node in self.neighbors[node]]
            print(f"{node} is connected to {neighbors}")

    def dfs(self, label):
        def traverse(root):
            graph.append(root.value)
            visited.add(root)
            neighbors = self.neighbors.get(root)
            if neighbors is None:
                return
            for neighbor in neighbors:
                if neighbor not in visited:
                    melvin = traverse(neighbor)

        root = self.nodes.get(label)
        if root is None:
            raise ValueError("Node not found")
        visited = set()
        graph = []
        traverse(root)
        print(graph)

    def dfs_iter(self, label):
        root = self.nodes.get(label)
        if root is None:
            raise ValueError("Node not found")
        visited = set()
        graph = []
        stack = [root]

        while len(stack) > 0:
            current = stack.pop()
            if current in visited:
                continue
            graph.append(current.value)
            visited.add(current)
            neighbors = self.neighbors.get(current)
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

        print(graph)

    def bfs(self, label):
        root = self.nodes.get(label)
        if root is None:
            raise ValueError("None not found")
        visited = set()
        queue = deque([root])
        graph = []

        # Traversing
        while len(queue) > 0:
            root = queue.popleft()
            if root in visited:
                continue
            graph.append(root.value)
            visited.add(root)
            neighbors = self.neighbors.get(root)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

        print(graph)

    def has_cycle(self):
        def find_cycle(node):
            visiting.add(node)
            neighbors = self.neighbors.get(node)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                if neighbor in visiting or find_cycle(neighbor):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False

        nodes = list(self.neighbors.keys())
        visiting = set()
        visited = set()

        while len(nodes) > 0:
            current_node = nodes.pop()
            if find_cycle(current_node):
                return True

        return False


graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_edge("A", "B")
graph.add_edge("A", "E")
graph.add_edge("B", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "B")
# graph.dfs("B")
# graph.dfs_iter("B")
# graph.print_graph()
print(graph.has_cycle())
