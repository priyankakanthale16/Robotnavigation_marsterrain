from direction_instructions import robot_navigation_direction
class RobotNavigation():    
    def __init__(self,grid_size,commands_for_robot):
        '''
        Intiliazing:
        grid_size to split and stored row size at 0 and column size at 1 index
        commands_for_robot - to store command in string and make it in upper case even if input given in lower case.
        current_cordinates - from where the robot will start
        robot_current_facing_direction- starting position of robot will always be North
        robot_directions-robot direction accessed from direction_instruction file
        
        '''
        self.grid_size= grid_size.split('x') 
        self.commands_for_robot= commands_for_robot.upper() 
        self.current_cordinates=[1,1]
        self.robot_current_facing_direction='North' 
        self.robot_directions=robot_navigation_direction 
    
    
    def check_robot_position(self) -> bool:
        '''
        function to check if the initial position of robot is facing towards north and on correct coordinates
        '''
        if self.current_cordinates == [1, 1] and self.robot_current_facing_direction == 'North':
            return True
        return False    
    
    def check_if_robot_moved(self, commands_for_robot) -> bool:
        '''
        function to check if robot can be moved 
        param: commands_for_robot
        '''
        if commands_for_robot == 'F':
            return True
        return False   
    
    def check_if_robot_move_valid(self, coordintes, max_size) -> bool:
        '''
        function to check if move valid
        param:
        coordinates of robot position 
        max-size 
        '''
        if (coordintes[0] < int(max_size[0]) and coordintes[0] > -1) and (coordintes[1] < int(max_size[1]) and coordintes[1] > -1):
            return True
        return False
    
    def is_robot_move_possible(self, commands_for_robot):
        '''
        This function checks if the command given to robot is possible to move if yes move the robot
        Param : current command for robot      
             
        '''
        # Get match and get the direction of current command from 'direction_instructions file'
        next_robot_facing_direction = self.robot_directions[self.robot_current_facing_direction][commands_for_robot] 
        addition_to_perform = self.robot_directions[next_robot_facing_direction]['calculation'] 
        # Calculate current robot_coordinates
        next_cell_coordinates = [sum(i) for i in zip(self.current_cordinates, addition_to_perform)] 

        # to check boundaries if valid change robot direction
        if self.check_if_robot_move_valid(next_cell_coordinates, self.grid_size):
            self.robot_current_facing_direction = next_robot_facing_direction 

            # if command is 'F' then move forward
            if self.check_if_robot_moved(commands_for_robot):
                self.current_cordinates = next_cell_coordinates 
                
    def robot_commands_process(self) -> tuple:
        '''
        input of the command will alaways be string and only letters 
        L: Turn Left
        R: Turn Right
        F: Move forward
        Passing commands to functions
        '''
        for command in self.commands_for_robot:
            self.is_robot_move_possible(command)
        return self.current_cordinates, self.robot_current_facing_direction
    
if __name__=="__main__":
    grid_size=str(input().lower())
    commands_for_robot=str(input())
    robot=RobotNavigation(grid_size,commands_for_robot)
    if robot.check_robot_position():
        coordinates, direction = robot.robot_commands_process()
        print(str(coordinates[0]) +","+ str(coordinates[1]) +","+ direction)
    
    
    

