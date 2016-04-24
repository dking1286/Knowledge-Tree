import tkinter as tk

import knowledge_tree.constants as constants


class Controller(object):

    def __init__(self, main=None):
        if not main:
            raise ValueError("No value provided for main")

        self.main = main

        self.initial_balance_slider = self.make_scale(
            command=self.on_initial_balance_slider_change,
            **constants.initial_balance_slider_data
        )
        self.initial_balance_slider.set(constants.initial_balance['default'])

        self.interest_rate_slider = self.make_scale(
            command=self.on_interest_rate_slider_change,
            **constants.interest_rate_slider_data
        )
        self.interest_rate_slider.set(constants.interest_rate['default'])

    def on_initial_balance_slider_change(self, balance):
        """Event handler for the initial balance slider"""
        balance = float(balance)
        interest_rate = self._yearly_to_monthly(float(self.interest_rate_slider.get()))
        self.main.view.update_axes(balance, interest_rate)

    def on_interest_rate_slider_change(self, interest_rate):
        """Event handler for the interest rate slider"""
        interest_rate = float(interest_rate)
        balance = float(self.initial_balance_slider.get())
        self.main.view.update_axes(balance, interest_rate)

    @staticmethod
    def _yearly_to_monthly(rate):
        """Converts a yearly interest rate to a onthly interest rate"""
        return rate / 12

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
