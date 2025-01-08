import reflex as rx

config = rx.Config(
    app_name="portfolio_web",
    base_path="",
    frontend_only=True,
    build_path=".web",
    static_dir="public",
    env=rx.Env.PROD,
)