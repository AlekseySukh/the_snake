from random import choice, randint
from typing import List, Optional, Tuple

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption("Змейка")

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """Базовый класс, от которого наследуются другие игровые объекты."""

    def __init__(
        self,
        position: Optional[Tuple[int, int]] = None,
        body_color: Tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        if position is None:
            position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.position = position
        self.body_color = body_color

    def draw(self) -> None:
        """Абстрактный метод, который предназначен
        для переопределения в дочерних классах.
        """
        pass


class Apple(GameObject):
    """Класс, унаследованный от GameObject,
    описывающий яблоко и действия с ним.
    """

    def __init__(self) -> None:
        super().__init__(body_color=APPLE_COLOR)
        self.randomize_position()

    def randomize_position(self) -> None:
        """Устанавливает случайное положение яблока на игровом поле
        — задаёт атрибуту position новое значение.
        """
        self.position = (
            randint(0, GRID_WIDTH) * GRID_SIZE,
            randint(0, GRID_HEIGHT) * GRID_SIZE,
        )

    def draw(self) -> None:
        """Отрисовывает яблоко на игровой поверхности."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс, унаследованный от GameObject,
    описывающий змейку и её поведение.
    """

    def __init__(self) -> None:
        super().__init__(body_color=SNAKE_COLOR)
        self.positions: List[Tuple[int, int]] = [self.position]
        self.length: int = 1
        self.direction: Tuple[int, int] = RIGHT
        self.next_direction: Optional[Tuple[int, int]] = None
        self.last: Optional[Tuple[int, int]] = None

    def update_direction(self) -> None:
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self) -> None:
        """Обновляет позицию змейки (координаты каждой секции), добавляя новую
        голову в начало списка positions и удаляя последний элемент,
        если длина змейки не увеличилась.
        """
        current = self.get_head_position()
        x, y = self.direction
        new = (
            (current[0] + (x * GRID_SIZE)) % SCREEN_WIDTH,
            (current[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT,
        )
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
            return
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def draw(self) -> None:
        """Отрисовывает змейку на экране, затирая след."""
        for position in self.positions[:-1]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self) -> Tuple[int, int]:
        """Возвращает позицию головы змейки
        (первый элемент в списке positions).
        """
        return self.positions[0]

    def reset(self) -> None:
        """Сбрасывает змейку в начальное состояние
        после столкновения с собой.
        """
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = None
        self.last = None
        screen.fill(BOARD_BACKGROUND_COLOR)


def handle_keys(game_object):
    """Обрабатывает нажатия клавиш,
    чтобы изменить направление движения змейки.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Основная функция, в которой создаются экземпляры
    классов и запускается игровой цикл.
    """
    pygame.init()

    snake = Snake()
    apple = Apple()

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        apple.draw()
        snake.draw()

        pygame.display.update()


if __name__ == "__main__":
    main()
