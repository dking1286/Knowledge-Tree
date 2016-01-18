class TaskManager(object):
    """Manages and performs tasks in a program.
    
    Attributes:
        main (Main)
        _upcoming_tasks (list<Task>)
        _tasks (list<Task>)
        _finished_tasks (list<Task>)
        
    Public methods:
        add_task(task)
        process_tasks()
    """
    def __init__(self, main=None):
        self.main = main
        self._upcoming_tasks = list()
        self._tasks = list()
        self._finished_tasks = list()
        
    def add_task(self, task):
        self._upcoming_tasks.append(task)
        
    def process_tasks(self):
        # Move new tasks into _tasks list
        for task in self._upcoming_tasks:
            self._tasks.append(task)
        
        for task in self._tasks:
            # Remove new tasks from _upcoming_tasks
            if task in self._upcoming_tasks:
                self._upcoming_tasks.remove(task)

            # Do active tasks
            elif task.state == 'active':
                if task.description is not None:
                    print(task.description)
                task.execute()
                self._finished_tasks.append(task)
        
        #Delete finished tasks
        for task in self._finished_tasks:
            self._tasks.remove(task)
        self._finished_tasks = []

class Task(object):
    """Represents a task that needs to happen in the battle's _animate method
    Static members:
        validStates (dict<string, int>)
    Attributes:
        function    (function): A function that represents the action
            of the task
        args        (list): A list of the positional arguments to apply to the function when the task
            is executed.
        kwargs      (dict): A dictionary of the keyword arguments to apply to the
            function when the task is executed.
        _state      (int)
        state       (string, property)
        description (string)
    Public methods:
        Task(function=None, args=None, kwargs=None, state='active', description=None)
        execute()
    """
    validStates = {"upcoming":0, "active":1, "finished":2}
    
    def __init__(self, function=None, args=None, kwargs=None, state="active",
                    description=None):
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.description = description
        self.state = state
    
    @property
    def state(self):
        for name, num in Task.validStates.items():
            if self._state==num:
                return name
            else:
                continue
    
    @state.setter
    def state( self, name ):
        if name not in Task.validStates.keys():
            raise ValueError('That is not a valid name for a Task state.')
        
        self._state = Task.validStates[name]
    
    def execute(self):
        if self.args is None and self.kwargs is None:
           self.function()
        elif self.args is None:
            self.function(**self.kwargs)
        elif self.kwargs is None:
            self.function(*self.args)
        else:
            self.function(*self.args, **self.kwargs)
