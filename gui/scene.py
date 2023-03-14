import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Scene:
    def __init__(self):
        pygame.init()
        self.side_size = 4
        self.screen = None
        self.should_quit = False

    def draw(self, board):
        self.reset_screen(board)

        for row_number, row in enumerate(board):
            self.draw_row(row_number, row)

        pygame.display.flip()

        self.capture_quit_event()

    def capture_quit_event(self):
        self.should_quit = pygame.QUIT in [e.type for e in pygame.event.get()]

        return self.should_quit

    def draw_row(self, row_number, row):
        for col_number, cell in enumerate(row):
            if cell.is_alive():
                sprite = self._build_cell_sprite(row_number, col_number)
                pygame.draw.rect(self.screen, WHITE, sprite)

    def _build_cell_sprite(self, row, col):
        left = col * self.side_size
        top = row * self.side_size

        sprite = pygame.Rect(left, top, self.side_size, self.side_size)

        return sprite

    def _build_screen(self, board):
        width = board.size.col * self.side_size
        height = board.size.row * self.side_size

        screen = pygame.display.set_mode((width, height))

        return screen

    def reset_screen(self, board):
        if self.screen is None:
            self.screen = self._build_screen(board)

        self.screen.fill(BLACK)
