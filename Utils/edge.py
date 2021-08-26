''' @ auther Sr+'''
class edge_element():
    def __init__(self, number, common) -> None:
        self.number = number
        self.common = common

    def get_number(self):
        return self.number

    def set_common(self, common):
        self.common = common

    def get_common(self):
        return self.common


class edge_row():
    def __init__(self, number) -> None:
        self.number = number
        self.elements = list()

    def get_element(self, number):
        for element in self.elements:
            if element.get_number() == number:
                return element
        return None

    def delete_number(self, number):
        element = self.get_element(number)
        if element is not None:
            self.elements.remove(element)

    def get_row_num(self):
        return self.number

    def get_elements(self):
        return self.elements

    def show(self):
        number_list = [self.elements[i].get_number()
                       for i in range(len(self.elements))]
        print(number_list)


class edge_table():
    def __init__(self, length) -> None:
        self.rows = [edge_row(i) for i in range(length)]

    def get_row(self, number):
        for row in self.rows:
            if row.get_row_num() == number:
                return row
        return None

    def add_element(self, number, element):
        row = self.get_row(number)
        if row is not None:
            row.get_elements().append(element)

    def delete_number(self, number):
        self.rows.remove(self.get_row(number))
        for row in self.rows:
            row.delete_number(number)

    def show(self):
        for row in self.rows:
            row.show()
