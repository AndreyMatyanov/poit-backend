from fastapi import APIRouter

from app.api.endpoints import \
    post_endpoint, user, auth, group, lesson, discipline, file, publication, course_project, graduation_project, \
    stage_graduation_project, graduation_request_endpoint

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["User"])
api_router.include_router(post_endpoint.router, prefix="/post", tags=["Post"])
api_router.include_router(auth.router, prefix="/auth", tags=['Auth'])
api_router.include_router(group.router, prefix="/group", tags=['Group'])
api_router.include_router(lesson.router, prefix="/lesson", tags=['Lesson'])
api_router.include_router(discipline.router, prefix="/discipline", tags=['Discipline'])
api_router.include_router(file.router, prefix="/file", tags=['File'])
api_router.include_router(publication.router, prefix="/publication", tags=['Publication'])
api_router.include_router(course_project.router, prefix="/course-project", tags=['Course Project'])
api_router.include_router(graduation_project.router, prefix="/graduation-project", tags=['Graduation Project'])
api_router.include_router(stage_graduation_project.router, prefix="/stage-graduation-project", tags=['Stage Graduation Project'])
api_router.include_router(graduation_request_endpoint.router, prefix="/graduation-project-request", tags=['Graduation Project Request'])