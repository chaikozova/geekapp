from django.urls import path
from chat import views

urlpatterns = [
    path('api/room/', views.Rooms.as_view()),
    path('api/dialog/', views.Dialog.as_view()),
    path('api/users/', views.Rooms.as_view()),

]