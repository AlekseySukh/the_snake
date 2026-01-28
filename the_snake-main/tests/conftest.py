"""Configuration for pytest tests."""

import pytest

from the_snake import Snake, Apple, GameState


@pytest.fixture
def snake():
    """Create a Snake instance for testing."""
    return Snake()


@pytest.fixture
def apple():
    """Create an Apple instance for testing."""
    return Apple()


@pytest.fixture
def game_state():
    """Create a GameState instance for testing."""
    return GameState()


@pytest.fixture
def snake_body():
    """Return a snake body for testing."""
    return [
        {'x': 5, 'y': 5},
        {'x': 5, 'y': 4},
        {'x': 5, 'y': 3}
    ]


@pytest.fixture
def food_position():
    """Return food position for testing."""
    return {'x': 10, 'y': 10}


@pytest.fixture
def game_state_with_positions(snake_body, food_position):
    """Create GameState with specific positions."""
    return GameState(snake_body=snake_body, food=food_position)


class TestGameState:
    """Test class for GameState."""

    pass


@pytest.fixture
def test_game_state():
    """Create TestGameState instance."""
    return TestGameState()


@pytest.fixture
def initial_snake_position():
    """Return initial snake position."""
    return {'x': 5, 'y': 5}
