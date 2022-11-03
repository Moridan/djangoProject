from django.urls import path
from fabrikanten.views import FabrikantenListView, FabrikantenCreateView, FabrikantenUpdateView, FabrikantenDeleteView

app_name = 'fabrikanten'
urlpatterns = [
    path('', FabrikantenListView.as_view(), name="list"),
    path('add', FabrikantenCreateView.as_view(), name="add"),
    path('<int:pk>/update', FabrikantenUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', FabrikantenDeleteView.as_view(), name="delete"),
]