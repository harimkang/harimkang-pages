import reflex as rx

class ProjectState(rx.State):
    """State for managing project details visibility."""
    
    # Which project's details are currently shown
    selected_project: str = ""
    
    # Which tab is selected (development/research)
    selected_tab: str = "development"
    
    def toggle_project(self, project_id: str):
        """Toggle project expansion."""
        if self.selected_project == project_id:
            self.selected_project = ""
        else:
            self.selected_project = project_id
    
    def set_tab(self, tab: str):
        """Set the active tab."""
        self.selected_tab = tab 