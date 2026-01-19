class Figure:
    def __init__(self, figure_type, length) -> None:
        assert length > 0, "Length must be greater than zero"
        assert figure_type in ["square", "rectangle", "triangle"], "Invalid figure type"
        self.figure_type = figure_type
        self.length = length


a = Figure("trapezoid", 12)
b = Figure("square", 0)
c = Figure("square", 1)
