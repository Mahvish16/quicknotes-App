from django.urls import path
from .views import RegisterView,LoginView,NotesView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='Register'),
    path('login/', LoginView.as_view(), name='Login'),
    path('notes/', NotesView.as_view(), name='notes'),
    
]
