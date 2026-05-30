from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class MomentumDerivative(Scene):
    def construct(self):
        title = Text("Force is the rate of change of momentum", font_size=36)
        title.to_edge(UP)

        formula = MathTex(r"\vec{F}=\frac{d\vec{p}}{dt}")
        formula.next_to(title, DOWN, buff=0.35)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 9, 1],
            x_length=9,
            y_length=5,
            axis_config={"include_tip": True},
        )
        axes.to_edge(DOWN)

        axis_labels = axes.get_axis_labels(
            MathTex("t"),
            MathTex("p(t)")
        )

        # Example momentum function.
        # This is not yet gravity-specific.
        # It simply shows momentum increasing with time.
        def p(t):
            return 0.22 * t**2 + 0.45 * t + 0.8

        # Derivative of p(t).
        # This is dp/dt.
        def dp_dt(t):
            return 0.44 * t + 0.45

        graph = axes.plot(
            p,
            x_range=[0, 6],
            color=BLUE,
        )

        t_tracker = ValueTracker(0.5)

        moving_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    t_tracker.get_value(),
                    p(t_tracker.get_value())
                ),
                color=YELLOW
            )
        )

        tangent_line = always_redraw(
            lambda: self.make_tangent_line(
                axes,
                p,
                dp_dt,
                t_tracker.get_value()
            )
        )

        derivative_label = always_redraw(
            lambda: MathTex(
                r"\frac{dp}{dt} = ",
                f"{dp_dt(t_tracker.get_value()):.2f}",
                r"\quad \Rightarrow \quad F"
            )
            .scale(0.8)
            .to_corner(UR)
        )

        explanation = Text(
            "The steeper the curve, the larger the force.",
            font_size=28
        )
        explanation.next_to(formula, DOWN, buff=0.3)

        self.play(FadeIn(title))
        self.play(Write(formula))
        self.wait(0.5)

        self.play(Create(axes), Write(axis_labels))
        self.play(Create(graph))
        self.wait(0.5)

        self.play(FadeIn(explanation))
        self.add(moving_dot, tangent_line, derivative_label)

        self.play(
            t_tracker.animate.set_value(5.5),
            run_time=6,
            rate_func=linear
        )

        self.wait(2)

    def make_tangent_line(self, axes, p, dp_dt, t):
        slope = dp_dt(t)

        dx = 0.9
        x1 = max(0, t - dx)
        x2 = min(6, t + dx)

        y1 = p(t) + slope * (x1 - t)
        y2 = p(t) + slope * (x2 - t)

        return Line(
            axes.c2p(x1, y1),
            axes.c2p(x2, y2),
            color=YELLOW,
            stroke_width=5
        )
    

class C1Intro(Scene):
    def construct(self):
        # Title
        title = Text("Calculus in New Eden", font_size=46)
        subtitle = Text("Asteroid in a planet's gravitational field", font_size=28)
        title.to_edge(UP)
        subtitle.next_to(title, DOWN, buff=0.2)

        # Planet
        planet = Circle(radius=1.2, color=BLUE)
        planet.set_fill(BLUE_E, opacity=0.9)
        planet.move_to(LEFT * 4 + DOWN * 0.7)
        planet_label = Text("Planet", font_size=24).next_to(planet, DOWN)

        # Asteroid
        asteroid = Dot(point=RIGHT * 2 + UP * 1.2, radius=0.12, color=WHITE)
        asteroid_label = Text("Asteroid", font_size=24).next_to(asteroid, DOWN)

        # Velocity arrow
        velocity_arrow = Arrow(
            asteroid.get_center() + LEFT * 0.8,
            asteroid.get_center() + RIGHT * 0.8,
            buff=0,
            color=YELLOW
        )
        v_label = MathTex(r"\vec{v}", color=YELLOW).next_to(velocity_arrow, UP, buff=0.1)

        # Gravity arrow toward the planet
        gravity_arrow = Arrow(
            asteroid.get_center(),
            planet.get_center() + RIGHT * 1.1 + UP * 0.3,
            buff=0.1,
            color=RED
        )
        g_label = MathTex(r"\vec{F}_g", color=RED).next_to(gravity_arrow, UP, buff=0.1)

        # Optional field rings
        field_ring_1 = Circle(radius=1.8, color=BLUE_D).move_to(planet.get_center())
        field_ring_2 = Circle(radius=2.5, color=BLUE_D).move_to(planet.get_center())
        field_ring_1.set_stroke(opacity=0.35)
        field_ring_2.set_stroke(opacity=0.25)

        # Questions
        q1 = Text("How can calculus explain its velocity?", font_size=28)
        q2 = Text("How much will it accelerate?", font_size=28)
        q3 = Text("How fast can it become?", font_size=28)

        questions = VGroup(q1, q2, q3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.35
        )
        questions.move_to(RIGHT * 2.0 + DOWN * 1.6)

        # Animation
        self.play(FadeIn(title, shift=UP), FadeIn(subtitle, shift=UP))
        self.wait(0.5)

        self.play(Create(field_ring_1), Create(field_ring_2))
        self.play(FadeIn(planet), FadeIn(planet_label))
        self.play(FadeIn(asteroid), FadeIn(asteroid_label))
        self.play(GrowArrow(velocity_arrow), FadeIn(v_label))
        self.play(GrowArrow(gravity_arrow), FadeIn(g_label))
        self.wait(0.5)

        self.play(Write(q1))
        self.wait(0.8)
        self.play(Write(q2))
        self.wait(0.8)
        self.play(Write(q3))
        self.wait(2)

class C2Momentum(Scene):
    def construct(self):
        # Title
        title = Text("Momentum and Force", font_size=44).to_edge(UP)

        # Historical wording idea
        line1 = Text("Newton's second law connects force and motion.", font_size=30)
        line1.move_to(UP * 2)

        motion_text = Text('"motion"', font_size=42, color=YELLOW)
        momentum_text = Text('"momentum"', font_size=42, color=GREEN)

        note = Text("In modern language:", font_size=26)

        # Put the note first, then place both words to the right of it.
        note.move_to(LEFT * 2.2 + UP * 0.8)

        motion_text.next_to(note, RIGHT, buff=0.35)
        momentum_text.next_to(note, RIGHT, buff=0.35)

        # Momentum formula
        formula_p = MathTex(r"\vec{p} = m\vec{v}")
        formula_p.scale(1.3)
        formula_p.move_to(ORIGIN)

        # Meaning of momentum
        item1 = Text("mass", font_size=26)
        item2 = Text("speed", font_size=26)
        item3 = Text("direction", font_size=26)

        meaning = VGroup(item1, item2, item3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.25
        )
        meaning.move_to(RIGHT * 4 + DOWN * 0.3)

        # Small vector picture
        particle = Dot(point=LEFT * 4 + DOWN * 0.6, radius=0.12, color=WHITE)

        v_arrow = Arrow(
            particle.get_center(),
            particle.get_center() + RIGHT * 1.8,
            buff=0,
            color=YELLOW
        )
        p_arrow = Arrow(
            particle.get_center(),
            particle.get_center() + RIGHT * 2.3,
            buff=0,
            color=GREEN
        )

        v_label = MathTex(r"\vec{v}", color=YELLOW).next_to(v_arrow, UP, buff=0.1)
        p_label = MathTex(r"\vec{p}", color=GREEN).next_to(p_arrow, DOWN, buff=0.1)

        direction_text = Text("Both have direction", font_size=24)
        direction_text.next_to(particle, DOWN, buff=0.7)

        # Force formula
        formula_f = MathTex(r"\vec{F} = \frac{d\vec{p}}{dt}")
        formula_f.scale(1.3)
        formula_f.move_to(DOWN * 2.2)

        rate_text = Text("Force = rate of change of momentum", font_size=26)
        rate_text.next_to(formula_f, DOWN, buff=0.35)

        # Animation
        self.play(FadeIn(title))
        self.play(Write(line1))
        self.wait(0.7)

        self.play(FadeIn(note), FadeIn(motion_text))
        self.wait(0.5)
        self.play(Transform(motion_text, momentum_text))
        self.wait(0.8)

        self.play(Write(formula_p))
        self.wait(0.8)

        self.play(FadeIn(particle))
        self.play(GrowArrow(v_arrow), FadeIn(v_label))
        self.play(GrowArrow(p_arrow), FadeIn(p_label))
        self.play(FadeIn(direction_text))

        self.play(
            FadeIn(meaning[0], shift=RIGHT),
            FadeIn(meaning[1], shift=RIGHT),
            FadeIn(meaning[2], shift=RIGHT),
        )
        self.wait(1.2)

        self.play(Write(formula_f))
        self.play(FadeIn(rate_text, shift=UP))
        self.wait(2)