from app import Figure

def test_get_angles_triangle():
    fig = "triangle"
    triangle = Figure(fig, 1)
    assert triangle.get_angles == 3

def test_get_angles_square():
    fig = "square"
    square = Figure(fig, 2)
    assert square.get_angles == 4
