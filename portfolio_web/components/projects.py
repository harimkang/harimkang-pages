import reflex as rx
from ..utils.styles import (
    create_styled_heading, 
    create_paragraph,
    create_section_heading,
    create_link_with_icon
)
from ..state.project_state import ProjectState

def create_technologies_label():
    """Create a 'Technologies:' label in strong text."""
    return rx.text.strong("Technologies:")

def create_technologies_section(technologies):
    """Create a section displaying technologies used."""
    return rx.text(
        create_technologies_label(),
        technologies,
        margin_bottom="0.5rem",
    )

def create_project_details(project_details: dict = None):
    """Create the detailed content section of a project."""
    if project_details is None:
        project_details = {
            "detailed_description": "",
            "key_features": [],
            "development_contributions": [],
            "research_contributions": [],
            "image": None,
            "research_image": None,
        }

    return rx.vstack(
        # Project Details with Image
        rx.hstack(
            rx.box(
                create_styled_heading(
                    font_size="1.5rem",
                    line_height="2rem",
                    heading_text="Project Details",
                ),
                create_paragraph(
                    margin_bottom="1.5rem",
                    paragraph_text=project_details.get("detailed_description", ""),
                ),
                flex="1",
            ),
            rx.cond(
                project_details.get("image") is not None,
                rx.image(
                    src=project_details.get("image"),
                    alt="Project visualization",
                    height="auto",
                    min_height="200px",
                    max_height="400px",
                    width="40%",
                    max_width="600px",
                    object_fit="contain",
                    border_radius="0.5rem",
                ),
            ),
            width="100%",
            spacing="4",
            align_items="center",
        ),
        
        # Key Features
        rx.box(
            rx.text.strong("Key Features:", font_size="1.2rem"),
            rx.unordered_list(
                *[rx.list_item(feature) for feature in project_details.get("key_features", [])],
                padding_left="1.5rem",
                margin_top="0.5rem",
                margin_bottom="1.5rem",
            ),
        ),
        
        # Development Highlights
        rx.box(
            rx.text.strong("Development Key Contributions:", font_size="1.2rem"),
            rx.unordered_list(
                *[rx.list_item(highlight) for highlight in project_details.get("development_contributions", [])],
                padding_left="1.5rem",
                margin_top="0.5rem",
                margin_bottom="1.5rem",
            ),
        ),
        
        # Research Contributions with Image
        rx.box(
            rx.text.strong("Research Contributions:", font_size="1.2rem"),
            rx.hstack(
                rx.box(
                    rx.unordered_list(
                        *[rx.list_item(contribution) for contribution in project_details.get("research_contributions", [])],
                        padding_left="1.5rem",
                        margin_top="0.5rem",
                        margin_bottom="1.5rem",
                    ),
                    flex="1",
                ),
                rx.cond(
                    project_details.get("research_image") is not None,
                    rx.image(
                        src=project_details.get("research_image"),
                        alt="Research visualization",
                        height="auto",
                        min_height="200px",
                        max_height="400px",
                        width="40%",
                        max_width="600px",
                        object_fit="contain",
                        border_radius="0.5rem",
                    ),
                ),
                width="100%",
                spacing="4",
                align_items="center",
            ),
        ),
        align_items="start",
        width="100%",
        spacing="4",
    )

def create_project_card(
    animation_attrs,
    project_id: str,
    project_title: str,
    project_description: str,
    technologies_used: str,
    href: str,
    project_details: dict = None,
    link_text="GitHub Repository "
):
    """Create an expandable project card."""
    return rx.box(
        rx.vstack(
            rx.box(
                create_styled_heading(
                    font_size="1.25rem",
                    line_height="1.75rem",
                    heading_text=project_title,
                ),
                create_paragraph(
                    margin_bottom="1rem",
                    paragraph_text=project_description,
                ),
                create_technologies_section(technologies=technologies_used),
            ),
            rx.spacer(),
            rx.vstack(
                create_link_with_icon(
                    link_text=link_text,
                    icon_alt="External Link",
                    icon_tag="external-link",
                    href=href,
                ),
                rx.button(
                    rx.hstack(
                        rx.icon("info"),
                        rx.text("View Details"),
                    ),
                    on_click=lambda: ProjectState.toggle_project(project_id),
                    class_name="view-details-button",
                    color_scheme="blue",
                ),
                spacing="3",
                align_items="start",
                width="100%",
            ),
            rx.cond(
                ProjectState.selected_project == project_id,
                rx.divider(margin_y="1.5rem"),
            ),
            rx.cond(
                (ProjectState.selected_project == project_id) & (project_details is not None),
                create_project_details(project_details),
            ),
            height="100%",
            spacing="4",
        ),
        class_name="transform",
        custom_attrs=animation_attrs,
        background_color="#1F2937",
        transition="all 0.3s ease-in-out",
        _hover={"transform": rx.cond(
            ProjectState.selected_project != project_id,
            "scale(1.05)",
            "none"
        )},
        padding="1.5rem",
        border_radius="0.5rem",
        width="100%",
        height="100%",
    )

def create_projects_section():
    """Create the 'Projects' section with expandable project cards."""
    return rx.box(
        create_section_heading(heading_text="Projects"),
        rx.box(
            rx.cond(
                ProjectState.selected_project != "",
                # 선택된 프로젝트가 있을 때의 레이아웃
                rx.box(
                    rx.cond(
                        ProjectState.selected_project == "openvino",
                        create_project_card(
                            animation_attrs={
                                "data-aos": "fade-up",
                                "data-aos-delay": "200",
                            },
                            project_id="openvino",
                            project_title="OpenVINO™ Training Extensions",
                            project_description="A low-code training framework built on OpenVINO™, designed to streamline the development of computer vision solutions. It provides user-friendly CLI and Python APIs to simplify the process of training, fine-tuning, and deploying models. With built-in automation for tasks like data preparation, model optimization, and evaluation, OTX enables seamless workflows from training to deployment, making it easy for users to create high-performance computer vision applications with minimal effort.",
                            technologies_used=" PyTorch, CUDA, Python, Semi-Supervised Learning",
                            href="https://github.com/openvinotoolkit/training_extensions",
                            project_details={
                                "detailed_description": "OpenVINO™ Training Extensions is a low-code transfer learning framework for Computer Vision that provides an end-to-end workflow from training to deployment of OpenVINO Model.",
                                "key_features": [
                                    "Low-code API for rapid model development",
                                    "Built-in support for transfer learning and fine-tuning",
                                    "Optimized training pipelines for various CV tasks",
                                ],
                                "development_contributions": [
                                    "In v1.0, contributed as a team member by implementing and developing overall CLI and automation, while serving as the person responsible for classification.",
                                    "Proposed a new design in v2.0 that prioritized user-friendliness, scalability to enhance the framework’s adaptability and usability.",
                                    "Led the development team for the v2.0 release, guiding new architectural decisions to elevate user experience and functionality.",
                                    "Contributed to OTX, enabling seamless and unified API and CLI usage of models from various frameworks, including torchvision and Hugging Face",
                                    "Contributed to reaching 1.1k+ stars as the #1 main contributor for that repo"
                                ],
                                "research_contributions": [
                                    "Enhanced Semi-Supervised Learning (Semi-SL) with techniques like pseudo-labeling, adaptable thresholds, and unlabeled warm-up loss. These methods improved accuracy by 5-20% compared to supervised learning, with training times averaging up to 3x longer.",
                                    "Researched class-incremental learning algorithms for computer vision tasks, demonstrating performance improvements with incremental case.",
                                ],
                                "image": "https://openvinotoolkit.github.io/training_extensions/stable/_images/diagram_otx.png",
                                "research_image": "https://openvinotoolkit.github.io/training_extensions/stable/_images/semi-sl-mv3-large.png",
                            },
                        ),
                    ),
                    rx.cond(
                        ProjectState.selected_project == "geti",
                        create_project_card(
                            animation_attrs={
                                "data-aos": "fade-up",
                                "data-aos-delay": "400",
                            },
                            project_id="geti",
                            project_title="Intel® Geti™",
                            project_description="Intel® Geti™ software eases laborious data upload, labeling, model training, retraining, and optimization tasks across the computer vision model development process.",
                            technologies_used=" PyTorch, Python, Computer Vision, kubernetes",
                            href="https://geti.intel.com/",
                            link_text="Product Page ",
                            project_details={
                                "detailed_description": "Intel’s software for building computer vision models in a fraction of the time and with less data. This software eases laborious data labeling, model training and optimization tasks across the AI model development process, empowering teams to produce custom AI models at scale.",
                                "key_features": [
                                    "Automated data labeling and augmentation",
                                    "Interactive model training and evaluation",
                                    "Real-time performance monitoring",
                                    "Enterprise-grade deployment capabilities",
                                ],
                                "development_contributions": [
                                    "Maintained the training workflow for Intel® Geti™ product, which leverages OpenVINO Training Extensions as its backend.",
                                    "Responded to user inquiries on training and model performance issues.",
                                    "Supported the implementation of the Geti-SDK.",
                                ],
                                "research_contributions": [
                                    "Enhanced model performance for low-data and active learning scenarios.",
                                    "Supported the development of a novel active learning algorithm for efficient data labeling.",
                                ],
                                "image": None,
                            },
                        ),
                    ),
                    rx.cond(
                        ProjectState.selected_project == "anomalib",
                        create_project_card(
                            animation_attrs={
                                "data-aos": "fade-up",
                                "data-aos-delay": "600",
                            },
                            project_id="anomalib",
                            project_title="Anomalib",
                            project_description="An anomaly detection library comprising state-of-the-art algorithms and features such as experiment management, hyper-parameter optimization, and edge inference.",
                            technologies_used=" PyTorch, Python, Computer Vision",
                            href="https://github.com/openvinotoolkit/anomalib",
                            project_details={
                                "detailed_description": "Anomalib is a state-of-the-art anomaly detection library that provides comprehensive tools for developing and deploying anomaly detection models. It includes advanced features for experiment management, hyperparameter optimization, and efficient inference on edge devices.",
                                "key_features": [
                                    "Multiple state-of-the-art anomaly detection algorithms",
                                    "Comprehensive experiment tracking and visualization",
                                    "Automated hyperparameter optimization",
                                    "Efficient model deployment tools",
                                ],
                                "development_contributions": [
                                    "Proposed and implemented a 2-step installation for edge device environments.",
                                    "Optimize the installation experience for specific features in constrained settings.",
                                    "Optimized the CLI output to provide a simplified guide for lightweight users and refactored it so that all configurable parameters are visible for expert users.",
                                    "Propose a new API to provide features to enable a continuous workflow between the API and CLI.",
                                    "Contributed to reaching 3.8k GitHub stars.",
                                ],
                                "image": None,
                            },
                        ),
                    ),
                    width="100%",
                ),
                # 기본 그리드 레이아웃
                rx.box(
                    create_project_card(
                        animation_attrs={
                            "data-aos": "fade-up",
                            "data-aos-delay": "200",
                        },
                        project_id="openvino",
                        project_title="OpenVINO™ Training Extensions",
                        project_description="A low-code framework for computer vision, enabling seamless workflows from training to deployment. With user-friendly CLI, Python APIs, and automated processes for tasks like model training and optimization, it simplifies the creation and fine-tuning of high-performance models.",
                        technologies_used=" PyTorch, CUDA, Python, Semi-Supervised Learning",
                        href="https://github.com/openvinotoolkit/training_extensions",
                    ),
                    create_project_card(
                        animation_attrs={
                            "data-aos": "fade-up",
                            "data-aos-delay": "400",
                        },
                        project_id="geti",
                        project_title="Intel® Geti™",
                        project_description="Intel® Geti™ software eases laborious data upload, labeling, model training, retraining, and optimization tasks across the computer vision model development process.",
                        technologies_used=" PyTorch, Python, Computer Vision, kubernetes",
                        href="https://geti.intel.com/",
                        link_text="Product Page ",
                    ),
                    create_project_card(
                        animation_attrs={
                            "data-aos": "fade-up",
                            "data-aos-delay": "600",
                        },
                        project_id="anomalib",
                        project_title="Anomalib",
                        project_description="An anomaly detection library comprising state-of-the-art algorithms and features such as experiment management, hyper-parameter optimization, and edge inference.",
                        technologies_used=" PyTorch, Python, Computer Vision",
                        href="https://github.com/openvinotoolkit/anomalib",
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
            ),
            width="100%",
            transition="all 0.3s ease-in-out",
        ),
        id="projects",
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
