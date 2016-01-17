import tkinter as tk

from constants import (MINIMUM_INITIAL_BALANCE, MAXIMUM_INITIAL_BALANCE, INITIAL_BALANCE_STEP,
                       MINIMUM_INTEREST_RATE, MAXIMUM_INTEREST_RATE, INTEREST_RATE_STEP,
                       CANVAS_HEIGHT, CANVAS_WIDTH)
from point import Point

class View(object):
    """Manages all of the visible components of the program, including the
    displayed graph.
    
    Attributes:
        main (Main): A reference to the Main instance that contains the View instance
        canvas (tk.Canvas): The canvas on which the visible components will be drawn.
        progress_bar (Bar): A progress bar that displays the progress of calculating the data to
            display
        loading_text (text&): A reference to the text that is displayed above the progress bar
        axes (?): A reference to the set of axes that the points will be displayed on
        
    Public methods:
        View(main=None)
    """ 
    
    INTEREST_RATE_NUM_STEPS = (MAXIMUM_INTEREST_RATE - MINIMUM_INTEREST_RATE)/INTEREST_RATE_STEP
    INITIAL_BALANCE_NUM_STEPS = (MAXIMUM_INITIAL_BALANCE - MINIMUM_INITIAL_BALANCE)/INITIAL_BALANCE_STEP
    PROGRESS_BAR_SCALE_MAX = INTEREST_RATE_NUM_STEPS * INITIAL_BALANCE_NUM_STEPS
    
    def __init__(self, main=None):
    
        if not main:
            raise ValueError()
            
        self.main = main
        self.canvas = tk.Canvas(self.main.root,
                                height=CANVAS_HEIGHT,
                                width=CANVAS_WIDTH,
                                background='#FFFFFF')
        self.progress_bar = Bar(self, length=800,
                                scale_min=0,
                                scale_max=self.PROGRESS_BAR_SCALE_MAX,
                                initial_value=0)
                                
        self.canvas.grid()
        
class Bar(object):
    """Represents a display bar or gauge on the canvas
    attributes:
        view (View)
        value (numeric)
        orientation (str, property)
        corner (Point): represents the upper-left corner of a horizontal bar
                            or the lower-left corner of a vertical one
        width (int)
        length (int)
        scale_min (int)
        scale_max (int)
        color (str): A hex string representing the color of the bar
        display (rectangle&)
        border (rectangle&)
        
    instance methods:
        Bar( view, orientation='horizontal',
             corner=Point(0 ,0), width=40, length=100,
             scale_min=0, scale_max=10 )
        update( newVal )
    """
    def __init__( self, view, orientation='horizontal',
                  corner=Point(0, 0), width=40, length=100,
                  scale_min=0, scale_max=10, color='#0000FF',
                  initial_value=10):
        # Set internal attributes
        self.view = view
        self.value = initial_value
        self.orientation = orientation
        self.corner = corner
        self.width = width
        self.length = length
        self.scale_min = scale_min
        self.scale_max = scale_max
        self.color = '#0000FF'
        
        # Place bar on canvas
        if self.orientation == 'horizontal':
            upperLeft = self.corner.coords()
            lowerRight = ( self.corner + Point(self.length, self.width) ).coords()
        elif self.orientation == 'vertical':
            upperLeft = ( self.corner + Point( 0, -self.length ) ).coords()
            lowerRight = ( self.corner + Point( self.width, 0 ) ).coords()
        self.display = self.view.canvas.create_rectangle( *upperLeft,
                                                               *lowerRight,
                                                               fill=self.color )
        self.border = self.view.canvas.create_rectangle(*upperLeft,
                                                        *lowerRight,
                                                        width=3)
        
        if initial_value != scale_max:
            self.update(initial_value)
    
    @property
    def orientation( self ):
        return self._orientation
    
    @orientation.setter
    def orientation( self, newVal ):
        isValid = (newVal == 'horizontal' or newVal == 'vertical')
        if not isValid:
            raise ValueError('orientation can only take the values'
                             ' \'horizontal\' or \'vertical\'.' )
        self._orientation = newVal
    
    def update( self, newVal ):
        """update the length of the bar to reflect the new value"""
        if newVal > self.scale_max or newVal < self.scale_min:
            raise ValueError('The bar\'s maximum or minimum value has been exceeded.')
        
        self.value = newVal
        newLength = int(self.length*newVal/self.scale_max)
        self.view.canvas.itemconfigure( self.display, state=tk.HIDDEN )
        if self.orientation == 'horizontal':
            upperLeft = self.corner.coords()
            lowerRight = ( self.corner + Point(newLength, self.width) ).coords()
        elif self.orientation == 'vertical':
            upperLeft = ( self.corner + Point( 0, -newLength ) ).coords()
            lowerRight = ( self.corner + Point( self.width, 0 ) ).coords()
        self.display = self.view.canvas.create_rectangle( *upperLeft,
                                                               *lowerRight,
                                                               fill=self.color )