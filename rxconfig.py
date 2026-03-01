import reflex as rx

config = rx.Config(
    app_name="docker_tutorial",
    api_url="http://158.180.92.202:8000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)