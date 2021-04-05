from manimlib.scene.graph_scene import *
import random
from manimlib.animation.animation import *
from manimlib.animation.composition import *
from manimlib.animation.creation import *
from manimlib.animation.fading import *
from manimlib.animation.growing import *
from manimlib.animation.indication import *
from manimlib.animation.movement import *
from manimlib.animation.numbers import *
from manimlib.animation.rotation import *
from manimlib.animation.specialized import *
from manimlib.animation.transform import *
from manimlib.animation.update import *
from manimlib.mobject.coordinate_systems import *
from manimlib.mobject.changing import *
from manimlib.mobject.frame import *
from manimlib.mobject.functions import *
from manimlib.mobject.geometry import *
from manimlib.mobject.matrix import *
from manimlib.mobject.mobject import *
from manimlib.mobject.number_line import *
from manimlib.mobject.numbers import *
from manimlib.mobject.probability import *
from manimlib.mobject.shape_matchers import *
from manimlib.mobject.svg.brace import *
from manimlib.mobject.svg.drawings import *
from manimlib.mobject.svg.svg_mobject import *
from manimlib.mobject.svg.tex_mobject import *
from manimlib.mobject.svg.text_mobject import *
from manimlib.mobject.svg.code_mobject import *
from manimlib.mobject.three_d_utils import *
from manimlib.mobject.three_dimensions import *
from manimlib.mobject.types.image_mobject import *
from manimlib.mobject.types.point_cloud_mobject import *
from manimlib.mobject.types.vectorized_mobject import *
from manimlib.mobject.mobject_update_utils import *
from manimlib.mobject.value_tracker import *
from manimlib.mobject.vector_field import *
TIME_INTERVAL = 1/6.0
media_dir="/Volumes/Xun/social/建党100周年纪念/assets/raster_images"

def Graphic(text):
        tex = Text(text)
        tex.set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE)
        tex.move_to(DOWN*3.5)
        #self.play(Write(tex),rate_func=smooth,run_time=t)
        #self.remove(tex)
        return tex

class Graphic_Image(GraphScene):
    def gi(self,text,image):
        tex = Graphic(text)
        time_interval = TIME_INTERVAL
        time = len(text)*TIME_INTERVAL
        fig = ImageMobject(image,media_dir,height = 6,width = 8)
        self.play(FadeIn(fig),Write(tex),run_time = time)
        self.clear()
    def gi_(self,image,*text):
        tex = [0 for i in range(len(text))] 
        time = 0
        for i in range(len(text)):
            tex[i] = Graphic(text[i])
            time += len(text[i])*TIME_INTERVAL
        fig = ImageMobject(image,media_dir,height = 6,width = 8)
        self.add(fig)
        for i in range(len(text)):
            self.play(Write(tex[i]), run_time = len(text[i])*TIME_INTERVAL)
            self.remove(tex[i])
        self.clear()
        
            

    def big_text(self,text):
        tex = Text(text,font = "SCFwxz",height = 1, color = RED)
        self.play(Write(tex),run_time = len(text)*TIME_INTERVAL)
        self.remove(tex)
    def two_fig(self,image1,image2,*text):
        tex = [0 for i in range(len(text))]
        time = 0
        for i in range(len(text)):
            tex[i] = Graphic(text[i])
            time += len(text[i])*TIME_INTERVAL
        fig1 = ImageMobject(image1,media_dir,height = 4,width = 3)
        Cross(fig1)
        fig1.shift(3.5*LEFT)
        self.add(fig1)
        fig2 = ImageMobject(image2,media_dir,height = 4,width = 3)
        fig2.shift(3.5*RIGHT)
        self.add(fig2)
        for i in range(len(text)):
            self.play(Write(tex[i]), run_time = len(text[i])*TIME_INTERVAL)
            self.remove(tex[i])
        self.clear()

    def right_connect(self,text1,text2):
        start = text1.get_right()
        end = text2.get_left()
        connect = Arrow(start,end,color=BLUE)
        return connect

    def left_connect(self,text1,text2):
        start = text1.get_left()
        end = text2.get_right()
        connect = Arrow(start,end,color=YELLOW)
        return connect

    def up_connect(self,text1,text2):
        start = text1.get_top()
        end = text2.get_bottom()
        connect = Arrow(start,end,color=GREEN)
        return connect

    def down_connect(self,text1,text2):
        start = text1.get_bottom()
        end = text2.get_top()
        connect = Arrow(start,end,color=PURPLE)
        return connect

    def mind_start(self,position,*text):
        tex = [0 for i in range(len(text))]
        tex[0] = Text(text[0],color=RED)
        tex[0].shift(position)
        for i in range(len(text)-1):
            tex[i+1] = Graphic(text[i+1])
            if i==0:
                self.play(Write(tex[0]),Write(tex[1]),run_time = len(text[1])*TIME_INTERVAL)
            else:
                self.play(Write(tex[i+1]),run_time = len(text[i+1])*TIME_INTERVAL)
            self.remove(tex[i+1])
        return tex[0]
    def mind_node(self,position,text0,*text):
        color_ = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
        tex = [0 for i in range(len(text))]
        tex[0] = Text(text[0],color=color_[random.randint(0,5)])
        tex[0].move_to(text0.get_center()+np.array([(text0.get_width()+tex[0].get_width())/2+1,position,0]),aligned_edge=ORIGIN)
        connect = self.right_connect(text0,tex[0])
        self.add(connect,tex[0])
        for i in range(len(text)-1):
            tex[i+1] = Graphic(text[i+1])
            if i==0:
                self.play(ShowCreation(connect),Write(tex[0]),Write(tex[1]),run_time = len(text[1])*TIME_INTERVAL)
            else:
                self.play(Write(tex[i+1]),run_time = len(text[i+1])*TIME_INTERVAL)
            self.remove(tex[i+1])
        return [connect, tex[0]]

    def flow_chart_start(self,position,*text):
        tex = [0 for i in range(len(text))]
        tex[0] = Text(text[0],color=RED)
        tex[0].shift(position)
        frame = SurroundingRectangle(tex[0])
        for i in range(len(text)-1):
            tex[i+1] = Graphic(text[i+1])
            if i==0:
                self.play(ShowCreation(frame),Write(tex[0]),Write(tex[1]),run_time = len(text[1])*TIME_INTERVAL)
            else:
                self.play(Write(tex[i+1]),run_time = len(text[i+1])*TIME_INTERVAL)
            self.remove(tex[i+1])
        return [tex[0], frame]
    def flow_chart_left(self,position,text0,*text):
        color_ = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
        tex = [0 for i in range(len(text))]
        tex[0] = Text(text[0],color=color_[random.randint(0,5)])
        tex[0].move_to(text0.get_center()-np.array([(text0.get_width()+tex[0].get_width())/2+1,-1*position,0]),aligned_edge=ORIGIN)
        frame = SurroundingRectangle(tex[0])
        connect = self.left_connect(text0,tex[0])
        for i in range(len(text)-1):
            tex[i+1] = Graphic(text[i+1])
            if i==0:
                self.play(ShowCreation(frame),ShowCreation(connect),Write(tex[0]),Write(tex[1]),run_time = len(text[1])*TIME_INTERVAL)
            else:
                self.play(Write(tex[i+1]),run_time = len(text[i+1])*TIME_INTERVAL)
            self.remove(tex[i+1])
        return [connect, tex[0],frame]

    def flow_chart_right(self,position,text0,*text):
        color_ = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
        tex = [0 for i in range(len(text))]
        tex[0] = Text(text[0],color=color_[random.randint(0,5)])
        tex[0].move_to(text0.get_center()+np.array([(text0.get_width()+tex[0].get_width())/2+2,position,0]),aligned_edge=ORIGIN)
        frame = SurroundingRectangle(tex[0])
        connect = self.right_connect(text0,tex[0])
        for i in range(len(text)-1):
            tex[i+1] = Graphic(text[i+1])
            if i==0:
                self.play(ShowCreation(frame),ShowCreation(connect),Write(tex[0]),Write(tex[1]),run_time = len(text[1])*TIME_INTERVAL)
            else:
                self.play(Write(tex[i+1]),run_time = len(text[i+1])*TIME_INTERVAL)
            self.remove(tex[i+1])
        return [connect, tex[0], frame]

    def flow_chart_down(self,position,text0,*text):
        color_ = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
        tex = [0 for i in range(len(text))]
        tex[0] = Text(text[0],color=color_[random.randint(0,5)])
        tex[0].move_to(text0.get_center()+np.array([position,
            -1*((tex[0].get_height()+text0.get_height())/2+1),0]),aligned_edge=ORIGIN)
        frame = SurroundingRectangle(tex[0])
        connect = self.down_connect(text0,tex[0])
        for i in range(len(text)-1):
            tex[i+1] = Graphic(text[i+1])
            if i==0:
                self.play(ShowCreation(frame),ShowCreation(connect),Write(tex[0]),Write(tex[1]),run_time = len(text[1])*TIME_INTERVAL)
            else:
                self.play(Write(tex[i+1]),run_time = len(text[i+1])*TIME_INTERVAL)
            self.remove(tex[i+1])
        return [connect, tex[0], frame]


    def flow_chart_up(self,position,text0,*text):
        color_ = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
        tex = [0 for i in range(len(text))]
        tex[0] = Text(text[0],color=color_[random.randint(0,5)])
        tex[0].move_to(text0.get_center()+np.array([position,
            (tex[0].get_height()+text0.get_height())/2+1,0]),aligned_edge=ORIGIN)
        frame = SurroundRectangle(tex[0])
        connect = self.up_connect(text0,tex[0])
        for i in range(len(text)-1):
            tex[i+1] = Graphic(text[i+1])
            if i==0:
                self.play(ShowCreation(frame),ShowCreation(connect),Write(tex[0]),Write(tex[1]),run_time = len(text[1])*TIME_INTERVAL)
            else:
                self.play(Write(tex[i+1]),run_time = len(text[i+1])*TIME_INTERVAL)
            self.remove(tex[i+1])
        return [connect, tex[0], frame]

    def group_(self,index_start,index_end,tex):
        group = VGroup(tex[index_start][0],tex[index_start][1])
        for i in range(index_end-index_start):
            group.add(tex[index_start+i+1][0])
            group.add(tex[index_start+i+1][1])
            group.add(tex[index_start+i+1][2])
        return group



    def construct(self):
        pass


