import pygame

import ui
import globals as g
import constants as c


def main() -> None:
    pygame.display.set_caption("immediate-mode-ui")

    toggle1 = [False]
    toggle2 = [False]
    toggle3 = [False]
    slider = [50]

    running = True

    while running:
        g.clock.tick(c.FPS)

        g.mouse_pos = pygame.mouse.get_pos()
        g.mouse_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                g.mouse_clicked = True
                g.mouse_held = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                g.mouse_held = False

        g.window.fill((255, 255, 255))

        ui.im_reset_position()
        ui.im_checkbox("checkbox", toggle1)
        ui.im_checkbox("checkbox", toggle2)
        ui.im_same_line()
        ui.im_checkbox("checkbox", toggle3)
        ui.im_same_line()
        ui.im_checkbox("checkbox", toggle3)
        ui.im_button("hello world!")
        ui.im_set_next_position(100, 100)
        ui.im_slider("sliiiideerr", slider, 0, 100)
        ui.im_same_line()
        ui.im_same_line()
        ui.im_button("hello world!")

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
