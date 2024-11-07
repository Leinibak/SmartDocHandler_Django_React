from django.urls import path
from .views import PatternListCreateView, PatternRetrieveDeleteView

urlpatterns = [
    path("patterns/", PatternListCreateView.as_view(), name="pattern-list-create"),
    path("patterns/<int:pk>/", PatternRetrieveDeleteView.as_view(), name="pattern-retrieve-delete"),
]
