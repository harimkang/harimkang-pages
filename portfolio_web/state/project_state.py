from reflex import State

class ProjectState(State):
    """State for managing project details visibility."""
    
    # Which project's details are currently shown
    selected_project: str = ""
    
    # Which tab is selected (development/research)
    selected_tab: str = "development"
    
    # WebSocket 연결 비활성화
    async def handle_connect(self):
        """Handle websocket connection."""
        pass  # WebSocket 연결 시도를 하지 않음
    
    # 추가 설정
    class Config:
        client_connect = False  # 클라이언트 연결 비활성화
    
    def toggle_project(self, project_id: str):
        """Toggle project expansion."""
        if self.selected_project == project_id:
            self.selected_project = ""
        else:
            self.selected_project = project_id
    
    def set_tab(self, tab: str):
        """Set the active tab."""
        self.selected_tab = tab
