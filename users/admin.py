from django.contrib import admin
from .models import  User, Student, Teacher, Guest, Coordinator

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Guest)
admin.site.register(Coordinator)
