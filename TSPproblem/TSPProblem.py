''' @ auther Sr+'''
class TSPProblem():
    '''The TSP problem:
    name means the TSP problem name,
    dimension means the gene length of the individual,
    edge_weight_type means the computing type of the edge weight,
    dist_mat means the distance matrix of the individuals'''
    def __init__(self, name, dimension, edge_weight_type, dist_mat) -> None:
        self.name = name
        self.dimension = dimension
        self.edge_weight_type = edge_weight_type
        self.dist_mat = dist_mat

    def get_name(self):
        '''return the name of the TSP problem'''
        return self.name

    def get_dimension(self):
        '''return the dimension of the TSP problem'''
        return self.dimension

    def get_edge_weight_type(self):
        '''return the edge_weight_type of the TSP problem'''
        return self.edge_weight_type

    def get_dist_mat(self):
        '''return the dist_mat of the TSP problem'''
        return self.dist_mat
