"""Formal definition of the directional derivative (Manim Community).

Render from the repository root:
    .venv/bin/manim -pql scripts/manim_scenes/directional_derivative.py DirectionalDerivative

Use -pqh for a high-quality render. MathTex requires a working LaTeX installation.
"""

from manim import *
import numpy as np


class DirectionalDerivative(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#101624"

        def overlay(*mobjects):
            self.add_fixed_in_frame_mobjects(*mobjects)
            self.remove(*mobjects)
            self.play(*(FadeIn(m) for m in mobjects))

        def clear():
            objects = list(self.mobjects)
            self.play(*(FadeOut(m) for m in objects))
            self.remove_fixed_in_frame_mobjects(*objects)

        title = Text("The directional derivative", font_size=42).to_edge(UP)
        assumptions = VGroup(
            MathTex(r"f:U\subseteq\mathbb R^n\to\mathbb R,\qquad U\text{ open}"),
            MathTex(r"\mathbf a\in U,\qquad \mathbf u\in\mathbb R^n,\quad\|\mathbf u\|=1"),
            Text("Choose a point and a unit direction.", font_size=27, color=GRAY_B),
        ).arrange(DOWN, buff=0.45).shift(UP * 0.8)
        definition = MathTex(
            r"D_{\mathbf u}f(\mathbf a)", "=", r"\lim_{h\to0}",
            r"\frac{f(\mathbf a+h\mathbf u)-f(\mathbf a)}{h}",
            font_size=45,
        ).shift(DOWN * 1.1)
        definition[0].set_color(YELLOW)
        condition = Text(
            "The derivative exists when this two-sided limit is finite.",
            font_size=25,
        ).to_edge(DOWN, buff=0.65)
        overlay(title)
        self.play(Write(assumptions))
        self.wait(2)
        self.play(Write(definition))
        self.play(FadeIn(condition))
        self.wait(3)
        clear()

        # Restrict a surface to the straight line a + h u in its domain.
        self.set_camera_orientation(phi=65 * DEGREES, theta=-55 * DEGREES)
        heading = Text("Follow one line across the surface", font_size=35).to_edge(UP)
        example = MathTex(
            r"f(x,y)=\frac{x^2+y^2}{2},\quad"
            r"\mathbf a=(1,0),\quad\mathbf u=\left(\frac35,\frac45\right)",
            font_size=30,
        ).next_to(heading, DOWN)
        axes = ThreeDAxes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1], z_range=[0, 4, 1],
            x_length=6, y_length=6, z_length=3.5,
        ).shift(DOWN * 0.7)
        surface = Surface(
            lambda x, y: axes.c2p(x, y, (x*x + y*y) / 2),
            u_range=[-1.8, 1.8], v_range=[-1.8, 1.8],
            resolution=(20, 20), fill_opacity=0.35,
            checkerboard_colors=[BLUE_D, BLUE_E], stroke_width=0.3,
        )
        a = np.array([1.0, 0.0])
        u = np.array([0.6, 0.8])

        def point(h, on_surface=True):
            x, y = a + h * u
            return axes.c2p(x, y, (x*x + y*y) / 2 if on_surface else 0)

        domain_line = Line(point(-1.6, False), point(1.1, False), color=GREEN)
        direction = Arrow3D(point(0, False), point(0.8, False), color=GREEN)
        lifted_curve = ParametricFunction(point, t_range=[-1.6, 1.1], color=YELLOW)
        base_dot = Dot3D(point(0), color=YELLOW)
        caption = MathTex(
            r"g(h)=f(\mathbf a+h\mathbf u)\quad\Longrightarrow\quad "
            r"D_{\mathbf u}f(\mathbf a)=g'(0)", font_size=34,
        ).to_edge(DOWN, buff=0.45)
        overlay(heading, example)
        self.play(Create(axes), FadeIn(surface), run_time=2)
        self.play(Create(domain_line), FadeIn(direction))
        self.play(Create(lifted_curve), FadeIn(base_dot), run_time=2)
        overlay(caption)
        self.wait(3)
        clear()

        # Plot the one-variable restriction and its secant slopes.
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        heading = Text("Secant slopes approach the tangent slope", font_size=34).to_edge(UP)
        formula = MathTex(r"g(h)=\frac12+\frac35h+\frac12h^2", font_size=34)
        formula.next_to(heading, DOWN)
        axes = Axes(
            x_range=[-1.6, 1.6, 0.5], y_range=[0, 3, 1],
            x_length=7, y_length=4.2, tips=False,
        ).shift(LEFT * 2 + DOWN * 0.55)
        labels = axes.get_axis_labels(MathTex("h"), MathTex("g(h)"))
        g = lambda h: 0.5 + 0.6*h + 0.5*h*h
        graph = axes.plot(g, x_range=[-1.5, 1.5], color=BLUE_B)
        h = ValueTracker(1.3)
        anchor = Dot(axes.c2p(0, g(0)), color=YELLOW)
        moving = always_redraw(lambda: Dot(axes.c2p(h.get_value(), g(h.get_value())), color=GREEN))
        # Simplified quotient is well defined at zero, avoiding numerical division.
        secant = always_redraw(lambda: axes.plot(
            lambda t: g(0) + (0.6 + 0.5*h.get_value()) * t,
            x_range=[-1.3, 1.4], color=GREEN,
        ))
        panel = VGroup(
            MathTex(r"\frac{g(h)-g(0)}h=\frac35+\frac h2", font_size=31),
            Text("Signed step", font_size=24),
            VGroup(MathTex("h="), DecimalNumber(1.3, num_decimal_places=2)).arrange(RIGHT),
            Text("Secant slope", font_size=24, color=GREEN),
            DecimalNumber(1.25, num_decimal_places=3, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to(RIGHT * 4.1)
        panel[2][1].add_updater(lambda m: m.set_value(h.get_value()))
        panel[4].add_updater(lambda m: m.set_value(0.6 + 0.5*h.get_value()))
        note = Text("Approach zero from positive steps.", font_size=26).to_edge(DOWN)
        self.play(FadeIn(heading), Write(formula), Create(axes), Write(labels))
        self.play(Create(graph), FadeIn(anchor), FadeIn(panel), FadeIn(note))
        self.add(secant, moving)
        self.play(h.animate.set_value(0.04), run_time=4)
        self.wait(1)
        self.remove(secant, moving)
        h.set_value(-1.3)
        self.add(secant, moving)
        new_note = Text("Approach zero from negative steps, too.", font_size=26).to_edge(DOWN)
        self.play(Transform(note, new_note))
        self.play(h.animate.set_value(-0.04), run_time=4)
        tangent = axes.plot(lambda t: 0.5 + 0.6*t, x_range=[-0.8, 1.5], color=YELLOW)
        self.play(Create(tangent), FadeOut(secant), FadeOut(moving))
        result = MathTex(r"g'(0)=\frac35", color=YELLOW).move_to(panel)
        panel.clear_updaters()
        self.play(ReplacementTransform(panel, result))
        self.wait(2)
        clear()

        # Formal epsilon-delta condition and the differentiable special case.
        heading = Text("What does the limit require?", font_size=38).to_edge(UP)
        formal = VGroup(
            MathTex(r"D_{\mathbf u}f(\mathbf a)=L\quad\Longleftrightarrow", font_size=38),
            MathTex(r"\forall\varepsilon>0\;\exists\delta>0\;\forall h\in\mathbb R:", font_size=35),
            MathTex(
                r"0<|h|<\delta\quad\Longrightarrow\quad "
                r"\left|\frac{f(\mathbf a+h\mathbf u)-f(\mathbf a)}h-L\right|<\varepsilon",
                font_size=34,
            ),
            Text("Choose delta small enough that a + h u stays in U.", font_size=24, color=GRAY_B),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.6)
        gradient = VGroup(
            Text("If f is differentiable at a:", font_size=27),
            MathTex(r"D_{\mathbf u}f(\mathbf a)=\nabla f(\mathbf a)\cdot\mathbf u", color=YELLOW),
            MathTex(r"\nabla f(1,0)=(1,0)\quad\Rightarrow\quad (1,0)\cdot(3/5,4/5)=3/5", font_size=30),
        ).arrange(DOWN, buff=0.3).shift(DOWN * 2)
        self.play(FadeIn(heading), Write(formal), run_time=3)
        self.wait(3)
        self.play(Write(gradient), run_time=2)
        self.wait(4)
