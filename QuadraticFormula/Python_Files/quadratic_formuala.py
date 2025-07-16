from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class Quadratic(Scene):
    def construct(self):
        self.camera.background_color = "#003300"
        
        # Title
        title = Tex("Deriving the Quadratic Formula").scale(1.75)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Step 1
        step1 = MathTex("ax^2 + bx + c = 0")
        step1.scale(1.75)
        explanation1 = Tex("Start with the general quadratic equation").scale(1.5)
        explanation1.to_edge(UP)
        self.play(Write(step1))
        self.play(FadeIn(explanation1))
        self.wait(3)
        self.play(FadeOut(explanation1))

        # Step 2
        step2 = MathTex("x^2 + \\frac{b}{a}x + \\frac{c}{a} = 0")
        step2.scale(1.75)
        explanation2 = Tex("Divide the entire equation by $a$ to simplify").scale(1.5)
        explanation2.to_edge(UP)
        self.play(Transform(step1, step2))
        self.play(FadeIn(explanation2))
        self.wait(3)
        self.play(FadeOut(explanation2))

        # Step 3
        step3 = MathTex("x^2 + \\frac{b}{a}x = -\\frac{c}{a}")
        step3.scale(1.75)
        explanation3 = Tex("Move the constant term to the right side").scale(1.5)
        explanation3.to_edge(UP)
        self.play(Transform(step1, step3))
        self.play(FadeIn(explanation3))
        self.wait(3)
        self.play(FadeOut(explanation3))

        # Step 4
        step4 = MathTex(
            "x^2 + \\frac{b}{a}x + \\left(\\frac{b}{2a}\\right)^2 = "
            "-\\frac{c}{a} + \\left(\\frac{b}{2a}\\right)^2"
        )
        step4.scale(1.75)
        explanation4 = Tex("Complete the square on the left side").scale(1.5)
        explanation4.to_edge(UP)
        self.play(Transform(step1, step4))
        self.play(FadeIn(explanation4))
        self.wait(3)
        self.play(FadeOut(explanation4))

        # Step 5
        step5 = MathTex(
            "\\left(x + \\frac{b}{2a}\\right)^2 = "
            "-\\frac{c}{a} + \\frac{b^2}{4a^2}"
        )
        step5.scale(1.75)
        explanation5 = Tex("Factor the perfect square on the left").scale(1.5)
        explanation5.to_edge(UP)
        self.play(Transform(step1, step5))
        self.play(FadeIn(explanation5))
        self.wait(3)
        self.play(FadeOut(explanation5))

        # Step 6
        step6 = MathTex(
            "\\left(x + \\frac{b}{2a}\\right)^2 = "
            "\\frac{b^2 - 4ac}{4a^2}"
        )
        step6.scale(1.75)
        explanation6 = Tex("Simplify the right-hand side").scale(1.5)
        explanation6.to_edge(UP)
        self.play(Transform(step1, step6))
        self.play(FadeIn(explanation6))
        self.wait(3)
        self.play(FadeOut(explanation6))

        # Step 7
        step7 = MathTex(
            "x + \\frac{b}{2a} = \\pm \\frac{\\sqrt{b^2 - 4ac}}{2a}"
        )
        step7.scale(1.75)
        explanation7 = Tex("Take square root on both sides").scale(1.5)
        explanation7.to_edge(UP)
        self.play(Transform(step1, step7))
        self.play(FadeIn(explanation7))
        self.wait(3)
        self.play(FadeOut(explanation7))

        # Step 8 (Final)
        step8 = MathTex(
            "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"
        )
        step8.scale(1.75)
        explanation8 = Tex("Solve for $x$ — this is the quadratic formula!").scale(1.5)
        explanation8.to_edge(UP)
        self.play(Transform(step1, step8))
        self.play(FadeIn(explanation8))
        self.wait(3)

        # Outro
        self.play(FadeOut(step1), FadeOut(explanation8))
        final_text = Tex("Thank you for watching!").scale(1.75)
        self.play(Write(final_text))
        self.wait(2)