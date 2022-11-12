
robot_navigation_direction = {   # Guides for the direction and calculation of cell moved for the command
            'North': {'L': 'West', 'R': 'East', 'F': 'North', 'calculation': [0, 1]},
            'East': {'L': 'North', 'R': 'South', 'F': 'East', 'calculation': [1, 0]},
            'West': {'L': 'South', 'R': 'North', 'F': 'West', 'calculation': [-1, 0]},
            'South': {'L': 'East', 'R': 'West', 'F': 'South', 'calculation': [0, -1]}
        }
        