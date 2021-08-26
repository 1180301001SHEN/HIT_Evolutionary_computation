''' @ auther Sr+'''
import math


class Distance():
    '''Some methods to compute the distance'''
    def compute_EUC_2D(node1, node2):
        '''EUC_2D distance'''
        node1_x, node1_y = node1.get_coordinate()
        node2_x, node2_y = node2.get_coordinate()

        distance_x = abs(node1_x-node2_x)
        distance_y = abs(node1_y-node2_y)

        distance = math.sqrt(distance_x**2+distance_y**2)
        return round(distance)

    def compute_Manhattan_2D(node1, node2):
        '''Manhattan_2D distance'''
        node1_x, node1_y = node1.get_coordinate()
        node2_x, node2_y = node2.get_coordinate()

        distance_x = abs(node1_x-node2_x)
        distance_y = abs(node1_y-node2_y)

        distance = distance_x+distance_y
        return round(distance)

    def compute_Maximum_2D(node1, node2):
        '''Maximum_2D distance'''
        node1_x, node1_y = node1.get_coordinate()
        node2_x, node2_y = node2.get_coordinate()

        distance_x = abs(node1_x-node2_x)
        distance_y = abs(node1_y-node2_y)

        distance = max(round(distance_x), round(distance_y))
        return distance

    def compute_Geographical(node1, node2):
        '''Geographical distance'''
        node1_x, node1_y = node1.get_coordinate()
        node2_x, node2_y = node2.get_coordinate()

        PI = 3.141592
        deg1_x = round(node1_x)
        min1_x = node1_x - deg1_x
        latitude1_x = PI * (deg1_x + 5.0 * min1_x / 3.0) / 180.0
        deg1_y = round(node1_y)
        min1_y = node1_y - deg1_y
        longitude1_y = PI * (deg1_y + 5.0 * min1_y / 3.0) / 180.0

        deg2_x = round(node2_x)
        min2_x = node2_x - deg2_x
        latitude2_x = PI * (deg2_x + 5.0 * min2_x / 3.0) / 180.0
        deg2_y = round(node2_y)
        min2_y = node2_y - deg2_y
        longitude2_y = PI * (deg2_y + 5.0 * min2_y / 3.0) / 180.0

        RRR = 6378.388
        q1 = math.acos(longitude1_y-longitude2_y)
        q2 = math.acos(latitude1_x-latitude2_x)
        q3 = math.acos(latitude1_x+latitude2_x)
        distance = int(RRR * math.acos(0.5*((1.0+q1)*q2 - (1.0-q1)*q3)) + 1.0)
        return distance

    def compute_Pseudo_Euc_2D(node1, node2):
        '''Pseudo_Euc_2D distance'''
        node1_x, node1_y = node1.get_coordinate()
        node2_x, node2_y = node2.get_coordinate()

        xd = node1_x - node2_x
        yd = node1_y - node2_y
        rij = math.sqrt((xd**2 + yd**2)/10.0)
        tij = round(rij)
        if tij < rij:
            dij = tij + 1
        else:
            dij = tij
        return dij
