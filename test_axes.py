import tkinter as tk
from functools import partial

from axes import Axes

def main():
    root = tk.Tk()
    canvas = tk.Canvas(
        root,
        height=800,
        width=800,
        background='#FFFFFF')
    canvas.grid()
    axes = Axes(
        canvas=canvas,
        corner_x=200, corner_y=600,
        display_width=400, display_height=400,
        x_min=0, x_max=4000, x_step=500,
        y_min=0, y_max=10, y_step=1,
        y_ticks=True)
    axes.add_point(1000, 1)
    create_up_button(root, canvas, axes)
    create_down_button(root, canvas, axes)
    #axes.move_point_in_y_direction(x=5, new_y=10)
    root.mainloop()
    
def create_up_button(root, canvas, axes):
    button = tk.Button(root, command=partial(on_up_button_click, axes), text='up')
    canvas.create_window(100,  700, window=button)
    return button

def on_up_button_click(axes):   
    for point in axes.plotted_points:
        axes.move_point(point, point.x, 2 * point.y)
    
def create_down_button(root, canvas, axes):
    button = tk.Button(root, command=partial(on_down_button_click, axes), text='down')
    canvas.create_window(700,  700, window=button)
    return button

def on_down_button_click(axes):
    for point in axes.plotted_points:
        axes.move_point(point, point.x, 0.5 * point.y)
        
if __name__ == '__main__':
    main()