class TestSquare:
    def test_add_circle_area(self, default_circle, default_rectangle, default_square, default_triangle):
        """Checks that circle area can be added to other figure area """
        assert default_circle.area + default_rectangle.area == 7738.5, "Sum of circle area and rectangle area counted wrongly"
        assert default_circle.area + default_square.area == 6407.5, "Sum of circle area and circle area counted wrongly"
        assert default_circle.area + default_triangle.area == 6446.68, "Sum of circle area and triangle area counted wrongly"

    def test_add_rectangle_area(self, default_circle, default_rectangle, default_square, default_triangle):
        """Checks that rectangle area can be added to other figure area """
        assert default_rectangle.area + default_circle.area == 7738.5, "Sum of rectangle area and circle area counted wrongly"
        assert default_rectangle.area + default_square.area == 1429, "Sum of rectangle area and square area counted wrongly"
        assert default_rectangle.area + default_triangle.area == 1468.18, "Sum of rectangle area and triangle area counted wrongly"

    def test_add_square_area(self, default_circle, default_rectangle, default_square, default_triangle):
        """Checks that square area can be added to other figure area """
        assert default_square.area + default_circle.area == 6407.5, "Sum of square area and circle area counted wrongly"
        assert default_square.area + default_rectangle.area == 1429, "Sum of square area and rectangle area counted wrongly"
        assert default_square.area + default_triangle.area == 137.18, "Sum of square area and triangle area counted wrongly"

    def test_add_triangle_area(self, default_circle, default_rectangle, default_square, default_triangle):
        """Checks that triangle area can be added to other figure area """
        assert default_triangle.area + default_circle.area == 6446.68, "Sum of triangle area and circle area counted wrongly"
        assert default_triangle.area + default_rectangle.area == 1468.18, "Sum of triangle area and rectangle area counted wrongly"
        assert default_triangle.area + default_square.area == 137.18, "Sum of triangle area and square area counted wrongly"
