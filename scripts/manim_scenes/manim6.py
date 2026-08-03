from manim import *


class CovarianceAndCorrelation(Scene):
    """
    Visual continuation for the narration about covariance and Pearson
    correlation as geometric measurements of deviation vectors.

    Render:
        manim -pql covariance_correlation_manim.py CovarianceAndCorrelation

    High quality:
        manim -pqh --fps 60 covariance_correlation_manim.py CovarianceAndCorrelation

    The concrete example used throughout is

        X  = [1, 2, 4, 5],       Y  = [1, 4, 2, 5]
        Xc = [-2, -1, 1, 2],     Yc = [-2, 1, -1, 2]

    Therefore:

        Xc ⊙ Yc = [4, -1, -1, 4]
        Xc · Yc = 6
        Cov(X, Y) = 6 / 4 = 3/2
        Var(X) = Var(Y) = 10 / 4 = 5/2
        r = 6 / (sqrt(10) sqrt(10)) = 3/5
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

        def bottom_note(text, color=YELLOW, size=23):
            note = Text(text, font_size=size, color=color)
            if note.width > 13.2:
                note.scale_to_fit_width(13.2)
            note.to_edge(DOWN)
            note.shift(UP * 0.2)
            return note

        def clear_all(*objects, run_time=0.7):
            anims = [FadeOut(obj) for obj in objects if obj is not None]
            if anims:
                self.play(*anims, run_time=run_time)

        def section_heading(text, color=GRAY_A):
            heading = Text(text, font_size=30, color=color)
            if heading.width > 12.8:
                heading.scale_to_fit_width(12.8)
            heading.move_to(UP * 2.15)
            return heading

        def formula_box(formula, color, width=5.7, height=1.28):
            box = RoundedRectangle(
                width=width,
                height=height,
                corner_radius=0.12,
                color=color,
                stroke_width=2.5,
            )
            box.set_fill(color, opacity=0.08)
            formula.move_to(box.get_center())
            return VGroup(box, formula)

        # Color language used in the entire video.
        x_color = BLUE_B
        y_color = RED_B
        mean_color = GREEN
        deviation_color = YELLOW
        product_color = ORANGE
        covariance_color = GREEN
        correlation_color = PURPLE_B

        # ------------------------------------------------------------
        # Persistent title
        # ------------------------------------------------------------
        title = Text("Covariance and Correlation", font_size=38)
        title.to_edge(UP)

        subtitle = Text(
            "Part 4 - Geometry of two deviation vectors",
            font_size=23,
            color=GRAY_B,
        )
        subtitle.next_to(title, DOWN, buff=0.14)

        self.play(FadeIn(title), FadeIn(subtitle, shift=UP * 0.12))
        self.wait(0.4)

        # ============================================================
        # 1. Recap: one data vector has two orthogonal components
        # ============================================================
        recap_heading = section_heading("One dataset: constant + deviation")

        decomposition = MathTex(
            r"\mathbf{x}",
            r"=",
            r"\operatorname{proj}_{\mathcal C}(\mathbf{x})",
            r"+",
            r"\mathbf{x}_c",
        ).scale(1.08)
        decomposition.move_to(UP * 0.95)
        decomposition[0].set_color(x_color)
        decomposition[2].set_color(mean_color)
        decomposition[4].set_color(deviation_color)

        orthogonality = MathTex(
            r"\operatorname{proj}_{\mathcal C}(\mathbf{x})",
            r"\perp",
            r"\mathbf{x}_c",
        ).scale(1.0)
        orthogonality.move_to(DOWN * 0.25)
        orthogonality[0].set_color(mean_color)
        orthogonality[1].set_color(WHITE)
        orthogonality[2].set_color(deviation_color)

        recap_note = bottom_note(
            "The mean component is constant; the deviation vector contains everything that varies.",
            color=deviation_color,
            size=22,
        )

        self.play(FadeIn(recap_heading))
        self.play(Write(decomposition))
        pulse(decomposition[2], color=mean_color)
        pulse(decomposition[4], color=deviation_color)
        self.play(Write(orthogonality))
        self.play(FadeIn(recap_note, shift=UP * 0.12))
        self.wait(1.2)

        # ============================================================
        # 2. Two variables measured for the same observations
        # ============================================================
        clear_all(recap_heading, decomposition, orthogonality, recap_note)

        paired_heading = section_heading("Two variables, paired by coordinate")

        observation_labels = VGroup(
            *[
                Text(str(index), font_size=23, color=GRAY_B)
                for index in range(1, 5)
            ]
        ).arrange(RIGHT, buff=0.72)
        observation_labels.move_to(UP * 1.25 + RIGHT * 0.7)

        index_label = Text("observation", font_size=22, color=GRAY_B)
        index_label.next_to(observation_labels, LEFT, buff=0.55)

        x_label = MathTex(r"\mathbf{X}=").scale(1.0).set_color(x_color)
        x_values = VGroup(
            *[
                MathTex(value).scale(0.95).set_color(x_color)
                for value in ("1", "2", "4", "5")
            ]
        ).arrange(RIGHT, buff=0.82)
        x_row = VGroup(x_label, x_values).arrange(RIGHT, buff=0.55)
        x_row.move_to(UP * 0.25)

        y_label = MathTex(r"\mathbf{Y}=").scale(1.0).set_color(y_color)
        y_values = VGroup(
            *[
                MathTex(value).scale(0.95).set_color(y_color)
                for value in ("1", "4", "2", "5")
            ]
        ).arrange(RIGHT, buff=0.82)
        y_row = VGroup(y_label, y_values).arrange(RIGHT, buff=0.55)
        y_row.move_to(DOWN * 0.75)

        # Align the four coordinate groups exactly under the index labels.
        x_values.move_to(observation_labels.get_center() + DOWN * 1.0)
        y_values.move_to(observation_labels.get_center() + DOWN * 2.0)
        x_label.next_to(x_values, LEFT, buff=0.55)
        y_label.next_to(y_values, LEFT, buff=0.55)

        pair_lines = VGroup(
            *[
                Line(
                    x_values[i].get_bottom() + DOWN * 0.04,
                    y_values[i].get_top() + UP * 0.04,
                    color=GRAY_D,
                    stroke_width=2,
                )
                for i in range(4)
            ]
        )

        pair_note = bottom_note(
            "Coordinates with the same index belong to the same observation.",
            color=GRAY_A,
            size=23,
        )

        self.play(FadeIn(paired_heading))
        self.play(
            FadeIn(index_label),
            LaggedStart(*[FadeIn(m) for m in observation_labels], lag_ratio=0.08),
        )
        self.play(Write(x_label), LaggedStart(*[Write(m) for m in x_values], lag_ratio=0.10))
        self.play(Write(y_label), LaggedStart(*[Write(m) for m in y_values], lag_ratio=0.10))
        self.play(LaggedStart(*[Create(line) for line in pair_lines], lag_ratio=0.10))
        self.play(FadeIn(pair_note, shift=UP * 0.12))
        self.wait(1.2)

        # ============================================================
        # 3. The question: do deviations move together?
        # ============================================================
        clear_all(
            paired_heading,
            observation_labels,
            index_label,
            x_label,
            x_values,
            y_label,
            y_values,
            pair_lines,
            pair_note,
        )

        question_heading = section_heading("Do the variables deviate together?")

        same_direction = VGroup(
            MathTex(r"X_i-\bar X>0", color=x_color),
            MathTex(r"Y_i-\bar Y>0", color=y_color),
        ).arrange(DOWN, buff=0.22)
        same_direction.move_to(LEFT * 3.6 + UP * 0.35)

        same_arrow = DoubleArrow(
            LEFT * 0.55,
            RIGHT * 0.55,
            color=mean_color,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.16,
        )
        same_arrow.rotate(PI / 4)
        same_arrow.move_to(ORIGIN + UP * 0.35)

        opposite_direction = VGroup(
            MathTex(r"X_i-\bar X>0", color=x_color),
            MathTex(r"Y_i-\bar Y<0", color=y_color),
        ).arrange(DOWN, buff=0.22)
        opposite_direction.move_to(RIGHT * 3.6 + UP * 0.35)

        same_text = Text("same direction?", font_size=24, color=mean_color)
        same_text.next_to(same_direction, DOWN, buff=0.45)

        opposite_text = Text("opposite directions?", font_size=24, color=y_color)
        opposite_text.next_to(opposite_direction, DOWN, buff=0.45)

        question_note = bottom_note(
            "We compare positions relative to each variable's own mean.",
            color=deviation_color,
            size=23,
        )

        self.play(FadeIn(question_heading))
        self.play(Write(same_direction), Write(opposite_direction))
        self.play(GrowArrow(same_arrow))
        self.play(FadeIn(same_text), FadeIn(opposite_text))
        self.play(FadeIn(question_note, shift=UP * 0.12))
        self.wait(1.2)

        # ============================================================
        # 4. Center X and Y
        # ============================================================
        clear_all(
            question_heading,
            same_direction,
            same_arrow,
            opposite_direction,
            same_text,
            opposite_text,
            question_note,
        )

        center_heading = section_heading("Remove each constant component")

        x_center_formula = MathTex(
            r"\mathbf{X}_c",
            r"=",
            r"\mathbf{X}-\bar X\cdot\mathbf{1}_4",
            r"=",
            r"\begin{bmatrix}-2\\-1\\1\\2\end{bmatrix}",
        ).scale(0.94)
        x_center_formula.move_to(LEFT * 3.25 + UP * 0.55)
        x_center_formula[0].set_color(x_color)
        x_center_formula[2].set_color(mean_color)
        x_center_formula[4].set_color(deviation_color)

        y_center_formula = MathTex(
            r"\mathbf{Y}_c",
            r"=",
            r"\mathbf{Y}-\bar Y\cdot\mathbf{1}_4",
            r"=",
            r"\begin{bmatrix}-2\\1\\-1\\2\end{bmatrix}",
        ).scale(0.94)
        y_center_formula.move_to(RIGHT * 3.25 + UP * 0.55)
        y_center_formula[0].set_color(y_color)
        y_center_formula[2].set_color(mean_color)
        y_center_formula[4].set_color(deviation_color)

        means = MathTex(
            r"\bar X=3",
            r"\qquad",
            r"\bar Y=3",
        ).scale(0.95)
        means.move_to(DOWN * 1.25)
        means[0].set_color(x_color)
        means[2].set_color(y_color)

        center_note = bottom_note(
            "The two deviation vectors now live in the same zero-sum hyperplane.",
            color=deviation_color,
            size=22,
        )

        self.play(FadeIn(center_heading))
        self.play(Write(means))
        self.play(Write(x_center_formula))
        self.play(Write(y_center_formula))
        pulse(x_center_formula[4], color=x_color)
        pulse(y_center_formula[4], color=y_color)
        self.play(FadeIn(center_note, shift=UP * 0.12))
        self.wait(1.3)

        # ============================================================
        # 5. Multiply corresponding deviations
        # ============================================================
        clear_all(center_heading, means, x_center_formula, y_center_formula, center_note)

        products_heading = section_heading("Multiply corresponding deviations")

        x_dev = MathTex(
            r"\mathbf{X}_c=",
            r"\begin{bmatrix}-2\\-1\\1\\2\end{bmatrix}",
        ).scale(0.93)
        x_dev.move_to(LEFT * 4.25 + UP * 0.15)
        x_dev[0].set_color(x_color)
        x_dev[1].set_color(deviation_color)

        hadamard = MathTex(r"\odot").scale(1.35)
        hadamard.move_to(LEFT * 2.45 + UP * 0.15)
        hadamard.set_color(WHITE)

        y_dev = MathTex(
            r"\mathbf{Y}_c=",
            r"\begin{bmatrix}-2\\1\\-1\\2\end{bmatrix}",
        ).scale(0.93)
        y_dev.move_to(LEFT * 0.6 + UP * 0.15)
        y_dev[0].set_color(y_color)
        y_dev[1].set_color(deviation_color)

        product_equals = MathTex(r"=").scale(1.15)
        product_equals.move_to(RIGHT * 1.25 + UP * 0.15)

        product_vector = MathTex(
            r"\mathbf{p}=",
            r"\begin{bmatrix}4\\-1\\-1\\4\end{bmatrix}",
        ).scale(0.98)
        product_vector.move_to(RIGHT * 3.7 + UP * 0.15)
        product_vector[0].set_color(product_color)
        product_vector[1].set_color(product_color)

        sign_key = VGroup(
            VGroup(
                MathTex(r"(+)(+)\ \text{or}\ (-)(-)", color=mean_color).scale(0.82),
                MathTex(r"\Longrightarrow\ \text{positive}", color=mean_color).scale(0.82),
            ).arrange(RIGHT, buff=0.25),
            VGroup(
                MathTex(r"(+)(-)\ \text{or}\ (-)(+)", color=y_color).scale(0.82),
                MathTex(r"\Longrightarrow\ \text{negative}", color=y_color).scale(0.82),
            ).arrange(RIGHT, buff=0.25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        sign_key.move_to(DOWN * 1.6)

        products_note = bottom_note(
            "Positive products record same-direction deviations; negative products record opposite directions.",
            color=product_color,
            size=20,
        )

        self.play(FadeIn(products_heading))
        self.play(
            Write(x_dev),
            Write(y_dev),
            Write(hadamard),
            Write(product_equals),
        )
        self.play(Write(product_vector))
        pulse(product_vector[1], color=product_color)
        self.play(FadeIn(sign_key, shift=UP * 0.12))
        self.play(FadeIn(products_note, shift=UP * 0.12))
        self.wait(1.4)

        # ============================================================
        # 6. Dot product: total alignment
        # ============================================================
        clear_all(
            products_heading,
            x_dev,
            hadamard,
            y_dev,
            product_equals,
            product_vector,
            sign_key,
            products_note,
        )

        dot_heading = section_heading("The dot product adds the products")

        dot_expansion = MathTex(
            r"\mathbf{X}_c\cdot\mathbf{Y}_c",
            r"=",
            r"4-1-1+4",
            r"=",
            r"6",
        ).scale(1.15)
        dot_expansion.move_to(UP * 0.75)
        dot_expansion[0].set_color(deviation_color)
        dot_expansion[2].set_color(product_color)
        dot_expansion[4].set_color(product_color)

        balance_line = NumberLine(
            x_range=[-4, 8, 2],
            length=7.4,
            include_numbers=True,
            font_size=23,
            color=GRAY_B,
        )
        balance_line.move_to(DOWN * 0.75)

        zero_marker = Dot(balance_line.n2p(0), color=GRAY_A, radius=0.07)
        result_marker = Dot(balance_line.n2p(6), color=product_color, radius=0.10)
        result_label = MathTex(r"6>0", color=product_color).scale(0.82)
        result_label.next_to(result_marker, UP, buff=0.14)

        alignment_note = bottom_note(
            "Positive total: same-direction products dominate in this dataset.",
            color=product_color,
            size=23,
        )

        self.play(FadeIn(dot_heading))
        self.play(Write(dot_expansion))
        self.play(Create(balance_line), FadeIn(zero_marker))
        self.play(FadeIn(result_marker, scale=1.5), Write(result_label))
        pulse(dot_expansion[4], color=product_color)
        self.play(FadeIn(alignment_note, shift=UP * 0.12))
        self.wait(1.2)

        # ============================================================
        # 7. Covariance is the mean, not the total
        # ============================================================
        clear_all(
            dot_heading,
            dot_expansion,
            balance_line,
            zero_marker,
            result_marker,
            result_label,
            alignment_note,
        )

        covariance_heading = section_heading("Covariance is the mean of the products")

        total_vs_mean = MathTex(
            r"\underbrace{\mathbf{X}_c\cdot\mathbf{Y}_c}_{\text{total alignment}}",
            r"=",
            r"6",
            r"\qquad",
            r"\underbrace{\operatorname{Cov}(X,Y)}_{\text{mean product}}",
            r"=",
            r"\frac{6}{4}",
            r"=",
            r"\frac{3}{2}",
        ).scale(0.88)
        total_vs_mean.move_to(UP * 0.65)
        total_vs_mean[0].set_color(product_color)
        total_vs_mean[2].set_color(product_color)
        total_vs_mean[4].set_color(covariance_color)
        total_vs_mean[6].set_color(covariance_color)
        total_vs_mean[8].set_color(covariance_color)

        covariance_definition = MathTex(
            r"\operatorname{Cov}_{\mathrm{pop}}(X,Y)",
            r"=",
            r"\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar X)(y_i-\bar Y)",
            r"=",
            r"\frac{\mathbf{X}_c\cdot\mathbf{Y}_c}{n}",
        ).scale(0.86)
        covariance_definition.move_to(DOWN * 0.75)
        covariance_definition[0].set_color(covariance_color)
        covariance_definition[2].set_color(deviation_color)
        covariance_definition[4].set_color(covariance_color)

        covariance_note = bottom_note(
            "Population covariance divides total alignment by the number of observations.",
            color=covariance_color,
            size=22,
        )

        self.play(FadeIn(covariance_heading))
        self.play(Write(total_vs_mean))
        pulse(total_vs_mean[0], color=product_color)
        pulse(total_vs_mean[8], color=covariance_color)
        self.play(Write(covariance_definition))
        self.play(FadeIn(covariance_note, shift=UP * 0.12))
        self.wait(1.3)

        # ============================================================
        # 8. Projection of the product vector
        # ============================================================
        clear_all(
            covariance_heading,
            total_vs_mean,
            covariance_definition,
            covariance_note,
        )

        projection_heading = section_heading("Apply the projection principle again")

        product_column = MathTex(
            r"\mathbf{p}=",
            r"\begin{bmatrix}4\\-1\\-1\\4\end{bmatrix}",
        ).scale(1.02)
        product_column.move_to(LEFT * 4.35 + DOWN * 0.05)
        product_column[0].set_color(product_color)
        product_column[1].set_color(product_color)

        projection_arrow = Arrow(
            LEFT * 2.7 + DOWN * 0.05,
            RIGHT * 2.7 + DOWN * 0.05,
            color=covariance_color,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.14,
        )

        projection_label = MathTex(
            r"\operatorname{proj}_{\mathcal C}(\mathbf{p})",
            r"=",
            r"\frac{\mathbf{p}\cdot\mathbf{1}_4}{\mathbf{1}_4\cdot\mathbf{1}_4}\mathbf{1}_4",
        ).scale(0.77)
        projection_label.next_to(projection_arrow, UP, buff=0.18)
        projection_label[0].set_color(covariance_color)
        projection_label[2].set_color(covariance_color)

        covariance_vector = MathTex(
            r"=",
            r"\begin{bmatrix}3/2\\3/2\\3/2\\3/2\end{bmatrix}",
        ).scale(1.0)
        covariance_vector.move_to(RIGHT * 4.25 + DOWN * 0.05)
        covariance_vector[1].set_color(covariance_color)

        projection_calculation = MathTex(
            r"\mathbf{p}\cdot\mathbf{1}_4=6",
            r"\qquad",
            r"\|\mathbf{1}_4\|^2=4",
            r"\qquad",
            r"\frac{6}{4}=\frac{3}{2}",
        ).scale(0.82)
        projection_calculation.move_to(DOWN * 1.75)
        projection_calculation[0].set_color(product_color)
        projection_calculation[2].set_color(mean_color)
        projection_calculation[4].set_color(covariance_color)

        projection_note = bottom_note(
            "The projected vector is constant; its common coordinate is the population covariance.",
            color=covariance_color,
            size=21,
        )

        self.play(FadeIn(projection_heading))
        self.play(Write(product_column))
        self.play(GrowArrow(projection_arrow), Write(projection_label))
        self.play(Write(covariance_vector))
        pulse(covariance_vector[1], color=covariance_color)
        self.play(Write(projection_calculation))
        self.play(FadeIn(projection_note, shift=UP * 0.12))
        self.wait(1.4)

        # ============================================================
        # 9. Unit dependence of covariance
        # ============================================================
        clear_all(
            projection_heading,
            product_column,
            projection_arrow,
            projection_label,
            covariance_vector,
            projection_calculation,
            projection_note,
        )

        units_heading = section_heading("Covariance still contains both scales")

        meter_formula = MathTex(
            r"X_{\mathrm{m}}",
            r"\longrightarrow",
            r"X_{\mathrm{cm}}=100X_{\mathrm{m}}",
        ).scale(1.05)
        meter_formula.move_to(UP * 0.8)
        meter_formula[0].set_color(x_color)
        meter_formula[2].set_color(x_color)

        deviation_scaling = MathTex(
            r"\mathbf{X}_{c,\mathrm{cm}}",
            r"=",
            r"100\,\mathbf{X}_{c,\mathrm{m}}",
        ).scale(1.02)
        deviation_scaling.move_to(DOWN * 0.1)
        deviation_scaling[0].set_color(deviation_color)
        deviation_scaling[2].set_color(deviation_color)

        covariance_scaling = MathTex(
            r"\operatorname{Cov}(X_{\mathrm{cm}},Y)",
            r"=",
            r"100\,\operatorname{Cov}(X_{\mathrm{m}},Y)",
        ).scale(1.02)
        covariance_scaling.move_to(DOWN * 1.05)
        covariance_scaling[0].set_color(covariance_color)
        covariance_scaling[2].set_color(covariance_color)

        units_note = bottom_note(
            "The numerical relationship is unchanged, but the covariance is multiplied by 100.",
            color=covariance_color,
            size=22,
        )

        self.play(FadeIn(units_heading))
        self.play(Write(meter_formula))
        self.play(Write(deviation_scaling))
        pulse(deviation_scaling[2], color=deviation_color)
        self.play(Write(covariance_scaling))
        pulse(covariance_scaling[2], color=covariance_color)
        self.play(FadeIn(units_note, shift=UP * 0.12))
        self.wait(1.3)

        # ============================================================
        # 10. Move into z-score space
        # ============================================================
        clear_all(
            units_heading,
            meter_formula,
            deviation_scaling,
            covariance_scaling,
            units_note,
        )

        z_heading = section_heading("Standardize: move into z-score space")

        zx_formula = MathTex(
            r"\mathbf{Z}_X",
            r"=",
            r"\frac{\mathbf{X}_c}{\sigma_X}",
        ).scale(1.08)
        zx_formula.move_to(LEFT * 3.0 + UP * 0.55)
        zx_formula[0].set_color(x_color)
        zx_formula[2].set_color(deviation_color)

        zy_formula = MathTex(
            r"\mathbf{Z}_Y",
            r"=",
            r"\frac{\mathbf{Y}_c}{\sigma_Y}",
        ).scale(1.08)
        zy_formula.move_to(RIGHT * 3.4 + UP * 0.55)
        zy_formula[0].set_color(y_color)
        zy_formula[2].set_color(deviation_color)

        z_coordinate = MathTex(
            r"z_{X,i}",
            r"=",
            r"\frac{x_i-\bar X}{\sigma_X}",
            r"\qquad",
            r"z_{Y,i}",
            r"=",
            r"\frac{y_i-\bar Y}{\sigma_Y}",
        ).scale(0.92)
        z_coordinate.move_to(DOWN * 0.6)
        z_coordinate[0].set_color(x_color)
        z_coordinate[2].set_color(x_color)
        z_coordinate[4].set_color(y_color)
        z_coordinate[6].set_color(y_color)

        unit_labels = VGroup(
            Text("not metres", font_size=23, color=GRAY_B),
            Text("not kilograms", font_size=23, color=GRAY_B),
            Text("standard-deviation units", font_size=24, color=correlation_color),
        ).arrange(RIGHT, buff=0.55)
        unit_labels.move_to(DOWN * 1.55)

        z_note = bottom_note(
            "Each coordinate now tells how many standard deviations it lies from its mean.",
            color=correlation_color,
            size=22,
        )

        self.play(FadeIn(z_heading))
        self.play(Write(zx_formula), Write(zy_formula))
        self.play(Write(z_coordinate))
        self.play(LaggedStart(*[FadeIn(label) for label in unit_labels], lag_ratio=0.15))
        pulse(unit_labels[2], color=correlation_color)
        self.play(FadeIn(z_note, shift=UP * 0.12))
        self.wait(1.3)

        # ============================================================
        # 11. Scaling changes length, not direction
        # ============================================================
        clear_all(
            z_heading,
            zx_formula,
            zy_formula,
            z_coordinate,
            unit_labels,
            z_note,
        )

        direction_heading = section_heading("Positive scaling preserves direction and angle")

        origin = LEFT * 4.5 + DOWN * 1.25
        original_arrow = Arrow(
            origin,
            origin + RIGHT * 4.6 + UP * 2.3,
            color=x_color,
            stroke_width=6,
            buff=0,
            max_tip_length_to_length_ratio=0.12,
        )
        scaled_arrow = Arrow(
            origin,
            origin + RIGHT * 2.5 + UP * 1.25,
            color=correlation_color,
            stroke_width=6,
            buff=0,
            max_tip_length_to_length_ratio=0.16,
        )

        original_label = MathTex(r"\mathbf{X}_c", color=x_color).scale(0.9)
        original_label.next_to(original_arrow.get_end(), RIGHT, buff=0.12)

        scaled_label = MathTex(
            r"\mathbf{Z}_X=\frac{1}{\sigma_X}\mathbf{X}_c",
            color=correlation_color,
        ).scale(0.82)
        scaled_label.next_to(scaled_arrow.get_end(), DOWN, buff=0.18)

        direction_formula = MathTex(
            r"\frac{1}{\sigma_X}>0",
            r"\Longrightarrow",
            r"\text{same ray, same direction}",
        ).scale(0.9)
        direction_formula.move_to(RIGHT * 3.3 + DOWN * 1.2)
        direction_formula[0].set_color(correlation_color)
        direction_formula[2].set_color(correlation_color)

        direction_note = bottom_note(
            "Standardization changes vector lengths but leaves the angle between them unchanged.",
            color=correlation_color,
            size=22,
        )

        self.play(FadeIn(direction_heading))
        self.play(GrowArrow(original_arrow), Write(original_label))
        self.play(GrowArrow(scaled_arrow), Write(scaled_label))
        self.play(Write(direction_formula))
        pulse(scaled_arrow, color=correlation_color)
        self.play(FadeIn(direction_note, shift=UP * 0.12))
        self.wait(1.3)

        # ============================================================
        # 12. Mean product of z-scores = Pearson correlation
        # ============================================================
        clear_all(
            direction_heading,
            original_arrow,
            scaled_arrow,
            original_label,
            scaled_label,
            direction_formula,
            direction_note,
        )

        pearson_heading = section_heading("Pearson correlation: mean product of z-scores")

        z_mean_formula = MathTex(
            r"r",
            r"=",
            r"\frac{1}{n}\sum_{i=1}^{n}z_{X,i}z_{Y,i}",
        ).scale(1.05)
        z_mean_formula.move_to(UP * 1.0)
        z_mean_formula[0].set_color(correlation_color)
        z_mean_formula[2].set_color(correlation_color)

        cancel_formula = MathTex(
            r"r",
            r"=",
            r"\frac{\mathbf{X}_c\cdot\mathbf{Y}_c}{n\sigma_X\sigma_Y}",
            r"=",
            r"\frac{\mathbf{X}_c\cdot\mathbf{Y}_c}{\|\mathbf{X}_c\|\,\|\mathbf{Y}_c\|}",
        ).scale(0.9)
        cancel_formula.move_to(DOWN * 0.22)
        cancel_formula[0].set_color(correlation_color)
        cancel_formula[2].set_color(covariance_color)
        cancel_formula[4].set_color(correlation_color)

        example_correlation = MathTex(
            r"r",
            r"=",
            r"\frac{6}{\sqrt{10}\sqrt{10}}",
            r"=",
            r"\frac{3}{5}",
            r"=",
            r"0.6",
        ).scale(0.98)
        example_correlation.move_to(DOWN * 1.35)
        example_correlation[0].set_color(correlation_color)
        example_correlation[2].set_color(product_color)
        example_correlation[4].set_color(correlation_color)
        example_correlation[6].set_color(correlation_color)

        pearson_note = bottom_note(
            "Dividing by both vector lengths removes the two scales of variation.",
            color=correlation_color,
            size=22,
        )

        self.play(FadeIn(pearson_heading))
        self.play(Write(z_mean_formula))
        self.play(Write(cancel_formula))
        pulse(cancel_formula[4], color=correlation_color)
        self.play(Write(example_correlation))
        pulse(example_correlation[6], color=correlation_color)
        self.play(FadeIn(pearson_note, shift=UP * 0.12))
        self.wait(1.4)

        # ============================================================
        # 13. Normalized dot product is the cosine
        # ============================================================
        clear_all(
            pearson_heading,
            z_mean_formula,
            cancel_formula,
            example_correlation,
            pearson_note,
        )

        cosine_heading = section_heading("Correlation is the cosine of the angle")

        diagram_origin = LEFT * 4.6 + DOWN * 1.25
        x_arrow = Arrow(
            diagram_origin,
            diagram_origin + RIGHT * 4.0,
            color=x_color,
            stroke_width=6,
            buff=0,
            max_tip_length_to_length_ratio=0.13,
        )
        y_arrow = Arrow(
            diagram_origin,
            diagram_origin + RIGHT * 2.4 + UP * 3.2,
            color=y_color,
            stroke_width=6,
            buff=0,
            max_tip_length_to_length_ratio=0.13,
        )

        x_ray = Line(diagram_origin, diagram_origin + RIGHT * 2.0)
        y_ray = Line(diagram_origin, diagram_origin + RIGHT * 1.2 + UP * 1.6)
        theta_arc = Angle(x_ray, y_ray, radius=0.75, color=correlation_color)
        theta_label = MathTex(r"\theta", color=correlation_color).scale(0.9)
        theta_label.move_to(diagram_origin + RIGHT * 0.95 + UP * 0.45)

        x_arrow_label = MathTex(r"\mathbf{X}_c", color=x_color).scale(0.9)
        x_arrow_label.next_to(x_arrow.get_end(), DOWN, buff=0.12)
        y_arrow_label = MathTex(r"\mathbf{Y}_c", color=y_color).scale(0.9)
        y_arrow_label.next_to(y_arrow.get_end(), RIGHT, buff=0.12)

        cosine_formula = MathTex(
            r"r",
            r"=",
            r"\frac{\mathbf{X}_c\cdot\mathbf{Y}_c}{\|\mathbf{X}_c\|\,\|\mathbf{Y}_c\|}",
            r"=",
            r"\cos\theta",
        ).scale(0.98)
        cosine_formula.move_to(RIGHT * 3.55 + UP * 0.45)
        cosine_formula[0].set_color(correlation_color)
        cosine_formula[2].set_color(deviation_color)
        cosine_formula[4].set_color(correlation_color)

        example_angle = MathTex(
            r"r=0.6",
            r"\Longrightarrow",
            r"\theta\approx53.1^\circ",
        ).scale(0.9)
        example_angle.move_to(RIGHT * 3.55 + DOWN * 0.8)
        example_angle[0].set_color(correlation_color)
        example_angle[2].set_color(correlation_color)

        cosine_note = bottom_note(
            "Only directional alignment remains.",
            color=correlation_color,
            size=24,
        )

        self.play(FadeIn(cosine_heading))
        self.play(GrowArrow(x_arrow), Write(x_arrow_label))
        self.play(GrowArrow(y_arrow), Write(y_arrow_label))
        self.play(Create(theta_arc), Write(theta_label))
        self.play(Write(cosine_formula))
        pulse(cosine_formula[4], color=correlation_color)
        self.play(Write(example_angle))
        self.play(FadeIn(cosine_note, shift=UP * 0.12))
        self.wait(1.4)

        # ============================================================
        # 14. The three geometric landmarks: +1, -1, and 0
        # ============================================================
        clear_all(
            cosine_heading,
            x_arrow,
            y_arrow,
            theta_arc,
            theta_label,
            x_arrow_label,
            y_arrow_label,
            cosine_formula,
            example_angle,
            cosine_note,
        )

        landmarks_heading = section_heading("Three geometric landmarks")

        panel_centers = [LEFT * 4.4, ORIGIN, RIGHT * 4.4]
        panel_colors = [mean_color, y_color, correlation_color]
        panel_titles = [r"r=+1", r"r=-1", r"r=0"]
        panel_captions = [
            "same direction",
            "opposite directions",
            "perpendicular",
        ]

        panels = VGroup()
        panel_arrows = VGroup()
        panel_text = VGroup()

        for i, center in enumerate(panel_centers):
            panel = RoundedRectangle(
                width=3.65,
                height=3.3,
                corner_radius=0.14,
                color=panel_colors[i],
                stroke_width=2.5,
            )
            panel.set_fill(panel_colors[i], opacity=0.06)
            panel.move_to(center + DOWN * 0.2)
            panels.add(panel)

            result = MathTex(panel_titles[i], color=panel_colors[i]).scale(1.0)
            result.move_to(panel.get_top() + DOWN * 0.42)

            caption = Text(
                panel_captions[i],
                font_size=21,
                color=panel_colors[i],
            )
            caption.move_to(panel.get_bottom() + UP * 0.38)
            panel_text.add(result, caption)

            arrow_origin = panel.get_center() + DOWN * 0.2
            if i == 0:
                first = Arrow(
                    arrow_origin,
                    arrow_origin + RIGHT * 1.2 + UP * 0.7,
                    color=x_color,
                    buff=0,
                    stroke_width=5,
                )
                second = Arrow(
                    arrow_origin,
                    arrow_origin + RIGHT * 1.6 + UP * 0.93,
                    color=y_color,
                    buff=0,
                    stroke_width=5,
                )
            elif i == 1:
                first = Arrow(
                    arrow_origin,
                    arrow_origin + RIGHT * 1.25,
                    color=x_color,
                    buff=0,
                    stroke_width=5,
                )
                second = Arrow(
                    arrow_origin,
                    arrow_origin + LEFT * 1.25,
                    color=y_color,
                    buff=0,
                    stroke_width=5,
                )
            else:
                first = Arrow(
                    arrow_origin,
                    arrow_origin + RIGHT * 1.25,
                    color=x_color,
                    buff=0,
                    stroke_width=5,
                )
                second = Arrow(
                    arrow_origin,
                    arrow_origin + UP * 1.25,
                    color=y_color,
                    buff=0,
                    stroke_width=5,
                )
            panel_arrows.add(first, second)

        landmarks_note = bottom_note(
            "The sign and magnitude of r describe the angle between the deviation patterns.",
            color=correlation_color,
            size=21,
        )

        self.play(FadeIn(landmarks_heading))
        self.play(LaggedStart(*[Create(panel) for panel in panels], lag_ratio=0.12))
        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in panel_arrows], lag_ratio=0.08))
        self.play(LaggedStart(*[FadeIn(item) for item in panel_text], lag_ratio=0.08))
        self.play(FadeIn(landmarks_note, shift=UP * 0.12))
        self.wait(1.5)

        # ============================================================
        # 15. Zero correlation does not imply no relationship
        # ============================================================
        clear_all(
            landmarks_heading,
            panels,
            panel_arrows,
            panel_text,
            landmarks_note,
        )

        nonlinear_heading = section_heading("Zero correlation means no linear alignment")

        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[0, 4.8, 1],
            x_length=5.0,
            y_length=3.6,
            axis_config={
                "color": GRAY_B,
                "stroke_width": 2,
                "include_tip": True,
                "tip_width": 0.14,
                "tip_height": 0.14,
            },
        )
        axes.move_to(LEFT * 3.6 + DOWN * 0.1)

        parabola = axes.plot(
            lambda x: x**2,
            x_range=[-2.1, 2.1],
            color=product_color,
            stroke_width=4,
        )

        sample_x = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
        nonlinear_dots = VGroup(
            *[
                Dot(
                    axes.c2p(x, x**2),
                    radius=0.055,
                    color=product_color,
                )
                for x in sample_x
            ]
        )

        nonlinear_formula = MathTex(
            r"Y=X^2",
            r"\qquad",
            r"r=0",
        ).scale(1.08)
        nonlinear_formula.move_to(RIGHT * 3.55 + UP * 0.5)
        nonlinear_formula[0].set_color(product_color)
        nonlinear_formula[2].set_color(correlation_color)

        nonlinear_text = Paragraph(
            "A strong curved relationship",
            "can have zero Pearson correlation.",
            alignment="center",
            font_size=24,
            color=GRAY_A,
            line_spacing=0.85,
        )
        nonlinear_text.move_to(RIGHT * 3.55 + DOWN * 0.65)

        nonlinear_note = bottom_note(
            "Pearson correlation detects linear directional alignment, not every possible relationship.",
            color=correlation_color,
            size=21,
        )

        self.play(FadeIn(nonlinear_heading))
        self.play(Create(axes))
        self.play(Create(parabola), LaggedStart(*[FadeIn(dot) for dot in nonlinear_dots], lag_ratio=0.06))
        self.play(Write(nonlinear_formula))
        pulse(nonlinear_formula[2], color=correlation_color)
        self.play(FadeIn(nonlinear_text, shift=UP * 0.1))
        self.play(FadeIn(nonlinear_note, shift=UP * 0.12))
        self.wait(1.5)

        # ============================================================
        # 16. Connect the full geometric picture
        # ============================================================
        clear_all(
            nonlinear_heading,
            axes,
            parabola,
            nonlinear_dots,
            nonlinear_formula,
            nonlinear_text,
            nonlinear_note,
        )

        summary_heading = section_heading("One geometric picture")

        mean_formula = MathTex(
            r"\text{mean:}\quad",
            r"\operatorname{proj}_{\mathcal C}(\mathbf{X})",
        ).scale(0.78)
        mean_formula[0].set_color(GRAY_A)
        mean_formula[1].set_color(mean_color)
        mean_box = formula_box(mean_formula, mean_color, width=5.8, height=1.2)
        mean_box.move_to(LEFT * 3.2 + UP * 0.9)

        variance_formula = MathTex(
            r"\text{variance:}\quad",
            r"\frac{\|\mathbf{X}_c\|^2}{n}",
        ).scale(0.82)
        variance_formula[0].set_color(GRAY_A)
        variance_formula[1].set_color(deviation_color)
        variance_box = formula_box(variance_formula, deviation_color, width=5.8, height=1.2)
        variance_box.move_to(RIGHT * 3.2 + UP * 0.9)

        covariance_summary = MathTex(
            r"\text{covariance:}\quad",
            r"\frac{\mathbf{X}_c\cdot\mathbf{Y}_c}{n}",
        ).scale(0.82)
        covariance_summary[0].set_color(GRAY_A)
        covariance_summary[1].set_color(covariance_color)
        covariance_box = formula_box(
            covariance_summary,
            covariance_color,
            width=5.8,
            height=1.2,
        )
        covariance_box.move_to(LEFT * 3.2 + DOWN * 0.75)

        correlation_summary = MathTex(
            r"\text{correlation:}\quad",
            r"\frac{\mathbf{X}_c\cdot\mathbf{Y}_c}{\|\mathbf{X}_c\|\,\|\mathbf{Y}_c\|}",
            r"=\cos\theta",
        ).scale(0.70)
        correlation_summary[0].set_color(GRAY_A)
        correlation_summary[1].set_color(correlation_color)
        correlation_summary[2].set_color(correlation_color)
        correlation_box = formula_box(
            correlation_summary,
            correlation_color,
            width=5.8,
            height=1.2,
        )
        correlation_box.move_to(RIGHT * 3.2 + DOWN * 0.75)

        summary_note = bottom_note(
            "Variance, covariance, and correlation are measurements constructed from deviation vectors.",
            color=correlation_color,
            size=21,
        )

        self.play(FadeIn(summary_heading))
        self.play(Create(mean_box[0]), FadeIn(mean_box[1]))
        self.play(Create(variance_box[0]), FadeIn(variance_box[1]))
        self.play(Create(covariance_box[0]), FadeIn(covariance_box[1]))
        self.play(Create(correlation_box[0]), FadeIn(correlation_box[1]))
        self.play(FadeIn(summary_note, shift=UP * 0.12))
        self.wait(1.6)

        # ============================================================
        # 17. Closing statement
        # ============================================================
        clear_all(
            summary_heading,
            mean_box,
            variance_box,
            covariance_box,
            correlation_box,
            summary_note,
        )

        closing_box = RoundedRectangle(
            width=11.6,
            height=2.25,
            corner_radius=0.16,
            color=correlation_color,
            stroke_width=3,
        )
        closing_box.set_fill(correlation_color, opacity=0.09)
        closing_box.move_to(DOWN * 0.25)

        closing_text = Paragraph(
            "Covariance keeps scale and direction.",
            "Pearson correlation removes scale.",
            "What remains is the cosine of the angle.",
            alignment="center",
            font_size=27,
            color=correlation_color,
            line_spacing=0.8,
        )
        closing_text.move_to(closing_box.get_center())

        self.play(Create(closing_box))
        self.play(FadeIn(closing_text, shift=UP * 0.12))
        self.wait(2.5)