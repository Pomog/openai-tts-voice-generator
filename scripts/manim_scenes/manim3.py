from manim import *


class C7EscapeVelocityFromWorkStraight(Scene):
    def construct(self):
        # ------------------------------------------------------------
        # Helper
        # ------------------------------------------------------------
        def pulse(mobj, color=YELLOW, scale_factor=1.12):
            self.play(
                Indicate(
                    mobj,
                    color=color,
                    scale_factor=scale_factor,
                ),
                run_time=0.65,
            )

        def right_formula(tex, scale=1.0, y=1.25):
            f = MathTex(tex)
            f.scale(scale)
            f.move_to(RIGHT * 3.15 + UP * y)
            return f

        def make_note(text, color=YELLOW, y=-2.55, size=22):
            note = Text(text, font_size=size, color=color)
            note.move_to(RIGHT * 3.15 + UP * y)
            return note

        # ------------------------------------------------------------
        # Title
        # ------------------------------------------------------------
        title = Text("From Gravitational Work to Escape Velocity", font_size=36)
        title.to_edge(UP)

        # ------------------------------------------------------------
        # Left-side physical picture
        # Same planet / asteroid style and position as C6GravityIntroPart1
        # ------------------------------------------------------------
        planet = Circle(radius=0.75, color=BLUE)
        planet.set_fill(BLUE_E, opacity=0.85)
        planet.move_to(LEFT * 4.5 + DOWN * 1.0)

        planet_label = Text("Planet", font_size=22)
        planet_label.next_to(planet, DOWN, buff=0.2)

        planet_mass_label = MathTex("M", color=BLUE_B).scale(1.0)
        planet_mass_label.move_to(planet.get_center())
        planet_mass_label.shift(LEFT * 0.35)

        asteroid = Dot(point=LEFT * 0.8 + DOWN * 1.0, radius=0.12, color=WHITE)
        asteroid_label = Text("asteroid", font_size=20)
        asteroid_label.next_to(asteroid, UP, buff=0.15)

        asteroid_mass_label = MathTex("m", color=WHITE).scale(0.9)
        asteroid_mass_label.next_to(asteroid, RIGHT, buff=0.2)

        # Straight radial line only. No bent path.
        radial_line = Line(
            planet.get_right(),
            asteroid.get_center(),
            color=GRAY_B,
            stroke_width=4,
        )

        center_line = DashedLine(
            planet.get_center(),
            asteroid.get_center(),
            color=GRAY_B,
            stroke_width=3,
            dash_length=0.12,
        )

        # Starting distance r0
        r0_double_arrow = DoubleArrow(
            planet.get_center() + UP * 0.70,
            asteroid.get_center() + UP * 0.70,
            buff=0,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.08,
        )
        r0_label = MathTex(r"r_0", color=YELLOW).scale(0.85)
        r0_label.next_to(r0_double_arrow, UP, buff=0.12)

        # Final radius rf = R
        radius_line = Line(
            planet.get_center(),
            planet.get_right(),
            color=GREEN,
            stroke_width=5,
        )
        rf_label = MathTex(r"r_f=R", color=GREEN).scale(0.82)
        rf_label.next_to(radius_line, DOWN, buff=0.12)

        infinity_label = MathTex(r"r_0\to\infty", color=BLUE_B).scale(0.75)
        infinity_label.next_to(asteroid, RIGHT, buff=0.35)
        infinity_label.shift(DOWN * 0.35)

        # Field rings in the same visual language as earlier
        ring_1 = Circle(radius=1.35, color=BLUE_D).move_to(planet.get_center())
        ring_2 = Circle(radius=2.0, color=BLUE_D).move_to(planet.get_center())
        ring_3 = Circle(radius=2.65, color=BLUE_D).move_to(planet.get_center())
        for ring, opacity in [(ring_1, 0.35), (ring_2, 0.25), (ring_3, 0.18)]:
            ring.set_stroke(opacity=opacity, width=2)

        # Gravity force arrow toward the planet
        gravity_arrow = Arrow(
            asteroid.get_center(),
            asteroid.get_center() + LEFT * 1.0,
            buff=0,
            color=RED,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
        )
        gravity_label = MathTex(r"\vec{F}_g", color=RED).scale(0.85)
        gravity_label.next_to(gravity_arrow, DOWN, buff=0.1)

        # Velocity arrow toward the planet
        velocity_arrow_start = Arrow(
            asteroid.get_center() + UP * 0.55,
            asteroid.get_center() + UP * 0.55 + LEFT * 0.75,
            buff=0,
            color=YELLOW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
        )
        velocity_arrow_final = Arrow(
            asteroid.get_center() + UP * 0.55,
            asteroid.get_center() + UP * 0.55 + LEFT * 1.35,
            buff=0,
            color=YELLOW,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.25,
        )
        velocity_label = MathTex(r"\vec{v}", color=YELLOW).scale(0.85)
        velocity_label.next_to(velocity_arrow_start, UP, buff=0.1)

        # Tiny radial displacement marks along the straight line
        tiny_segments = VGroup()
        for alpha in [0.15, 0.30, 0.45, 0.60, 0.75, 0.90]:
            x = interpolate(planet.get_right()[0], asteroid.get_center()[0], alpha)
            p = np.array([x, asteroid.get_center()[1], 0])
            seg = Line(
                p + LEFT * 0.10,
                p + RIGHT * 0.10,
                color=YELLOW,
                stroke_width=5,
            )
            tiny_segments.add(seg)

        # Animated asteroid falling on a straight radial line
        asteroid_falling = Dot(point=asteroid.get_center(), radius=0.12, color=WHITE)
        straight_fall_path = Line(
            asteroid.get_center(),
            planet.get_right() + RIGHT * 0.20,
            color=GRAY_B,
        )

        # ------------------------------------------------------------
        # Right-side formulas
        # ------------------------------------------------------------
        work_formula = right_formula(
            r"W_g=\int \vec{F}_g\cdot d\vec{r}",
            scale=1.05,
            y=1.45,
        )

        gravity_force = right_formula(
            r"\vec{F}_g=-\frac{GMm}{r^2}\hat{r}",
            scale=1.05,
            y=0.45,
        )

        substituted_work = right_formula(
            r"W_g=\int\left(-\frac{GMm}{r^2}\hat{r}\right)\cdot d\vec{r}",
            scale=0.85,
            y=1.25,
        )

        kinetic_work = right_formula(
            r"W_g=m\int\vec{v}\cdot d\vec{v}",
            scale=1.05,
            y=0.10,
        )

        combined_vector = right_formula(
            r"\int\left(-\frac{GMm}{r^2}\hat{r}\right)\cdot d\vec{r}"
            r"=m\int\vec{v}\cdot d\vec{v}",
            scale=0.76,
            y=0.95,
        )

        radial_motion = right_formula(
            r"d\vec{r}=dr\,\hat{r},\quad \hat{r}\cdot\hat{r}=1",
            scale=0.92,
            y=-0.15,
        )

        scalar_radial = right_formula(
            r"-GMm\int\frac{dr}{r^2}=m\int v\,dv",
            scale=0.98,
            y=1.05,
        )

        limits_formula = right_formula(
            r"-GMm\int_{r_0}^{r_f}\frac{dr}{r^2}"
            r"=m\int_{v_0}^{v_f}v\,dv",
            scale=0.88,
            y=1.05,
        )

        integrated_formula = right_formula(
            r"GMm\left(\frac{1}{r_f}-\frac{1}{r_0}\right)"
            r"=m\left(\frac{v_f^2}{2}-\frac{v_0^2}{2}\right)",
            scale=0.78,
            y=1.05,
        )

        special_case = right_formula(
            r"r_0\to\infty,\quad v_0=0,\quad r_f\to R",
            scale=0.9,
            y=-0.05,
        )

        simplified_energy = right_formula(
            r"\frac{GMm}{R}=\frac{m v_f^2}{2}",
            scale=1.05,
            y=1.05,
        )
        

        cancel_mass = right_formula(
            r"\frac{GM}{R}=\frac{v_f^2}{2}",
            scale=1.05,
            y=-0.1,
        )
        cancel_mass.shift(DOWN * 0.45)

        escape_formula = right_formula(
            r"v_f=\sqrt{\frac{2GM}{R}}",
            scale=1.25,
            y=0.95,
        )

        escape_meaning = VGroup(
            Text("minimum speed to escape", font_size=23, color=GREEN),
            Text("reaches infinity with zero speed left", font_size=21, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        escape_meaning.move_to(RIGHT * 3.35 + DOWN * 1.05)

        constants = VGroup(
            MathTex(r"G=6.6743\times10^{-11}\;\mathrm{m^3kg^{-1}s^{-2}}"),
            MathTex(r"M_{\mathrm{Earth}}=5.9722\times10^{24}\;\mathrm{kg}"),
            MathTex(r"R_{\mathrm{Earth}}=6.378\times10^6\;\mathrm{m}"),
        )
        constants.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        constants.scale(0.67)
        constants.move_to(RIGHT * 3.15 + UP * 0.05)

        numeric_formula = right_formula(
            r"v_f=\sqrt{\frac{2\cdot6.6743\cdot5.9722\times10^{13}}{6.378\times10^6}}",
            scale=0.64,
            y=1.1,
        )

        numeric_result = right_formula(
            r"v_f\approx11180\;\mathrm{m/s}\approx11.18\;\mathrm{km/s}",
            scale=0.9,
            y=-0.15,
        )

        final_result = MathTex(
            r"v_{\mathrm{escape}}\approx11.18\;\mathrm{km/s}",
            color=GREEN,
        )
        final_result.scale(1.18)
        final_result.move_to(RIGHT * 3.15 + UP * 0.95)

        # ------------------------------------------------------------
        # Notes
        # ------------------------------------------------------------
        note_combine = make_note("combine gravitational work and kinetic energy", color=GREEN)
        note_radial = make_note("for radial motion, vectors simplify to scalars", color=YELLOW)
        note_limits = make_note("start far away, fall to the planet radius", color=BLUE)
        note_cancel = make_note("the asteroid mass cancels", color=GREEN)
        note_escape = make_note("falling from infinity reversed gives escape", color=GREEN, y=-2.25, size=22)
        note_earth = make_note("Earth parameters give the numerical value", color=BLUE)
        note_final = make_note("same value as escape velocity", color=GREEN, y=-2.35, size=24)

        # ------------------------------------------------------------
        # Animation timeline
        # ------------------------------------------------------------
        self.play(FadeIn(title))
        self.wait(0.4)

        # Physical setup, same position as previous scene
        self.play(
            Create(ring_1),
            Create(ring_2),
            Create(ring_3),
            FadeIn(planet),
            FadeIn(planet_label),
            FadeIn(planet_mass_label),
        )
        self.play(
            Create(radial_line),
            Create(center_line),
            FadeIn(asteroid),
            FadeIn(asteroid_label),
            FadeIn(asteroid_mass_label),
        )
        self.play(GrowArrow(r0_double_arrow), FadeIn(r0_label))
        self.play(GrowArrow(gravity_arrow), FadeIn(gravity_label))
        self.play(GrowArrow(velocity_arrow_start), FadeIn(velocity_label))
        self.wait(0.6)

        # Work formula and force substitution
        self.play(Write(work_formula))
        pulse(work_formula.get_part_by_tex(r"\vec{F}_g"), color=RED)
        pulse(work_formula.get_part_by_tex(r"d\vec{r}"), color=YELLOW)

        self.play(Write(gravity_force))
        pulse(gravity_force.get_part_by_tex(r"-"), color=RED)
        pulse(gravity_force.get_part_by_tex(r"\hat{r}"), color=YELLOW)
        self.wait(0.5)

        # Substitute gravity and combine with kinetic work
        self.play(
            ReplacementTransform(work_formula, substituted_work),
            FadeOut(gravity_force),
        )
        self.play(FadeIn(note_combine, shift=UP * 0.3))
        self.play(Write(kinetic_work))
        pulse(kinetic_work.get_part_by_tex(r"\vec{v}"), color=BLUE)
        pulse(kinetic_work.get_part_by_tex(r"d\vec{v}"), color=YELLOW)
        self.wait(0.5)

        self.play(
            ReplacementTransform(substituted_work, combined_vector),
            FadeOut(kinetic_work),
            FadeOut(note_combine, shift=DOWN * 0.3),
        )
        self.wait(0.5)

        # Radial simplification. No curved trajectory.
        self.play(Write(radial_motion))
        self.play(FadeIn(note_radial, shift=UP * 0.3))
        pulse(radial_motion.get_part_by_tex(r"d\vec{r}"), color=YELLOW)
        pulse(radial_motion.get_part_by_tex(r"\hat{r}\cdot\hat{r}"), color=GREEN)
        self.play(LaggedStart(*[Create(seg) for seg in tiny_segments], lag_ratio=0.08))
        self.wait(0.5)

        self.play(
            ReplacementTransform(combined_vector, scalar_radial),
            FadeOut(radial_motion),
            FadeOut(note_radial, shift=DOWN * 0.3),
        )
        pulse(scalar_radial.get_part_by_tex(r"dr"), color=YELLOW)
        pulse(scalar_radial.get_part_by_tex(r"v"), color=BLUE)
        self.wait(0.6)

        # Apply limits
        self.play(ReplacementTransform(scalar_radial, limits_formula))
        self.play(FadeIn(note_limits, shift=UP * 0.3))
        self.play(FadeIn(infinity_label))
        self.play(Create(radius_line), FadeIn(rf_label))
        pulse(limits_formula.get_part_by_tex(r"r_0"), color=BLUE)
        pulse(limits_formula.get_part_by_tex(r"r_f"), color=GREEN)
        pulse(limits_formula.get_part_by_tex(r"v_0"), color=BLUE)
        pulse(limits_formula.get_part_by_tex(r"v_f"), color=GREEN)
        self.wait(0.5)

        # Integrate
        self.play(
            ReplacementTransform(limits_formula, integrated_formula),
            FadeOut(note_limits, shift=DOWN * 0.3),
        )
        pulse(integrated_formula.get_part_by_tex(r"\frac{1}{r_f}"), color=GREEN)
        pulse(integrated_formula.get_part_by_tex(r"\frac{v_f^2}{2}"), color=GREEN)
        self.wait(0.6)

        self.play(FadeOut(infinity_label))

        self.play(Write(special_case))
        pulse(special_case.get_part_by_tex(r"r_0\to\infty"), color=BLUE)
        pulse(special_case.get_part_by_tex(r"v_0=0"), color=BLUE)
        pulse(special_case.get_part_by_tex(r"r_f\to R"), color=GREEN)
        self.wait(0.5)

        # Straight-line falling animation. This replaces the old bent path.
        self.play(FadeOut(asteroid), FadeOut(asteroid_label), FadeOut(asteroid_mass_label))
        self.add(asteroid_falling)
        self.play(
            MoveAlongPath(asteroid_falling, straight_fall_path),
            run_time=2.0,
            rate_func=smooth,
        )
        self.play(
            ReplacementTransform(velocity_arrow_start, velocity_arrow_final),
            velocity_label.animate.next_to(velocity_arrow_final, UP, buff=0.1),
            run_time=0.8,
        )
        self.wait(0.3)

        # Simplify to escape velocity formula
        self.play(
            ReplacementTransform(integrated_formula, simplified_energy),
            FadeOut(special_case),
        )
        pulse(simplified_energy.get_part_by_tex("m"), color=YELLOW)
        self.play(Write(cancel_mass))
        self.play(FadeIn(note_cancel, shift=UP * 0.3))
        pulse(cancel_mass, color=GREEN)
        self.wait(0.4)

        self.play(
            FadeOut(note_cancel, shift=DOWN * 0.3),
            FadeOut(cancel_mass),
            ReplacementTransform(simplified_energy, escape_formula),
        )
        pulse(escape_formula, color=GREEN)
        self.wait(0.4)

        # Add escape velocity meaning
        self.play(FadeIn(escape_meaning, shift=UP * 0.3))
        self.play(FadeIn(note_escape, shift=UP * 0.3))
        self.wait(1.2)

        # Earth numerical example
        self.play(
            FadeOut(escape_formula),
            FadeOut(escape_meaning),
            FadeOut(note_escape, shift=DOWN * 0.3),
        )
        self.play(Write(constants))
        self.play(FadeIn(note_earth, shift=UP * 0.3))
        pulse(constants[0], color=BLUE)
        pulse(constants[1], color=BLUE)
        pulse(constants[2], color=BLUE)
        self.wait(0.4)

        self.play(
            FadeOut(note_earth, shift=DOWN * 0.3),
            FadeOut(constants),
            Write(numeric_formula),
        )
        self.wait(0.8)
        self.play(Write(numeric_result))
        pulse(numeric_result, color=GREEN)
        self.wait(0.8)

        # Final conclusion
        self.play(
            FadeOut(numeric_formula),
            ReplacementTransform(numeric_result, final_result),
        )
        self.play(FadeIn(note_final, shift=UP * 0.3))
        pulse(final_result, color=GREEN, scale_factor=1.08)
        self.wait(2.0)