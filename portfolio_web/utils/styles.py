import reflex as rx

def load_script(script_source):
    """Load a script from the given source URL."""
    return rx.script(src=script_source)

def create_styled_link(link_url, link_content):
    """Create a styled anchor element with hover effects and transitions."""
    return rx.el.a(
        link_content,
        href=link_url,
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        _hover={"color": "#60A5FA"},
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )

def create_styled_heading(font_size, line_height, heading_text, **kwargs):
    """Create a styled heading with customizable font size and line height."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom="1rem",
        font_size=font_size,
        line_height=line_height,
        as_="h3",
        **kwargs
    )

def create_paragraph(margin_bottom, paragraph_text, **kwargs):
    """Create a paragraph with a specified bottom margin."""
    return rx.text(
        paragraph_text, 
        margin_bottom=margin_bottom,
        **kwargs
    )

def create_text(text_content):
    """Create a simple text element."""
    return rx.text(text_content)

def create_icon(alt_text, icon_height, icon_tag, icon_width):
    """Create an icon with specified dimensions and alt text."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height=icon_height,
        display="inline",
        width=icon_width,
    )

def create_section_heading(heading_text: str, text_align: str = "left"):
    """Create a section heading with fade-in animation."""
    return rx.heading(
        heading_text,
        custom_attrs={"data-aos": "fade-right"},
        font_weight="700",
        margin_bottom="2rem",
        font_size="1.875rem",
        line_height="2.25rem",
        as_="h2",
        text_align=text_align,
    )

def create_link_with_icon(link_text, icon_alt, icon_tag, href):
    """Create a link with an icon and hover effects."""
    return rx.el.a(
        link_text,
        create_icon(
            alt_text=icon_alt,
            icon_height="1rem",
            icon_tag=icon_tag,
            icon_width="1rem",
        ),
        href=href,
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        _hover={"color": "#93C5FD"},
        color="#60A5FA",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )

# ... 기타 스타일 관련 유틸리티 함수들 