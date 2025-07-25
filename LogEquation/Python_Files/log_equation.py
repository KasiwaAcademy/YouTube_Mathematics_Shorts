#%%manim -pqm -v WARNING SolveLogEquation
from manim import *
import math

config.pixel_width = 720
config.pixel_height = 1280
config.frame_rate = 30

class SolveLogEquation(Scene):
    def construct(self):
        # Add background image
        background = ImageMobject("../Image/chalk_board.jpg")
        background.set_z_index(-1)
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)

         # Load and position logo image
        logo = ImageMobject("../Image/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR)
        self.add(logo_corner)

        # Intro
        note = Tex(r"Solving Logarithmic Equations").scale(1.75).shift(UP)
        institution = Tex(r"@Kasiwa Academy")
        self.play(Write(note))
        self.wait()
        self.play(FadeIn(institution))
        self.wait(2)
        self.play(FadeOut(note, institution))
        self.wait()
        
        # Title
        text = Tex(r"Problem Statement:").scale(1.75).to_edge(UP)
        statement = Tex(r"Solve the equation $2\log y = \log(3y + 4)$").scale(1.5)
        self.add(text)
        self.wait()
        self.play(Write(statement))
        self.wait(3)
        self.play(FadeOut(text, statement))

        # Step 1: Original equation
        eq1 = MathTex(r"2\log y = \log(3y + 4)").shift(DOWN)
        eq1.scale(1.75)
        note1 = Tex("Start with the given equation:").to_edge(UP).scale(1.5)
        self.play(Write(eq1), FadeIn(note1))
        self.wait(3)

        # Step 2: Apply power rule
        eq2 = MathTex(r"\log(y^2) = \log(3y + 4)").shift(DOWN)
        eq2.scale(1.75)
        note2 = Tex(r"Use: $a\log b = \log(b^a)$").to_edge(UP).scale(1.5)
        self.play(Transform(eq1, eq2), Transform(note1, note2))
        self.wait(3)

        # Step 3: Remove logs
        eq3 = MathTex("y^2 = 3y + 4").shift(DOWN)
        eq3.scale(1.75)
        note3 = Tex("Equal logs → equal arguments").to_edge(UP).scale(1.5)
        self.play(Transform(eq1, eq3), Transform(note1, note3))
        self.wait(3)

        # Step 4: Rearranged quadratic form
        eq4 = MathTex("y^2 - 3y - 4 = 0").shift(DOWN)
        eq4.scale(1.75)
        note4 = Tex("Move all terms to one side:").to_edge(UP).scale(1.5)
        self.play(Transform(eq1, eq4), Transform(note1, note4))
        self.wait(3)

        # Step 5: Quadratic formula
        formula = MathTex(r"y = \frac{-(-3) \pm \sqrt{(-3)^2 - 4(1)(-4)}}{2(1)}").scale(1.75).shift(DOWN)
        note5 = Tex("Use quadratic formula: $a=1$, $b=-3$, $c=-4$").to_edge(UP).scale(1.3)
        self.play(Transform(eq1, formula), Transform(note1, note5))
        self.wait(3)

        # Step 6: Simplify step by step
        step1 = MathTex(r"y = \frac{3 \pm \sqrt{9 + 16}}{2}").scale(1.75).shift(DOWN)
        self.play(Transform(eq1, step1))
        self.wait(3)

        step2 = MathTex(r"y = \frac{3 \pm \sqrt{25}}{2}").scale(1.75).shift(DOWN)
        self.play(Transform(eq1, step2))
        self.wait(3)

        step3 = MathTex(r"y = \frac{3 \pm 5}{2}").scale(1.75).shift(DOWN)
        self.play(Transform(eq1, step3))
        self.wait(3)

        # Step 7: Show both possible answers
        answers = MathTex(r"y = 4 \quad \text{or} \quad y = -1").scale(1.75).shift(DOWN)
        note7 = Tex("Solve for both possibilities:").to_edge(UP).scale(1.5)
        self.play(Transform(eq1, answers), Transform(note1, note7))
        self.wait(3)

        # Step 8: Check for valid log values
        final = MathTex(r"\log y\text{ is undefined for } y \leq 0").to_edge(DOWN).scale(1.5)
        self.play(Write(final))
        self.wait(3)

        # Final boxed answer
        solution = MathTex(r"\boxed{y = 4}").scale(4)
        solution_text = Tex("Therefore:").to_edge(UP).scale(1.5)        
        self.play(FadeOut(eq1, note1, final), FadeIn(solution), Write(solution_text))
        self.wait(3)
        self.play(FadeOut(solution, solution_text))
        self.wait()

        # Outro
        final_text = Tex("Thank you for watching!").to_edge(DOWN).scale(1.75)
        logo_final = logo.move_to(ORIGIN).scale(3)
        self.play(Write(final_text))
        self.wait()
        self.play(Transform(logo_corner, logo_final))
        self.wait(2)
        self.play(FadeOut(final_text, logo_final))
        self.wait()