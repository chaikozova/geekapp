from django.urls import path
from . import views as request_views


urlpatterns = [
    path('api/request-create/',
         request_views.CreateRequestMentorHelpAPIView.as_view(),
         name='mentor-request-create'),
    path('api/all_notifications/', request_views.NotificationsListAPIView.as_view()),
    path('api/my_notifications/', request_views.MyNotificationsAPIView.as_view()),
    path('api/my_requests/', request_views.MyRequestsAPIView.as_view()),
    path('api/mentor_response/<int:id>/', request_views.MentorResponseToRequestAPIView.as_view()),
    path('api/create_room/<int:id>/', request_views.CreateRoomForMentorAndStudentAPIView.as_view()),
    path('api/student_reject/<int:id>/', request_views.StudentRejectNotificationAPIView.as_view()),
    path('api/end_chat/<int:id>/', request_views.EndTheRoomAPIView.as_view()),
]
