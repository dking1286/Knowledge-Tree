import tkinter as tk

import knowledge_tree.constants as constants


class Controller(object):
    """Manages the user interface components, including buttons and sliders.
    
    Attributes:
        main (Main): A reference to the Main instance that contains the Controller instance
        calculate_button (tk.Button)
        load_button (tk.Button)
        delete_button (tk.Button)
        initial_balance_slider (tk.Scale)
        interest_rate_slider (tk.Scale): A slider that controls the interest rate of
            the data to be displayed.
            
    Public methods:
        on_calculate_button_click()
        on_load_button_click()
        on_delete_button_click()
        on_initial_balance_slider_change(new_Bo)
        on_interest_rate_slider_change(new_r)
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
            
        self.delete_button = self.make_button(
            300, 100,
            command=self.on_delete_button_click,
            text="DANGER!")
            
        self.initial_balance_slider = self.make_scale(
            200, 700,
            scale_min=constants.initial_balance['min'],
            scale_max=constants.initial_balance['max'],
            resolution=constants.initial_balance['step'],
            command=self.on_initial_balance_slider_change,
            label="Initial balance")
        self.initial_balance_slider.set(constants.initial_balance['default'])
        
        self.interest_rate_slider = self.make_scale(
            600, 700,
            scale_min=constants.interest_rate['min'],
            scale_max=constants.interest_rate['max'],
            resolution=constants.interest_rate['step'],
            command=self.on_interest_rate_slider_change,
            label="Interest rate")
        self.interest_rate_slider.set(constants.interest_rate['default'])

    def on_calculate_button_click(self):
        """Event handler for calculate button"""
        self.main.model.calculate_payoff_times()
    
    def on_load_button_click(self):
        """Event handler for load button"""
        self.main.model.load_payoff_times()
    
    def on_delete_button_click(self):
        """Event handler for delete button"""
        self.main.model.delete_payoff_times_from_database()
            
    def on_initial_balance_slider_change(self, new_Bo_string):
        """Event handler for initial balance slider"""
        new_Bo = self.initial_balance_slider.get()
        self.main.model.initial_balance = new_Bo
        r = self.main.model.interest_rate
        self.main.view.graph_manager.update_points_for_new_values(new_Bo, r)
    
    def on_interest_rate_slider_change(self, new_r_string):
        """Event handler for interest rate slider"""
        new_r = self.interest_rate_slider.get()
        Bo = self.main.model.initial_balance
        self.main.model.interest_rate = new_r
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
        if command is None:
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
            from_=scale_min,
            to=scale_max,
            label=label,
            resolution=resolution)
        self.main.view.canvas.create_window(x, y, window=scale)
        return scale
