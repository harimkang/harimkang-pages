import reflex as rx
from ..utils.styles import create_styled_heading, create_paragraph, create_section_heading
import rxconfig

def create_contact_icon(icon_alt, icon_tag):
    """Create an icon for contact information."""
    return rx.icon(
        alt=icon_alt,
        tag=icon_tag,
        height="1.5rem",
        display="inline",
        margin_right="0.5rem",
        width="1.5rem",
    )

def create_contact_link(link_url, icon_alt, icon_tag, link_text):
    """Create a contact link with an icon."""
    return rx.link(
        rx.hstack(
            create_contact_icon(icon_alt=icon_alt, icon_tag=icon_tag),
            rx.text(link_text),
            spacing="2",
            align_items="center",
        ),
        href=link_url,
        is_external=True,
        transition="all 0.3s ease-in-out",
        _hover={"color": "#93C5FD", "transform": "translateY(-2px)"},
        color="#60A5FA",
    )

def create_contact_section():
    """Create the 'Contact' section with contact information and resume download."""
    return rx.box(
        create_section_heading(heading_text="Contact"),
        rx.box(
            rx.vstack(
                create_styled_heading(
                    font_size="1.5rem",
                    line_height="2rem",
                    heading_text="Let's Connect!",
                    text_align="center",
                ),
                create_paragraph(
                    margin_bottom="1.5rem",
                    paragraph_text="Feel free to reach out for collaborations, speaking engagements, or just to chat about AI and technology!",
                    text_align="center",
                ),
                rx.vstack(
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon(
                                    tag="download",
                                    height="1.5rem",
                                    width="1.5rem",
                                ),
                                rx.text("Download Resume"),
                                spacing="2",
                                align_items="center",
                                justify_content="center",
                            ),
                            padding="1rem 2rem",
                            background_color="rgb(59, 130, 246)",
                            border_radius="0.5rem",
                            width="100%",
                            _hover={
                                "background_color": "rgb(37, 99, 235)",
                                "transform": "translateY(-2px)",
                            },
                            transition="all 0.3s ease-in-out",
                        ),
                        href=f"{rxconfig.config.base_path}/resume.pdf",
                        is_external=True,
                        text_decoration="none",
                    ),
                    rx.divider(
                        margin_y="1.5rem",
                        opacity="0.2",
                    ),
                    create_contact_link(
                        link_url="mailto:harimkang4422@gmail.com",
                        icon_alt="Email",
                        icon_tag="mail",
                        link_text="harimkang4422@gmail.com",
                    ),
                    create_contact_link(
                        link_url="https://www.linkedin.com/in/harim-kang-hk1129",
                        icon_alt="LinkedIn",
                        icon_tag="linkedin",
                        link_text="LinkedIn Profile",
                    ),
                    create_contact_link(
                        link_url="https://github.com/harimkang",
                        icon_alt="GitHub",
                        icon_tag="github",
                        link_text="GitHub Profile",
                    ),
                    spacing="3",
                    align_items="center",
                    padding="2rem",
                    background="rgba(17, 24, 39, 0.7)",
                    border_radius="0.75rem",
                    backdrop_filter="blur(10px)",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    width="100%",
                ),
                width="100%",
                max_width="600px",
                align_items="center",
                spacing="3",
            ),
            width="100%",
            display="flex",
            justify_content="center",
        ),
        id="contact",
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
        padding_top="2rem",
        padding_bottom="2rem",
    ) 