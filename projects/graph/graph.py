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
        if not vertex in self.vertices:
            # each vertex needs an identifier that when called upon in the dictionary, has a list of edges.
            # because we dont want to hold duplicates, we use a set
            self.vertices[vertex] = set()
        else:
            print("Warning: vertex exists")

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # first check if the vertices both exist.
        if v1 and v2 in self.vertices:
            # if they do, add to the set of vertex one, the reference to vertex two
            # .add() adds a single parameter, adds one element to the set
            # this adds v2 to v1's set of edges
            self.vertices[v1].add(v2)
        else:
            # if they do not both exist
            print("ERROR: Vertex doesn't exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Steps to complete traversal

        # Create an empty set to store the visited nodes
        visited = set()
        # Create an empty queue
        q = Queue()
        # Add starting_vertex to the queue
        q.enqueue(starting_vertex)

        print("Starting BFT")

        # While queue is not empty
        while q.size() > 0:
            # Dequeue first vertex in the queue
            current = q.dequeue()
        # If it hasn't been visited yet
            if current not in visited:
                print(current)
                # mark as visited (add to the set)
                visited.add(current)
        # Add it's neighbors to the back of the queue
                for neighbor in self.vertices[current]:
                    # appends the neighbor
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Steps to complete traversal

        # Create a set to store the nodes that we have visited
        visited = set()
        # Create an empty stack using the provided queue
        s = Stack()
        # Add starting_vertex to the stack
        s.push(starting_vertex)

        print("Starting DFT")

        # While stack is not empty
        # Iterate through each level starting at first vert
        while s.size() > 0:
            # Dequeue first vertex in the queue
            current = s.pop()
        # If it hasn't been visited yet,
            if current not in visited:
                print(current)
                # visit it (add it to the set)
                visited.add(current)
        # Add it's neighbors to the top of the stack
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
        # Create an empty set to store the visited nodes
        visited = set()
        # Create an empty queue
        q = Queue()
        # Add a PATH to starting_vertex to the queue
        # return a [list] containing shortest path
        q.enqueue([starting_vertex])

        # While queue is not empty
        while q.size() > 0:
            # Dequeue first PATH in the queue
            path = q.dequeue()
            # Grab the vertex from the end of the path!
            current = path[-1]
            # If the vertex hasn't been visited yet
            if current not in visited:
                # if vertex = target
                if current == destination_vertex:
                    # return the path
                    return "BFS: " + str(path)
                # Mark it as visited (add to set)
                visited.add(current)
                # Add a PATH to all of it's neighbors to the back of the queue
                for neighbor in self.vertices[current]:
                    # copy the path
                    new_path = list(path)
                    # append neighbor to back of the copy
                    new_path.append(neighbor)
                    # enqueue copy
                    q.enqueue(new_path)
        return "BFS: Value not found"

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Instead of storing nodes like traversal, we store a path to the node
        # Steps to complete search

        # Create an empty set to store the visited nodes
        visited = set()
        # Create an empty queue
        s = Stack()
        # Add a PATH to starting_vertex to the queue
        s.push([starting_vertex])

        # While queue is not empty
        while s.size() > 0:
            # Dequeue first PATH in the queue
            path = s.pop()
            # Grab the vertex from the end of the path!
            current = path[-1]
            # If the vertex hasn't been visited yet
            if current not in visited:
                # if vertex = target
                if current == destination_vertex:
                    # return the path
                    return "DFS: " + str(path)
                 # Mark it as visited (add to set)
                visited.add(current)
                # Add a PATH to all of it's neighbors to the back of the queue
                for neighbor in self.vertices[current]:
                    # copy the path
                    path_copy = list(path)
                    # append neighbor to back of the copy
                    path_copy.append(neighbor)
                    # enqueue copy
                    s.push(path_copy)
        return "DFS: Value not found"


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
    print(graph.bfs(1, 42))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs(1, 43))
