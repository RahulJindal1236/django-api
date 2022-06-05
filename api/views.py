from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def allTask(request):
    task = {
     "name":'Maths Assignment',
     "description":'some description of the task',
     "email":'email@gmail.com'
    }

    return Response(task)

@api_view(['POST'])
def newTask(request):
     print(request.data)
     return Response('item recieved and saved successfully')