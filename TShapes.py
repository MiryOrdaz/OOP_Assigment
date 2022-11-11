# Initiating Class in Python (3D) Shapes
import math
import ascii_magic


class Shape3D:

    def __init__(self, type, colour):
        self.type = type
        self.colour = colour

    def volume(self):
        return None

    def surface_area(self):
        return None

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def draw(self):
        return None


class Octapoints:
    def __init__(self, A1=(0, 0, -1), A2=(-1, 0, 0), A3=(0, 0, 1), A4=(1, 0, 0), B1=(0, 1, 0), C1=(0, -1, 0)):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.B1 = B1
        self.C1 = C1

    def set_A1(self, A1):
        self.A1 = A1

    def set_A2(self, new):
        self.A2 = (new)

    def set_A3(self, new):
        self.A3 = (new)

    def set_A4(self, new):
        self.A4 = (new)

    def set_B1(self, new):
        self.B1 = (new)

    def set_C1(self, new):
        self.C1 = (new)

    def get_coordinates(self):
        print(
            f'Point 1: {self.A1}\nPoint 2: {self.A2}\nPoint 3: {self.A3}\nPoint 4: {self.A4}\nPoint 5: {self.B1}\nPoint 6: {self.C1}')


class Hexapoints:
    def __init__(self, O=(0, 8, 0), A=(-5, 0, 0), B=(-2.5, 0, 4.33), C=(2.5, 0, 4.33), D=(5, 0, 0), E=(2.5, 0, -4.33),
                 F=(-2.5, 0, -4.33)):
        self.O = O
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F


class Octahedron(Shape3D, Octapoints):
    def __init__(self, type, colour, edge, A1=(0, 0, -1), A2=(-1, 0, 0), A3=(0, 0, 1), A4=(1, 0, 0), B1=(0, 1, 0),
                 C1=(0, -1, 0)):
        super().__init__(type, colour)
        super(Shape3D, self).__init__()
        self.edge = edge

        # Just upload defintion and like the variables there and the methods would be iherited as well. so setting new values would not be hard, adding an additional value would not be bad.

    def get_edge(self):
        return self.edge

    def set_edge(self, edge):
        self.edge = edge

    def volume(self):
        volume = ((self.edge ** 3) * (math.sqrt(2) / 3))
        return volume

    def surface_area(self):
        surface_area = 2 * math.sqrt(3) * self.edge ** 2
        return surface_area

    def draw(self):
        output = ascii_magic.from_image_file('octa1.png', columns=100, char='@', back=ascii_magic.Back.WHITE)
        ascii_magic.to_terminal(output)
