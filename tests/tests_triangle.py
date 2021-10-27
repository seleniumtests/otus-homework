class TestSquare:
    def test_name(self, default_triangle):
        """Checks area is counting correctly for triangle"""
        assert default_triangle.name == "triangle", "Figure has a wrong name"

    def test_counting_area(self, default_triangle):
        """Checks area is counting correctly for triangle"""
        assert default_triangle.area == 88.18, "Area is counted wrongly"

    def test_counting_perimeter(self, default_triangle):
        """Checks perimeter is counting correctly for triangle"""
        assert default_triangle.perimeter == 48, "Perimeter is counted wrongly"

    def test_triangle_exists(self, triangle_with_bigger_first_side, triangle_with_bigger_second_side,
                             triangle_with_bigger_third_side):
        """Checks triangle can't exist if one of the side more than the sum of two others"""
        assert triangle_with_bigger_first_side is None, "Such triangle exists"
        assert triangle_with_bigger_second_side is None, "Such triangle exists"
        assert triangle_with_bigger_third_side is None, "Such triangle exists"
