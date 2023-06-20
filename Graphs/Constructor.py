class Graph:
    
    def __init__(self):
        self.adj_list = {}
        
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])
            
    def add_vertex(self,val):
        if val not in self.adj_list.keys():
            self.adj_list[val] = []
            return True
        return False
    
    def add_edge(self,v1,v2):
        if v1 and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        if v1 and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self,val):
        if val in self.adj_list.keys():
            for other_vertex in self.adj_list[val]:
                self.adj_list[other_vertex].remove(val)
            del self.adj_list[val]
            return True
        return False
    
my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')

my_graph.remove_edge('A', 'D')
my_graph.remove_vertex('C')

my_graph.print_graph()