from django.urls import path
from . import views as user_views

urlpatterns = [
    path('api/login/', user_views.LoginView.as_view(), name='login'),
    path('api/logout/', user_views.LogoutView.as_view(), name='logout'),
    path('api/user-create/', user_views.UserRegistrationView.as_view(), name='user-create'),
    path('api/user/<int:pk>/', user_views.UserRetrieveUpdateDeleteAPIView.as_view(), name='user'),
    path('api/user/', user_views.UserListView.as_view(), name='user-list'),
    path('api/change_password/<int:pk>/', user_views.ChangePasswordView.as_view(), name='reset_password'),
    path('api/mentor_comment/', user_views.MentorCommentsView.as_view(), name='mentor_comment'),
    path('api/image-update/user/<int:pk>/', user_views.ImageUpdateView.as_view(), name='image_update'),
    path('api/email-update/user/<int:pk>/', user_views.EmailUpdateView.as_view(), name='email_update'),
    path('api/main-info/user/<int:pk>/', user_views.UserMainInfoUpdateView.as_view(), name='email_update'),
    path('api/social-media-info/user/<int:pk>/', user_views.UserSocialInfoUpdateView.as_view(), name='email_update'),
    path('api/is-mentor/', user_views.IsMentorView.as_view(), name='email_update'),

]