from .models import Project, ProjectMember


class ProjectService:

    @staticmethod
    def create_project(user, data):
        project = Project.objects.create(
        owner=user,
        **data,
)

        ProjectMember.objects.create(
        project=project,
        user=user,
        role="owner",
)

class ProjectMemberService:

    @staticmethod
    def add_member(project, user):
        return ProjectMember.objects.create(
            project=project,
            user=user,
            role="member",
        )
return project