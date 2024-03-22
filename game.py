import pygame


class Game:
    def __init__(self, name, w, h):
        self.game_name = name
        self.height, self.width = h, w
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.game_name)
        self.currentState = None

    def run(self, state):
        game_over = False
        self.currentState = state
        clock = pygame.time.Clock()

        while not game_over:
            clock.tick(10)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    game_over = True
            self.screen.fill((0, 0, 0))
            self.currentState = self.currentState.update(events)
            self.currentState.draw(self.screen)
            pygame.display.update()

        pygame.quit()
