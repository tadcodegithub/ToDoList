from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import TaskSerializer,my_view
from .models import Task
from django.shortcuts import render, redirect
"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)
"""
Below Function going to display all the tasks store in the data base.
"""
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    data=my_view(tasks)
    context={"data":data}
    return render(request,"userpage/tasklist.html", context)
"""
This Function going to display Detailed view of one perticuler task with the help of pk.
"""
@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(title=pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)
@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Taks deleted successfully.")