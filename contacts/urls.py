from django.urls import path
from . import views as courses_views

urlpatterns = [
    path('api/contacts/', courses_views.ContactAPIView.as_view()),
    path('api/join-course/', courses_views.ToJoinTheCourseAPIView.as_view()),
    path('api/join-course/', courses_views.QandAAPIView.as_view()),
]
