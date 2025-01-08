import reflex as rx
from ..utils.styles import create_styled_heading, create_paragraph, create_text

def create_logo_image(alt_text, image_src):
    """Create a logo image with specified dimensions and alt text."""
    return rx.image(
        alt=alt_text,
        src=image_src,
        height="3rem",
        margin_right="1rem",
        object_fit="contain",
        width="3rem",
    )

def create_subheading(content):
    """Create a subheading with custom styling."""
    return rx.heading(
        content,
        font_weight="600",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h4",
    )

def create_info_box(title, subtitle, description):
    """Create an information box with title, subtitle, and description."""
    return rx.box(
        create_subheading(content=title),
        rx.text(subtitle, color="#60A5FA"),
        rx.text(description)
    )

def create_skill_item(icon_src: str, skill_text: str):
    """Create a skill item with an icon and text."""
    return rx.hstack(
        rx.image(
            src=icon_src,
            height="1.5rem",
            width="1.5rem",
            object_fit="contain",
            alt=f"{skill_text} icon",
        ),
        rx.text(skill_text),
        spacing="3",
        align_items="center",
    )

def highlight_text(text: str) -> str:
    """Add color spans to highlighted keywords."""
    keywords = {
        "Python": "rgb(96, 165, 250)",  # 파란색
        "PyTorch": "rgb(239, 68, 68)",  # 빨간색
        "OpenVINO": "rgb(16, 185, 129)",  # 초록색
        "Deep Learning": "rgb(139, 92, 246)",  # 보라색
        "Computer Vision": "rgb(139, 92, 246)",
        "Semi-Supervised Learning": "rgb(139, 92, 246)",
        "Transfer Learning": "rgb(139, 92, 246)",
        "Incremental Learning": "rgb(139, 92, 246)",
    }
    
    for keyword, color in keywords.items():
        text = text.replace(
            keyword,
            f'<span style="color: {color}; font-weight: 600;">{keyword}</span>'
        )
    return text

def create_about_summary():
    """Create the professional summary and expertise section for the About Me page."""
    return rx.box(
        create_styled_heading(
            font_size="1.5rem",
            line_height="2rem",
            heading_text="Professional Summary",
        ),
        rx.html(
            highlight_text(
                "With a strong engineering background, I enhanced Deep Learning frameworks through streamlined APIs and impactful research in Semi-Supervised Learning and Transfer Learning, contributing strategically to open-source AI projects with high-performance teams."
            ),
            margin_bottom="1rem",
        ),
        rx.heading(
            "Skills & Tools",
            font_weight="600",
            margin_bottom="1rem",
            margin_top="1.5rem",
            font_size="1.5rem",
            line_height="2rem",
            as_="h3",
        ),
        rx.box(
            rx.vstack(
                create_skill_item(
                    "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",
                    "Python | PyTorch | OpenVINO"
                ),
                create_skill_item(
                    "https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg",
                    "Git | Github | PyTest | Tox | Linux"
                ),
                create_skill_item(
                    "https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg",
                    "Software development | Architecture | Open-Source"
                ),
                create_skill_item(
                    "https://cdn-icons-png.flaticon.com/512/2103/2103633.png",
                    "Deep Learning | Computer Vision | Semi & Weakly Supervised Learning"
                ),
                create_skill_item(
                    "https://cdn-icons-png.flaticon.com/512/484/484633.png",
                    "Korean: Native | English: Business working proficiency"
                ),
                align_items="start",
                spacing="3",
                width="100%",
            ),
        ),
        rx.divider(
            margin_y="2rem",
            opacity="0.2",
        ),
        custom_attrs={
            "data-aos": "fade-up",
            "data-aos-delay": "200",
        },
    )


def create_work_experience():
    """Create the work experience section with multiple job entries."""
    return rx.box(
        rx.flex(
            create_logo_image(
                alt_text="Intel Logo",
                image_src="https://www.intel.com/content/dam/www/central-libraries/us/en/images/intel-new-logo-16x9.jpg.rendition.intel.web.720.405.jpg",
            ),
            create_info_box(
                title="AI Software Engineer",
                subtitle="Intel (2021.06 - 2024.11) | Full-Time",
                description="Developed and optimized AI solutions at Intel, focusing on computer vision, Semi-Supervised Learning, and scalable frameworks like OpenVINO™ Training Extensions, while leading global collaborations and product releases.",
            ),
            display="flex",
            align_items="flex-start",
        ),
        rx.flex(
            create_logo_image(
                alt_text="Intel Logo",
                image_src="https://www.intel.com/content/dam/www/central-libraries/us/en/images/intel-new-logo-16x9.jpg.rendition.intel.web.720.405.jpg",
            ),
            create_info_box(
                title="Software Engineer",
                subtitle="Intel (2020.05 - 2021.05) | Contract",
                description="Validated deep learning frameworks and APIs, designed and executed end-to-end tests, and contributed to algorithm improvements, including entropy-based sampling for dataset management frameworks.",
            ),
            display="flex",
            align_items="flex-start",
        ),
        display="flex",
        flex_direction="column",
        gap="1.5rem",
    )

def create_education():
    return rx.box(
        rx.flex(
            create_logo_image(
                alt_text="SSU Logo",
                    image_src="https://ssu.ac.kr/wp-content/uploads/2019/04/cymbal_mark.png",
                ),
            create_info_box(
                title="Soongsil University",
                subtitle="B.S. in Mathematics & Software",
                description="Graduated with a Bachelor of Science in Mathematics and Software.",
            ),
            display="flex",
            align_items="flex-start",
        ),
        display="flex",
        flex_direction="column",
        gap="1.5rem",
    )

def create_section_heading(heading_text):
    """Create a section heading with fade-in animation."""
    return rx.heading(
        heading_text,
        custom_attrs={"data-aos": "fade-right"},
        font_weight="700",
        margin_bottom="2rem",
        font_size="1.875rem",
        line_height="2.25rem",
        as_="h2",
    )

def create_list_item(item_text):
    """Create a simple list item."""
    return rx.el.li(item_text)

def create_about_section():
    """Create the 'About Me' section with expertise and professional journey."""
    return rx.box(
        create_section_heading(heading_text="About Me"),
        rx.box(
            create_about_summary(),
            rx.box(
                create_styled_heading(
                    font_size="1.5rem",
                    line_height="2rem",
                    heading_text="Work Experience",
                ),
                create_styled_heading(
                    font_size="1rem",
                    line_height="1rem",
                    heading_text="4 years 6 months",
                ),
                create_work_experience(),
                create_styled_heading(
                    font_size="1.5rem",
                    margin_top="2rem",
                    line_height="2rem",
                    heading_text="Education",
                ),
                create_education(),
                custom_attrs={
                    "data-aos": "fade-up",
                    "data-aos-delay": "400",
                },
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
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
