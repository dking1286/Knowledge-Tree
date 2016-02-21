import knowledge_tree.constants as constants


class GraphManager(object):
    """Manages the movement of the points on the axes
    
    Attributes:
        view (View): The view that the GraphManager belongs to
        
    Public methods:
        update_points_for_new_values(Bo, r)
    """
    def __init__(self, view):
        self.view = view
        
    def update_points_for_new_values(self, Bo, r):
        for p in constants.monthly_payment_range():
            try:
                new_y = self.view.main.model.get_payoff_time(Bo=Bo, r=r, p=p)
                print(1, new_y)
            except ValueError:
                # If there's no point stored in the database with the given values,
                # skip this one.
                print("No DataPoint was found with Bo={}, r={}, p={}".format(Bo, r, p))
                continue
            else:
                print(2, new_y)
                try:
                    self.view.axes.move_point_in_y_direction(
                        x=p,
                        new_y=new_y)
                except ValueError:
                    # If the point isn't already plotted on the graph, add it.
                    self.view.axes.add_point(p, new_y)
