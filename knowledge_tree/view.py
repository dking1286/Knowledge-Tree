import tkinter as tk

import knowledge_tree.constants as constants
from knowledge_tree.point import Point
from knowledge_tree.axes import Axes
from knowledge_tree.financial_tools import payments_to_payoff


class View(object):
    """Manages all of the visible components of the program, including the
    displayed graph.
    """ 

    def __init__(self, main=None):
    
        if not main:
            raise ValueError("No value provided for main")
            
        self.main = main
        self.canvas = tk.Canvas(
            self.main.root,
            background='#FFFFFF',
            **constants.canvas_dimensions)
        self.axes = Axes(
            canvas=self.canvas,
            **constants.axes_display,
            **constants.axes_scale)
                                
        self.canvas.grid()

        for p in constants.monthly_payment_range():
            a = constants.initial_balance['default']
            i = constants.interest_rate['default']
            payoff_months = payments_to_payoff(a, i / 12, p)
            if payoff_months is None:
                continue
            self.axes.add_point(p, payoff_months / 12)

    def update_axes(self, a, i):
        """Updates the points on the axes to reflect the new values of a and i.

        Args:
            a (numeric): The initial balance of the loan
            i (numeric): The interest rate per payment period (NOT per year) in decimal form
        """
        for p in constants.monthly_payment_range():
            try:
                payoff_months = payments_to_payoff(a, i / 12, p)
                point = self.axes.get_point_by_x(p)
                self.axes.move_point(point, p, payoff_months / 12)
            except AssertionError:
                # payments_to_payoff failed preconditions
                continue
            except ValueError:
                # No point exists on graph with x = p
                continue
