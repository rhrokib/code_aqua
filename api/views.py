from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User
from .serializers import UserSerializer

@api_view(['GET'])
def api_overview(request):
    api_url = {
        'All users' : 'users/',
        'Detail': 'user/id',
        'Create': 'user/create',
        'Update': 'user/update/<str:pk>',
        'Delete': 'user/delete/<str:pk>',
        
    }
    return Response(api_url)


@api_view(['GET'])
def user_list(request):
    users = User.objects.all().order_by('-id')
    serialize = UserSerializer(users, many=True)
    
    return Response(serialize.data)

@api_view(['GET'])
def user_detail(request, pk):
    user = User.objects.get(id=pk)
    serialize = UserSerializer(user, many=False)
    
    return Response(serialize.data)

@api_view(['POST'])
def user_create(request):
    serialize = UserSerializer(data=request.data)
    
    if serialize.is_valid():
        serialize.save()
    
    return Response('User created succesfully')

@api_view(['PUT'])
def user_update(request, pk):
    user = User.objects.get(id=pk)
    serialize = UserSerializer(instance=user, data=request.data)
    
    if serialize.is_valid():
        serialize.save()
    
    return Response(serialize.data)

@api_view(['DELETE'])
def user_delete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('User deleted succesfully')
    