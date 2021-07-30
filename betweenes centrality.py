#!/usr/bin/env python3

import re
import itertools

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
    name = "rachit"
    email = "rachit18404"
    roll_num = "2018404"

    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices
        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
        
        self.edges    = ordered_edges
        
        self.validate()

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))

    def min_dist(self, start_node, end_node):
        self.redges=[]
        for i in self.edges:          #taking reverse of a tuple
            self.i=i[::-1]
            self.redges.append(i)
        self.a=[]
        self.matrix=[]
        for i in range(1,len(vertices)+1):
            self.a.append(vertices)         #creating adjacency matrix
        for i in range(1,len(vertices)+1):
            for j in range(1,len(vertices)+1):
                self.a[i-1][j-1]=i,j
                if self.a[i-1][j-1] in edges:
                    self.a[i-1][j-1]=1
                elif self.a[i-1][j-1] in self.redges:
                    self.a[i-1][j-1]=1
                else:
                    self.a[i-1][j-1]=0
                self.matrix.append(self.a[i-1][j-1])


        self.newl=[]
        for i in range(0,(len(vertices))**2,len(vertices)):
            self.x=self.matrix[i:i+len(vertices)]
            self.newl.append(self.x)           #splitting list into sublist

            
        self.allp=[]           
        self.visited=[]
        self.queue=[[start_node]]     #add into queue the starting node
        while self.queue:
            self.path=self.queue.pop(0)     #taking first element of q and delete it from queue
            self.node=self.path[-1]
            if self.node not in self.visited:     #so that visited node does not occur again
              self.n=[]         
              for i in range(1,len(vertices)+1):
                  for j in range(1,len(vertices)+1):
                        if i ==self.node and self.newl[i-1][j-1]==1 :   #finding its neighbours
                            self.n.append(j)
              
                            
                          
              for i in self.n:
                  
                  self.np=list(self.path)  #adding neighbour to form path
                  self.np.append(i) 
                  self.queue.append(self.np)     #adding those path in queue
                  
                  if i == end_node:
                       self.allp.append(self.np)  #if neighbour is the end point, append that path to allp
                       
              self.visited.append(self.node)     #push explored node in visited so that it does'nt occur again
        
        self.m=len(self.allp[0])
        for i in range(len(self.allp)):
            
            if len(self.allp[0])>len(self.allp[i]):  #finding minimum distance
                self.m=len(self.allp[i])
            else:
                pass
        print (self.m)


    def all_shortest_paths(self, start_node, end_node):
        self.redges=[]
        for i in self.edges:
            self.i=i[::-1]
            self.redges.append(i)
        self.a=[]
        self.matrix=[]
        for i in range(1,len(vertices)+1):
            self.a.append(vertices)
        for i in range(1,len(vertices)+1):
            for j in range(1,len(vertices)+1):
                self.a[i-1][j-1]=i,j
                if self.a[i-1][j-1] in edges:
                    self.a[i-1][j-1]=1
                elif self.a[i-1][j-1] in self.redges:
                    self.a[i-1][j-1]=1
                else:
                    self.a[i-1][j-1]=0
                self.matrix.append(self.a[i-1][j-1])


        self.newl=[]
        for i in range(0,(len(vertices))**2,len(vertices)):
            self.x=self.matrix[i:i+len(vertices)]
            self.newl.append(self.x)
        

        self.allp=[]
        self.visited=[]
        self.queue=[[start_node]]
        while self.queue:
            self.path=self.queue.pop(0)
            self.node=self.path[-1]
            if self.node not in self.visited:
              self.n=[]
              for i in range(1,len(vertices)+1):
                  for j in range(1,len(vertices)+1):
                        if i ==self.node and self.newl[i-1][j-1]==1 :
                            self.n.append(j)
                            
              for i in self.n:
                  
                  self.np=list(self.path)
                  self.np.append(i)
                  
                  self.queue.append(self.np)
                  
                  if i == end_node:
                       self.allp.append(self.np)
                       
              self.visited.append(self.node)
        self.m=len(self.allp[0])
        for i in range(len(self.allp)):
            
            if len(self.allp[0])>len(self.allp[i]):
                self.m=len(self.allp[i])
            else:
                pass
        
        for i in self.allp:      #only those path will occur which are of minimum distance
            if len(i)==self.m:
                print (i)

    def all_paths(node, destination, dist, path):
        self.redges=[]
        for i in self.edges:
            self.i=i[::-1]
            self.redges.append(i)
        self.a=[]
        self.matrix=[]
        for i in range(1,len(vertices)+1):
            self.a.append(vertices)
        for i in range(1,len(vertices)+1):
            for j in range(1,len(vertices)+1):
                self.a[i-1][j-1]=i,j
                if self.a[i-1][j-1] in edges:
                    self.a[i-1][j-1]=1
                elif self.a[i-1][j-1] in self.redges:
                    self.a[i-1][j-1]=1
                else:
                    self.a[i-1][j-1]=0
                self.matrix.append(self.a[i-1][j-1])


        self.newl=[]
        for i in range(0,(len(vertices))**2,len(vertices)):
            self.x=self.matrix[i:i+len(vertices)]
            self.newl.append(self.x)
        

        self.allp=[]
        self.visited=[]
        self.queue=[[start_node]]
        while self.queue:
            self.path=self.queue.pop(0)
            self.node=self.path[-1]
            if self.node not in self.visited:
              self.n=[]
              for i in range(1,len(vertices)+1):
                  for j in range(1,len(vertices)+1):
                        if i ==self.node and self.newl[i-1][j-1] :
                            self.n.append(j)
                            
              for i in self.n:
                  
                  self.np=list(self.path)
                  self.np.append(i)
                  
                  self.queue.append(self.np)
                  
                  if i == end_node:
                       print(self.np)
                       
              self.visited.append(self.node)

        

    def betweenness_centrality(self, node):


        self.redges=[]
        for i in self.edges:
            self.i=i[::-1]
            self.redges.append(i)
        self.a=[]
        self.matrix=[]
        for i in range(1,len(vertices)+1):
            self.a.append(vertices)
        for i in range(1,len(vertices)+1):
            for j in range(1,len(vertices)+1):
                self.a[i-1][j-1]=i,j
                if self.a[i-1][j-1] in edges:
                    self.a[i-1][j-1]=1
                elif self.a[i-1][j-1] in self.redges:
                    self.a[i-1][j-1]=1
                else:
                    self.a[i-1][j-1]=0
                self.matrix.append(self.a[i-1][j-1])


        self.newl=[]
        for i in range(0,(len(vertices))**2,len(vertices)):
            self.x=self.matrix[i:i+len(vertices)]
            self.newl.append(self.x)
        

        self.allp=[]
        self.visited=[]
        self.queue=[[start_node]]
        while self.queue:
            self.path=self.queue.pop(0)
            self.node=self.path[-1]
            if self.node not in self.visited:
              self.n=[]
              for i in range(1,len(vertices)+1):
                  for j in range(1,len(vertices)+1):
                        if i ==self.node and self.newl[i-1][j-1]==1 :
                            self.n.append(j)
                            
              for i in self.n:
                  
                  self.np=list(self.path)
                  self.np.append(i)
                  
                  self.queue.append(self.np)
                  
                  if i == end_node:
                       self.allp.append(self.np)
                       
              self.visited.append(self.node)
        self.m=len(self.allp[0])
        for i in range(len(self.allp)):
            
            if len(self.allp[0])>len(self.allp[i]):
                self.m=len(self.allp[i])
            else:
                pass
        
        for i in self.allp:
            if len(i)==self.m:
                sp.append(i)
        self.count=0
        for i in self.sp:
            for j in i:
                if j==2:
                    self.count=self.count+1
        print (float(self.count)/float(len(self.sp)))

    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.

        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """

        raise NotImplementedError

if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6]
    edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]


    graph = Graph(vertices, edges)
    
