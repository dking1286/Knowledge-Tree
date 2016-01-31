import tkinter as tk
import math

class Axes(object):
    """Represents a set of axes to be drawn on a tkinter Canvas
    
    Attributes:
        canvas              (tk.Canvas): A reference to the canvas the Axes should be drawn on
        scale               (dict): Stores the min, max, and step values for each of the axes
        corner              (dict): Stores the coordinates of the top left corner of the plot_new_points
        display_dimensions  (dict): Stores the width and height in pixels of the display
            of the Axes on the Canvas
        axes_labels         (dict): Stores the strings to label on the axes
        pixels_per_unit     (numeric): Stores the size conversion factor from units on the graph
            to Canvas pixels
        plotted_points      (list): Each element is a 3-list
    
    Public methods:
        add_point(x, y, radius=3)
        get_point_by_x(x)
        get_point_by_y(y)
        move_point(point, new_x, new_y)
        move_point_in_x_direction(y=0, new_x=0)
        move_point_in_y_direction(x=0, new_y=0)
        
    Private methods:
        _get_canvas_coords(x, y)
        _draw_on_canvas()
        _draw_x_axis()
        _draw_y_axis()
        _draw_x_ticks()
        _draw_y_ticks()
        _label_x_ticks()
        _label_y_ticks()
        _x_tick_locations()
        _y_tick_locations()
    """
    def __init__(self, canvas=None, corner_x=0, corner_y=0, display_width=0, display_height=0,
                 x_min=0, x_max=1000, x_step=100, y_min=0, y_max=1000, y_step=100,
                 x_label='x', y_label='y'):
        self.canvas = canvas
        self.scale = {
            "x_min": x_min,
            "x_max": x_max,
            "x_step": x_step,
            "y_min": y_min,
            "y_max": y_max,
            "y_step": y_step}
        self.corner = {
            "x": corner_x,
            "y": corner_y}
        self.display_dimensions = {
            "width": display_width,
            "height": display_height,
            "half_tick_length": 5}
        self.axes_labels = {
            'x': x_label,
            'y': y_label}
        self.pixels_per_unit = self.display_dimensions['width'] / (self.scale['x_max'] - self.scale['x_min'])
        self.plotted_points = []
        
        self._draw_on_canvas()
        
    def add_point(self, x, y, radius=3):
        """Plots a point on the Axes and draws it on the Canvas"""
        canvas_x, canvas_y = self._get_canvas_coords(x, y)
        bounding_box = (
            canvas_x - radius,
            canvas_y - radius,
            canvas_x + radius,
            canvas_y + radius)
        reference = self.canvas.create_oval(*bounding_box, fill='red', outline='black')
        self.plotted_points.append(AxesPoint(x, y, reference, radius=radius))
    
    def get_point_by_x(self, x):
        for point in self.plotted_points:
            if point.x == x:
                return point
        raise ValueError('No point exists with that value on the graph')
        
    def get_point_by_y(self, y):
        for point in self.plotted_points:
            if point.y == y:
                return point
        raise ValueError('No point exists with that value on the graph')
        
    def move_point_in_x_direction(self, y=0, new_x=0):
        point = self.get_point_by_y(y)
        canvas_x, canvas_y = self._get_canvas_coords(new_x, y)
        bounding_box = (
            canvas_x - point.radius,
            canvas_y - point.radius,
            canvas_x + point.radius,
            canvas_y + point.radius)    
        self.canvas.coords(point.reference, *bounding_box)
    
    def move_point_in_y_direction(self, x=0, new_y=0):
        point = self.get_point_by_x(x)
        canvas_x, canvas_y = self._get_canvas_coords(x, new_y)
        bounding_box = (
            canvas_x - point.radius,
            canvas_y - point.radius,
            canvas_x + point.radius,
            canvas_y + point.radius)
        self.canvas.coords(point.reference, *bounding_box)
    
    def _get_canvas_coords(self, x, y):
        """Transforms the coordinates of the given point to reflect the coordinates on the Canvas
        at which that point must be plotted."""
        canvas_x = self.corner['x'] + math.floor(x * self.pixels_per_unit)
        canvas_y = self.corner['y'] - math.floor(y * self.pixels_per_unit)
        return canvas_x, canvas_y
        
    def _draw_on_canvas(self):
        """Draws the axes on the canvas"""
        self._draw_x_axis()
        self._draw_y_axis()
        self._draw_x_ticks()
        self._draw_y_ticks()
                
    def _draw_x_axis(self):
        self.canvas.create_line(
            self.corner['x'], self.corner['y'],
            self.corner['x'] + self.display_dimensions['width'], self.corner['y'],
            arrow=tk.LAST)
        self.canvas.create_text(
            self.corner['x'] + self.display_dimensions['width'], self.corner['y'] + 10,
            text=self.axes_labels['x'])
    
    def _draw_y_axis(self):
        self.canvas.create_line(
            self.corner['x'], self.corner['y'],
            self.corner['x'], self.corner['y'] - self.display_dimensions['height'],
            arrow=tk.LAST)
        self.canvas.create_text(
            self.corner['x'] - 10, self.corner['y'] - self.display_dimensions['height'],
            text=self.axes_labels['y'])
            
    def _draw_x_ticks(self):
        for x in self._x_tick_locations():
            self.canvas.create_line(
                x, self.corner['y'] - self.display_dimensions['half_tick_length'],
                x, self.corner['y'] + self.display_dimensions['half_tick_length'])
                
    def _draw_y_ticks(self):
        for y in self._y_tick_locations():
            self.canvas.create_line(
                self.corner['x'] - self.display_dimensions['half_tick_length'], y,
                self.corner['x'] + self.display_dimensions['half_tick_length'], y)
    def _label_x_ticks(self):
        """TODO: Implement"""
        
    def _label_y_ticks(self):
        """TODO: Implement"""

    def _x_tick_locations(self):
        val = self.corner['x'] + self.scale['x_step'] * self.pixels_per_unit
        while val < self.corner['x'] + self.display_dimensions['width']:
            yield val
            val += self.scale['x_step'] * self.pixels_per_unit
        
    def _y_tick_locations(self):
        val = self.corner['y'] - self.scale['y_step'] * self.pixels_per_unit
        while val > self.corner['y'] - self.display_dimensions['height']:
            yield val
            val -= self.scale['y_step'] * self.pixels_per_unit
            
    
class AxesPoint(object):
    """Represents one of the points plotted on an Axes object"""
    def __init__(self, x, y, reference, radius=3):
        self.x = x
        self.y = y
        self.reference = reference
        self.radius = radius
        
                