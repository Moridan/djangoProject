from django.urls import path
from autos.views import AutoListView, AutoCreateView, AutoUpdateView, AutoDeleteView

app_name = 'autos'
urlpatterns = [
    path('', AutoListView.as_view(), name="list"),
    path('add', AutoCreateView.as_view(), name="add"),
    path('<int:pk>/update', AutoUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', AutoDeleteView.as_view(), name="delete"),
]