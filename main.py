import tkinter as tk

from model import Model
from view import View
from controller import Controller
from task import TaskManager
import database

class Main(object):
    """Manages the communication between the Model, View, and Controller instances
    
    Attributes:
        root (tk.Tk): Root window
        model (Model)
        view (View)
        controller (Controller)
        task_manager (TaskManager)
        
    Public methods:
        task_loop()
        main()
    Private methods:
        _manage_tasks()
    """
    def __init__(self):
        database.initialize()
        self.root = tk.Tk()
        self.model = Model(main=self)
        self.view = View(main=self)
        self.controller = Controller(main=self)
        self.task_manager = TaskManager(main=self)
        
    def task_loop(self):
        self.task_manager.process_tasks()
        self.root.after(17, self.task_loop)
        
    def main(self):
        self.task_loop()
        self.root.mainloop()
        
        
if __name__=='__main__':
    Main().main()