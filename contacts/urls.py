from django.urls import path
from . import views as courses_views

urlpatterns = [
    path('api/contacts/', courses_views.ContactAPIView.as_view()),
]
