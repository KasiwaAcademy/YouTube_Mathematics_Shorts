from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class ChangeSubjectFormula(Scene):
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
        title = Tex(r"Changing the Subject of Formula").shift(UP).scale(1.5)
        institution = Tex(r"@Kaswia Academy")
        self.play(Write(title))
        self.wait()
        self.play(FadeIn(institution))
        self.wait()
        self.play(FadeOut(title, institution))

        # Problem Statement
        statement = Tex(r"Problem Statement:").to_edge(UP).scale(1.5)
        question = Tex(r"Make $k$ the subject of the Formula in:").shift(UP).scale(1.3)
        formula = MathTex(r"x = \frac{b - k^3}{k^3}").shift(DOWN).scale(1.75)
        self.add(statement)
        self.play(Write(question))
        self.wait()
        self.play(FadeIn(formula))
        self.wait()
        self.play(FadeOut(statement, question, formula))

        # Step 1
        text_1 = Tex(r"Multiply both sides by $k^3$:").to_edge(UP).scale(1.5)
        eq1 = MathTex(r"x = \frac{b - k^3}{k^3}").shift(2*UP).scale(1.5)
        eq2 = MathTex(r"k^3 \times x = \frac{b - k^3}{k^3} \times k^3").scale(1.5)
        eq3 = MathTex(r"k^3 \times x = b - k^3").next_to(eq2, direction = DOWN, buff = 0.5).scale(1.5)
        eq4 = MathTex(r"k^3x = b - k^3").next_to(eq3, direction = DOWN, buff = 0.5).scale(1.5)
        self.add(text_1, eq1)
        self.wait()
        self.play(Write(eq2))
        self.wait()
        self.play(TransformFromCopy(eq2, eq3))
        self.wait()
        self.play(TransformFromCopy(eq3, eq4))
        self.play(FadeOut(text_1, eq1, eq2, eq3, eq4))
        self.wait()

        # Step 2
        text_2 = Tex(r"Add $k^3$ to both sides of the equation").to_edge(UP).scale(1.5)
        eq1 = MathTex(r"k^3x = b - k^3").shift(2*UP).scale(1.5)
        eq2 = MathTex(r"k^3x + k^3 = b - k^3 + k^3").next_to(eq1, direction = DOWN, buff = 1).scale(1.5)
        eq3 = MathTex(r"k^3x + k^3 = b").next_to(eq2, direction = DOWN, buff = 1).scale(1.5)
        self.add(text_2)
        self.play(Write(eq1))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait()
        self.play(TransformFromCopy(eq2, eq3))
        self.wait()
        self.play(FadeOut(text_2, eq1, eq2, eq3))
        self.wait()

        # Step 3
        text_3 = Tex(r"Factorise the left-hand side of the equation:").to_edge(UP).scale(1.5)
        eq1 = MathTex(r"k^3x + k^3 = b").shift(2*UP).scale(1.5)
        eq2 = MathTex(r"k^3(x + 1) = b").next_to(eq1, direction = DOWN, buff = 1).scale(1.5)
        self.add(text_3)
        self.wait()
        self.play(Write(eq1))
        self.play(TransformFromCopy(eq1, eq2))
        self.wait()
        self.play(FadeOut(text_3, eq1, eq2))
        self.wait()

        # Step 4
        text_4 = Tex(r"Devide both sides by $x + 1$").to_edge(UP).scale(1.5)
        eq1 = MathTex(r"k^3(x + 1) = b").shift(2*UP).scale(1.5)
        eq2 = MathTex(r"\frac{k^3(x + 1)}{(x + 1)} = \frac{b}{(x + 1)}").next_to(eq1, direction = DOWN, buff = 1).scale(1.5)
        eq3 = MathTex(r"k^3 = \frac{b}{x + 1}").next_to(eq2, direction = DOWN, buff = 1).scale(1.5)
        self.add(text_4)
        self.wait()
        self.play(FadeIn(eq1))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait()
        self.play(TransformFromCopy(eq2, eq3))
        self.wait()
        self.play(FadeOut(text_4, eq1, eq2, eq3))
        self.wait()

        # Step 5
        text_5 = Tex(r"Take the cube-root of both sides:").to_edge(UP).scale(1.5)
        eq1 = MathTex(r"k^3 = \frac{b}{x + 1}").shift(2*UP).scale(1.5)
        eq2 = MathTex(r"\sqrt[3]{k^3} = \sqrt[3]{\frac{b}{x + 1}}").next_to(eq1, direction = DOWN, buff = 1).scale(1.5)
        eq3 = MathTex(r"k = \sqrt[3]{\frac{b}{x + 1}}").next_to(eq2, direction = DOWN, buff = 1).scale(1.5)
        self.add(text_5)
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait()
        self.play(TransformFromCopy(eq2, eq3))
        self.wait()
        self.play(FadeOut(text_5, eq1, eq2, eq3))
        self.wait()
        
        # Final Answer
        text_6 = Tex(r"The Final Answer is:").to_edge(UP).scale(1.75)
        final_answer = MathTex(r"\boxed{k = \sqrt[3]{\frac{b}{x + 1}}}").shift(DOWN).scale(1.75)
        self.add(text_6)
        self.play(Write(final_answer))
        self.wait()
        self.play(FadeOut(text_6, final_answer))
        
        # Outro
        text_7 = Tex(r"Thank You for Watching!").to_edge(DOWN).scale(1.75)
        logo_final = logo.move_to(ORIGIN).scale(3)
        self.play(Write(text_7))
        self.wait()
        self.play(Transform(logo_corner, logo_final))
        self.wait(2)
        self.play(FadeOut(text_7, logo_final))
        self.wait
