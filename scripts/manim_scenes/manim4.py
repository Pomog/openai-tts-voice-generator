from manim import *


class DatasetAsVectorPart1Opening(Scene):
    def construct(self):
        # ------------------------------------------------------------
        # Helpers
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

        def make_note(text, color=YELLOW, y=-2.75, size=22):
            note = Text(text, font_size=size, color=color)
            note.move_to(UP * y)
            return note

        def concept_row(left_text, right_text, color):
            left = Text(left_text, font_size=28, color=color)
            arrow = MathTex(r"\longrightarrow", color=GRAY_B).scale(0.9)
            right = Text(right_text, font_size=28)
            row = VGroup(left, arrow, right)
            row.arrange(RIGHT, buff=0.35)
            return row

        # ------------------------------------------------------------
        # Title
        # ------------------------------------------------------------
        title = Text("A Dataset as a Vector", font_size=40)
        title.to_edge(UP)

        subtitle = Text(
            "Part 1 — The mean and the deviation vector",
            font_size=25,
            color=GRAY_B,
        )
        subtitle.next_to(title, DOWN, buff=0.18)

        # ------------------------------------------------------------
        # Opening: familiar representations of one variable
        # ------------------------------------------------------------
        one_variable_label = Text(
            "One numerical variable",
            font_size=28,
            color=BLUE_B,
        )
        one_variable_label.move_to(UP * 1.65)

        table_box = RoundedRectangle(
            width=3.7,
            height=2.65,
            corner_radius=0.12,
            color=GRAY_B,
            stroke_width=2,
        )
        table_box.move_to(DOWN * 0.15)

        table_header = VGroup(
            Text("Observation", font_size=22, color=GRAY_A),
            Text("Value", font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.85)
        table_header.move_to(table_box.get_top() + DOWN * 0.38)

        divider = Line(
            table_box.get_left() + RIGHT * 1.95 + UP * 0.9,
            table_box.get_left() + RIGHT * 1.95 + DOWN * 1.0,
            color=GRAY_D,
            stroke_width=2,
        )

        table_rows = VGroup(
            VGroup(Text("1", font_size=25), MathTex("2").scale(0.9)).arrange(RIGHT, buff=1.55),
            VGroup(Text("2", font_size=25), MathTex("4").scale(0.9)).arrange(RIGHT, buff=1.55),
            VGroup(Text("3", font_size=25), MathTex("6").scale(0.9)).arrange(RIGHT, buff=1.55),
        )
        table_rows.arrange(DOWN, buff=0.28)
        table_rows.move_to(table_box.get_center() + DOWN * 0.28)

        table_group = VGroup(table_box, table_header, divider, table_rows)

        list_label = Text("The same data as a list", font_size=25, color=GRAY_B)
        list_values = MathTex(r"2,\;4,\;6").scale(1.35)
        list_group = VGroup(list_label, list_values).arrange(DOWN, buff=0.38)
        list_group.move_to(DOWN * 0.1)

        # ------------------------------------------------------------
        # Vector representation
        # ------------------------------------------------------------
        vector_name = MathTex(r"\mathbf{V}=").scale(1.25)
        vector_matrix = Matrix(
            [["2"], ["4"], ["6"]],
            left_bracket="[",
            right_bracket="]",
            bracket_h_buff=0.22,
            v_buff=0.55,
        ).scale(1.08)
        vector_group = VGroup(vector_name, vector_matrix)
        vector_group.arrange(RIGHT, buff=0.28)
        vector_group.move_to(DOWN * 0.05)

        coordinate_labels = VGroup(
            Text("first coordinate", font_size=21, color=BLUE_B),
            Text("second coordinate", font_size=21, color=BLUE_B),
            Text("third coordinate", font_size=21, color=BLUE_B),
        )
        coordinate_labels.arrange(DOWN, buff=0.43, aligned_edge=LEFT)
        coordinate_labels.next_to(vector_matrix, RIGHT, buff=0.65)

        coordinate_arrows = VGroup()
        entries = vector_matrix.get_entries()
        for entry, label in zip(entries, coordinate_labels):
            arrow = Arrow(
                entry.get_right() + RIGHT * 0.08,
                label.get_left() + LEFT * 0.08,
                buff=0.05,
                color=BLUE_D,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.16,
            )
            coordinate_arrows.add(arrow)

        vector_with_labels = VGroup(
            vector_group,
            coordinate_labels,
            coordinate_arrows,
        )
        vector_with_labels.move_to(DOWN * 0.05)

        note_single_variable = make_note(
            "Here, one column of observations is represented as one vector.",
            color=BLUE_B,
            y=-2.75,
            size=22,
        )

        # ------------------------------------------------------------
        # Dimensionality
        # ------------------------------------------------------------
        dimension_three = MathTex(
            r"3\ \text{observations}",
            r"\quad\Longrightarrow\quad",
            r"\mathbf{V}\in\mathbb{R}^{3}",
        ).scale(1.05)
        dimension_three.move_to(DOWN * 0.15)

        dimension_n = MathTex(
            r"n\ \text{observations}",
            r"\quad\Longrightarrow\quad",
            r"\mathbf{V}\in\mathbb{R}^{n}",
        ).scale(1.05)
        dimension_n.move_to(DOWN * 0.15)

        dimension_note = make_note(
            "The number of observations becomes the dimension of the vector.",
            color=YELLOW,
            y=-1.35,
            size=23,
        )

        # ------------------------------------------------------------
        # Preview of the geometric interpretation
        # ------------------------------------------------------------
        preview_title = Text(
            "Statistics through vector geometry",
            font_size=31,
            color=GRAY_A,
        )
        preview_title.move_to(UP * 1.55)

        preview_rows = VGroup(
            concept_row("Mean", "projection", GREEN),
            concept_row("Deviations", "a separate vector", YELLOW),
            concept_row("Variance", "squared length, with scaling", BLUE_B),
            concept_row("Correlation", "cosine of an angle", PURPLE_B),
        )
        preview_rows.arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        preview_rows.move_to(DOWN * 0.25)

        preview_note = make_note(
            "We will build each idea step by step.",
            color=GREEN,
            y=-2.75,
            size=23,
        )

        # ------------------------------------------------------------
        # Dataset-vector section
        # ------------------------------------------------------------
        section_title = Text("The Dataset Vector", font_size=35)
        section_title.to_edge(UP)

        example_label = Text("Example data", font_size=26, color=GRAY_B)
        example_values = MathTex(r"2,\;4,\;6").scale(1.25)

        example_box = RoundedRectangle(
            width=3.2,
            height=1.65,
            corner_radius=0.14,
            color=BLUE_D,
            stroke_width=3,
        )
        example_box.set_fill(BLUE_E, opacity=0.12)

        example_group = VGroup(example_box, example_label, example_values)
        example_label.move_to(example_box.get_top() + DOWN * 0.38)
        example_values.move_to(example_box.get_center() + DOWN * 0.22)
        example_group.move_to(LEFT * 3.45 + DOWN * 0.15)

        dataset_vector_name = MathTex(r"\mathbf{V}=").scale(1.18)
        dataset_vector_matrix = Matrix(
            [["2"], ["4"], ["6"]],
            left_bracket="[",
            right_bracket="]",
            bracket_h_buff=0.22,
            v_buff=0.52,
        ).scale(1.0)
        dataset_vector_group = VGroup(dataset_vector_name, dataset_vector_matrix)
        dataset_vector_group.arrange(RIGHT, buff=0.25)
        dataset_vector_group.move_to(RIGHT * 3.15 + DOWN * 0.15)

        conversion_arrow = Arrow(
            example_group.get_right() + RIGHT * 0.20,
            dataset_vector_group.get_left() + LEFT * 0.20,
            buff=0.1,
            color=YELLOW,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.16,
        )

        conversion_label = Text(
            "each value becomes a coordinate",
            font_size=20,
            color=YELLOW,
        )
        conversion_label.next_to(conversion_arrow, UP, buff=0.7)

        # ------------------------------------------------------------
        # Decomposition
        # ------------------------------------------------------------
        decomposition = MathTex(
            r"\mathbf{V}",
            "=",
            r"\mathbf{V}_{\text{mean}}",
            "+",
            r"\mathbf{V}_{\text{dev}}",
        ).scale(1.18)
        decomposition[0].set_color(BLUE_B)
        decomposition[2].set_color(GREEN)
        decomposition[4].set_color(YELLOW)
        decomposition.move_to(UP * 0.4)

        mean_label = Text(
            "common level",
            font_size=24,
            color=GREEN,
        )
        mean_label.next_to(decomposition[2], DOWN, buff=0.72)

        dev_label = Text(
            "differences from that level",
            font_size=24,
            color=YELLOW,
        )
        dev_label.next_to(decomposition[4], DOWN, buff=0.92)

        mean_arrow = Arrow(
            mean_label.get_top(),
            decomposition[2].get_bottom(),
            buff=0.08,
            color=GREEN,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.18,
        )

        dev_arrow = Arrow(
            dev_label.get_top(),
            decomposition[4].get_bottom(),
            buff=0.08,
            color=YELLOW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.18,
        )

        decomposition_note = make_note(
            "First, we will find the mean component.",
            color=GREEN,
            y=-2.25,
            size=24,
        )

        # ------------------------------------------------------------
        # Animation timeline
        # ------------------------------------------------------------
        self.play(FadeIn(title), FadeIn(subtitle, shift=UP * 0.15))
        self.wait(0.5)

        # VOICEOVER:
        # "We usually think of one numerical variable as a table,
        # a column, or simply a list of numbers."
        self.play(FadeIn(one_variable_label))
        self.play(
            Create(table_box),
            FadeIn(table_header),
            Create(divider),
            LaggedStart(*[FadeIn(row) for row in table_rows], lag_ratio=0.12),
        )
        self.wait(0.8)

        # VOICEOVER:
        # "But there is another way to see it."
        self.play(
            FadeOut(table_group),
            FadeIn(list_group),
        )
        self.wait(0.6)

        # VOICEOVER:
        # "We can treat the entire column as one vector,
        # with each observation becoming one coordinate."
        self.play(
            FadeOut(list_group),
            FadeIn(vector_group),
            FadeIn(note_single_variable, shift=UP * 0.2),
        )
        self.play(
            LaggedStart(
                *[
                    AnimationGroup(
                        GrowArrow(arrow),
                        FadeIn(label, shift=LEFT * 0.15),
                    )
                    for arrow, label in zip(coordinate_arrows, coordinate_labels)
                ],
                lag_ratio=0.18,
            )
        )
        for entry in vector_matrix.get_entries():
            pulse(entry, color=BLUE_B, scale_factor=1.18)
        self.wait(0.7)

        # VOICEOVER:
        # "A dataset with three observations becomes a vector
        # in three-dimensional space."
        self.play(
            FadeOut(one_variable_label),
            FadeOut(vector_group),
            FadeOut(coordinate_labels),
            FadeOut(coordinate_arrows),
            FadeOut(note_single_variable),
            Write(dimension_three),
        )
        pulse(dimension_three[0], color=YELLOW)
        pulse(dimension_three[2], color=BLUE_B)
        self.play(FadeIn(dimension_note, shift=UP * 0.2))
        self.wait(0.7)

        # VOICEOVER:
        # "More generally, a dataset with n observations becomes
        # a vector in n-dimensional space."
        self.play(
            TransformMatchingTex(dimension_three, dimension_n),
        )
        pulse(dimension_n[0], color=YELLOW)
        pulse(dimension_n[2], color=BLUE_B)
        self.wait(0.8)

        # VOICEOVER:
        # "This geometric point of view lets us reinterpret familiar
        # statistical concepts using vectors."
        self.play(
            FadeOut(dimension_n),
            FadeOut(dimension_note),
            FadeIn(preview_title),
        )
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=RIGHT * 0.25) for row in preview_rows],
                lag_ratio=0.22,
            )
        )

        # VOICEOVER:
        # "The mean becomes a projection. The deviations form a new vector.
        # Variance comes from the squared length of that vector.
        # And correlation becomes the cosine of the angle between
        # two deviation vectors."
        for row, color in zip(
            preview_rows,
            [GREEN, YELLOW, BLUE_B, PURPLE_B],
        ):
            pulse(row, color=color, scale_factor=1.04)

        self.play(FadeIn(preview_note, shift=UP * 0.2))
        self.wait(0.8)

        # VOICEOVER:
        # "We will build these ideas step by step.
        # Let us begin with the mean."
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(preview_title),
            FadeOut(preview_rows),
            FadeOut(preview_note),
            FadeIn(section_title),
        )
        self.wait(0.4)

        # VOICEOVER:
        # "Here is our example dataset: two, four, and six.
        # Written as a vector, it becomes V."
        self.play(FadeIn(example_group))
        self.play(GrowArrow(conversion_arrow), FadeIn(conversion_label))
        self.play(FadeIn(dataset_vector_group, shift=LEFT * 0.25))
        for entry in dataset_vector_matrix.get_entries():
            pulse(entry, color=BLUE_B, scale_factor=1.16)
        self.wait(0.7)

        # VOICEOVER:
        # "Now we want to separate this vector into two parts."
        self.play(
            FadeOut(example_group),
            FadeOut(conversion_arrow),
            FadeOut(conversion_label),
            FadeOut(dataset_vector_group),
            Write(decomposition),
        )
        pulse(decomposition[0], color=BLUE_B)
        self.wait(0.4)

        # VOICEOVER:
        # "One part will represent the common level of the data.
        # The other part will represent how each observation differs
        # from that common level."
        self.play(
            GrowArrow(mean_arrow),
            FadeIn(mean_label, shift=UP * 0.15),
        )
        pulse(decomposition[2], color=GREEN)

        self.play(
            GrowArrow(dev_arrow),
            FadeIn(dev_label, shift=UP * 0.15),
        )
        pulse(decomposition[4], color=YELLOW)

        # VOICEOVER:
        # "We will call them the mean component and the deviation component."
        self.play(FadeIn(decomposition_note, shift=UP * 0.2))
        self.wait(2.0)