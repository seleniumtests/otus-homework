class Figure:
    Pi = 3.14

    def add_area(self, figure_name):
        if figure_name.name not in ["circle", "rectangle", "square", "triangle"]:
            raise ValueError("Wrong class name")
        print(self.area + figure_name.area)
