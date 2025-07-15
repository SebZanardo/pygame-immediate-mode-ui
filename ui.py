from dataclasses import dataclass


@dataclass(slots=True)
class StyleUI:
    button_w: int = 50
    button_h: int = 20
    checkbox_w: int = 20
    checkbox_h: int = 20
    slider_w: int = 100
    slider_h: int = 20


@dataclass(slots=True)
class ContextUI:
    # To track selected element for keyboard input and sliders
    id: int

    # Where to render next element
    x: int
    y: int

    # Stored incase you want the next element to sit next to the current one
    width: int
    last_height: int

    # Each context can have one active style
    style: StyleUI


def im_button(label: str) -> bool:
    pass


# NOTE: Passing value in list so can modify
def im_checkbox(label: str, value: list[bool]) -> bool:
    pass


# NOTE: Passing value in list so can modify
def im_slider(label: str, value: list[float], min: float, max: float) -> bool:
    pass
