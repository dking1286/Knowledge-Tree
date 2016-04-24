import tkinter as tk

from knowledge_tree.view import View
from knowledge_tree.controller import Controller


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
        self.root = tk.Tk()
        self.view = View(main=self)
        self.controller = Controller(main=self)
        
    def main(self):
        self.root.mainloop()
        
        
if __name__ == '__main__':
    Main().main()
