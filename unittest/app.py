class Figure:
    FIGURES = ["square", "rectangle", "triangle"]

    def __init__(self, figure_type, length) -> None:
        assert length > 0
        assert figure_type in self.FIGURES
        self.figure_type = figure_type
        self.length = length

    @property
    def get_figure_type(self):
        return self.figure_type

    @property
    def get_figure_length(self):
        return self.length

    @property
    def get_angles(self):
        if self.figure_type in ["square", "rectangle"]:
            return 4
        if self.figure_type == "triangle":
            return 3
