from django.urls import path
from .views import HelloView

urlpatterns = [
  path('hello-view/', HelloView.as_view())
]