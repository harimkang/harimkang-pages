import reflex as rx

config = rx.Config(
    app_name="portfolio_web",
    base_path="/harimkang-pages",
    frontend_only=True,
    build_path=".web",
    static_dir="public",
    env=rx.Env.PROD,
    route_prefix="/harimkang-pages",
    next_config={
        "basePath": "/harimkang-pages",
        "assetPrefix": "/harimkang-pages",
        "trailingSlash": True,
        "publicRuntimeConfig": {
            "basePath": "/harimkang-pages",
        },
    },
    connect_on_init=False,
    disable_ws=True,
)