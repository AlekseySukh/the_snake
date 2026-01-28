"""Tests for code structure and imports."""

import ast
import importlib
import inspect


def test_snake_class_exists():
    """Test that Snake class exists."""
    import the_snake
    assert hasattr(the_snake, 'Snake'), 'Snake class not found'


def test_apple_class_exists():
    """Test that Apple class exists."""
    import the_snake
    assert hasattr(the_snake, 'Apple'), 'Apple class not found'


def test_game_state_class_exists():
    """Test that GameState class exists."""
    import the_snake
    assert hasattr(the_snake, 'GameState'), 'GameState class not found'


def test_snake_has_move_method():
    """Test that Snake class has move method."""
    from the_snake import Snake
    snake = Snake()
    assert hasattr(snake, 'move'), 'Snake class has no move method'
    assert callable(snake.move), 'move is not a method'


def test_snake_has_grow_method():
    """Test that Snake class has grow method."""
    from the_snake import Snake
    snake = Snake()
    assert hasattr(snake, 'grow'), 'Snake class has no grow method'
    assert callable(snake.grow), 'grow is not a method'


def test_apple_has_regenerate_method():
    """Test that Apple class has regenerate method."""
    from the_snake import Apple
    apple = Apple()
    assert hasattr(apple, 'regenerate'), 'Apple class has no regenerate method'
    assert callable(apple.regenerate), 'regenerate is not a method'


def test_game_state_has_check_collision_method():
    """Test that GameState has check_collision method."""
    from the_snake import GameState
    game_state = GameState()
    assert hasattr(game_state, 'check_collision'), (
        'GameState has no check_collision method'
    )
    assert callable(game_state.check_collision), (
        'check_collision is not a method'
    )


def test_game_state_has_check_eaten_method():
    """Test that GameState has check_eaten method."""
    from the_snake import GameState
    game_state = GameState()
    assert hasattr(game_state, 'check_eaten'), (
        'GameState has no check_eaten method'
    )
    assert callable(game_state.check_eaten), 'check_eaten is not a method'
