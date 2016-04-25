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
        options             (dict)
        pixels_per_unit     (dict): Stores the size conversion factor from units on the graph
            to Canvas pixels, for the x and y directions
        plotted_points      (list): Each element is an AxesPoint object
    
    Public methods:
        add_point(x, y, radius=3)
        hide_point(point)
        show_point(point)
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
                 x_label='x', y_label='y', x_ticks=True, y_ticks=True):
        if not canvas:
            raise ValueError()
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
            "half_tick_length": 5,
            "tick_label_offset": 10}
        self.axes_labels = {
            'x': x_label,
            'y': y_label}
        self.options = {
            'x_ticks': x_ticks,
            'y_ticks': y_ticks}
        self.pixels_per_unit = {
            'x': self.display_dimensions['width'] / (self.scale['x_max'] - self.scale['x_min']),
            'y': self.display_dimensions['height'] / (self.scale['y_max'] - self.scale['y_min'])}
        self.plotted_points = []
        
        self._draw_on_canvas()
        
    def add_point(self, x, y, radius=3):
        """Plots a point on the Axes and draws it on the Canvas

        Args:
            x (numeric): The x coordinate of the point
            y (numeric): The y coordinate of the point
            radius (numeric): The radius of the circle to be drawn on the axes
        Returns:
            A reference to the point that was added
        """
        canvas_x, canvas_y = self._get_canvas_coords(x, y)
        bounding_box = (
            canvas_x - radius,
            canvas_y - radius,
            canvas_x + radius,
            canvas_y + radius)
        reference = self.canvas.create_oval(*bounding_box, fill='red', outline='black')
        point = AxesPoint(x, y, reference, radius=radius)
        self.plotted_points.append(point)
        return point

    def hide_point(self, point):
        """Hides a point that has already been plotted on the axis

        Args:
            point: A reference to the point in the plotted_points list to be hidden
        """
        point.visible = False
        point.reference.coords(point.x, 0)
        point.reference.item_configure(state=tk.HIDDEN)

    def show_point(self, point):
        """Shows a point that has been hidden

        Args:
            point: A reference to the point to be shown
        """
        point.visible = True
        point.reference.item_configure(state=tk.NORMAL)
    
    def get_point_by_x(self, x):
        """Returns an AxesPoint object representing a point plotted on the Axes at a
        certain x value.
        
        Args:
            x (numeric): The x-coordinate of the desired point
        """
        for point in self.plotted_points:
            if point.x == x:
                return point
        raise ValueError('No point exists with that value on the graph')
        
    def get_point_by_y(self, y):
        """Returns an AxesPoint object representing a point plotted on the Axes at a
        certain y value.
        
        Args:
            y (numeric): The x-coordinate of the desired point
        """
        for point in self.plotted_points:
            if point.y == y:
                return point
        raise ValueError('No point exists with that value on the graph')
        
    def move_point(self, point, new_x, new_y):
        """Moves a point to a new position on the axes.
        
        The x and y attributes of the AxesPoint object will be updated, and
        the corresponding oval on the canvas will be moved.
        
        Args:
            point (AxesPoint): The point to be moved
            new_x (numeric): The new x coordinate
            new_y (numeric): The new y coordinate
        """
        
        point.x, point.y = new_x, new_y
        canvas_x, canvas_y = self._get_canvas_coords(new_x, new_y)
        bounding_box = (
            canvas_x - point.radius,
            canvas_y - point.radius,
            canvas_x + point.radius,
            canvas_y + point.radius)
        self.canvas.coords(point.reference, *bounding_box)
        
    def move_point_in_x_direction(self, y=0, new_x=0):
        """Moves a point to a new x coordinate.
        
        Args:
            y (numeric): The current y coordinate of the point
            new_x (numeric): The desired new x coordinate for the point
        """
        point = self.get_point_by_y(y)
        self.move_point(point, new_x, y)
    
    def move_point_in_y_direction(self, x=0, new_y=0):
        """Moves a point to a new y coordinate.
        
        Args:
            x (numeric): The current x coordinate of the point
            new_y (numeric): The desired new y coordinate for the point
        """
        point = self.get_point_by_x(x)
        self.move_point(point, x, new_y)
    
    def _get_canvas_coords(self, x, y):
        """Transforms the coordinates of the given point to reflect the coordinates on the Canvas
        at which that point must be plotted."""
        canvas_x = self.corner['x'] + math.floor(x * self.pixels_per_unit['x'])
        canvas_y = self.corner['y'] - math.floor(y * self.pixels_per_unit['y'])
        return canvas_x, canvas_y
        
    def _draw_on_canvas(self):
        """Draws the axes on the canvas"""
        self._draw_x_axis()
        self._draw_y_axis()
        if self.options['x_ticks']:
            self._draw_x_ticks()
            self._label_x_ticks()
        if self.options['y_ticks']:
            self._draw_y_ticks() 
            self._label_y_ticks()
                
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
        for x, canvas_x in self._x_tick_locations():
            self.canvas.create_line(
                canvas_x, self.corner['y'] - self.display_dimensions['half_tick_length'],
                canvas_x, self.corner['y'] + self.display_dimensions['half_tick_length'])
                
    def _draw_y_ticks(self):
        for y, canvas_y in self._y_tick_locations():
            self.canvas.create_line(
                self.corner['x'] - self.display_dimensions['half_tick_length'], canvas_y,
                self.corner['x'] + self.display_dimensions['half_tick_length'], canvas_y)

    def _label_x_ticks(self):
        for x, canvas_x in self._x_tick_locations():
            self.canvas.create_text(
                canvas_x, self.corner['y'] + self.display_dimensions['tick_label_offset'],
                text=str(x), anchor=tk.N)
        
    def _label_y_ticks(self):
        for y, canvas_y in self._y_tick_locations():
            self.canvas.create_text(
                self.corner['x'] - self.display_dimensions['tick_label_offset'], canvas_y,
                text=str(y), anchor=tk.E)
            
    def _x_tick_locations(self):
        """Generator function returning an iterator to the locations of the x ticks.
        
        Each element yielded by the iterator is a tuple (x, canvas_x), consisting of
            the abstract coordinate x along with the corresponding canvas coordinate
            canvas_x
        """
        x = self.scale['x_step']
        while x < self.scale['x_max']:
            canvas_x, canvas_y = self._get_canvas_coords(x, 0)
            yield x, canvas_x
            x += self.scale['x_step']
        
    def _y_tick_locations(self):
        """Generator function returning an iterator to the locations of the y ticks.
        
        Each element yielded by the iterator is a tuple (y, canvas_y), consisting of
            the abstract coordinate y along with the corresponding canvas coordinate
            canvas_y
        """
        y = self.scale['y_step']
        while y < self.scale['y_max']:
            canvas_x, canvas_y = self._get_canvas_coords(0, y)
            yield y, canvas_y
            y += self.scale['y_step']
            
    
class AxesPoint(object):
    """Represents one of the points plotted on an Axes object"""
    def __init__(self, x, y, reference, radius=3):
        self.x = x
        self.y = y
        self.reference = reference
        self.radius = radius
        self.visible = True
