from django.urls import path, include
from .views import HelloViewAPI, HelloViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')

urlpatterns = [
  path('hello-viewapi/', HelloViewAPI.as_view()),
  path('', include(router.urls))
]