from django.contrib import admin

# Register your models here.
from courses.models import Course, Level, Lesson, GroupLevel

admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Lesson)
admin.site.register(GroupLevel)
