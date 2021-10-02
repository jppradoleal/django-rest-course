from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView, Response

# Create your views here.
class HelloView(APIView):
  """Test API View"""

  def get(self, request, format=None):
    """Return a list of APIView features"""
    an_apiview = [
      'Uses HTTP methos as function (get, post, path, put, delete)',
      'Is similar to a traditional Django View',
      'Gives you the most control over your application logic',
      'Is mapped manually to URLs',
    ]

    return Response({'message': 'Hello', 'an_apiview': an_apiview})