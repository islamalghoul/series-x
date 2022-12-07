from django.urls import path
from .views import SeriesListView, SeriesDetailView, SeriesCreateView, SeriesUpdateView, SeriesDeleteView

urlpatterns = [
    path('series/', SeriesListView.as_view(), name='series_list'),
    path('<int:pk>/', SeriesDetailView.as_view(), name='series_detail'),
    path('create/', SeriesCreateView.as_view(), name='series_create'),
    path('<int:pk>/update/', SeriesUpdateView.as_view(), name='series_update'),
    path('<int:pk>/delete/', SeriesDeleteView.as_view(), name='series_delete'),
]