from django.contrib import admin
from .mentor_comment import MentorComment
from .models import User, IsMentor

admin.site.register(User)
admin.site.register(MentorComment)
admin.site.register(IsMentor)
