from django.urls import path
from . import views as user_views

urlpatterns = [
    path('api/login/', user_views.LoginView.as_view(), name='login'),
    path('api/logout/', user_views.LogoutView.as_view(), name='logout'),
    path('api/user-create/', user_views.UserRegistrationView.as_view(), name='user-create'),
    path('api/user/<int:pk>/', user_views.UserRetrieveUpdateDeleteAPIView.as_view(), name='user'),
    path('api/user/', user_views.UserListView.as_view(), name='user-list'),
    path('api/password-reset/', user_views.reset_user_password, name="password-reset"),

]