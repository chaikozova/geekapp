from django.urls import path
from . import views as courses_views

urlpatterns = [
path('api/join-course/', courses_views.ToJoinTheCourseAPIView.as_view()),
]
