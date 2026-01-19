def triangle_area(base, height):
    """
    Обчислює площу трикутника за формулою S = (base * height) / 2
    """
    if base <= 0 or height <= 0:
        return 0
    return (base * height) / 2
