import pygame


WIDTH = 480
HEIGHT = 360
FPS = 60


def main() -> None:
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("immediate-mode-ui")

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((255, 255, 255))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
