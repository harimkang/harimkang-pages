function toggleProject(projectId) {
    const projectDetails = document.querySelector(`#project-${projectId}-details`);
    const allDetails = document.querySelectorAll('[id^="project-"][id$="-details"]');
    
    // 다른 모든 프로젝트 상세 정보 숨기기
    allDetails.forEach(detail => {
        if (detail.id !== `project-${projectId}-details`) {
            detail.style.display = 'none';
        }
    });
    
    // 현재 프로젝트 상세 정보 토글
    if (projectDetails) {
        const currentDisplay = projectDetails.style.display;
        projectDetails.style.display = currentDisplay === 'none' ? 'block' : 'none';
    }
} 