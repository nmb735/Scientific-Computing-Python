# Define a base class for geometric shapes
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        # Set the dimensions of the shape.
        self.width = width
        self.height = height

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __str__(self):
        # Return a string representation of the rectangle.
        return f"Rectangle(width={self.width}, height={self.height})"
  
    def set_width(self, width):
        # Set the width of the rectangle.
        self.width = width

    def set_height(self, height):
        # Set the height of the rectangle.
        self.height = height

    def get_area(self):
        # Calculate and return the area of the rectangle.
        return self.width * self.height
  
    def get_perimeter(self):
        # Calculate and return the perimeter of the rectangle.
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # Calculate and return the diagonal length of the rectangle.
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # Return a string representing the rectangle as a picture of '*' characters.
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        shape = ""
        for i in range(self.height):
            shape += "*" * self.width + "\n"
        return shape

    def get_amount_inside(self, shape):
        # Calculate and return the number of times 'shape' can fit inside this rectangle.
        return (self.width // shape.width) * (self.height // shape.height)

# Define a Square class that inherits from Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        # Return a string representation of the square.
        return f"Square(side={self.width})"
  
    def set_side(self, side):
        # Set the side length of the square.
        self.set_dimensions(side, side)

    # Override the set_dimensions method to ensure the square remains square
    def set_dimensions(self, width, height):
        # Set the dimensions of the square, ensuring it remains a square.
        side_length = max(width, height)
        super().set_dimensions(side_length, side_length)

# Example usage:
if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    square = Square(5)
    print(rectangle)
    print(square)
    print(rectangle.get_area())
    print(square.get_area())
    square.set_dimensions(3, 3)
    print(square.get_picture())
    print(rectangle.get_amount_inside(square))
    rectangle.set_width(8)  # Adding a call to set_width
    print(rectangle)
