from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()                   # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(ShowCreation(circle))     # show the circle on screen


class SquareToCircle2(Scene):
    def construct(self):
        circle = Circle()                    # create a circle
        circle.set_fill(PINK, opacity=0.5)   # set color and transparency

        square = Square()                    # create a square
        square.flip(RIGHT)                   # flip horizontally
        square.rotate(-3 * TAU / 8)          # rotate a certain amount

        self.play(ShowCreation(square))      # animate the creation of the square
        self.play(Transform(square, circle)) # interpolate the square into the circle
        self.play(FadeOut(square))           # fade out animation
    