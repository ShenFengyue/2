from manim import *

class LiquidityScene(Scene):
    def construct(self):
        # 字体配置（Mac请改为 "PingFang SC"，Windows 保持 "SimHei" 或 "Microsoft YaHei"）
        MY_FONT = "SimHei"
        
        # ==========================================
        # 1. 开场 & 标题
        # ==========================================
        title = Text("什么是流动性？", font_size=48, font=MY_FONT)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # ==========================================
        # 2. 定义与举例
        # ==========================================
        definition = VGroup(
            Text("流动性：", font_size=36, font=MY_FONT, weight=BOLD),
            Text("资产转换成“现金”的损耗程度", font_size=28, font=MY_FONT),
            Text("即“变现难易度”", font_size=28, font=MY_FONT),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(definition, shift=DOWN))
        
        # 左边：高流动性
        high_liquidity = VGroup(
            Text("高流动性", font_size=32, color=GREEN, font=MY_FONT),
            Text("现金", font_size=24, font=MY_FONT)
        ).arrange(DOWN, aligned_edge=LEFT)

        # 右边：低流动性
        low_liquidity = VGroup(
            Text("低流动性", font_size=32, color=RED, font=MY_FONT),
            Text("房产", font_size=24, font=MY_FONT)
        ).arrange(DOWN, aligned_edge=LEFT)

        # 左右并排
        examples = VGroup(high_liquidity, low_liquidity).arrange(RIGHT, buff=3)
        examples.next_to(definition, DOWN, buff=1)

        self.play(FadeIn(high_liquidity, shift=LEFT), FadeIn(low_liquidity, shift=RIGHT))
        self.wait(1)

        # --- 演示水和冰 (临时高亮) ---
        # 为了防止遮挡，先把上面的文字变暗或者直接覆盖，这里选择简单的生成新对象演示
        water_icon = Text("💧 水", font_size=48).move_to(high_liquidity.get_center() + DOWN*1)
        ice_icon = Text("🧊 冰", font_size=48).move_to(low_liquidity.get_center() + DOWN*1)
        
        self.play(FadeIn(water_icon), FadeIn(ice_icon))
        
        rect_water = SurroundingRectangle(water_icon, color=GREEN)
        rect_ice = SurroundingRectangle(ice_icon, color=BLUE)
        
        self.play(Create(rect_water))
        self.play(ReplacementTransform(rect_water, rect_ice))
        self.wait(0.5)

        # ===【关键点1：彻底清场】===
        # 在进入下一章前，把屏幕上所有东西（定义、例子、图标、框）全部清除
        # 这样绝对不会有遮挡
        self.play(
            FadeOut(definition),
            FadeOut(examples),
            FadeOut(water_icon),
            FadeOut(ice_icon),
            FadeOut(rect_ice)
        )

        # ==========================================
        # 3. 流动性不可能三角 (Perfect Triangle)
        # ==========================================
        # 更改标题
        triangle_title = Text("流动性“不可能三角”", font_size=42, font=MY_FONT).to_edge(UP)
        self.play(ReplacementTransform(title, triangle_title))

        # ===【关键点2：画一个完美的几何三角形】===
        # 使用 Manim 内置的 Triangle 类，它保证是等边三角形
        base_triangle = Triangle(color=WHITE).scale(2.5).shift(DOWN * 0.5)
        
        # 获取三角形的三个顶点坐标
        # Manim 的 Triangle 顶点顺序通常是：[右下, 左下, 上] 或 [上, 左下, 右下]，取决于版本
        # 我们用 get_vertices() 获取后，根据位置判断一下比较保险
        vertices = base_triangle.get_vertices()
        
        # 简单的顶点排序：按Y轴高度排序，最高的那个是顶角
        # 然后剩下的两个按X轴排序，左边是左下角，右边是右下角
        sorted_vertices = sorted(vertices.tolist(), key=lambda p: p[1], reverse=True)
        top_point = np.array(sorted_vertices[0])
        
        bottom_points = sorted(sorted_vertices[1:], key=lambda p: p[0])
        left_point = np.array(bottom_points[0])
        right_point = np.array(bottom_points[1])

        # 创建文字标签
        txt_speed = Text("速度 Speed", font_size=24, font=MY_FONT)
        txt_price = Text("价格 Price", font_size=24, font=MY_FONT)
        txt_size  = Text("体量 Size",  font_size=24, font=MY_FONT)

        # 将文字放到顶点旁边
        txt_speed.next_to(top_point, UP)
        txt_price.next_to(left_point, LEFT)
        txt_size.next_to(right_point, RIGHT)

        # 组合整个三角形组，方便后面统一操作
        triangle_group = VGroup(base_triangle, txt_speed, txt_price, txt_size)

        self.play(Create(base_triangle))
        self.play(Write(txt_speed), Write(txt_price), Write(txt_size))
        self.wait(1)

        # 动态演示冲突（高亮）
        h_rect = SurroundingRectangle(txt_speed, color=YELLOW)
        self.play(Create(h_rect))
        self.wait(0.3)
        self.play(h_rect.animate.move_to(txt_price)) # 使用 animate.move_to 更平滑
        self.wait(0.3)
        self.play(h_rect.animate.move_to(txt_size))
        self.wait(0.3)
        self.play(FadeOut(h_rect))

        # ===【关键点3：再次清场】===
        # 在显示总结前，把三角形和标题都清掉
        self.play(
            FadeOut(triangle_group),
            FadeOut(triangle_title)
        )

        # ==========================================
        # 4. 总结
        # ==========================================
        summary = VGroup(
            Text("流动性 = 自由度 + 安全感", font_size=36, color=BLUE, font=MY_FONT),
            Line(LEFT, RIGHT, color=GREY).set_width(8), # 加条分割线好看点
            Text("金融工程核心：", font_size=28, color=GREY, font=MY_FONT),
            Text("让低流动性资产 → 创造出高流动性", font_size=32, font=MY_FONT)
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN) # 居中显示

        self.play(FadeIn(summary, shift=UP))
        self.wait(2)