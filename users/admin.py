from django.contrib import admin
from .mentor_comment import MentorComment
from .models import User, Request


admin.site.register(User)
admin.site.register(Request)
admin.site.register(MentorComment)