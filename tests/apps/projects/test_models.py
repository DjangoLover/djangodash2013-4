from django.test import TestCase
from model_mommy import mommy
from hamcrest import *


class TestBoardModel(TestCase):
    def setUp(self):
        self.project = mommy.make('projects.Project')
        self.project2 = mommy.make('projects.Project')

    def test_board_counter_with_one_board(self):
        new_board = mommy.make('projects.Board', title='To Do', project=self.project)
        result = new_board.count_project_boards()
        assert_that(result, is_(1))

    def test_board_counter_with_five_boards_of_one_project(self):
        board1 = mommy.make('projects.Board', title='123', project=self.project)
        board2 = mommy.make('projects.Board', project=self.project)
        board3 = mommy.make('projects.Board', project=self.project)
        board4 = mommy.make('projects.Board', project=self.project)
        board5 = mommy.make('projects.Board',title='321', project=self.project)
        result = board3.count_project_boards()
        assert_that(result, is_(5))

    def test_board_counter_with_five_boards_of_two_projects(self):
        board1 = mommy.make('projects.Board', project=self.project)
        board2 = mommy.make('projects.Board', project=self.project)
        board3 = mommy.make('projects.Board', project=self.project2)
        board4 = mommy.make('projects.Board', project=self.project)
        board5 = mommy.make('projects.Board', project=self.project2)
        result1 = board1.count_project_boards()
        result2 = board3.count_project_boards()
        assert_that(result1, is_(3))
        assert_that(result2, is_(2))

    def test_increase_board_position_once(self):
        board1 = mommy.make('projects.Board', project=self.project)
        board2 = mommy.make('projects.Board', project=self.project)
        board1.increase_position()
        assert_that(board1.position, is_(1))

    def test_increase_board_position_twice(self):
        board1 = mommy.make('projects.Board', project=self.project)
        board2 = mommy.make('projects.Board', project=self.project)
        board1.increase_position()
        board1.increase_position()
        assert_that(board1.position, is_(1))

    def test_increase_board_position_once_with_one_instance(self):
        board1 = mommy.make('projects.Board', project=self.project)
        board1.increase_position()
        assert_that(board1.position, is_(0))

    def test_increase_board_position_twice_with_one_instance(self):
        board1 = mommy.make('projects.Board', project=self.project)
        board1.increase_position()
        board1.increase_position()
        assert_that(board1.position, is_(0))

    def test_decrease_board_position_once(self):
        board1 = mommy.make('projects.Board', project=self.project)
        board2 = mommy.make('projects.Board', project=self.project)
        board2.decrease_position()
        assert_that(board1.position, is_(0))

    def test_decrease_board_position_once_with_one_instance(self):
        board1 = mommy.make('projects.Board', project=self.project)
        board1.decrease_position()
        assert_that(board1.position, is_(0))

    def test_decrease_board_position_twice_with_one_instance(self):
        board1 = mommy.make('projects.Board', project=self.project)
        board1.decrease_position()
        board1.decrease_position()
        assert_that(board1.position, is_(0))