from django.urls import path
from . import views

urlpatterns = [
    path("patterns/", views.PatternListCreateView.as_view(), name="pattern-list-create"),
    path("patterns/<int:pk>/", views.PatternDeleteView.as_view(), name="pattern-delete"),
]
