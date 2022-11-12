import unittest
from robot_navigation import RobotNavigation


class Test_RobotNavigtion(unittest.TestCase):

    def setUp(self):
        self.robot = RobotNavigation(grid_size='5x5', commands_for_robot='FFRFLFLF')

    def test_check_robot_position(self):
        self.assertEqual(self.robot.check_robot_position(), True)

    def test_if_to_be_moved(self):
        self.assertEqual(self.robot.check_if_robot_moved('F'), True)

    def test_check_if_command_valid(self):
        self.assertEqual(self.robot.check_if_robot_move_valid([-1, -1], [5, 5]), False)

    def test_final_result(self):
        self.assertEqual(self.robot.robot_commands_process(), ([1, 4], 'West'))

if __name__ == "__main__":
    unittest.main()