import reflex as rx
from ..utils.styles import (
    create_styled_heading, 
    create_paragraph,
    create_section_heading,
    create_link_with_icon
)

def create_blog_post_card(animation_attrs, post_title, post_excerpt, href):
    """Create a blog post card with title and excerpt."""
    return rx.box(
        create_styled_heading(
            font_size="1.25rem",
            line_height="1.75rem",
            heading_text=post_title,
        ),
        create_paragraph(
            margin_bottom="1rem",
            paragraph_text=post_excerpt,
        ),
        create_link_with_icon(
            link_text="Read More ",
            icon_alt="Arrow Right",
            icon_tag="arrow-right",
            href=href,
        ),
        class_name="transform",
        custom_attrs=animation_attrs,
        background_color="#374151",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        _hover={"transform": "scale(1.05)"},
        padding="1.5rem",
        border_radius="0.5rem",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )

def create_blog_section():
    """Create the 'Blog' section with blog post cards."""
    return rx.box(
        create_section_heading(heading_text="Blog"),
        rx.box(
            create_blog_post_card(
                animation_attrs={
                    "data-aos": "fade-up",
                    "data-aos-delay": "200",
                },
                post_title="Torch 모델부터 OpenVINO모델까지: OTX로 간단하게 컴퓨터 비전 모델 완성하기",
                post_excerpt="AI 기술이 발전하면서, 이제 누구나 자신만의 딥러닝 모델을 만들 수 있는 시대가 되었습니다. 하지만 여전히 많은 사람들에게 AI 모델 학습은 높은 기술 장벽으로 다가옵니다.",
                href="https://davinci-ai.tistory.com/59",
            ),
            create_blog_post_card(
                animation_attrs={
                    "data-aos": "fade-up",
                    "data-aos-delay": "400",
                },
                post_title="딥러닝 (8) - [RL1] 강화학습(Reinforcement Learning)이란?",
                post_excerpt="해당 포스팅은 '시작하세요! 텐서플로 2.0 프로그래밍'책의 흐름을 따라가면서, 책 이외에 검색 및 다양한 자료들을 통해 공부하면서 정리한 내용의 포스팅입니다.",
                href="https://davinci-ai.tistory.com/31",
            ),
            create_blog_post_card(
                animation_attrs={
                    "data-aos": "fade-up",
                    "data-aos-delay": "600",
                },
                post_title="파이썬으로 구현하는 자료구조 요약 정리 - 배열(Array), 큐(Queue), Stack, Linked List..",
                post_excerpt="해당 내용은 코딩 테스트 및 기술 면접을 대비하기 위해서 자료구조를 공부하며 정리한 내용입니다.",
                href="https://davinci-ai.tistory.com/16",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                    "1024px": "repeat(3, minmax(0, 1fr))",
                }
            ),
        ),
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
    )
