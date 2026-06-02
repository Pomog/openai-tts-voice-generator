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


from manim import *


class C3ForceToAcceleration(Scene):
    def construct(self):
        # ------------------------------------------------------------
        # Title
        # ------------------------------------------------------------
        title = Text(
            "Constant Mass: From Momentum to Acceleration",
            font_size=38,
        )
        title.to_edge(UP)

        # ------------------------------------------------------------
        # Formula positions
        # ------------------------------------------------------------
        main_formula_pos = RIGHT * 2.4 + UP * 0.95
        secondary_formula_pos = RIGHT * 2.4 + DOWN * 0.05
        note_pos = RIGHT * 2.4 + DOWN * 1.1
        gravity_note_pos = RIGHT * 2.4 + UP * 0.25

        def main_formula(tex):
            f = MathTex(tex)
            f.scale(1.35)
            f.move_to(main_formula_pos)
            return f

        def secondary_formula(tex):
            f = MathTex(tex)
            f.scale(1.15)
            f.move_to(secondary_formula_pos)
            return f

        # Formula chain
        f_newton = main_formula(r"\vec{F} = \frac{d\vec{p}}{dt}")
        f_momentum = main_formula(r"\vec{p} = m\vec{v}")
        f_substitute = main_formula(r"\vec{F} = \frac{d(m\vec{v})}{dt}")
        f_mass_outside = main_formula(r"\vec{F} = m\frac{d\vec{v}}{dt}")
        f_acceleration = secondary_formula(r"\frac{d\vec{v}}{dt} = \vec{a}")
        f_final = main_formula(r"\vec{F} = m\vec{a}")
        f_gravity = main_formula(r"\vec{F}_g = m\vec{a}")

        # Notes
        note_constant_mass = Text(
            "object with constant mass",
            font_size=26,
            color=YELLOW,
        ).move_to(note_pos)

        note_substitution = Text(
            "substitute momentum into Newton's second law",
            font_size=24,
            color=YELLOW,
        ).move_to(note_pos)

        note_mass_outside = Text(
            "mass does not change with time",
            font_size=24,
            color=YELLOW,
        ).move_to(note_pos)

        note_acceleration = Text(
            "velocity derivative = acceleration",
            font_size=25,
            color=ORANGE,
        ).move_to(RIGHT * 2.4 + DOWN * 1.45)

        note_force_changes_velocity = Text(
            "force changes velocity",
            font_size=27,
            color=GREEN,
        ).move_to(note_pos)

        note_gravity = Text(
            "in a gravitational field, this force is gravity",
            font_size=24,
            color=RED,
        ).move_to(gravity_note_pos)

        # ------------------------------------------------------------
        # Physical picture on the left
        # ------------------------------------------------------------
        planet = Circle(radius=0.7, color=BLUE)
        planet.set_fill(BLUE_E, opacity=0.85)
        planet.move_to(LEFT * 4.3 + DOWN * 1.55)

        planet_label = Text("planet", font_size=22)
        planet_label.next_to(planet, DOWN, buff=0.2)

        asteroid = Dot(
            point=LEFT * 0.6 + DOWN * 1.55,
            radius=0.12,
            color=WHITE,
        )

        asteroid_label = Text("asteroid", font_size=20)
        asteroid_label.next_to(asteroid, UP, buff=0.18)

        # Path line reaches the planet
        path = Line(
            planet.get_right(),
            asteroid.get_center(),
            color=GRAY_B,
            stroke_width=4,
        )

        # Velocity vector starts from asteroid center
        velocity_arrow = Arrow(
            asteroid.get_center(),
            asteroid.get_center() + RIGHT * 1.15,
            buff=0,
            color=YELLOW,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.25,
        )

        velocity_label = MathTex(r"\vec{v}", color=YELLOW).scale(0.85)
        velocity_label.next_to(velocity_arrow, DOWN, buff=0.1)

        # Gravity force arrow
        gravity_arrow = Arrow(
            asteroid.get_center(),
            asteroid.get_center() + LEFT * 1.15,
            buff=0,
            color=RED,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.25,
        )

        gravity_label = MathTex(r"\vec{F}_g", color=RED).scale(0.85)
        gravity_label.next_to(gravity_arrow, DOWN, buff=0.1)

        # Acceleration arrow placed below the gravity arrow
        acceleration_arrow = Arrow(
            asteroid.get_center() + DOWN * 1,
            asteroid.get_center() + DOWN * 1 + LEFT * 0.9,
            buff=0,
            color=ORANGE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.25,
        )

        acceleration_label = MathTex(r"\vec{a}", color=ORANGE).scale(0.85)
        acceleration_label.next_to(acceleration_arrow, DOWN, buff=0.1)

        left_note_1 = Text(
            "force points toward the planet",
            font_size=22,
            color=RED,
        )
        left_note_1.move_to(LEFT * 3.35 + DOWN * 0.2)

        left_note_2 = Text(
            "acceleration follows the force",
            font_size=22,
            color=ORANGE,
        )
        left_note_2.move_to(LEFT * 3.5 + DOWN * 3)

        # ------------------------------------------------------------
        # Animation
        # ------------------------------------------------------------
        self.play(FadeIn(title))
        self.wait(0.3)

        # Now let’s apply this to an object with constant mass.
        self.play(Write(f_newton))
        self.play(FadeIn(note_constant_mass, shift=UP))
        self.wait(1.0)

        # Since momentum is mass multiplied by velocity...
        self.play(
            FadeOut(note_constant_mass),
            ReplacementTransform(f_newton, f_momentum),
        )
        self.wait(0.9)

        # ...we can substitute it into Newton’s second law.
        self.play(
            ReplacementTransform(f_momentum, f_substitute),
            FadeIn(note_substitution, shift=UP),
        )
        self.wait(1.0)

        # Because the mass is constant, it does not change with time.
        self.play(
            FadeOut(note_substitution),
            FadeIn(note_mass_outside, shift=UP),
        )
        self.wait(1.0)

        # So we can move the mass outside the derivative.
        self.play(ReplacementTransform(f_substitute, f_mass_outside))
        self.wait(1.0)

        # The derivative of velocity with respect to time is acceleration.
        self.play(
            FadeOut(note_mass_outside),
            Write(f_acceleration),
            FadeIn(note_acceleration, shift=UP),
        )
        self.wait(1.2)

        # So Newton’s second law becomes the familiar formula.
        self.play(
            FadeOut(note_acceleration),
            FadeOut(f_acceleration),
            ReplacementTransform(f_mass_outside, f_final),
        )
        self.play(FadeIn(note_force_changes_velocity, shift=UP))
        self.wait(1.0)

        # This means force changes velocity.
        self.play(
            FadeIn(planet),
            FadeIn(planet_label),
            Create(path),
            FadeIn(asteroid),
            FadeIn(asteroid_label),
        )
        self.play(GrowArrow(velocity_arrow), FadeIn(velocity_label))
        self.wait(0.4)

        self.play(GrowArrow(gravity_arrow), FadeIn(gravity_label))
        self.play(FadeIn(left_note_1, shift=UP))
        self.wait(0.4)

        self.play(GrowArrow(acceleration_arrow), FadeIn(acceleration_label))
        self.play(FadeIn(left_note_2, shift=UP))
        self.wait(0.8)

        # In a gravitational field, this force is gravity.
        self.play(
            FadeOut(note_force_changes_velocity),
            ReplacementTransform(f_final, f_gravity),
        )
        self.wait(0.3)

        # Clean final state: keep only what helps
        self.play(
            FadeIn(note_gravity, shift=UP),
        )
        self.wait(2.0)

class C4WorkAlongPath(Scene):
    def construct(self):
        # ------------------------------------------------------------
        # Helper
        # ------------------------------------------------------------
        def pulse(mobj, color=YELLOW, scale_factor=1.15):
            self.play(
                Indicate(
                    mobj,
                    color=color,
                    scale_factor=scale_factor,
                ),
                run_time=0.8,
            )

        # ------------------------------------------------------------
        # Title
        # ------------------------------------------------------------
        title = Text("Work is the energy transferred to or from an object ", font_size=38)
        title.to_edge(UP)

        # ------------------------------------------------------------
        # Left-side physical picture
        # ------------------------------------------------------------
        planet = Circle(radius=0.75, color=BLUE)
        planet.set_fill(BLUE_E, opacity=0.85)
        planet.move_to(LEFT * 4.5 + DOWN * 1.0)

        planet_label = Text("planet", font_size=22)
        planet_label.next_to(planet, DOWN, buff=0.2)

        asteroid = Dot(point=LEFT * 0.8 + DOWN * 1.0, radius=0.12, color=WHITE)
        asteroid_label = Text("asteroid", font_size=20)
        asteroid_label.next_to(asteroid, UP, buff=0.15)

        path = Line(
            planet.get_right(),
            asteroid.get_center(),
            color=GRAY_B,
            stroke_width=4,
        )

        # Main force and displacement arrows: same direction
        force_arrow = Arrow(
            asteroid.get_center(),
            asteroid.get_center() + LEFT * 1.0,
            buff=0,
            color=RED,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
        )
        force_label = MathTex(r"\vec{F}", color=RED).scale(0.9)
        force_label.next_to(force_arrow, DOWN, buff=0.1)

        ds_arrow = Arrow(
            asteroid.get_center() + UP * 0.60,
            asteroid.get_center() + UP * 0.60+ LEFT * 0.95,
            buff=0,
            color=YELLOW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
        )
        ds_label = MathTex(r"d\vec{s}", color=YELLOW).scale(0.9)
        ds_label.next_to(ds_arrow, UP, buff=0.1)

        # Perpendicular displacement example
        ds_perp_arrow = Arrow(
            asteroid.get_center() + RIGHT * 0.6,
            asteroid.get_center() + RIGHT * 0.6 + UP * 0.95,
            buff=0,
            color=YELLOW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
        )
        ds_perp_label = MathTex(r"d\vec{s}", color=YELLOW).scale(0.9)
        ds_perp_label.next_to(ds_perp_arrow, RIGHT, buff=0.1)

        # Tiny path segments for line integral idea
        tiny_segments = VGroup()
        for i in range(7):
            x = interpolate(planet.get_right()[0], asteroid.get_center()[0], i / 6)
            seg = Line(
                [x - 0.12, asteroid.get_center()[1], 0],
                [x + 0.12, asteroid.get_center()[1], 0],
                color=YELLOW,
                stroke_width=5,
            )
            tiny_segments.add(seg)

        # ------------------------------------------------------------
        # Right-side formulas
        # ------------------------------------------------------------
        work_formula = MathTex(
            "W", "=", r"\int", r"\vec{F}", r"\cdot", r"d\vec{s}"
        )
        work_formula.scale(1.25)
        work_formula.move_to(RIGHT * 3.0 + UP * 1.2)

        gravity_formula = MathTex(
            r"\left|\vec{F}_g\right|", "=", r"\frac{GMm}{r^2}"
        )
        gravity_formula.scale(1.1)
        gravity_formula.move_to(RIGHT * 3.0 + UP * 0.1)

        velocity_formula = MathTex(
            r"\vec{v}", "=", r"\frac{d\vec{s}}{dt}"
        )
        velocity_formula.scale(1.1)
        velocity_formula.next_to(gravity_formula, DOWN, buff=0.45)

        ds_formula = MathTex(
            r"d\vec{s}", "=", r"\vec{v}", "dt"
        )
        ds_formula.scale(1.1)
        ds_formula.next_to(velocity_formula, DOWN, buff=0.45)

        work_time_formula = MathTex(
            "W", "=", r"\int", r"\vec{F}", r"\cdot", r"\vec{v}", "dt"
        )
        work_time_formula.scale(1.25)
        work_time_formula.move_to(RIGHT * 3.0 + UP * 1.2)

        # ------------------------------------------------------------
        # Notes
        # ------------------------------------------------------------
        note_work = Text(
            "work = force acting along displacement",
            font_size=24,
            color=GREEN,
        )
        note_work.move_to(UP * 2.2)

        note_parallel = Text(
            "same direction  →  kinetic energy increases",
            font_size=22,
            color=GREEN,
        )
        note_parallel.move_to(LEFT * 2.0 + DOWN * 2.6)

        note_perp = Text(
            "perpendicular  →  changes direction, not speed",
            font_size=22,
            color=ORANGE,
        )
        note_perp.move_to(LEFT * 1.4 + DOWN * 2.6)

        note_path = Text(
            "add tiny work pieces along the path",
            font_size=22,
            color=YELLOW,
        )
        note_path.next_to(force_arrow, UP, buff=1)
        # I am here 

        note_inverse_square = Text(
            "gravity gets stronger closer to the planet",
            font_size=22,
            color=RED,
        )
        note_inverse_square.move_to(RIGHT * 2.7 + DOWN * 2.55)

        note_velocity = Text(
            "velocity = displacement per unit time",
            font_size=22,
            color=BLUE,
        )
        note_velocity.move_to(RIGHT * 2.6 + DOWN * 2.55)

        # ------------------------------------------------------------
        # Start animation
        # ------------------------------------------------------------
        self.play(FadeIn(title))
        self.wait(0.3)

        self.play(
            FadeIn(planet),
            FadeIn(planet_label),
            Create(path),
            FadeIn(asteroid),
            FadeIn(asteroid_label),
        )

        # The gravitational field affects our asteroid by doing work on it.
        self.play(Write(work_formula))
        pulse(work_formula[0], color=GREEN)      # W
        self.play(FadeIn(note_work, shift=UP))
        self.wait(0.5)

        # Work is the energy transferred ... force acting along displacement, the dot product.
        pulse(work_formula.get_part_by_tex(r"\vec{F}"), color=RED)
        pulse(work_formula.get_part_by_tex(r"d\vec{s}"), color=YELLOW)
        pulse(work_formula.get_part_by_tex(r"\cdot"), color=YELLOW)

        self.play(GrowArrow(force_arrow), FadeIn(force_label))
        self.play(GrowArrow(ds_arrow), FadeIn(ds_label))
        self.wait(0.5)

        # If the force points along the displacement...
        self.play(FadeIn(note_parallel, shift=UP))
        pulse(force_arrow, color=RED)
        pulse(ds_arrow, color=YELLOW)
        self.wait(1.0)

        # If the force is perpendicular to the motion...
        self.play(
            FadeOut(ds_arrow),
            FadeOut(ds_label),
            FadeOut(note_parallel),
        )
        self.play(GrowArrow(ds_perp_arrow), FadeIn(ds_perp_label))
        self.play(FadeIn(note_perp, shift=UP))
        pulse(ds_perp_arrow, color=YELLOW)
        pulse(force_arrow, color=RED)
        self.wait(1.0)

        # Now imagine the object moves along a path.
        self.play(
            FadeOut(ds_perp_arrow),
            FadeOut(ds_perp_label),
            FadeOut(note_perp),
        )
        self.play(LaggedStart(*[Create(seg) for seg in tiny_segments], lag_ratio=0.12))
        self.play(FadeIn(note_path, shift=UP))
        pulse(work_formula.get_part_by_tex(r"\int_C"), color=YELLOW)
        self.wait(0.8)

        
        self.play(FadeOut(note_path, shift=RIGHT))

        # The force becomes stronger closer to the planet, inverse-square relation.
        self.play(Write(gravity_formula))
        pulse(gravity_formula.get_part_by_tex(r"\vec{F}_g"), color=RED)
        pulse(gravity_formula.get_part_by_tex(r"r^2"), color=ORANGE)
        self.play(FadeIn(note_inverse_square, shift=UP))
        self.wait(1.0)

        # So we cannot always use one force multiplied by one distance.
        self.play(
            Circumscribe(work_formula, color=WHITE, fade_out=True),
            run_time=1.0,
        )
        self.wait(0.4)

        # Instead, divide into tiny displacements ... calculus adds them together.
        pulse(tiny_segments, color=YELLOW, scale_factor=1.05)
        pulse(work_formula.get_part_by_tex(r"\int_C"), color=YELLOW)
        self.wait(0.8)

        # That is why work is written as the integral of force dotted with displacement.
        pulse(work_formula.get_part_by_tex(r"\vec{F}"), color=RED)
        pulse(work_formula.get_part_by_tex(r"\cdot"), color=BLUE)
        pulse(work_formula.get_part_by_tex(r"d\vec{s}"), color=YELLOW)
        self.wait(0.8)

        # Now we connect this to velocity.
        self.play(Write(velocity_formula))
        pulse(velocity_formula.get_part_by_tex(r"\vec{v}"), color=BLUE)
        pulse(velocity_formula.get_part_by_tex(r"d\vec{s}"), color=YELLOW)
        self.play(FadeOut(note_inverse_square), FadeIn(note_velocity, shift=UP))
        self.wait(0.8)

        self.play(FadeOut(note_velocity, shift=DOWN))

        # So a displacement can be written as velocity multiplied by a time step.
        self.play(Write(ds_formula))
        pulse(ds_formula.get_part_by_tex(r"d\vec{s}"), color=YELLOW)
        pulse(ds_formula.get_part_by_tex(r"\vec{v}"), color=BLUE)
        pulse(ds_formula.get_part_by_tex("dt"), color=GREEN)
        self.wait(1.0)

        # Instead of force dotted with displacement, we can write force dotted with velocity, integrated over time.
        self.play(
            TransformMatchingTex(work_formula.copy(), work_time_formula),
            FadeOut(work_formula),
        )
        self.wait(0.3)

        pulse(work_time_formula.get_part_by_tex(r"\vec{F}"), color=RED)
        pulse(work_time_formula.get_part_by_tex(r"\vec{v}"), color=BLUE)
        pulse(work_time_formula.get_part_by_tex("dt"), color=GREEN)
        self.wait(2.0)