from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tasks
from .serializers import TaskSerializer
# Create your views here.

@api_view(['GET'])
def allTask(request):
    # task = {
    #  "name":'Maths Assignment',
    #  "description":'some description of the task',
    #  "email":'email@gmail.com'
    # }

    tasks = Tasks.objects.all()
    serializer = TaskSerializer(tasks,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def newTask(request):
     print(request.data)
     serializer = TaskSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
     return Response('item recieved and saved successfully')
    #  else:
    #      print(serializer.errors)
    #      return Response({'message':'Error occured | {serializer.errors}'})