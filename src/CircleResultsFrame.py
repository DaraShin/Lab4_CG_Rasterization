from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from plot import draw_rasterized_figure


class CircleResultsFrame:
    def __init__(self, circle_rasterization_func, plot_title):
        self.circle_rasterization_func = circle_rasterization_func
        self.title = plot_title

        self.root_frame = Frame()
        self.canvas = None
        self.canvas_frame = Frame(master=self.root_frame)
        self.canvas_frame.pack()

        center_x = 0
        center_y = 0
        radius = 20

        points = circle_rasterization_func(radius, center_x, center_y)
        self.draw_plot_on_canvas(points)

        points_frame = Frame(master=self.root_frame)
        points_frame.pack()

        show_btn = Button(master=self.root_frame, text="Показать", command=self.show_btn_click, font=("Arial", 12))
        show_btn.pack()

        frame = Frame(master=points_frame)
        frame.grid(row=0, column=0)
        label = Label(master=frame, text="x: ", font=("Arial", 12))
        label.pack(side=LEFT, anchor=S)
        self.center_x_slider = Scale(master=frame, from_=-100, to=100, orient=HORIZONTAL, font=("Arial", 10), length=160)
        self.center_x_slider.set(center_x)
        self.center_x_slider.pack(side=LEFT, anchor=S)

        frame = Frame(master=points_frame)
        frame.grid(row=0, column=1)
        label = Label(master=frame, text="y: ", font=("Arial", 12))
        label.pack(side=LEFT, anchor=S)
        self.center_y_slider = Scale(master=frame, from_=-100, to=100, orient=HORIZONTAL, font=("Arial", 10), length=160)
        self.center_y_slider.set(center_y)
        self.center_y_slider.pack(side=LEFT, anchor=S)

        frame = Frame(master=points_frame)
        frame.grid(row=1, column=0)
        label = Label(master=frame, text="R: ", font=("Arial", 12))
        label.pack(side=LEFT, anchor=S)
        self.radius_slider = Scale(master=frame, from_=0, to=80, orient=HORIZONTAL, font=("Arial", 10), length=160)
        self.radius_slider.set(radius)
        self.radius_slider.pack(side=LEFT, anchor=S)


    def draw_plot_on_canvas(self, points):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(draw_rasterized_figure(points, self.title), master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().configure(width=500, height=240)
        self.canvas.get_tk_widget().pack(side=TOP, fill=None, expand=0)

    def show_btn_click(self):
        radius = self.radius_slider.get()
        center_x = self.center_x_slider.get()
        center_y = self.center_y_slider.get()
        try:
            points = self.circle_rasterization_func(radius, center_x, center_y)
        except:
            print("error")
            pass
        self.draw_plot_on_canvas(points)