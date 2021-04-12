from django.urls import path
from . import views as request_views

urlpatterns = [
    path('api/request-create/',
         request_views.CreateRequestMentorHelpAPIView.as_view(),
         name='mentor-request-create'),
]
