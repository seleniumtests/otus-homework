class TestSquare:
    def test_name(self, default_square):
        """Checks correctness of figure name"""
        assert default_square.name == "square", "Figure has a wrong name"

    def test_counting_area(self, default_square):
        """Checks area is counting correctly for square"""
        assert default_square.area == 49, "Area is counted wrongly"

    def test_counting_perimeter(self, default_square):
        """Checks perimeter is counting correctly for square"""
        assert default_square.perimeter == 28, "Perimeter is counted wrongly"

