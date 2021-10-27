class TestCircle:
    def test_name(self, default_circle):
        """Checks correctness of figure name"""
        assert default_circle.name == "circle", "Figure has a wrong name"

    def test_counting_area(self, default_circle):
        """Checks area is counting correctly for circle"""
        assert default_circle.area == 6358.5, "Area is counted wrongly"

    def test_counting_perimeter(self, default_circle):
        """Checks perimeter is counting correctly for circle"""
        assert default_circle.perimeter == 282.6, "Perimeter is counted wrongly"

