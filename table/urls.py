from django.urls import path
from . import views as table_view

urlpatterns = [
    path('api/table-create/<int:lesson_id>/<int:student_id>/', table_view.TableCreateAPIView.as_view()),
    path('api/table-create/<int:group_id>/', table_view.TableCreateAPIView.as_view()),
    path('api/table-show/<int:group_id>/', table_view.TableShowAPIView.as_view()),


]