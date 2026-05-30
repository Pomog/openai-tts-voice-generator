from manim import *


class GravityIntegral(Scene):
    def construct(self):
        title = Text("Calculus in New Eden", font_size=44)

        formula1 = MathTex(r"F_r = -\frac{GMm}{r^2}")
        formula2 = MathTex(r"A = \int_{\infty}^{R} F_r\,dr")
        formula3 = MathTex(r"A = \int_{\infty}^{R} -\frac{GMm}{r^2}\,dr")
        formula4 = MathTex(r"A = \frac{GMm}{R}")
        formula5 = MathTex(r"v = \sqrt{v_\infty^2 + \frac{2GM}{R}}")

        title.to_edge(UP)
        formula1.move_to(ORIGIN)

        self.play(FadeIn(title, shift=UP))
        self.wait(0.5)

        self.play(Write(formula1))
        self.wait(1)

        self.play(TransformMatchingTex(formula1, formula2))
        self.wait(1)

        self.play(TransformMatchingTex(formula2, formula3))
        self.wait(1)

        self.play(TransformMatchingTex(formula3, formula4))
        self.wait(1)

        self.play(TransformMatchingTex(formula4, formula5))
        self.wait(2)