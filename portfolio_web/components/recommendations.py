import reflex as rx

def create_recommendation_card(
    quote: str,
    author_name: str,
    author_title: str,
    linkedin_url: str = None,
):
    """Create a recommendation card with quote and author info."""
    return rx.box(
        rx.box(
            rx.text(
                f'"{quote}"',
                font_style="italic",
                color="white",
                font_size="1.1rem",
                line_height="1.75rem",
                margin_bottom="1rem",
            ),
            rx.box(
                rx.text(
                    f"- {author_name}",
                    font_weight="bold",
                    color="white",
                    margin_bottom="0.25rem",
                ),
                rx.text(
                    author_title,
                    color="rgb(156, 163, 175)",
                    font_size="0.875rem",
                    margin_bottom="0.5rem",
                ),
                rx.cond(
                    linkedin_url is not None,
                    rx.link(
                        "View on LinkedIn",
                        href=linkedin_url,
                        color="rgb(96, 165, 250)",
                        font_size="0.875rem",
                        text_decoration="none",
                        _hover={"text_decoration": "underline"},
                    ),
                ),
            ),
        ),
        padding="2rem",
        background="rgba(17, 24, 39, 0.7)",
        border_radius="0.75rem",
        backdrop_filter="blur(10px)",
        border="1px solid rgba(255, 255, 255, 0.1)",
        width="100%",
    )

def create_recommendations_section():
    """Create the recommendations section."""
    return rx.box(
        rx.heading(
            "Recommendations",
            font_size="2rem",
            font_weight="bold",
            margin_bottom="2rem",
            color="white",
        ),
        rx.grid(
            create_recommendation_card(
                quote="Harim's versatility and adaptability are remarkable—he's the ultimate Swiss Army knife who delivers complete, production-ready pipelines with impressive speed. His rare combination of technical excellence, rapid learning ability, and outstanding interpersonal skills makes him an invaluable asset to any team.",
                author_name="Samet Akcay",
                author_title="Technical Lead at Intel",
                linkedin_url="https://www.linkedin.com/in/harim-kang-hk1129/",  # 실제 LinkedIn URL로 교체
            ),
            create_recommendation_card(
                quote="Harim's leadership in the OTX2.0 release was exceptional—he combined technical expertise, proactive communication, and a user-centric approach to create a product that resonated with its audience. His ability to anticipate client needs and foster collaboration makes him an invaluable team member.",
                author_name="Sungman Cho",
                author_title="Co-founder TBD Labs | ex-Intel",
                linkedin_url="https://www.linkedin.com/in/harim-kang-hk1129/",  # 실제 LinkedIn URL로 교체
            ),
            template_columns=rx.breakpoints(
                {
                    "0px": "1fr",
                    "768px": "repeat(2, 1fr)",
                }
            ),
            gap="2rem",
            width="100%",
        ),
        id="recommendations",
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="4rem",
        padding_bottom="4rem",
    ) 