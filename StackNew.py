from manim import *

class Stack(Scene):
    def construct(self):
        # Title
        title = Text("Stack").scale(0.8)
        self.play(Write(title), run_time = 0.3)
        self.play(title.animate.to_edge(UP))

      
        stack_base = Line(LEFT, RIGHT).scale(2).shift(2*DOWN)

        # Menampilkan stack_base
        self.play(Create(stack_base), run_time = 0.4)

        #push 1
        push_text = Text("Push 2").scale(0.7).to_edge(DOWN)
        new_box = Square(side_length=1).next_to(stack_base, UP, buff=0)
        new_label = Text("2").move_to(new_box)

        self.play(Write(push_text), run_time = 0.5)
        self.play(FadeIn(new_box), Write(new_label))

        self.play(new_box.animate, new_label.animate)
        self.play(Unwrite(push_text), run_time = 0.8)

        #push 2
        push_text = Text("Push 3").scale(0.7).to_edge(DOWN)
        new_box = Square(side_length=1).next_to(stack_base, UP, buff=1)
        new_label = Text("3").move_to(new_box)

        self.play(Write(push_text), run_time = 0.5)
        self.play(FadeIn(new_box), Write(new_label))

        self.play(new_box.animate, new_label.animate)
        self.play(Unwrite(push_text), run_time = 0.8)

        #push 3
        push_text = Text("Push 1").scale(0.7).to_edge(DOWN)
        new_box = Square(side_length=1).next_to(stack_base, UP, buff=2)
        new_label = Text("1").move_to(new_box)

        self.play(Write(push_text), run_time = 0.5)
        self.play(FadeIn(new_box), Write(new_label))

        self.play(new_box.animate, new_label.animate)
        self.play(Unwrite(push_text), run_time = 0.8)

        #push 4

        push_text = Text("Push 5").scale(0.7).to_edge(DOWN)
        new_box = Square(side_length=1).next_to(stack_base, UP, buff=3)
        new_label = Text("5").move_to(new_box)

        self.play(Write(push_text), run_time = 0.5)
        self.play(FadeIn(new_box), Write(new_label))

        self.play(new_box.animate, new_label.animate)
        self.play(Unwrite(push_text), run_time = 0.8)

        #pop
        pop_text = Text("Pop").scale(0.7).to_edge(DOWN)
        self.play(Write(pop_text))
        self.play(new_box.animate.shift(4*RIGHT), new_label.animate.shift(4*RIGHT))
        self.play(FadeOut(new_box), FadeOut(new_label))
        self.play(Unwrite(pop_text))

        self.wait(0.5)