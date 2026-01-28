"""Tests for main game functionality."""

import pytest


def test_snake_initialization(snake):
    """Test snake initialization."""
    assert len(snake.body) == 3
    assert snake.direction == 'RIGHT'
