from dataclasses import dataclass
import pygame

import globals as g


Pos = tuple[int, int]
Bbox = tuple[int, int, int, int]
Colour = tuple[int, int, int]


@dataclass(slots=True)
class StyleUI:
    button_dim: Pos = (50, 20)
    checkbox_dim: Pos = (20, 20)
    slider_dim: Pos = (100, 20)

    padding_x: int = 5
    padding_y: int = 5

    background_colour: Colour = (0, 0, 0)
    hovered_colour: Colour = (50, 50, 50)
    clicked_colour: Colour = (200, 200, 200)
    text_colour: Colour = (255, 0, 255)


@dataclass(slots=True)
class ContextUI:
    rx: int = 0
    ry: int = 0

    # To track selected element for keyboard input and sliders
    current_id: int = 0

    # Where to render next element
    x: int = 0
    y: int = 0

    # Stored incase you want the next element to sit next to the current one
    tracked_id: int = -1
    last_x: int = 0
    last_y: int = 0

    def bbox(self, width: int, height: int) -> Bbox:
        rect = (
                self.x,
                self.y,
                width,
                height
            )

        self.last_x = self.x + width + style.padding_x
        self.last_y = self.y

        self.x = self.rx
        self.y += height + style.padding_y

        self.current_id += 1

        return rect

    def interact(self, bbox: bbox) -> tuple[bool, bool, bool]:
        mx, my = g.mouse_pos
        x, y, w, h = bbox

        hovered = False
        clicked = False
        held = False

        if self.tracked_id == self.current_id:
            if g.mouse_held:
                held = True
            else:
                held = False
                self.tracked_id = -1

        elif mx >= x and my >= y and mx <= x + w and my <= y + h:
            hovered = True
            if g.mouse_clicked and self.tracked_id == -1:
                clicked = True
                self.tracked_id = self.current_id

        return hovered, clicked, held


# GLOBALS #####################################################################
style = StyleUI()
context = ContextUI()
###############################################################################


def im_button(label: str) -> bool:
    bbox = context.bbox(*style.button_dim)
    hovered, clicked, held = context.interact(bbox)
    pygame.draw.rect(
        g.window,
        style.background_colour,
        bbox
    )
    if clicked:
        # pygame.draw.rect(
        #     g.window,
        #     style.clicked_colour,
        #     bbox
        # )
        pass
    elif held:
        pygame.draw.rect(
            g.window,
            style.clicked_colour,
            bbox
        )
    elif hovered:
        pygame.draw.rect(
            g.window,
            style.hovered_colour,
            bbox
        )

    return clicked


def im_checkbox(label: str, value: list[bool]) -> bool:
    bbox = context.bbox(*style.checkbox_dim)
    hovered, clicked, held = context.interact(bbox)

    pygame.draw.rect(
        g.window,
        style.background_colour,
        bbox
    )

    if clicked:
        value[0] = not value[0]
        # pygame.draw.rect(
        #     g.window,
        #     style.clicked_colour,
        #     bbox
        # )
        pass
    elif held:
        pygame.draw.rect(
            g.window,
            style.clicked_colour,
            bbox
        )
    elif hovered:
        pygame.draw.rect(
            g.window,
            style.hovered_colour,
            bbox
        )

    if value[0]:
        pygame.draw.circle(
            g.window,
            style.text_colour,
            (bbox[0] + bbox[2] // 2, bbox[1] + bbox[3] // 2),
            8
        )

    return clicked


def im_slider(label: str, value: list[float], lo: float, hi: float) -> bool:
    bbox = context.bbox(*style.slider_dim)
    hovered, clicked, held = context.interact(bbox)
    pygame.draw.rect(
        g.window,
        style.background_colour,
        bbox
    )
    if held:
        value[0] = g.mouse_pos[0] - bbox[0]
        value[0] = min(max(value[0], lo), hi)
        pygame.draw.rect(
            g.window,
            style.clicked_colour,
            bbox
        )
    elif hovered:
        pygame.draw.rect(
            g.window,
            style.hovered_colour,
            bbox
        )

    pygame.draw.rect(
        g.window,
        style.text_colour,
        (
            bbox[0],
            bbox[1],
            value[0] / hi * style.slider_dim[0],
            bbox[3]
        )
    )

    return clicked


def im_same_line() -> None:
    context.x = context.last_x
    context.y = context.last_y


def im_set_next_position(x: int, y: int) -> None:
    context.x = x
    context.y = y


def im_reset_position() -> None:
    context.x = context.rx
    context.y = context.ry
    context.current_id = 0
