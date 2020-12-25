from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = '' #creates a color attribute for the bipartite function (str)
        self.visited = False #creates a visited attribute (bool)
        self.dead_end = False #creates a dead_end attribute (bool)


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        # This method should call add_vertex and add_edge
        self.adj_dict = {} #creates a dictionary to hold the vertex objects of the graph
        with open(filename, 'r') as opened_file: #opens and closes the input file for reading edges

            for line in opened_file: #for each line in opened file...
                line = line.split() #split the line into a list of the two vertices
                v1 = line[0] #create a variable for the first vertex
                v2 = line[1] #create a variable for the second vertex
                self.add_vertex(v1) #make sure the first vertex exists in graph
                self.add_vertex(v2) #make sure the second vertex exists in graph
                self.add_edge(v1, v2) #create an edge between the two vertices


    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        # Should be called by init
        if key not in self.adj_dict: #if the vertex is not already in the graph ...
            self.adj_dict[key] = Vertex(key) #create a new vertex object and put it in the graph (dictionary)


    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.adj_dict[v1].adjacent_to.append(v2) #add vertex 2 to the adjacency list of the first vertex
        self.adj_dict[v2].adjacent_to.append(v1) #add vertex 1 to the adjacency list of the second vertex


    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.adj_dict: #if key in the vertex dictionary...
            return self.adj_dict[key] #return the vertex object associated with its key

        return None #if the key is not in the dictionary, return None


    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        returning_list = [] #creates a list for the vertices to be appended to and returned
        for key in self.adj_dict: #for each key in the dictionary of vertices...
            returning_list.append(key) #append to the returning list the key

        returning_list.sort() #sort the returning list 

        return returning_list #return the returning list


    def conn_components(self): 
        '''Return a list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.'''
        #This method MUST use Depth First Search logic!
        self.reset_vertices() #makes sure that the attributes of each vertex (for breadth first search and depth first search) are reset
        vertices_list = self.get_vertices() #create a vertices list (all vertices in graph lowest to highest)
        list_of_subtrees = [] #create a list for lists of vertices for subtrees
        i = 0

        while i < len(vertices_list): #while there are still vertices in the vertices_list...
            if self.adj_dict[vertices_list[i]].visited:
                i += 1
                continue
            first_vertex = vertices_list[i] #create a first vertex variable and next vertex variable for the while loop
            list_of_subtrees.append(self.depth_first_search(first_vertex, vertices_list)) #append subtree list to the list of subtrees
            i += 1

        return list_of_subtrees #return the list of subtrees


    def is_bipartite(self):
        '''Return True if the graph is bicolorable and False otherwise.'''
        #This method MUST use Breadth First Search logic!
        self.reset_vertices() #makes sure that the attributes of each vertex (for breadth first search and depth first search) are reset
        vertices_list = self.get_vertices() #creates a vertices list 
        i = 0

        while i < len(vertices_list): #while the length of the vertices list is greater than 0 ...
            if self.adj_dict[vertices_list[i]].visited:
                i += 1
                continue
            first_vertex = vertices_list[i] #first vertex is the first index in the vertices list
            if not self.breadth_first_search(first_vertex, vertices_list): #if the breadth first search returnes False ...
                return False #return False

        return True #if there are no issues then return True


# Helper Functions --------------------------------------------------------------------------------------------------------

    def breadth_first_search(self, first_vertex, vertices_list):
        queue = Queue(len(vertices_list)) #creates a queue with capacity of the length of the vertices list
        self.adj_dict[first_vertex].visited = True #makes the first vertex visited
        queue.enqueue(first_vertex) #enqueues the first vertex
        #vertices_list.remove(first_vertex) #removes the first vertex from the vertices list
        self.adj_dict[first_vertex].color = 'r' #makes the color of the first vertex red ('r')
        

        while not queue.is_empty(): #while the queue is not empty ...
            if self.enqueue_all_children(vertices_list, queue) is False: #if the enqueue all children function returns false ...
                return False #return False

        return True #if there are no issures found return True


    def enqueue_all_children(self, vertices_list, queue):
        dequeued_vertex = queue.dequeue() #creates a variable for the dequeud vertex
        adj_list = self.adj_dict[dequeued_vertex].adjacent_to #create a variable for the adjacency list of the dequeued vertex
        #adj_list.sort() #sorts the adjacency list 
        old_color = self.adj_dict[dequeued_vertex].color #creates a variable for the dequeued vertex's color
        if old_color == 'b': #if old color is black ('b') ...
            color = 'r' #color variable is red ('r')
        else: #if old color is red ('r') ...
            color = 'b' #color variable is black ('b')

        for vertex in adj_list: #for each vertex in the adjacency list of the vertex that was dequeued ...
            if not self.adj_dict[vertex].visited: #if the vertex in adjacency list has not already been visited ...
                #vertices_list.remove(vertex) #remove the vertex fromt the vertices list
                queue.enqueue(vertex) #enqueue the vertex being visited
                self.adj_dict[vertex].visited = True #set the visited attribute of the vertex to True
                self.adj_dict[vertex].color = color #makes the color of the vertex being visited the colot determined earlier
            elif vertex != dequeued_vertex: #if the vertex in adjacency list has been visited and is not the dequeued vertex ...
                current_color = self.adj_dict[vertex].color #creates a variable for the color of the vertex being visited
                if current_color != color: #if the color of the vertex being visited is not the same as the color determined earlier ...
                    return False #return False


    def depth_first_search(self, first_vertex, vertices_list): #uses breadth first search algorithm for the conn_components function
        subtree_list = [first_vertex] #creates a variable for the subtree list and puts the first vertex inside
        vertex = first_vertex #creates a variable called vertex (used to traverse through the graph)
        stack = Stack(len(vertices_list)) #create a stack with the capacity of the amount of vertex objects in the graph


        while not self.adj_dict[first_vertex].dead_end: #while the first vertex is not a "dead end"
            if self.adj_dict[vertex].dead_end: #if the vertex is a "dead end" ...
                vertex = stack.pop() #traverse to previous vertex by setting new vertex to the one popped from the stack
                continue 

            #if not self.adj_dict[vertex].visited: #makes sure the vertex isn't already deleted from the vertices list
                #vertices_list.remove(vertex) #deletes the visited vertex from the vertices list

            self.adj_dict[vertex].visited = True #marks the vertex as visited
            stack.push(vertex) #push the vertex being visited to the stack
            next_vertex = self.check_adj_list(vertex) #uses helper function check_adj_list to return the next available vertex

            if next_vertex is None: #if there is no further available vertices ...
                self.adj_dict[vertex].dead_end = True #mark the vertex as a "dead end"
                vertex = stack.pop() #set the new vertex variable to the vertex popped from the stack (back-tracking)

            if not next_vertex is None: #if there is an available vertex ...
                subtree_list.append(next_vertex) #append the next vertex to the subtree list
                vertex = next_vertex #traverses to the next vertex

        subtree_list.sort() #sort the subtree list

        return subtree_list #return subtree
                

    def check_adj_list(self, vertex):
        i = 0 #creates a variable i for the while loop
        adj_list = self.adj_dict[vertex].adjacent_to #creates a variable for the adjacent to list of the specified vertex
        #adj_list.sort()
        while i < len(adj_list): #while i is less than the length of the adjacent to list ...
            if not self.adj_dict[adj_list[i]].visited: #if the vertex in the adjacent to list has not already been visited ...
                return adj_list[i] #return the unvisited vertex
            i += 1 #increase i

        return None #if no unvisited vertex is found then return None

    def reset_vertices(self):
        vertices_list = self.get_vertices() #create a list of all the vertices 

        for vertex in vertices_list: #for each vertex in the vertices list ...
            self.adj_dict[vertex].color = '' #set the color to empty string ''
            self.adj_dict[vertex].visited = False #set the visited attribute to False
            self.adj_dict[vertex].dead_end = False #set the dead_end attribute to False