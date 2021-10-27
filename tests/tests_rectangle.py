class TestSquare:
    def test_name(self, default_rectangle):
        """Checks correctness of figure name"""
        assert default_rectangle.name == "rectangle", "Figure has a wrong name"

    def test_counting_area(self, default_rectangle):
        """Checks area is counting correctly for rectangle"""
        assert default_rectangle.area == 1380, "Area is counted wrongly"

    def test_counting_perimeter(self, default_rectangle):
        """Checks perimeter is counting correctly for rectangle"""
        assert default_rectangle.perimeter == 214, "Perimeter is counted wrongly"

