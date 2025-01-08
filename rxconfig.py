import reflex as rx

config = rx.Config(
    app_name="portfolio_web",
    base_path="/harimkang-pages",
    frontend_only=True,
    build_path=".web",
    static_dir=".web/_static",
    env=rx.Env.PROD,
)