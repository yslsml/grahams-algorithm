class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, other):
        return self.x == other.x and self.y == other.y
