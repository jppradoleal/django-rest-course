from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView, Response
from rest_framework import status, viewsets
from profiles_api import serializers

# Create your views here.
class HelloViewAPI(APIView):
  """Test API View"""

  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """Return a list of APIView features"""
    an_apiview = [
      'Uses HTTP methos as function (get, post, path, put, delete)',
      'Is similar to a traditional Django View',
      'Gives you the most control over your application logic',
      'Is mapped manually to URLs',
    ]

    return Response({'message': 'Hello', 'an_apiview': an_apiview})
  
  def post(self, request):
    """Create a hello message with our name"""
    serializer = self.serializer_class(data = request.data)
    
    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'
      return Response({'message': message})
    else:
      return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
  
  def put(self, request, pk=None):
    """Handle updating an object"""
    return Response({'method': 'PUT', 'pk': pk})

  def patch(self, request, pk=None):
    """Handle a partial update of an object"""
    return Response({'method': 'PATCH', 'pk': pk})

  def delete(self, request, pk=None):
    """Handle deleting an object"""
    return Response({'method': 'DELETE', 'pk': pk})

class HelloViewSet(viewsets.ViewSet):
  """Test API ViewSet"""
  serializer_class = serializers.HelloSerializer

  def list(self, request):
    """Return a hello message"""

    a_viewset = [
      'Uses actions (list, create, retrieve, update, partial_update)',
      'Automatically maps to URLs using Routers',
      'Provides more functionality with less code'
    ]

    return Response({'message': 'Hello!', 'a_viewset': a_viewset})

  def create(self, request):
    """Create a new hello message"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'

      return Response({'message': message})
    else:
      return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

  def retrieve(self, request, pk=None):
    """Handle getting an object by its ID"""
    return Response({'http_method': 'GET', 'pk': pk})

  def update(self, request, pk=None):
    """Handle updating an object"""
    return Response({'http_method': 'PUT', 'pk': pk})

  def partial_update(self, request, pk=None):
    """Handle updating part of an object"""
    return Response({'http_method': 'PATCH', 'pk': pk})

  def destroy(self, request, pk=None):
    """Handle removing an object"""
    return Response({'http_method': 'DELETE', 'pk': None})