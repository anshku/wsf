from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PlayerView, PlayerDetailView

urlpatterns = [
    path('players/', PlayerView.as_view()),
    path('players/<str:pk>/', PlayerDetailView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)