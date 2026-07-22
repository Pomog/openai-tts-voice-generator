from manim import *


class DatasetMeanAsProjection(Scene):
    """
    Visual continuation for the narration about the mean as the common
    coordinate of the orthogonal projection onto the constant subspace.

    Render:
        manim -pql dataset_mean_as_projection.py DatasetMeanAsProjection

    High quality:
        manim -pqh --fps 60 dataset_mean_as_projection.py DatasetMeanAsProjection
    """

    def construct(self):
        # ------------------------------------------------------------
        # Helpers
        # ------------------------------------------------------------
        def pulse(mobject, color=YELLOW, scale_factor=1.10, run_time=0.65):
            self.play(
                Indicate(
                    mobject,
                    color=color,
                    scale_factor=scale_factor,
                ),
                run_time=run_time,
            )

        def bottom_note(text, color=YELLOW, size=23, y=-3.25):
            note = Text(text, font_size=size, color=color)
            note.move_to(UP * y)
            return note

        def clear(*objects, run_time=0.7):
            animations = [FadeOut(obj) for obj in objects if obj is not None]
            if animations:
                self.play(*animations, run_time=run_time)

        # ------------------------------------------------------------
        # Persistent title
        # ------------------------------------------------------------
        title = Text("The Mean as a Projection", font_size=38)
        title.to_edge(UP)

        subtitle = Text(
            "Part 1 — Projection onto the constant subspace",
            font_size=23,
            color=GRAY_B,
        )
        subtitle.next_to(title, DOWN, buff=0.14)

        self.play(FadeIn(title), FadeIn(subtitle, shift=UP * 0.12))
        self.wait(0.4)

        # ============================================================
        # 1. Opening statement: mean = common coordinate
        # ============================================================
        dataset_general = MathTex(
            r"\mathbf{x}=",
            r"\begin{bmatrix}x_1\\x_2\\\vdots\\x_n\end{bmatrix}",
            r"\in\mathbb{R}^n",
        ).scale(0.95)
        dataset_general.move_to(LEFT * 3.6 + UP * 0.45)

        projection_general = MathTex(
            r"\operatorname{proj}_{\mathcal C}(\mathbf{x})=",
            r"\begin{bmatrix}c\\c\\\vdots\\c\end{bmatrix}",
            r"\in\mathbb{R}^n",
        ).scale(0.92)
        projection_general.move_to(RIGHT * 3.35 + UP * 0.45)
        projection_general[1].set_color(GREEN)

        projection_arrow = Arrow(
            dataset_general.get_right() + RIGHT * 0.15,
            projection_general.get_left() + LEFT * 0.15,
            buff=0.05,
            color=GREEN,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.16,
        )

        constant_space = MathTex(
            r"\mathcal C=\operatorname{span}\{\mathbf 1_n\}",
            r"=\left\{c\mathbf 1_n:c\in\mathbb R\right\}",
        ).scale(0.93)
        constant_space.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        constant_space.move_to(DOWN * 1.25)

        common_coordinate = Text(
            "one common coordinate:  c",
            font_size=25,
            color=GREEN,
        )
        common_coordinate.next_to(constant_space, DOWN, buff=0.25)

        opening_note = bottom_note(
            "The scalar c will turn out to be the arithmetic mean.",
            color=YELLOW,
            size=23,
        )
        opening_note.next_to(constant_space, DOWN, buff=0.55)

        # VOICEOVER:
        # "I want to share a geometric point of view on the mean..."
        self.play(Write(dataset_general))
        self.play(GrowArrow(projection_arrow))
        self.play(Write(projection_general))
        pulse(projection_general[1], color=GREEN)
        self.play(Write(constant_space))
        self.play(FadeIn(common_coordinate))
        self.play(FadeIn(opening_note))
        self.wait(1.0)

        # ============================================================
        # 2. Same ambient space, one degree of freedom
        # ============================================================
        clear(
            dataset_general,
            projection_general,
            projection_arrow,
            constant_space,
            common_coordinate,
            opening_note,
        )

        same_space = MathTex(
            r"\mathbf{x}\in\mathbb R^n",
            r"\qquad",
            r"\operatorname{proj}_{\mathcal C}(\mathbf{x})\in\mathbb R^n",
        ).scale(1.05)
        same_space.move_to(UP * 1.3)
        same_space[0].set_color(BLUE_B)
        same_space[2].set_color(GREEN)

        n_coordinates = MathTex(
            r"\begin{bmatrix}c\\c\\\vdots\\c\end{bmatrix}",
        ).scale(1.2)
        n_coordinates.move_to(LEFT * 1.6 + DOWN * 0.5)

        coordinates_brace = Brace(n_coordinates, RIGHT, color=BLUE_B)
        coordinates_label = Text(
            "n coordinate positions",
            font_size=24,
            color=BLUE_B,
        )
        coordinates_label.next_to(coordinates_brace, RIGHT, buff=0.2)

        dof_formula = MathTex(
            r"c\in\mathbb R",
            r"\quad\Longrightarrow\quad",
            r"1\ \text{degree of freedom}",
        ).scale(1.0)
        dof_formula.move_to(RIGHT * 3.1 + DOWN * 1.5)
        dof_formula[0].set_color(GREEN)
        dof_formula[2].set_color(YELLOW)

        equality_note = bottom_note(
            "The coordinates remain present, but they cannot vary independently.",
            color=YELLOW,
            size=22,
        )

        # VOICEOVER:
        # "The projected vector still lies in the same n-dimensional space..."
        self.play(Write(same_space))
        pulse(same_space[0], color=BLUE_B)
        pulse(same_space[2], color=GREEN)
        self.play(
            Write(n_coordinates),
            GrowFromCenter(coordinates_brace),
            FadeIn(coordinates_label, shift=LEFT * 0.15),
        )
        self.play(Write(dof_formula))
        pulse(dof_formula[0], color=GREEN)
        pulse(dof_formula[2], color=YELLOW)
        self.play(FadeIn(equality_note, shift=UP * 0.15))
        self.wait(1.0)

        # ============================================================
        # 3. Decomposition into two components
        # ============================================================
        clear(
            same_space,
            n_coordinates,
            coordinates_brace,
            coordinates_label,
            dof_formula,
            equality_note,
        )

        decomposition = MathTex(
            r"\mathbf{x}",
            r"=",
            r"\underbrace{\operatorname{proj}_{\mathcal C}(\mathbf{x})}_{\text{constant component}}",
            r"+\;",
            r"\underbrace{\left(\mathbf{x}-\operatorname{proj}_{\mathcal C}(\mathbf{x})\right)}_{\text{remainder}}",
        ).scale(0.88)

        decomposition[0].set_color(BLUE_B)
        decomposition[2].set_color(GREEN)
        decomposition[4].set_color(YELLOW)

        decomposition.move_to(UP * 0.55)

        component_note = bottom_note(
            "First, we determine the constant component.",
            color=GREEN,
            size=24,
            y=-2.3,
        )

        # VOICEOVER:
        # "Let us separate the dataset vector into two components..."
        self.play(Write(decomposition))

        pulse(decomposition[0], color=BLUE_B)
        pulse(decomposition[2], color=GREEN)
        pulse(decomposition[4], color=YELLOW)

        self.play(
            FadeIn(
                component_note,
                shift=UP * 0.15,
            )
        )

        self.wait(0.9)

        

        # ============================================================
        # 4. Projection = closest point in the subspace
        # ============================================================
        clear(decomposition, component_note)

        geometry_title = Text(
            "Why the closest constant vector?",
            font_size=29,
            color=GRAY_A,
        )
        geometry_title.move_to(UP * 2.15)

        constant_line = Line(
            LEFT * 5.2 + DOWN * 1.25,
            RIGHT * 5.2 + UP * 1.15,
            color=GREEN,
            stroke_width=5,
        )
        constant_line_label = MathTex(
            r"\mathcal C=\operatorname{span}\{\mathbf 1_n\}",
            color=GREEN,
        ).scale(0.82)
        constant_line_label.next_to(constant_line.get_right(), UP, buff=0.15)
        constant_line_label.shift(LEFT * 1.15)

        x_point = Dot(LEFT * 0.8 + UP * 1.65, color=BLUE_B, radius=0.11)
        x_label = MathTex(r"\mathbf{x}", color=BLUE_B).scale(0.9)
        x_label.next_to(x_point, LEFT, buff=0.15)

        p_point = Dot(LEFT * 0.25 + DOWN * 0.12, color=GREEN, radius=0.11)
        p_label = MathTex(
            r"\mathbf{p}=\operatorname{proj}_{\mathcal C}(\mathbf{x})",
            color=GREEN,
        ).scale(0.78)
        p_label.next_to(p_point, DOWN, buff=0.2)

        remainder = DashedLine(
            x_point.get_center(),
            p_point.get_center(),
            color=YELLOW,
            stroke_width=4,
            dash_length=0.12,
        )

        q_left = Dot(LEFT * 2.8 + DOWN * 0.7, color=GRAY_B, radius=0.08)
        q_right = Dot(RIGHT * 2.6 + UP * 0.55, color=GRAY_B, radius=0.08)
        candidate_left = DashedLine(
            x_point.get_center(),
            q_left.get_center(),
            color=GRAY_C,
            stroke_width=2.5,
        )
        candidate_right = DashedLine(
            x_point.get_center(),
            q_right.get_center(),
            color=GRAY_C,
            stroke_width=2.5,
        )

        closest_note = bottom_note(
            "The projection leaves the smallest possible remainder.",
            color=YELLOW,
            size=23,
        )

        # VOICEOVER:
        # "We need the closest such vector because an orthogonal projection..."
        self.play(FadeIn(geometry_title))
        self.play(Create(constant_line), FadeIn(constant_line_label))
        self.play(FadeIn(x_point), FadeIn(x_label))
        self.play(
            FadeIn(q_left),
            FadeIn(q_right),
            Create(candidate_left),
            Create(candidate_right),
        )
        self.wait(0.35)
        self.play(
            FadeIn(p_point),
            FadeIn(p_label),
            Create(remainder),
        )
        pulse(remainder, color=YELLOW, scale_factor=1.04)
        self.play(FadeIn(closest_note, shift=UP * 0.15))
        self.wait(1.0)

        # ============================================================
        # 5. Example and general squared-distance formula
        # ============================================================
        clear(
            geometry_title,
            constant_line,
            constant_line_label,
            x_point,
            x_label,
            p_point,
            p_label,
            remainder,
            q_left,
            q_right,
            candidate_left,
            candidate_right,
            closest_note,
        )

        example_x = MathTex(
            r"\mathbf{x}=",
            r"\begin{bmatrix}2\\4\\6\end{bmatrix}",
        ).scale(1.02)
        example_x.move_to(LEFT * 4.5 + UP * 0.85)
        example_x[1].set_color(BLUE_B)

        example_constant = MathTex(
            r"\mathbf{q}(c)=",
            r"\begin{bmatrix}c\\c\\c\end{bmatrix}",
        ).scale(1.02)
        example_constant.move_to(LEFT * 4.45 + DOWN * 1.0)
        example_constant[1].set_color(GREEN)

        distance_example = MathTex(
            r"D^2(c)",
            "=",
            r"\left\|\mathbf{x}-\mathbf{q}(c)\right\|^2",
            "=",
            r"(2-c)^2+(4-c)^2+(6-c)^2",
        ).scale(0.83)
        distance_example.move_to(RIGHT * 2.25 + UP * 0.95)
        distance_example[0].set_color(YELLOW)

        distance_general = MathTex(
            r"D^2(c)",
            "=",
            r"\left\|\mathbf{x}-c\mathbf 1_n\right\|^2",
            "=",
            r"\sum_{i=1}^{n}(x_i-c)^2",
        ).scale(0.9)
        distance_general.move_to(RIGHT * 2.25 + DOWN * 0.65)
        distance_general[0].set_color(YELLOW)

        additive_note = bottom_note(
            "Each coordinate contributes one squared difference.",
            color=YELLOW,
            size=23,
        )

        # VOICEOVER:
        # "Therefore, to find the projection, we must choose c..."
        self.play(Write(example_x), Write(example_constant))
        pulse(example_x[1], color=BLUE_B)
        pulse(example_constant[1], color=GREEN)

        # VOICEOVER:
        # "We use the squared distance because..."
        self.play(Write(distance_example))
        pulse(distance_example[0], color=YELLOW)

        # VOICEOVER:
        # "For a general dataset vector..."
        self.play(Write(distance_general))
        self.play(FadeIn(additive_note, shift=UP * 0.15))
        pulse(distance_general[-1], color=YELLOW, scale_factor=1.06)
        self.wait(1.0)

        # ============================================================
        # 6. Squared distance as a function of c
        # ============================================================
        clear(example_x, example_constant, distance_example, distance_general, additive_note)

        function_formula = MathTex(
            r"D^2(c)=(2-c)^2+(4-c)^2+(6-c)^2"
        ).scale(0.9)

        function_formula.move_to(LEFT * 3.35 + UP * 1.55)

        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 60, 10],
            x_length=6.6,
            y_length=3.8,
            axis_config={"include_numbers": True, "font_size": 22},
            tips=False,
        )
        axes.move_to(RIGHT * 2.5 + DOWN * 1.0)
        x_axis_label = axes.get_x_axis_label(MathTex("c").scale(0.75))
        y_axis_label = axes.get_y_axis_label(MathTex(r"D^2(c)").scale(0.72))
        y_axis_label.shift(DOWN * 0.30)

        graph = axes.plot(
            lambda value: 3 * (value - 4) ** 2 + 8,
            x_range=[0, 8],
            color=YELLOW,
        )
        minimum_dot = Dot(axes.c2p(4, 8), color=GREEN, radius=0.1)
        minimum_label = MathTex(r"(4,8)", color=GREEN).scale(0.75)
        minimum_label.next_to(minimum_dot, UP + RIGHT, buff=0.12)

        variable_note = bottom_note(
            "Now c is the only variable.",
            color=GREEN,
            size=23,
        )

        # VOICEOVER:
        # "This squared distance is now a function of the single unknown value..."
        self.play(Write(function_formula))
        self.play(Create(axes), FadeIn(x_axis_label), FadeIn(y_axis_label))
        self.play(Create(graph), run_time=1.2)
        self.play(FadeIn(minimum_dot), FadeIn(minimum_label))
        self.play(FadeIn(variable_note, shift=UP * 0.15))
        pulse(minimum_dot, color=GREEN, scale_factor=1.25)
        self.wait(1.0)

        # ============================================================
        # 7. Derivative and minimum
        # ============================================================
        clear(
            function_formula,
            axes,
            x_axis_label,
            y_axis_label,
            graph,
            minimum_dot,
            minimum_label,
            variable_note,
        )

        general_distance = MathTex(
            r"D^2(c)=\sum_{i=1}^{n}(x_i-c)^2",
        ).scale(1.05)
        general_distance.move_to(UP * 1.75)

        derivative_line = MathTex(
            r"\frac{dD^2}{dc}",
            "=",
            r"-2\sum_{i=1}^{n}(x_i-c)",
            "=",
            r"0",
        ).scale(1.02)
        derivative_line.next_to(general_distance, DOWN, buff=0.25)
        derivative_line[0].set_color(BLUE_B)
        derivative_line[2].set_color(YELLOW)
        derivative_line[4].set_color(GREEN)

        algebra_line = MathTex(
            r"\sum_{i=1}^{n}x_i-nc=0",
            r"\quad\Longrightarrow\quad",
            r"c=\frac{1}{n}\sum_{i=1}^{n}x_i=\bar{x}",
        ).scale(1.0)
        algebra_line.next_to(derivative_line, DOWN, buff=0.25)
        algebra_line[2].set_color(GREEN)

        second_derivative = MathTex(
            r"\frac{d^2D^2}{dc^2}=2n>0",
            r"\quad\Longrightarrow\quad",
            r"\text{unique minimum}",
        ).scale(0.92)
        second_derivative.next_to(algebra_line, DOWN, buff=0.25)
        second_derivative[0].set_color(YELLOW)
        second_derivative[2].set_color(GREEN)


        # VOICEOVER:
        # "We differentiate this function and set the derivative equal to zero..."
        self.play(Write(general_distance))
        self.play(Write(derivative_line))
        pulse(derivative_line[4], color=GREEN)

        # VOICEOVER:
        # "Solving the resulting equation gives..."
        self.play(Write(algebra_line))
        pulse(algebra_line[2], color=GREEN)

        # VOICEOVER:
        # "This value is exactly the arithmetic mean..."
        mean_box = SurroundingRectangle(
            algebra_line[2],
            color=GREEN,
            buff=0.16,
            corner_radius=0.08,
        )
        self.play(Create(mean_box))

        # VOICEOVER:
        # "The second derivative is positive..."
        self.play(Write(second_derivative))
        pulse(second_derivative[0], color=YELLOW)
        pulse(second_derivative[2], color=GREEN)
        self.wait(1.1)

        # ============================================================
        # 8. Standard vector-projection formula
        # ============================================================
        clear(
            general_distance,
            derivative_line,
            algebra_line,
            second_derivative,
            mean_box,
        )

        span_formula = MathTex(
            r"\mathcal C=\operatorname{span}\{\mathbf 1_n\}",
            r"\qquad",
            r"\mathbf 1_n=\begin{bmatrix}1\\1\\\vdots\\1\end{bmatrix}",
        ).scale(0.92)
        span_formula.move_to(UP * 1.85)
        span_formula[0].set_color(GREEN)
        span_formula[2].set_color(BLUE_B)
        span_formula[2].shift(RIGHT * 1.5)

        projection_formula = MathTex(
            r"\operatorname{proj}_{\mathcal C}(\mathbf{x})",
            "=",
            r"\frac{\mathbf{x}\cdot\mathbf 1_n}"
            r"{\mathbf 1_n\cdot\mathbf 1_n}\mathbf 1_n",
        ).scale(1.02)
        projection_formula.move_to(UP * 0.55)
        projection_formula.move_to(LEFT * 0.55)
        projection_formula[0].set_color(GREEN)

        numerator = MathTex(
            r"\mathbf{x}\cdot\mathbf 1_n=\sum_{i=1}^{n}x_i",
        ).scale(0.9)
        numerator.move_to(LEFT * 3.25 + DOWN * 1.00)
        numerator.set_color(BLUE_B)

        denominator = MathTex(
            r"\mathbf 1_n\cdot\mathbf 1_n=n",
        ).scale(0.9)
        denominator.move_to(RIGHT * 3.25 + DOWN * 1.00)
        denominator.set_color(YELLOW)

        simplified_projection = MathTex(
            r"\operatorname{proj}_{\mathcal C}(\mathbf{x})",
            "=",
            r"\frac{1}{n}\sum_{i=1}^{n}x_i\,\mathbf 1_n",
            "=",
            r"\bar{x}\mathbf 1_n",
        ).scale(1.0)
        simplified_projection.move_to(DOWN * 2.15)
        simplified_projection[0].set_color(GREEN)
        simplified_projection[-1].set_color(GREEN)

        formula_note = bottom_note(
            "The denominator is n because the all-ones vector has n unit entries.",
            color=YELLOW,
            size=21,
            y=-3.28,
        )

        # VOICEOVER:
        # "This result also agrees with the standard vector-projection formula."
        self.play(Write(span_formula))

        # VOICEOVER:
        # "To project the dataset vector onto this subspace..."
        self.play(Write(projection_formula))
        pulse(projection_formula, color=GREEN, scale_factor=1.04)

        # VOICEOVER:
        # "The numerator is the sum of all observations..."
        self.play(Write(numerator), Write(denominator))
        pulse(numerator, color=BLUE_B)
        pulse(denominator, color=YELLOW)

        # VOICEOVER:
        # "Therefore, the projection is the mean multiplied..."
        self.play(Write(simplified_projection))
        self.play(FadeIn(formula_note, shift=UP * 0.12))
        pulse(simplified_projection[-1], color=GREEN)
        self.wait(1.0)

        # ============================================================
        # 9. Concrete example and final statement
        # ============================================================
        clear(
            span_formula,
            projection_formula,
            numerator,
            denominator,
            simplified_projection,
            formula_note,
        )

        example_mean = MathTex(
            r"\mathbf{x}=\begin{bmatrix}2\\4\\6\end{bmatrix}",
            r"\qquad",
            r"\bar{x}=4",
        ).scale(1.02)
        example_mean.move_to(UP * 1.35)
        example_mean[0].set_color(BLUE_B)
        example_mean[2].set_color(GREEN)

        example_projection = MathTex(
            r"\operatorname{proj}_{\mathcal C}(\mathbf{x})",
            "=",
            r"4\begin{bmatrix}1\\1\\1\end{bmatrix}",
            "=",
            r"\begin{bmatrix}4\\4\\4\end{bmatrix}",
        ).scale(1.0)
        example_projection.move_to(DOWN * 0.15)
        example_projection[0].set_color(GREEN)
        example_projection[-1].set_color(GREEN)

        final_box = RoundedRectangle(
            width=11.3,
            height=1.15,
            corner_radius=0.14,
            color=GREEN,
            stroke_width=3,
        )
        final_box.set_fill(GREEN_E, opacity=0.10)
        final_box.move_to(DOWN * 2.15)

        final_statement = Text(
            "The mean is the scalar repeated in every coordinate of the projection.",
            font_size=25,
            color=GREEN,
        )
        final_statement.move_to(final_box.get_center())

        # VOICEOVER:
        # "The mean of a dataset is the single scalar that..."
        self.play(Write(example_mean))
        self.play(Write(example_projection))
        pulse(example_mean[2], color=GREEN)
        pulse(example_projection[-1], color=GREEN)
        self.play(Create(final_box), FadeIn(final_statement, shift=UP * 0.10))
        self.wait(2.0)