from manim import *

class titulo(Scene):
    def construct(self):
        title = Tex(r"Solving the Schrödinger Equation for the Hydrogen atom")
        ecuacion = MathTex(r"-\frac{\hbar^2}{2m}\nabla^2\Psi + V(r)\Psi = E\Psi")
        grupo = VGroup(title,ecuacion).arrange(DOWN)
        self.play(Write(grupo,run_time=4))
        self.wait(2)
        self.play(FadeOut(grupo,run_time=2))
        
class problem(Scene):
    def construct(self):
        subtitle = Tex(r"Statement of the problem").to_corner(LEFT + UP)
        paragraph1 = Tex(r"""Consider a simple system consisting of a proton and an 
                              electron \\  bonded by an electric potencial $V(r)$
                              given by an electrostatic potential. That is to say $V(r) = -\frac{e^2}{4\pi\epsilon_0 r}$.""")
        paragraph1.font_size = 32
        self.play(Write(subtitle),Write(paragraph1,run_time = 3))
        self.play(Transform(paragraph1,paragraph1.copy().move_to(2*UP)))
        
        paragraph2 = Tex(r""" Due to the symmetry of the electrostatic potential, it is convinient to consider that the wavefunction \\
            depends on the spherical coordinates system variables: $r,\theta,\phi$. This is, the wavefunction can be written as \\ $\Psi = \Psi(r,\theta,\phi)$""")
        paragraph2.font_size = 32
        
        self.play(Write(paragraph2,run_time=4))
        
        paragraph3 = Tex(r""" So far nothing has been done. However, this analysis will lead us to find a way to calculate the wavefunction.""").move_to(2*DOWN)
        paragraph3.font_size = 32
        self.play(Write(paragraph3,run_time=2))


        
        
        