from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from plot import draw_rasterized_figure


class ResultsFrame:
    def __init__(self, rasterization_func, plot_title):
        self.rasterization_func = rasterization_func
        self.title = plot_title

        self.root_frame = Frame()
        self.canvas = None
        self.canvas_frame = Frame(master=self.root_frame)
        self.canvas_frame.pack()

        x1 = 0
        y1 = 20
        x2 = 20
        y2 = 0

        points = rasterization_func(x1, y1, x2, y2)
        self.draw_plot_on_canvas(points)

        points_frame = Frame(master=self.root_frame)
        points_frame.pack()

        show_btn = Button(master=self.root_frame, text="Показать", command=self.show_btn_click, font=("Arial", 12))
        show_btn.pack()

        frame = Frame(master=points_frame)
        frame.grid(row=0, column=0)
        label = Label(master=frame, text="x1: ", font=("Arial", 12))
        label.pack(side=LEFT, anchor=S)
        self.start_x_slider = Scale(master=frame, from_=-80, to=80, orient=HORIZONTAL, font=("Arial", 10), length=160)
        self.start_x_slider.set(x1)
        self.start_x_slider.pack(side=LEFT, anchor=S)

        frame = Frame(master=points_frame)
        frame.grid(row=0, column=1)
        label = Label(master=frame, text="y1: ", font=("Arial", 12))
        label.pack(side=LEFT, anchor=S)
        self.start_y_slider = Scale(master=frame, from_=-80, to=80, orient=HORIZONTAL, font=("Arial", 10), length=160)
        self.start_y_slider.set(y1)
        self.start_y_slider.pack(side=LEFT, anchor=S)

        frame = Frame(master=points_frame)
        frame.grid(row=1, column=0)
        label = Label(master=frame, text="x2: ", font=("Arial", 12))
        label.pack(side=LEFT, anchor=S)
        self.end_x_slider = Scale(master=frame, from_=-80, to=80, orient=HORIZONTAL, font=("Arial", 10), length=160)
        self.end_x_slider.set(x2)
        self.end_x_slider.pack(side=LEFT, anchor=S)

        frame = Frame(master=points_frame)
        frame.grid(row=1, column=1)
        label = Label(master=frame, text="y2: ", font=("Arial", 12))
        label.pack(side=LEFT, anchor=S)
        self.end_y_slider = Scale(master=frame, from_=-80, to=80, orient=HORIZONTAL, font=("Arial", 10), length=160)
        self.end_y_slider.set(y2)
        self.end_y_slider.pack(side=LEFT, anchor=S)

    def draw_plot_on_canvas(self, points):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(draw_rasterized_figure(points, self.title), master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().configure(width=500, height=240)
        self.canvas.get_tk_widget().pack(side=TOP, fill=None, expand=0)

    def show_btn_click(self):
        start_x = self.start_x_slider.get()
        start_y = self.start_y_slider.get()
        end_x = self.end_x_slider.get()
        end_y = self.end_y_slider.get()
        try:
            points = self.rasterization_func(start_x, start_y, end_x, end_y)
            self.draw_plot_on_canvas(points)
        except:
            print("error")
            pass