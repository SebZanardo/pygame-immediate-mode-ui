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

    background_colour = (0, 0, 0)
    hovered_colour = (50, 50, 50)
    clicked_colour = (200, 200, 200)
    text_colour = (255, 0, 255)


@dataclass(slots=True)
class ContextUI:
    rx: int = 0
    ry: int = 0

    # To track selected element for keyboard input and sliders
    id: int = 0

    # Where to render next element
    x: int = 0
    y: int = 0

    # Stored incase you want the next element to sit next to the current one
    last_x: int = 0
    last_y: int = 0

    def bbox(self, width: int, height: int) -> Bbox:
        rect = (
                g.ui_context.x,
                g.ui_context.y,
                width,
                height
            )

        g.ui_context.last_x = g.ui_context.x + width + g.ui_style.padding_x
        g.ui_context.last_y = g.ui_context.y

        g.ui_context.x = g.ui_context.rx
        g.ui_context.y += height + g.ui_style.padding_y

        return rect

    def interact(self, bbox: Bbox) -> tuple[bool, bool, bool]:
        mx, my = g.mouse_pos
        x, y, w, h = bbox

        hovered = False
        clicked = False
        held = False

        if mx >= x and my >= y and mx <= x + w and my <= y + h:
            hovered = True
            if g.mouse_clicked:
                clicked = True

        return hovered, clicked, held


def im_button(label: str) -> bool:
    rect = g.ui_context.bbox(*g.ui_style.button_dim)
    hovered, clicked, held = (False, False, False)
    return clicked


def im_checkbox(label: str, value: list[bool]) -> bool:
    bbox = g.ui_context.bbox(*g.ui_style.checkbox_dim)

    hovered, clicked, held = g.ui_context.interact(bbox)

    if clicked:
        value[0] = not value[0]

    # TODO: Draw loaded assets here not shapes
    pygame.draw.rect(
        g.window,
        g.ui_style.background_colour,
        bbox
    )

    if value[0]:
        pygame.draw.rect(
            g.window,
            g.ui_style.text_colour,
            bbox
        )

    return clicked


def im_slider(label: str, value: list[float], lo: float, hi: float) -> bool:
    rect = g.ui_context.bbox(*g.ui_style.slider_dim)

    hovered, clicked, held = (False, False, False)

    return clicked


def im_same_line() -> None:
    g.ui_context.x = g.ui_context.last_x
    g.ui_context.y = g.ui_context.last_y


def im_set_next_position(x: int, y: int) -> None:
    g.ui_context.x = x
    g.ui_context.y = y


def im_reset_position() -> None:
    g.ui_context.x = g.ui_context.rx
    g.ui_context.y = g.ui_context.ry
