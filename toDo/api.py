from .serializer import ToDoSerializer
from .models import ToDo
from rest_framework import viewsets


#all crud operation in one class
class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer