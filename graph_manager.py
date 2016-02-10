class GraphManager(object):
    """Manages the movement of the points on the axes
    
    Attributes:
        view (View): The view that the GraphManager belongs to
        
    Public methods:
        update_points_for_new_values(Bo, r)
    """
    def __init__(self, view):
        self.view = view
        
    def update_points_for_new_values(Bo, r):
        for p in self.view.main.model.get_time_vs_payment_data(Bo=Bo, r=r)
            self.view.axes.move_point_in_y_direction(
                x=p,
                new_y=self.view.main.model.payoff_times[Bo][r][p])
            
        