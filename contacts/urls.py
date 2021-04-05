from django.urls import path
from . import views as courses_views

urlpatterns = [
    path('api/contacts/', courses_views.ContactAPIView.as_view()),
    path('api/questions/', courses_views.QandAAPIView.as_view()),
]
