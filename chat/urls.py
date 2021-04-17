from django.urls import path
from chat import views

urlpatterns = [
    path('api/room/', views.RoomsView.as_view()),
    path('api/room/<int:id>/', views.RoomDetailView.as_view()),
    path('api/room/<int:id>/chat/', views.ChatsView.as_view()),
    path('api/room/<int:pk>/chat/<int:id>/', views.ChatDetailView.as_view()),
    path('api/add_users/', views.AddUserRoom.as_view()),
    path('api/room/<int:pk>/dialog/', views.DialogView.as_view()),
    path('api/users/', views.RoomsView.as_view()),

]