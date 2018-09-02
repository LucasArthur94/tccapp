from import_export import resources
from users.models import User, Student

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
