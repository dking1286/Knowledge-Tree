import tkinter as tk

class Controller(object):
    """Manages the user interface, in particular the interest rate slider.
    
    Attributes:
        main (Main): A reference to the Main instance that contains the Controller instance
        interest_rate_slider (tk.Scale): A slider that controls the interest rate of
            the data to be displayed.
            
    Public methods:
        on_interest_rate_slider_change (event handler for interest rate slider)
        
    """
    def __init__(self, main=None):
        if not main:
            raise ValueError()
            
        self.main = main
        self.go_button = self.make_button(100, 100,
                                          command=self.on_go_button_click,
                                          text="GO!")

    def on_go_button_click(self):
        go_task = Task(function=self.main.model.calculate_payoff_times)
        self.main.task_manager.add_task(go_task)
        
    def make_button( self, x, y, command=None, text=None ):
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
        
        ref = tk.Button( self.main.root, command=command, text=text )
        self.main.view.canvas.create_window( x, y, window=ref )
        return ref