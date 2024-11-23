from manim import *

class SinglyLinkedListScene(Scene):
    def highlight_effect(self, objs, colors, run_time=0.5):
        """
        Membuat efek highlight pada garis outline dari objek.

        Args:
        - objs: List objek Mobject yang akan di-highlight.
        - colors: List warna yang akan diterapkan secara berurutan.
        - run_time: Waktu setiap transisi warna.
        """
        for color in colors:
            # Menerapkan efek highlight untuk setiap objek di dalam list
            self.play(*[obj.animate.set_stroke(color, width=4) for obj in objs], run_time=run_time)
        # Kembalikan ke warna asli
        self.play(*[obj.animate.set_stroke(WHITE, width=2) for obj in objs], run_time=run_time)

    def construct(self):
        # Title
        title = Text("Singly Linked List").scale(0.8)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Properti untuk panah
        arrow_buff = 0.2
        arrow_stroke_width = 2
        arrow_scale = 1.0

        # Node 1
        value_1 = Square(side_length=0.5).shift(5 * LEFT)
        pointer_1 = Square(side_length=0.5).next_to(value_1, RIGHT, buff=0)
        label_val = Text("5").scale(0.5).move_to(value_1)
        label_poin = Text("NEXT").scale(0.2).move_to(pointer_1)
        arrow_1 = Arrow(pointer_1.get_right(), pointer_1.get_right() + RIGHT, 
                        buff=arrow_buff, stroke_width=arrow_stroke_width).scale(arrow_scale)

        self.play(Create(value_1), Create(pointer_1), Create(arrow_1))
        self.play(Write(label_val), Write(label_poin))

        # Node 2
        value_2 = Square(side_length=0.5).next_to(pointer_1, RIGHT, buff=1.2)
        pointer_2 = Square(side_length=0.5).next_to(value_2, RIGHT, buff=0)
        label_val2 = Text("1").scale(0.5).move_to(value_2)
        label_poin2 = Text("NEXT").scale(0.2).move_to(pointer_2)
        arrow_2 = Arrow(pointer_2.get_right(), pointer_2.get_right() + RIGHT, 
                        buff=arrow_buff, stroke_width=arrow_stroke_width).scale(arrow_scale)

        self.play(Create(value_2), Create(pointer_2), Create(arrow_2))
        self.play(Write(label_val2), Write(label_poin2))

        # Node 3
        value_3 = Square(side_length=0.5).next_to(pointer_2, RIGHT, buff=1.2)
        pointer_3 = Square(side_length=0.5).next_to(value_3, RIGHT, buff=0)
        label_val3 = Text("2").scale(0.5).move_to(value_3)
        label_poin3 = Text("NEXT").scale(0.2).move_to(pointer_3)
        arrow_3 = Arrow(pointer_3.get_right(), pointer_3.get_right() + RIGHT, 
                        buff=arrow_buff, stroke_width=arrow_stroke_width).scale(arrow_scale)
        
        self.play(Create(value_3), Create(pointer_3), Create(arrow_3))
        self.play(Write(label_val3), Write(label_poin3))
        
        # Node 4
        value_4 = Square(side_length=0.5).next_to(pointer_3, RIGHT, buff=1.2)
        pointer_4 = Square(side_length=0.5).next_to(value_4, RIGHT, buff=0)
        label_val4 = Text("6").scale(0.5).move_to(value_4)
        label_poin4 = Text("NEXT").scale(0.2).move_to(pointer_4)
        arrow_4 = Arrow(pointer_4.get_right(), pointer_4.get_right() + RIGHT, 
                        buff=arrow_buff, stroke_width=arrow_stroke_width).scale(arrow_scale)

        self.play(Create(value_4), Create(pointer_4), Create(arrow_4))
        self.play(Write(label_val4), Write(label_poin4))

        # Node NULL
        value_null = Rectangle(height=0.5, width=1, fill_opacity=0, stroke_color=WHITE, stroke_width=2).next_to(pointer_4, RIGHT, buff=1.2)
        label_valnull = Text("NULL").scale(0.2).move_to(value_null)

        self.play(Create(value_null))
        self.play(Write(label_valnull))

        # Animasi efek menyala pada value dan pointer secara bersamaan
        label_fin = Text("Transversal").scale(0.8).to_edge(DOWN) 
        self.play(Write(label_fin))
        

        self.highlight_effect([value_1, pointer_1], [YELLOW, RED], run_time=0.5)
        self.highlight_effect([value_2, pointer_2], [YELLOW, RED], run_time=0.5)
        self.highlight_effect([value_3, pointer_3], [YELLOW, RED], run_time=0.5)
        self.highlight_effect([value_4, pointer_4], [YELLOW, RED], run_time=0.5)

        self.play(Unwrite(label_fin))

        # Label untuk "SWAP"
        label_swap = Text("SWAP").scale(0.8).to_edge(DOWN)
        self.play(Write(label_swap))

        # Animasi SWAP antara dua node (misalnya node 1 dan node 2)
        self.play(
            value_1.animate.move_to(value_2.get_center()), 
            pointer_1.animate.move_to(pointer_2.get_center()),
            value_2.animate.move_to(value_1.get_center()),
            pointer_2.animate.move_to(pointer_1.get_center()),
            run_time=1.5
        )

        self.wait(1)  # Memberi waktu agar animasi selesai sebelum melanjutkan

        # Hapus teks SWAP
        self.play(Unwrite(label_swap))
