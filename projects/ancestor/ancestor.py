
from util import Stack, Queue


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        # Create the vertice if needed.
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)

        # Now add the edge from v1 to v2
        self.vertices[v1].add(v2)


#  HINTS
# The input will not be empty.
# There are no cycles in the input.
# There are no repeated ancestors. if two individuals are connected, it is by exactly one path
# IDs will always be positive integers.
# A parent may have any number of children.


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for group in ancestors:
        print("group: ", group)
        l = list(group)
        graph.add_edge(l[1], l[0])
        print(graph.add_edge(l[1], l[0]))

    q = Queue()
    path = []
    highest_nodes = []
    visited = set()

    q.enqueue(starting_node)
    highest_nodes.append(starting_node)
    visited.add(starting_node)

    index = len(highest_nodes)
    count = len(highest_nodes)

    while True:
        node = q.dequeue()
        path.append(node)
        highest_nodes += list(graph.vertices[node])

        if not q.size() and not graph.vertices[node]:
            break
        count -= 1

        if not count:
            highest_nodes = highest_nodes[index:]
            count = len(highest_nodes)
            index = len(highest_nodes)

        for parent in graph.vertices[node]:
            if parent not in visited:
                q.enqueue(parent)
                visited.add(parent)
                
    if highest_nodes[0] == starting_node:
        return -1
    else:
        return min(highest_nodes)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)


# Input:
# [ [1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 9] ]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# Output:
# 8 => 4 7 => 4 6 => 1, 2, or 4
