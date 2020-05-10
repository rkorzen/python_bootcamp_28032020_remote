class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<Vector: x={self.x}, y={self.y}>"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise NotImplementedError()

    def __eq__(self, other):
        return self.length == other.length

    def __gt__(self, other):
        return self.length > other.length

    def __lt__(self, other):
        return self.length < other.length

    @property
    def length(self):
        return pow(self.x ** 2 + self.y ** 2, 0.5)


class TestVector:

    def test_init(self):
        vector = Vector(1, 2)
        assert vector.x == 1
        assert vector.y == 2

    def test_add_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 + v2
        assert v3.x == 4
        assert v3.y == 6

    def test_sub_2_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 - v2
        assert v3.x == -2
        assert v3.y == -2

    def test_mul_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        assert v1 * v2 == 1 * 3 + 2 * 4

    def test_mul_vector_int(self):
        v1 = Vector(3, 4)
        v2 = v1 * 3
        assert v2.x == 9
        assert v2.y == 12

    def test_vector_comparision(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = Vector(1, 2)
        assert v2 > v1
        assert v1 < v2
        assert v1 == v3
        assert v1 != v2

    def test_length(self):
        v1 = Vector(2, 2)
        assert v1.length == pow(2 * 2 + 2 * 2, 0.5)

        v2 = Vector(5, 10)
        assert v2.length == pow(5 ** 2 + 10 ** 2, 0.5)

    def test_str(self):
        v1 = Vector(3, 4)
        assert str(v1) == "<Vector: x=3, y=4>"
