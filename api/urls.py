from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('tasks/', views.TaskListCreateAPIView.as_view(), name='api_task_list_create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view(), name='api_task_detail'),
    path('users/register/', views.UserRegistrationView.as_view(), name='api_user_register'),
    path('users/me/', views.CurrentUserView.as_view(), name='api_user_me'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]