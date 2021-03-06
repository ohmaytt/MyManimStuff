from manim import *
from manim.utils.rate_functions import ease_in_out_expo, ease_in_out_quint
import numpy as np
import math

class SinAndCosFunctionPlot(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-10,
            x_max=10.3,
            num_graph_anchor_points=100,
            y_min=-1.5,
            y_max=1.5,
            graph_origin=ORIGIN,
            axes_color=GREEN,
            x_labeled_nums=range(-10, 12, 2),
            **kwargs
        )
        self.function_color = RED

    def construct(self):
        self.setup_axes(animate=False)
        func_graph = self.get_graph(np.cos, self.function_color)
        func_graph2 = self.get_graph(np.sin)
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label="\\sin(x)",
                            x_val=-10, direction=UP / 2)
        two_pi = MathTex(r"x = 2 \pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT + UP)
        self.add(func_graph, func_graph2, vert_line, graph_lab, graph_lab2, two_pi)


class GraphAreaPlot(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=5,
            y_min=0,
            y_max=6,
            x_labeled_nums=[0,2,3],
            **kwargs
        )
    def construct(self):
        self.setup_axes()
        curve1 = self.get_graph(lambda x : -x**2 + 4*x,x_min=0,x_max=4)
        curve2 = self.get_graph(lambda x : 0.8*x**2 - 3*x + 4,x_min=0,x_max=4)
        line1 = self.get_vertical_line_to_graph(2,curve1,DashedLine,color=YELLOW)
        line2 = self.get_vertical_line_to_graph(3,curve1,DashedLine,color=YELLOW)
        area1 = self.get_area(curve1,0.3,0.6,dx_scaling=10,area_color=RED)
        area2 = self.get_area(curve2,2,3,bounded=curve1)
        self.add(curve1,curve2,line1,line2,area1,area2)


class Plot1(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            y_max = 50,
            y_min = 0,
            x_max = 7,
            x_min = 0,
            y_tick_frequency = 5, 
            x_tick_frequency = 0.5, 
            axes_color = BLUE, 
            y_labeled_nums= range(0,60,10),
            x_labeled_nums= list(np.arange(2, 7.0+0.5, 0.5)),
            x_label_decimal=1,
            y_label_direction= RIGHT,
            x_label_direction= UP,
            y_label_decimal=3,
            **kwargs
        )
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2, color = GREEN, x_min = 2, x_max = 4)
        self.play(
        	Create(graph),
            run_time = 2
        )
        self.wait()

class SinTangntLine(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            x_min = 0,
            x_max = 10,
            y_min = -1.5,
            y_max = 1.5,
            graph_origin= LEFT*6,
            axes_color= GREEN,
            **kwargs
        )

    def construct(self):
        self.setup_axes()
        alpha = ValueTracker(0)
        sin_graph = self.get_graph(np.sin,color=BLUE,x_min=0,x_max=5*PI)
        tangent_line = TangentLine(sin_graph,alpha.get_value(),length=1)
        tangent_line.add_updater(lambda x : x.become(TangentLine(sin_graph,alpha.get_value(),length=3)))

        self.add(sin_graph)
        self.play(Create(tangent_line),run_time=0.5)
        self.play(
            alpha.animate.set_value(0.6),
            rate_func = smooth,
            run_time = 3,
        )
        self.wait()


class CosPlusOne(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=3*PI,
            y_min=-1,
            y_max=3,
            graph_origin=6*LEFT+DOWN,
            **kwargs
        )

    def construct(self):
        self.setup_axes()
        cos_graph = self.get_graph(lambda x : np.cos(x)+1,x_min=0,x_max=2*PI,color=GREEN)
        self.add(cos_graph)

class CosPlusOneIntersection(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            x_min=-1*PI,
            x_max=3*PI,
            y_min=-1,
            y_max=3,
            x_labeled_nums=[0,PI,2*PI],
            graph_origin=4*LEFT+2*DOWN,
            **kwargs
        )

    def construct(self):
        self.setup_axes(animate=True)
        y_value = ValueTracker(1)
        #y_graph = self.get_graph(lambda x : y_value.get_value())
        y_graph = Line(self.coords_to_point(-1*PI,y_value.get_value()),self.coords_to_point(3*PI,y_value.get_value()))
        x_value = lambda x : np.arccos(y_value.get_value()-1)
        cos_graph = self.get_graph(lambda x : np.cos(x) + 1,x_min=-0.3*PI,x_max=2.3*PI)
        dot1 = Dot(self.coords_to_point(x_value(y_value.get_value()),y_value.get_value()),color=YELLOW)
        dot2 = Dot(self.coords_to_point(2*PI-x_value(y_value.get_value()),y_value.get_value()),color=YELLOW)

        y_graph.add_updater(lambda x : x.become(
            Line(self.coords_to_point(-1*PI,y_value.get_value()),self.coords_to_point(3*PI,y_value.get_value()))
        ))
        dot1.add_updater(lambda x : x.become(
            Dot(self.coords_to_point(x_value(y_value.get_value()),y_value.get_value()),color=YELLOW)
        ))
        dot2.add_updater(lambda x : x.become(
            Dot(self.coords_to_point(2*PI-x_value(y_value.get_value()),y_value.get_value()),color=YELLOW)
        ))

        #self.add(cos_graph,dot1,dot2,y_graph)
        self.play(Write(cos_graph))
        self.play(Create(y_graph),Create(dot1),Create(dot2))
        self.play(y_value.animate.set_value(2),rate_func=rate_functions.ease_in_out_quint,run_time=3)
        self.play(y_value.animate.set_value(0),rate_func=rate_functions.ease_in_out_quint,run_time=3)
        self.play(y_value.animate.set_value(1),rate_func=rate_functions.ease_in_out_quint,run_time=3)
        self.wait()

class SinArea(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            x_min=-1*PI,
            x_max=5*PI,
            y_min=-1,
            y_max=3,
            graph_origin=4*LEFT+2*DOWN,
            **kwargs
        )
    def construct(self):
        #Basic Setup
        self.setup_axes(animate=True)
        x_end = ValueTracker(2*PI)
        sin = self.get_graph(lambda x : np.sin(x)+1,x_min=0)
        line1 = self.get_vertical_line_to_graph(1/4*PI,sin,DashedLine,color=YELLOW)
        line2 = self.get_vertical_line_to_graph(x_end.get_value(),sin,DashedLine,color=YELLOW)
        area1 = self.get_area(sin,1/4*PI,2*PI,dx_scaling=0.5,area_color=BLUE)

        #Updaters
        line2.add_updater(lambda x : x.become(
            self.get_vertical_line_to_graph(x_end.get_value(),sin,DashedLine,color=YELLOW)
        ))
        area1.add_updater(lambda x : x.become(
            self.get_area(sin,1/4*PI,x_end.get_value(),dx_scaling=0.5,area_color=BLUE)
        ))

        #Animations
        self.play(Create(sin))
        self.play(Create(line1),Create(line2))
        self.play(Write(area1))
        self.play(x_end.animate.increment_value(PI),run_time=3)

class TaylorSeries(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            x_min = -4*PI,
            x_max=4*PI,
            y_min=-3,
            y_max=3,
            graph_origin=ORIGIN,
            **kwargs
        )

    def construct(self):
        #Basic Setup
        self.setup_axes(animate=True)
        x_t = ValueTracker(0)
        x_equals = MathTex("x = ").shift(3*DOWN+2*RIGHT)
        x_num = DecimalNumber(x_t.get_value(),num_decimal_places=2).next_to(x_equals,RIGHT)
        n = ValueTracker(1)
        n_equals = MathTex("n = ").next_to(x_equals,DOWN)
        n_num = Integer(n.get_value()).next_to(n_equals,RIGHT)
        cos_func = np.cos
        cos_graph = self.get_graph(cos_func,x_min=-4*PI,x_max=4*PI)
        dot = Dot(self.coords_to_point(x_t.get_value(),np.cos(x_t.get_value())),radius=0.5)
        def taylor_at_x(k,a,x):
            value = 0
            for i in range(k+1):
                #value += ((x**(2*i)*(-1)**i)/math.factorial(2*i))
                value += ((x-a)**i*np.cos(a+i*PI/2))/math.factorial(i)
            return value
        taylor1 = self.get_graph(lambda x : taylor_at_x(1,x_t.get_value(),x),color=YELLOW)
        taylor2 = self.get_graph(lambda x : taylor_at_x(2,x_t.get_value(),x),color=YELLOW)
        taylor3 = self.get_graph(lambda x : taylor_at_x(3,x_t.get_value(),x),color=YELLOW)
        taylor4 = self.get_graph(lambda x : taylor_at_x(4,x_t.get_value(),x),color=YELLOW)
        taylor5 = self.get_graph(lambda x : taylor_at_x(5,x_t.get_value(),x),color=YELLOW)
        taylor6 = self.get_graph(lambda x : taylor_at_x(6,x_t.get_value(),x),color=YELLOW)

        #Updaters
        taylor1.add_updater(
            lambda x : x.become(
                self.get_graph(lambda x : taylor_at_x(int(n.get_value()),x_t.get_value(),x),color=YELLOW)
            )
        )
        dot.add_updater(
            lambda x : x.become(
                Dot(self.coords_to_point(x_t.get_value(),np.cos(x_t.get_value())))
            ) 
        )
        x_num.add_updater(
            lambda x : x.become(
                DecimalNumber(x_t.get_value(),num_decimal_places=2).next_to(x_equals,RIGHT)
            )
        )
        n_num.add_updater(
            lambda x : x.become(
                Integer(n.get_value()).next_to(n_equals,RIGHT)
            )
        )

        #Animating
        self.play(Create(cos_graph))
        self.play(Write(taylor1),Create(dot),Write(x_equals),Write(x_num),Write(n_num),Write(n_equals))
        self.wait()
        self.play(Transform(taylor1,taylor2),n.animate.increment_value(1))
        self.wait()
        self.play(Transform(taylor1,taylor3),n.animate.increment_value(1))
        self.wait()
        self.play(Transform(taylor1,taylor4),n.animate.increment_value(1))
        self.wait()
        self.play(Transform(taylor1,taylor5),n.animate.increment_value(1))
        self.wait()
        self.play(Transform(taylor1,taylor6),n.animate.increment_value(1))
        self.wait()
        
        self.play(x_t.animate.set_value(5.5),run_time=10,rate_func=rate_functions.ease_in_out_quint)
        self.play(x_t.animate.set_value(-3.5),run_time=10,rate_func=rate_functions.ease_in_out_quint)
        self.play(x_t.animate.set_value(3.14),run_time=10,rate_func=rate_functions.ease_in_out_quint)
        self.wait()

class SingleQuadAxis(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=5,
            y_min=0,
            y_max=20,
            **kwargs
        )
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2)
        self.add(graph)

class ZeroSixZero(Scene):
    def construct(self):
        axes = Axes(x_range=[-3*PI,3*PI],y_range=[-1.5,1.5])
        self.add(axes)

class GetDerivGraph(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            x_min=-1,
            x_max=3,
            y_min=0,
            y_max=3,
            **kwargs
        )

    def construct(self):
        self.setup_axes()
        graf = self.get_graph(lambda x : x**2)
        deriv = self.get_derivative_graph(graf,dx=0.1)
        self.play(Create(graf),Write(deriv))
