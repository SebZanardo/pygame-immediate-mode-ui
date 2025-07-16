import pygame

import ui
import globals as g


WIDTH = 480
HEIGHT = 360
FPS = 60


def main() -> None:
    pygame.init()

    g.window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("immediate-mode-ui")

    g.ui_style = ui.StyleUI()
    g.ui_context = ui.ContextUI()

    toggle1 = [False]
    toggle2 = [False]
    toggle3 = [False]

    running = True

    while running:
        clock.tick(FPS)

        g.mouse_pos = pygame.mouse.get_pos()
        g.mouse_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                g.mouse_clicked = True

        g.window.fill((255, 255, 255))

        ui.im_reset_position()
        ui.im_checkbox("checkbox", toggle1)
        ui.im_checkbox("checkbox", toggle2)
        ui.im_same_line()
        ui.im_checkbox("checkbox", toggle3)
        ui.im_same_line()
        ui.im_checkbox("checkbox", toggle3)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
