from django.contrib import admin

# Register your models here.
from courses.models import Course, Level, Lesson, GroupLevel
from users.models import User

#
# class UserInLine(admin.TabularInline):
#     model = User
#     fk_name = 'group_students'
#
#
# class GroupAdmin(admin.ModelAdmin):
#     inlines = [
#         UserInLine,
#     ]


admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Lesson)
admin.site.register(GroupLevel)


