import tkinter as tk

from task import Task
import constants

class Controller(object):
    """Manages the user interface components, including buttons and sliders.
    
    Attributes:
        main (Main): A reference to the Main instance that contains the Controller instance
        calculate_button (tk.Button)
        load_button (tk.Button)
        initial_balance_slider (tk.Scale)
        interest_rate_slider (tk.Scale): A slider that controls the interest rate of
            the data to be displayed.
            
    Public methods:
        on_calculate_button_click
        on_load_button_click
        on_initial_balance_slider_change
        on_interest_rate_slider_change (event handler for interest rate slider)
        
    """
    def __init__(self, main=None):
        if not main:
            raise ValueError()
            
        self.main = main
        self.calculate_button = self.make_button(
            100, 100,
            command=self.on_calculate_button_click,
            text="Calculate data!")
            
        self.load_button = self.make_button(
            200, 100,
            command=self.on_load_button_click,
            text="Load data!")
            
        self.initial_balance_slider = self.make_scale(
            200, 700,
            scale_min=constants.MINIMUM_INITIAL_BALANCE,
            scale_max=constants.MAXIMUM_INITIAL_BALANCE,
            resolution=constants.INITIAL_BALANCE_STEP,
            command=self.on_initial_balance_slider_change,
            label="Initial balance")
        self.initial_balance_slider.set(constants.DEFAULT_INITIAL_BALANCE)
        
        self.interest_rate_slider = self.make_scale(
            600, 700,
            scale_min=constants.MINIMUM_INTEREST_RATE,
            scale_max=constants.MAXIMUM_INTEREST_RATE,
            resolution=constants.INTEREST_RATE_STEP,
            command=self.on_interest_rate_slider_change,
            label="Interest rate")
        self.interest_rate_slider.set(constants.DEFAULT_INTEREST_RATE)
        

    def on_calculate_button_click(self):
        """Event handler for calculate button"""
        self.main.task_manager.add_task(Task(
            function=self.main.model.calculate_payoff_times))
    
    def on_load_button_click(self):
        """Event handler for load button"""
        self.main.task_manager.add_task(Task(
            function=self.main.model.load_payoff_times))
            
    def on_initial_balance_slider_change(new_Bo):
        """Event handler for initial balance slider"""
        r = self.main.model.interest_rate
        self.main.view.graph_manager.update_points_for_new_values(new_Bo, r)
    
    def on_interest_rate_slider_change(new_r):
        """Event handler for interest rate slider"""
        Bo = self.main.model.initial_balance_slider
        self.main.view.graph_manager.update_points_for_new_values(Bo, new_r)
        
    def make_button(self, x, y, command=None, text=None):
        """Creates and places a button on the canvas
        args:
            x (int)
            y (int)
            command (function)
            text (str)
        returns: a reference to the button that was created
        """
        if command == None:
            raise TypeError('A button must have an associated function')
        
        ref = tk.Button(self.main.root, command=command, text=text)
        self.main.view.canvas.create_window(x, y, window=ref)
        return ref
        
    def make_scale(
        self, x, y, command=None, scale_min=0, scale_max=10,
        label='scale', resolution=1):
        if not command:
            raise TypeError('A scale must have an associated function')
            
        scale = tk.Scale(
            self.main.root,
            command=command,
            orient=tk.HORIZONTAL,
            from_=scale_min
            to=scale_max,
            label=label,
            resolution=resolution)
        self.main.view.canvas.create_window(x, y, window=scale)
        return scale