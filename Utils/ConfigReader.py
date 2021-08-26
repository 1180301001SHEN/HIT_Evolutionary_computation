''' @ auther Sr+'''
import numpy as np
from Utils.Distance import Distance


class Node():
    '''see the individuals as the nodes,
    node_serial_number means the serial number of the individual,
    node_x, node_y means the coordinate of the node'''

    def __init__(self, node_serial_number, node_x, node_y):
        self.node_serial_number = node_serial_number
        self.node_x = node_x
        self.node_y = node_y

    def show(self):
        print("node_serial_number:"+str(self.node_serial_number))
        print("node_x:"+str(self.node_x))
        print("node_y:"+str(self.node_y))

    def get_coordinate(self):
        '''return the coordinate of the node'''
        return self.node_x, self.node_y


class ConfigReader():
    '''According to the input file name parsing file'''

    def __init__(self, filename):
        self.nodelist = list()
        try:
            file = open(filename)
            file_content = list(file)
            for i in range(len(file_content)):
                content = file_content[i].strip()
                if content.startswith("NAME"):
                    self.name = content.split(":")[1].strip()
                elif content.startswith("DIMENSION"):
                    self.dimension = int(content.split(":")[1].strip())
                elif content.startswith("EDGE_WEIGHT_TYPE"):
                    self.edge_weight_type = content.split(":")[1].strip()
                elif content.startswith("NODE_COORD_SECTION"):
                    for j in range(i+1, i+self.dimension+1):
                        node_content = file_content[j].strip().split(" ")
                        self.nodelist.append(Node(int(node_content[0]), float(
                            node_content[1]), float(node_content[2])))
            self.dist_mat = np.zeros((self.dimension, self.dimension))
            if self.edge_weight_type == "EUC_2D":
                for i in range(self.dimension):
                    for j in range(i+1, self.dimension):
                        distance = Distance.compute_EUC_2D(
                            self.nodelist[i], self.nodelist[j])
                        self.dist_mat[i][j] = distance
                        self.dist_mat[j][i] = self.dist_mat[i][j]
            file.close()
        except Exception as e:
            print(e)

    def show(self):
        print("name:" + str(self.name))
        print("dimension:" + str(self.dimension))
        print("edge_weight_type:"+str(self.edge_weight_type))
        print("node_num:"+str(len(self.nodelist)))
        print("dist_mat:"+str(self.dist_mat.shape))

    def get_all(self):
        '''return the name, dimension, edge_weight_type, dist_mat according to the input file'''
        return self.name, self.dimension, self.edge_weight_type, self.dist_mat


if __name__ == "__main__":
    config = ConfigReader("ALL_tsp/pr2392.tsp")
    config.show()
    config.nodelist[0].show()
