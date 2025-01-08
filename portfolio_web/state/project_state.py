from reflex import State

class ProjectState(State):
    """State for managing project details visibility."""
    
    # Which project's details are currently shown
    selected_project: str = ""
    
    # Which tab is selected (development/research)
    selected_tab: str = "development"
    
    class Config:
        client_connect = False  # 클라이언트 연결 비활성화
        prevent_initial_call = True  # 초기 서버 호출 방지
    
    def toggle_project(self, project_id: str):
        """Toggle project expansion."""
        # 클라이언트 사이드에서만 상태 업데이트
        if self.selected_project == project_id:
            self.selected_project = ""
        else:
            self.selected_project = project_id
    
    def set_tab(self, tab: str):
        """Set the active tab."""
        self.selected_tab = tab
