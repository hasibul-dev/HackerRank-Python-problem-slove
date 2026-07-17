import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        # Subtracting coordinates and returning a new Points object
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        # Dot product: x1*x2 + y1*y2 + z1*z2
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        # Cross product of two 3D vectors
        rx = self.y * no.z - self.z * no.y
        ry = self.z * no.x - self.x * no.z
        rz = self.x * no.y - self.y * no.x
        return Points(rx, ry, rz)
        
    def absolute(self):
        # Magnitude of the vector
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
