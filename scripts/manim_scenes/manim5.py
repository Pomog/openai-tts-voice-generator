from manim import *


class DeviationVectorAndVariance(Scene):
    """
    Visual continuation for the narration about the deviation vector,
    variance, and standard deviation.

    Render:
        manim -pql deviation_vector_variance_manim.py DeviationVectorAndVariance

    High quality:
        manim -pqh --fps 60 deviation_vector_variance_manim.py DeviationVectorAndVariance
    """

    def construct(self):
        # ------------------------------------------------------------
        # Helpers
        # ------------------------------------------------------------
        def pulse(mobject, color=YELLOW, scale_factor=1.08, run_time=0.6):
            self.play(
                Indicate(mobject, color=color, scale_factor=scale_factor),
                run_time=run_time,
            )

        def bottom_note(text, color=YELLOW, size=24):
            note = Text(text, font_size=size, color=color)
            note.to_edge(DOWN)
            note.shift(UP * 0.2)
            return note

        def clear_all(*objects, run_time=0.7):
            anims = [FadeOut(obj) for obj in objects if obj is not None]
            if anims:
                self.play(*anims, run_time=run_time)

        # ------------------------------------------------------------
        # Title
        # ------------------------------------------------------------
        title = Text("The Deviation Vector", font_size=38)
        title.to_edge(UP)

        subtitle = Text(
            "Part 3 — Deviation, variance, and standard deviation",
            font_size=23,
            color=GRAY_B,
        )
        subtitle.next_to(title, DOWN, buff=0.14)

        self.play(FadeIn(title), FadeIn(subtitle, shift=UP * 0.12))
        self.wait(0.3)

        # ============================================================
        # 1. Decomposition and definition of the deviation vector
        # ============================================================
        decomposition = MathTex(
            r"\mathbf{x}",
            r"=",
            r"\operatorname{proj}_{\mathcal C}(\mathbf{x})",
            r"+",
            r"\mathbf{x}_c",
        ).scale(1.08)
        decomposition.move_to(UP * 1.0)
        decomposition[0].set_color(BLUE_B)
        decomposition[2].set_color(GREEN)
        decomposition[4].set_color(YELLOW)

        definition = MathTex(
            r"\mathbf{x}_c",
            r"=",
            r"\mathbf{x}",
            r"-",
            r"\operatorname{proj}_{\mathcal C}(\mathbf{x})",
        ).scale(1.0)
        definition.move_to(UP * 0.0)
        definition[0].set_color(YELLOW)
        definition[2].set_color(BLUE_B)
        definition[4].set_color(GREEN)

        component_note = bottom_note(
            "The deviation vector is the second component of the dataset vector.",
            color=YELLOW,
            size=23,
        )

        self.play(Write(decomposition))
        pulse(decomposition[2], color=GREEN)
        pulse(decomposition[4], color=YELLOW)
        self.play(Write(definition))
        self.play(FadeIn(component_note, shift=UP * 0.12))
        self.wait(1.0)

        # ============================================================
        # 2. Concrete example: x, projection, deviation
        # ============================================================
        clear_all(component_note)

        x_vec = MathTex(r"\mathbf{x}", r"\begin{bmatrix}2\\4\\6\end{bmatrix}").scale(1.0)
        x_vec.move_to(LEFT * 4.2 + DOWN * 1.4)
        x_vec[1].set_color(BLUE_B)

        p_vec = MathTex(
            r"\operatorname{proj}_{\mathcal C}(\mathbf{x})",
            r"\begin{bmatrix}4\\4\\4\end{bmatrix}",
        ).scale(0.95)
        p_vec.move_to(ORIGIN + DOWN * 1.4)
        p_vec[1].set_color(GREEN)

        xc_vec = MathTex(r"\mathbf{x}_c", r"\begin{bmatrix}-2\\0\\2\end{bmatrix}").scale(1.0)
        xc_vec.move_to(RIGHT * 4.0 + DOWN * 1.4)
        xc_vec[1].set_color(YELLOW)

        minus_sign = MathTex(r"-").scale(1.3)
        minus_sign.move_to(LEFT * 2.15 + DOWN * 1.4)

        equals_sign = MathTex(r"=").scale(1.2)
        equals_sign.move_to(RIGHT * 2.0 + DOWN * 1.4)

        meaning_text = VGroup(
            Text("-2: below mean", font_size=24, color=YELLOW),
            Text(" 0: at the mean", font_size=24, color=GRAY_B),
            Text(" 2: above mean", font_size=24, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        meaning_text.move_to(RIGHT * 4.2 + UP * 0.6)

        example_note = bottom_note(
            "Each coordinate shows how far the observation lies below or above the mean.",
            color=YELLOW,
            size=22,
        )

        self.play(Write(x_vec), Write(p_vec), Write(minus_sign), Write(equals_sign), Write(xc_vec))
        self.play(FadeIn(meaning_text, shift=LEFT * 0.1))
        pulse(xc_vec[1], color=YELLOW)
        self.play(FadeIn(example_note, shift=UP * 0.12))
        self.wait(1.2)

        # ============================================================
        # 3. Length and self-dot product
        # ============================================================
        clear_all(example_note)

        length_formula = MathTex(
            r"\|\mathbf{x}_c\|",
            r"=",
            r"\sqrt{(-2)^2+0^2+2^2}",
            r"=",
            r"\sqrt{8}",
        ).scale(0.95)
        length_formula.move_to(UP * 1.8)
        length_formula[0].set_color(YELLOW)
        length_formula[-1].set_color(YELLOW)

        # here


        dot_formula = MathTex(
            r"\mathbf{x}_c\cdot\mathbf{x}_c",
            r"=",
            r"(-2)^2+0^2+2^2",
            r"=",
            r"8",
        ).scale(0.98)
        dot_formula.move_to(UP * 0.85)
        dot_formula[0].set_color(YELLOW)
        dot_formula[-1].set_color(YELLOW)

        tss_label = MathTex(
            r"\text{sum of squared deviations }=8"
        ).scale(0.95)
        tss_label.move_to(UP * 0.0)
        tss_label.set_color(YELLOW)

        dot_note = bottom_note(
            "The self-dot product gives the squared length: total squared deviation.",
            color=YELLOW,
            size=23,
        )

        self.play(Write(length_formula))
        pulse(length_formula[-1], color=YELLOW)

        self.wait(1.2)

        clear_all(
            decomposition,
            definition,
            x_vec,
            p_vec,
            xc_vec,
            minus_sign,
            equals_sign,
            meaning_text,
            example_note,
        )

        self.play(Write(dot_formula))
        pulse(dot_formula[0], color=YELLOW)

        self.play(Write(tss_label))
        self.play(FadeIn(dot_note, shift=UP * 0.12))
        self.wait(1.2)

        # ============================================================
        # 4. Variance as a mean, and the role of the all-ones vector
        # ============================================================
        clear_all(
            dot_note,
            tss_label,
            dot_formula,
            length_formula,
        )

        self.wait(1.2)

        variance_title = Text("Variance is the mean squared deviation", font_size=30, color=GRAY_A)
        variance_title.move_to(UP * 2.0)

        ones_info = MathTex(
            r"\mathbf{1}_3=\begin{bmatrix}1\\1\\1\end{bmatrix}",
            r"\qquad",
            r"\mathbf{1}_3\cdot\mathbf{1}_3=3",
        ).scale(1.0)
        ones_info.move_to(UP * 0.95)
        ones_info[0].set_color(BLUE_B)
        ones_info[2].set_color(GREEN)

        variance_formula = MathTex(
            r"\mathrm{Var}(\mathbf{x})",
            r"=",
            r"\frac{\mathbf{x}_c\cdot\mathbf{x}_c}{\mathbf{1}_3\cdot\mathbf{1}_3}",
            r"=",
            r"\frac{8}{3}",
        ).scale(1.02)
        variance_formula.move_to(DOWN * 0.25)
        variance_formula[0].set_color(GREEN)
        variance_formula[2].set_color(YELLOW)
        variance_formula[-1].set_color(GREEN)

        variance_note = bottom_note(
            "The denominator counts observations through the squared length of the all-ones vector.",
            color=GREEN,
            size=22,
        )

        self.play(FadeIn(variance_title))
        self.play(Write(ones_info))
        pulse(ones_info[2], color=GREEN)
        self.play(Write(variance_formula))
        pulse(variance_formula[-1], color=GREEN)
        self.play(FadeIn(variance_note, shift=UP * 0.12))
        self.wait(1.2)

        # ============================================================
        # 5. Same projection principle on the squared deviations
        # ============================================================
        clear_all(
            variance_note,
            variance_formula,
            ones_info,
            )
        self.wait(1.2)

        sqdev_vec = MathTex(r"\begin{bmatrix}4\\0\\4\end{bmatrix}").scale(1.15)
        sqdev_vec.set_color(YELLOW)
        sqdev_vec.move_to(LEFT * 4.0 + DOWN * 1.2)

        sqdev_label = Text("squared deviations", font_size=24, color=YELLOW)
        sqdev_label.next_to(sqdev_vec, DOWN, buff=0.18)

        proj_arrow = Arrow(
            sqdev_vec.get_right() + RIGHT * 0.2,
            RIGHT * 0.4 + DOWN * 1.2,
            buff=0.05,
            color=GREEN,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.16,
        )

        # here 2

        proj_formula = MathTex(
            r"\quad\operatorname{proj}_{\mathcal C}",
            r"\left(\begin{bmatrix}4\\0\\4\end{bmatrix}\right)",
            r"=",
            r"\begin{bmatrix}8/3\\8/3\\8/3\end{bmatrix}",
        ).scale(0.96)
        proj_formula.next_to(
            proj_arrow,
            RIGHT,
            buff=0.25,
        )
        proj_formula[0].set_color(GREEN)
        proj_formula[-1].set_color(GREEN)

        proj_note = bottom_note(
            "Projecting the squared deviations onto the constant subspace gives a constant variance vector.",
            color=GREEN,
            size=21,
        )

        self.play(Write(sqdev_vec), FadeIn(sqdev_label, shift=UP * 0.08))
        self.play(GrowArrow(proj_arrow))
        self.play(Write(proj_formula))
        pulse(proj_formula[-1], color=GREEN)
        self.play(FadeIn(proj_note, shift=UP * 0.12))
        self.wait(1.2)

        # ============================================================
        # 6. Standard deviation and closing line
        # ============================================================
        clear_all(
            sqdev_vec,
            sqdev_label,
            proj_arrow,
            proj_formula,
            proj_note,
        )

        std_formula = MathTex(
            r"\sigma",
            r"=",
            r"\sqrt{\mathrm{Var}(\mathbf{x})}",
            r"=",
            r"\sqrt{8/3}",
        ).scale(1.08)
        std_formula.move_to(UP * 0.5)
        std_formula[0].set_color(BLUE_B)
        std_formula[2].set_color(GREEN)
        std_formula[-1].set_color(BLUE_B)
        
        final_box = RoundedRectangle(
            width=11.3,
            height=1.5,
            corner_radius=0.14,
            color=BLUE_B,
            stroke_width=3,
        )
        final_box.set_fill(BLUE_E, opacity=0.10)
        final_box.move_to(DOWN * 1.9)

        final_text = Paragraph(
            "Variance measures average squared variation;",
            "standard deviation brings it back to the original scale.",
            alignment="center",
            font_size=24,
            color=BLUE_B,
            line_spacing=0.8,
        )

        final_text.move_to(final_box.get_center())

        self.play(Write(std_formula))
        pulse(std_formula[-1], color=BLUE_B)
        self.play(Create(final_box), FadeIn(final_text, shift=UP * 0.10))
        self.wait(2.0)