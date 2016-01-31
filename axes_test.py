import tkinter as tk

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
        x_min=0, x_max=10, x_step=2,
        y_min=0, y_max=10, y_step=1)
    axes.add_point(5, 5)
    axes.add_point(1, 1)
    axes.move_point_in_y_direction(x=5, new_y=10)
    root.mainloop()
    
if __name__ == '__main__':
    main()