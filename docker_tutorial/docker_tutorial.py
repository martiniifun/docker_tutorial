"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    integer: int = 0

    @rx.event
    def plus(self) -> None:
        self.integer += 1

    @rx.event
    def minus(self) -> None:
        self.integer -= 1


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.hstack(
                rx.button("-", on_click=State.minus, color_scheme="red"),
                rx.heading(State.integer),
                rx.button("+", on_click=State.plus, color_scheme="green"),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
