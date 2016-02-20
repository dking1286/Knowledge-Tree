import tkinter as tk

from model import Model
from view import View
from controller import Controller
from database import initialize, DATABASE


class Main(object):
    """Manages the communication between the Model, View, and Controller instances
    
    Attributes:
        root (tk.Tk): Root window
        model (Model)
        view (View)
        controller (Controller)
        
    Public methods:
        main()
    """
    def __init__(self):
        initialize(DATABASE)
        self.root = tk.Tk()
        self.model = Model(main=self, db=DATABASE)
        self.view = View(main=self)
        self.controller = Controller(main=self)
        
    def main(self):
        self.root.mainloop()
        
        
if __name__ == '__main__':
    Main().main()
