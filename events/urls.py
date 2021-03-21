from django.urls import path
from . import views as events_views

urlpatterns = [
    path('api/events/', events_views.EventAPIView.as_view()),
    path('api/events/<int:id>/', events_views.EventDetailAPIView.as_view()),

]
