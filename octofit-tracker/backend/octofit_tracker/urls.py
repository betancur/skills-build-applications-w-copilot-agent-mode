from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')

# Define API root
api_root = views.api_root

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),  # Admin endpoint
    path('api/', include(router.urls)),
]
