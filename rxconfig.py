import reflex as rx

config = rx.Config(
    app_name="docker_tutorial",
    api_url="http://168.107.22.109:8000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)