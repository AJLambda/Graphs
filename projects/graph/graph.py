"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR: Vertex doesn't exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Steps to complete traversal

        # Create an empty queue using the provided queue
        q = Queue()
        # Create a set to store the nodes that we have visited
        visited = set()
        # Add starting_vertex to the queue
        q.enqueue(starting_vertex)

        print("Starting BFT")

        # While queue is not empty
        # Iterate through each level starting at first vert
        while q.size() > 0:
            # Dequeue first vertex in the queue
            current = q.dequeue()
        # If it hasn't been visited yet, visit it (add it to the set)
            if current not in visited:
                print(current)
                visited.add(current)
        # Add it's neighbors to the queue
                for next_vert in self.vertices[current]:
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Steps to complete traversal

        # Create an empty stack using the provided queue
        s = Stack()
        # Create a set to store the nodes that we have visited
        visited = set()
        # Add starting_vertex to the stack
        s.push(starting_vertex)

        print("Starting DFT")

        # While stack is not empty
        # Iterate through each level starting at first vert
        while s.size() > 0:
            # Dequeue first vertex in the queue
            current = s.pop()
        # If it hasn't been visited yet, visit it (add it to the set)
            if current not in visited:
                print(current)
                visited.add(current)
        # Add it's neighbors to the queue
                for next_vert in self.vertices[current]:
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Steps to complete search

        # Create an empty queue using the provided queue
        q = Queue()
        # Create a set to store the nodes that we have visited
        visited = set()
        # Add starting_vertex to the queue
        q.enqueue(starting_vertex)

        print("Starting BFS")

        # While queue is not empty
        # Iterate through each level starting at first vert
        while q.size() > 0:
            # Dequeue first vertex in the queue
            current = q.dequeue()
        # If it hasn't been visited yet, visit it (add it to the set)
            if current not in visited:
                print(current)
                visited.add(current)
        # Add it's neighbors to the queue
                for next_vert in self.vertices[current]:
                    q.enqueue(next_vert)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Steps to complete search

        # Create an empty stack using the provided queue
        s = Stack()
        # Create a set to store the nodes that we have visited
        visited = set()
        # Add starting_vertex to the stack
        s.push(starting_vertex)

        print("Starting DFS")

        # While stack is not empty
        # Iterate through each level starting at first vert
        while s.size() > 0:
            # Dequeue first vertex in the queue
            current = s.pop()
        # If it hasn't been visited yet, visit it (add it to the set)
            if current not in visited:
                print(current)
                visited.add(current)
        # Add it's neighbors to the queue
                for next_vert in self.vertices[current]:
                    s.push(next_vert)


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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
