from .serializer import ToDoSerializer
from .models import ToDo
from rest_framework import viewsetes


#all crud operation in one class
class ToDo(viewsetes.modelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer