from manim import *

class C6GravityIntroPart1(Scene):
    def construct(self):
        # ------------------------------------------------------------
        # Helper
        # ------------------------------------------------------------
        def pulse(mobj, color=YELLOW, scale_factor=1.12):
            self.play(
                Indicate(mobj, color=color, scale_factor=scale_factor),
                run_time=0.7,
            )

        # ------------------------------------------------------------
        # Title
        # ------------------------------------------------------------
        title = Text("Calculus Applied to Gravity", font_size=40)
        title.to_edge(UP)

        # ------------------------------------------------------------
        # Physical picture: planet and asteroid
        # ------------------------------------------------------------
        planet = Circle(radius=0.75, color=BLUE)
        planet.set_fill(BLUE_E, opacity=0.85)
        planet.move_to(LEFT * 4.5 + DOWN * 1.0)

        planet_label = Text("planet", font_size=22)
        planet_label.next_to(planet, DOWN, buff=0.2)

        planet_mass_label = MathTex("M", color=BLUE_B).scale(1.0)
        planet_mass_label.move_to(planet.get_center())
        planet_mass_label.shift(LEFT * 0.35)

        asteroid = Dot(point=LEFT * 0.8 + DOWN * 1.0, radius=0.12, color=WHITE)
        asteroid_label = Text("asteroid", font_size=20)
        asteroid_label.next_to(asteroid, UP, buff=0.15)

        asteroid_mass_label = MathTex("m", color=WHITE).scale(0.9)
        asteroid_mass_label.next_to(asteroid, RIGHT, buff=0.2)

        # Center-to-center line and r label
        center_line = DashedLine(
            planet.get_center(),
            asteroid.get_center(),
            color=GRAY_B,
            stroke_width=4,
            dash_length=0.12,
        )

        r_double_arrow = DoubleArrow(
            planet.get_center() + UP * 0.70,
            asteroid.get_center() + UP * 0.70,
            buff=0,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.08,
        )
        r_label = MathTex("r", color=YELLOW).scale(1.0)
        r_label.next_to(r_double_arrow, UP, buff=0.12)

        # Mutual attraction arrows
        force_on_asteroid = Arrow(
            asteroid.get_center(),
            asteroid.get_center() + LEFT * 1.0,
            buff=0,
            color=RED,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
        )
        force_asteroid_label = MathTex(r"\vec{F}_{g}", color=RED).scale(0.8)
        force_asteroid_label.next_to(force_on_asteroid, DOWN, buff=0.08)

        force_on_planet = Arrow(
            planet.get_center(),
            planet.get_center() + RIGHT * 0.85,
            buff=0,
            color=RED,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
        )
        force_planet_label = MathTex(r"-\vec{F}_{g}", color=RED).scale(0.75)
        force_planet_label.next_to(force_on_planet, UP, buff=0.1)

        # Radius and altitude illustration
        radius_line = Line(
            planet.get_center(),
            planet.get_right(),
            color=GREEN,
            stroke_width=5,
        )
        radius_label = MathTex("R", color=GREEN).scale(0.85)
        radius_label.next_to(radius_line, DOWN, buff=0.12)

        altitude_line = Line(
            planet.get_right(),
            asteroid.get_center(),
            color=ORANGE,
            stroke_width=5,
        )
        altitude_label = MathTex("h", color=ORANGE).scale(0.85)
        altitude_label.next_to(altitude_line, DOWN, buff=0.12)

        # ------------------------------------------------------------
        # Right-side formulas and notes
        # ------------------------------------------------------------
        formula_pos = RIGHT * 3.25 + UP * 1.45
        note_pos = RIGHT * 3.25 + DOWN * 2.45

        law_title = Text("Newtonian gravitational interaction", font_size=25)
        law_title.move_to(formula_pos + UP * 0.55)

        gravity_formula = MathTex(
            "F_g", "=", r"\frac{G M m}{r^2}"
        )
        gravity_formula.scale(1.2)
        gravity_formula.next_to(law_title, DOWN, buff=0.35)

        constants = VGroup(
            Text("G  gravitational constant", font_size=22, color=YELLOW),
            Text("M  planet mass", font_size=22, color=BLUE_B),
            Text("m  asteroid mass", font_size=22, color=WHITE),
            Text("r  center-to-center distance", font_size=22, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        constants.next_to(gravity_formula , DOWN, buff=0.35)
        constants.shift(RIGHT * 0.2)

        r_not_zero = MathTex(r"r \ne 0", color=RED)
        r_not_zero.scale(1.3)
        r_not_zero.move_to(RIGHT * 3.25 + UP * 1.15)

        division_note = Text(
            "division by zero is undefined",
            font_size=23,
            color=RED,
        )
        division_note.next_to(r_not_zero, DOWN, buff=0.3)

        next_formula = MathTex(r"W_g", "=", r"\int", r"\vec{F}_g", r"\cdot", r"d\vec{r}")
        next_formula.scale(1.2)
        next_formula.move_to(RIGHT * 3.15 + DOWN * 2.1)

        # ------------------------------------------------------------
        # Animation sequence matching voice script part 1
        # ------------------------------------------------------------
        self.play(FadeIn(title))
        self.wait(0.3)

        # Newton's law describes the force between two masses.
        self.play(
            FadeIn(planet),
            FadeIn(planet_label),
            FadeIn(planet_mass_label),
            FadeIn(asteroid),
            FadeIn(asteroid_label),
            FadeIn(asteroid_mass_label),
        )
        self.wait(0.4)

        # Strictly speaking, both objects attract each other, and both can move.
        self.play(GrowArrow(force_on_asteroid), FadeIn(force_asteroid_label))
        self.play(GrowArrow(force_on_planet), FadeIn(force_planet_label))
        self.wait(0.8)

        # Distance r is center-to-center.
        self.play(Create(center_line))
        self.play(GrowArrow(r_double_arrow), FadeIn(r_label))
        pulse(r_double_arrow, color=YELLOW, scale_factor=1.05)
        self.wait(0.6)

        # Newton's gravitational formula.
        self.play(Write(law_title))
        self.play(Write(gravity_formula))
        pulse(gravity_formula, color=RED)
        self.wait(0.5)

        self.play(FadeIn(constants, shift=UP * 0.2))
        pulse(constants[0], color=YELLOW)
        pulse(constants[1], color=BLUE)
        pulse(constants[2], color=WHITE)
        pulse(constants[3], color=YELLOW)
        self.wait(0.5)

        # r cannot be zero.
        self.play(
            FadeOut(law_title),
            FadeOut(constants),
        )
        self.play(gravity_formula.animate.move_to(RIGHT * 3.25 + UP * 2.05))
        self.play(Write(r_not_zero), FadeIn(division_note, shift=UP * 0.2))
        pulse(r_not_zero, color=RED, scale_factor=1.2)
        self.wait(0.8)

        self.play(FadeOut(division_note), FadeOut(r_not_zero))
        self.play(Create(radius_line), FadeIn(radius_label))
        self.play(Create(altitude_line), FadeIn(altitude_label))
        self.wait(0.8)

        # Newtonian gravity is a classical model; limits.
        self.play(
            FadeOut(gravity_formula),
        )
        self.wait(1.0)

        # Transition to next part: work integral.
        self.play(
            FadeOut(force_on_planet),
            FadeOut(force_planet_label),
        )
        self.play(Write(next_formula))
        pulse(next_formula.get_part_by_tex(r"\vec{F}_g"), color=RED)
        pulse(next_formula.get_part_by_tex(r"d\vec{r}"), color=YELLOW)
        self.wait(2.0)