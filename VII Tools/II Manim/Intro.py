from manim import *

class CreateCirce(Scene):
    def construct(self):
        circle = Circle()  # Create a circle
        circle.set_fill(PINK, opacity=0.5)  # Set the color and transparency
        self.play(Create(circle))  # Show the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        square = Square() # Create a square
        se

