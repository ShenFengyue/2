from manim import *

class ABCModel(Scene):
    def construct(self):
        # Step 1: 标题
        title = Text("认知行为模型 ABC", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Step 2: 创建 ABC 节点
        antecedent = Circle(radius=1, color=BLUE).shift(LEFT*4)
        belief = Circle(radius=1, color=GREEN)
        consequence = Circle(radius=1, color=RED).shift(RIGHT*4)

        text_A = Text("A\n前因", font_size=24).move_to(antecedent.get_center())
        text_B = Text("B\n信念", font_size=24).move_to(belief.get_center())
        text_C = Text("C\n结果", font_size=24).move_to(consequence.get_center())

        self.play(Create(antecedent), Write(text_A))
        self.play(Create(belief), Write(text_B))
        self.play(Create(consequence), Write(text_C))
        self.wait(1)

        # Step 3: 画箭头
        arrow_AB = Arrow(antecedent.get_right(), belief.get_left(), buff=0.1)
        arrow_BC = Arrow(belief.get_right(), consequence.get_left(), buff=0.1)

        label_AB = Text("触发信念", font_size=18).next_to(arrow_AB, UP)
        label_BC = Text("产生结果", font_size=18).next_to(arrow_BC, UP)

        self.play(GrowArrow(arrow_AB), Write(label_AB))
        self.play(GrowArrow(arrow_BC), Write(label_BC))
        self.wait(1)

        # Step 4: 演示动态变化
        highlight = Circle(radius=1.2, color=YELLOW)
        self.play(highlight.animate.move_to(antecedent.get_center()))
        self.wait(0.5)
        self.play(highlight.animate.move_to(belief.get_center()))
        self.wait(0.5)
        self.play(highlight.animate.move_to(consequence.get_center()))
        self.wait(1)

        # Step 5: 总结
        summary = Text("A → B → C\n前因触发信念，产生结果", font_size=28)
        self.play(summary.animate.to_edge(DOWN))
        self.wait(2)

        # Step 6: 清屏并显示署名
        all_elements = VGroup(title, antecedent, belief, consequence,
                              text_A, text_B, text_C,
                              arrow_AB, arrow_BC, label_AB, label_BC,
                              highlight, summary)
        self.play(FadeOut(all_elements))  # 清空屏幕
        made_by = Text("Made by 郦道元", font_size=36, color=WHITE)
        self.play(Write(made_by))
        self.wait(2)
        


